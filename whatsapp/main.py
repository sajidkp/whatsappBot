import pyautogui as pt
from time import sleep
import pyperclip
import dataset as data

sleep(2) #sleep time before start - for setting up whatsapp initially

position1 = pt.locateOnScreen(data.img_smiley_and_paperclip, confidence=.6)
print("Position is: ", position1)
x = position1[0]
y = position1[1]

# Function to press Control + a key stroke
def controlPress( value):
    with pt.hold('ctrl'):
        pt.press(value)

#Get the new message
def get_message():
    global x, y
    position = pt.locateOnScreen(data.img_smiley_and_paperclip, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration = .05)
    pt.moveTo(x+150, y-80, duration = .5 )
    pt.tripleClick()
    controlPress('c')
    whatsappMessage = pyperclip.paste()
    #Remove Selection and move mouse slightly so that it retain initial status
    pt.click()
    pt.moveRel(-100,0)
    pt.moveRel(100,0)
    print("Whatsapp Message is: " + whatsappMessage)

    return whatsappMessage

#Post Response
def post_response(message):
    global x, y
    position = pt.locateOnScreen(data.img_smiley_and_paperclip, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+250, y+20, duration=.5)
    pt.click()

    if type(message) == list:
        for line in message:
            pt.typewrite(str(line), interval=.01)
            pt.hotkey('ctrl','enter')
    else:
        pt.typewrite(str(message), interval=.01 )
    pt.typewrite("\n", interval=.01)

#Process response
def process_response(message):
    if "i saw this" in str(message).lower():
        return data.instagram_link_response_message + data.offer_message

    else:
        return False

#Label Addition function from a message selection
def update_label():
    try:
        position = pt.locateOnScreen(data.bottom_label_star, confidence=.6)
        if position is not None:
            pt.moveTo(position, duration=.5)
            pt.moveRel(-30,0)
            pt.click()
            sleep(.5)
            #find label with text "Reply"
            position = pt.locateOnScreen(data.reply_label, confidence=.6)
            if position is not None:
                pt.moveTo(position, duration=.5)
                pt.click()
                sleep(.5)
            else:
                print("Reply label not found. Escape to initial state.")
                pt.press('esc')
                sleep(.5)
                pt.press('esc')
                return False

            position = pt.locateOnScreen(data.save_btn, confidence=.6)
            if position is not None:
                pt.moveTo(position)
                pt.click()
                sleep(.5)
            else:
                print("Save Button not found. Escape to initial state")
                pt.press('esc')
                sleep(.5)
                pt.press('esc')
                return False

            return True
    except (Exception):
        print("Bottom label not located")


#Add Chat Label
def add_chat_label(msg_x, msg_y):
    try:
        position = pt.locateOnScreen(data.message_menu, confidence=.6)
        if position is not None:
            pt.moveTo(position, duration=.5)
            pt.moveRel(10,10)
            pt.click()
            sleep(.5)
            edit_label_position = pt.locateOnScreen(data.edit_label, confidence=.6)
            if edit_label_position is not None:
                pt.moveTo(edit_label_position[0], edit_label_position[1])
                pt.click()
                sleep(.5)
                update_label()
        else:
            print("Arrow not detected")

        return True

    except(Exception):
        print("Message drop down menu not detected")
        return False

#Check for new messages
def check_for_new_messages():
    msg_x = int(x+120)
    msg_y = int(y-55)
    pt.moveTo(msg_x, msg_y, duration=.5)
    while True:
        #Continuously check for new message
        try:
            position = pt.locateOnScreen(data.green_circle, confidence=.6)

            if position is not None:
                print("Located new message")
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except (Exception):
            print("No new messages found")

        if pt.pixelMatchesColor(msg_x, msg_y, (38,45,49), tolerance=10):
            print("is white")
            try:
                processed_response = process_response(get_message())
                if processed_response: post_response(processed_response)
                else:
                    add_chat_label(msg_x, msg_y)
                    post_response(data.no_action_response)

            except (Exception):
                print("Whatsapp Window not active")
        else:
            print("No new messages yet...")

        sleep(3)

check_for_new_messages()

