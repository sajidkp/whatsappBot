
import pyautogui as pt
from time import sleep
import pyperclip
import dataset as data
import common as c

PAGE_TOP = 1
SCROLL_ACTIVE= 2
PAGE_END = 3
SCROLL_DOWN_VALUE = -2000
SCROLL_REPEAT_MAX = 25

# Generic Scroll function
# Return Values:  PAGE_TOP - When user reached top of page
# PAGE_END - When user reached bottom of page
# SCROLL_ACTIVE - When the scroll is active after the maximum iterations are completed
def full_scroll(scroll_length, repeat_count):
    pt.moveTo(450,450)
    # Reference screenshot taken, to check if scroll has ended.
    temporary_reference_screenshot = pt.screenshot()
    scroll_ended = False
    i = repeat_count
    while i >= 0:
        x= pt.vscroll(scroll_length)
        # Compare previous screenshot with with the screen after scroll
        if pt.locateOnScreen(temporary_reference_screenshot, confidence = .9):
            scroll_ended = True
            break
        else: temporary_reference_screenshot = pt.screenshot()
        print(i)
        i -= 1
        sleep(1)

    if scroll_ended:
        if scroll_length >0: return PAGE_TOP
        else: return PAGE_END

    if scroll_length == -2000 : return PAGE_END

    return SCROLL_ACTIVE

    # elif i <= 0 : return SCROLL_ACTIVE
    # elif scroll_length > 0: return PAGE_TOP
    # else: return PAGE_END

def follow_up_activity():
    print("Entered Follow up Activity")

def process_active_message():
    return "process_active_message"

#Check if the previous message was sent by the Author. If True, returns the message
def latest_message_from_author():
    try:
        location = pt.locateOnScreen(data.mic, confidence=.8)

        if location is not None:
            #Moving to the expected location of author message
            loc_x = int (location[0] - 180)
            loc_y = int (location[1]- 40)
            pt.moveTo(loc_x, loc_y, duration=.5)
            sleep(2)
            if pt.pixelMatchesColor(loc_x, loc_y, (5, 97, 98), tolerance=10):
                pt.tripleClick()
                c.controlPress('c')
                message = pyperclip.paste()
                print("Sent Message is: ", message)
                return message
            else: return False
    except (Exception):
        return False

#Follow up all detected locations in the active page
def follow_up_from_active_page(locations):
    for l in locations:
        #move to the yesterday label of a chat
        pt.moveTo(l, duration=.25)
        print("Location printing: ", l)
        pt.moveRel(5,5)
        pt.click()
        sleep(.5)
        message = latest_message_from_author()
        if message == False:
            print("Latest message is not from author")
        else:
            # When a response is sent, the side menu gets reset. Hence after sending response, the function exits
            if data.author_compare_message in str(message).lower():
                c.post_response("Autobot sending response")
                return True
            elif "i saw this" in str(message).lower():
                c.post_response("Autobot sending response 2")
                return True

    return False

# Check for messages from "Yesterday" and send follow-up messages
# Auto-responder will reply if the last message was sent by author yesterday.
def follow_up_message():
    # Ensure position is top of screen
    scroll_status = full_scroll(SCROLL_DOWN_VALUE, SCROLL_REPEAT_MAX)
    if SCROLL_ACTIVE == scroll_status:
        print("Too long to Scroll. Exiting")
        return 0
    elif scroll_status == PAGE_END: print("Reached bottom of page")

    #Scroll Up until top of page
    yesterday_message_detected = False
    while scroll_status != PAGE_TOP:
        pt.moveTo(1000,1000, duration=.25)

        #List all messages from yesterday, in the active page
        locations = list((pt.locateAllOnScreen(data.yesterday_label, confidence=.7)))
        if len(locations) != 0:
            yesterday_message_detected = True
            print("THE LOCATION:", list(locations))
            if follow_up_from_active_page(locations):
                scroll_status = full_scroll(SCROLL_DOWN_VALUE, SCROLL_REPEAT_MAX)
                continue
        # Scroll up to next page
        scroll_status = full_scroll(800, 0)

    return 1