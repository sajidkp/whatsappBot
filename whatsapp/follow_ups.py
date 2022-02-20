
import pyautogui as pt
from time import sleep
import pyperclip
import dataset as data
import common as c

PAGE_TOP = 1
SCROLL_ACTIVE= 2
PAGE_END = 3

AUTHOR_LAST_MESSAGE_POS_X = 1682
AUTHOR_LAST_MESSAGE_POS_Y = 920

#Scroll till the end of whatsapp chats
def full_scroll(scroll_length, repeat_count):
    pt.moveTo(450,450)
    temporary_reference_screenshot = pt.screenshot()
    scroll_ended = False
    i = repeat_count
    while i >= 0:
        x= pt.vscroll(scroll_length)
        sleep(2)
        if pt.locateOnScreen(temporary_reference_screenshot, confidence = .95):
            print("Break at", i)
            scroll_ended = True
            break
        else: temporary_reference_screenshot = pt.screenshot()
        print(i)
        i -= 1

    if scroll_ended:
        if scroll_length >0: return PAGE_TOP
        else: return PAGE_END

    # if scroll_length == -2000 : return PAGE_END

    return SCROLL_ACTIVE

    # elif i <= 0 : return SCROLL_ACTIVE
    # elif scroll_length > 0: return PAGE_TOP
    # else: return PAGE_END


def follow_up_activity():
    print("Entered Follow up Activity")

def process_active_message():
    return "process_active_message"

#Check if the previous message was sent by the Author. If True, returns the message
def check_if_latest_message_from_author():
    try:
        location = pt.locateOnScreen(data.mic, confidence=.8)
        print("Mic Located")
        if location is not None:
            #Moving to the expected location of author message
            loc_x = AUTHOR_LAST_MESSAGE_POS_X
            loc_y = AUTHOR_LAST_MESSAGE_POS_Y
            # print("Current Position of mouse is: ", pt.position())
            pt.moveTo(loc_x, loc_y, duration=1)
            print("Mouse moved to: ", pt.position())
            # if pt.pixelMatchesColor(loc_x, loc_y, (5, 97, 98), tolerance=10):
            if pt.pixelMatchesColor(loc_x, loc_y, (0, 92, 75), tolerance=10):
                pt.tripleClick()
                c.controlPress('c')
                message = pyperclip.paste()
                print("Sent Message is: ", message)
                pt.press("esc", presses=2)
                sleep(1)
                return message
            else: return False
        else:
            print("Mic not located")
            return False
    except (Exception):
        print("Icon not found")
        return False

#Follow up all detected locations in the active page
def follow_up_from_active_page(locations):
    number_of_items = len(locations)
    print("No. of items: ", number_of_items)
    i = 0
    items_not_required = 0
    item_archived = False
    for l in reversed(locations):
        if i%4 !=0:
            i+=1
            continue
        else: i+=1
        #move to the yesterday label of a chat
        pt.moveTo(l, duration=.25)
        print("Location printing: ", l)
        pt.moveRel(5,5)
        pt.click()
        sleep(.5)
        message = check_if_latest_message_from_author()
        if message == False:
            print("Latest message is not from author")
            items_not_required += 1
            continue
        else:
            item_archived = False
            #First Level Follow Up comparison
            for keyValue in data.author_compare_message:
                if keyValue.lower() in str(message).lower():
                    if data.author_compare_message[keyValue]['response_type'] == data.FOLLOW_UP:
                        c.post_response(data.author_compare_message[keyValue]['response'])
                        return True, items_not_required
                    elif data.author_compare_message[keyValue]['response_type'] == data.RESPOND_IMAGE:
                        c.post_image_response(
                            data.author_compare_message[keyValue]['response'],
                            data.author_compare_message[keyValue]['image_path'])
                        return True, items_not_required
                    elif data.author_compare_message[keyValue]['response_type'] == data.ARCHIVE_CHAT:
                        c.archive_chat(l)
                        item_archived = True
            if item_archived == False:
                items_not_required +=1

            # elif "i saw this" in str(message).lower():
            #     c.post_response("Autobot sending response 2")
            #     return True
            # else:
            #     c.post_response("Hi. Just checking out")
            #     return True

    return False, items_not_required


def follow_up_message(debug_flag):
    if (c.DEBUG == debug_flag):
        print("**==>Debug Active")
        checking_latest_message_data()
        return False
    # Ensure position is top of screen
    scroll_status = full_scroll(-4000, 20)
    if SCROLL_ACTIVE == scroll_status:
        print("Too long to Scroll. Exiting")
        return 0
    elif scroll_status == PAGE_END: print("Reached bottom of page")

    #Scroll Up until top of page
    yesterday_message_detected = False
    items_not_required = 0
    while scroll_status != PAGE_TOP:
        pt.moveTo(1000,1000, duration=.25)
        locations = list((pt.locateAllOnScreen(data.yesterday_label, confidence=.7)))

        if len(locations) != 0:
            yesterday_message_detected = True
            print("THE LOCATION:", list(locations))
            status, temp = follow_up_from_active_page(locations)

            items_not_required +=temp
            print ("Status:", status, "RetVal: ", temp, "Item not required:", items_not_required)
            if status == True:
                scroll_status = full_scroll(-5000, 20)
                scroll_status = full_scroll(55*items_not_required, 0)
                continue
        else: break
        scroll_status = full_scroll(600, 0)
    print("Items not required:", items_not_required)
    return 1


# Navigate through current active message
# Check if message was from user
# Send Response
def checking_latest_message_data():
    message = check_if_latest_message_from_author()
    if message is False: return False
    else:
        if "value2" in str(message).lower():
            c.post_response(data.author_compare_message['MULTI_LINE']['response'])
            # c.post_image_response(
            #     data.author_compare_message['MULTI_LINE']['response'],
            #     data.author_compare_message['TEST_DATA_ONE']['image_path'])
            return True