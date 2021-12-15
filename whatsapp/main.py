import pyautogui as pt
from time import sleep
import pyperclip
import dataset as data
import follow_ups as fl
import common as c
# sleep(2) #sleep time before start - for setting up whatsapp initially

# Initial calibration. Requires user to open first chat and keep it active.
# # System checks this and only proceeds if this is true.
# position1 = pt.locateOnScreen(data.img_smiley_and_paperclip, confidence=.6)
# print("Position is: ", position1)
# x = position1[0]
# y = position1[1]

#Get the new message
def get_message():
    global x, y
    position = pt.locateOnScreen(data.img_smiley_and_paperclip, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration = .05)
    pt.moveTo(x+150, y-80, duration = .5 )
    pt.tripleClick()
    c.controlPress('c')
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

# Selects required label from  the label seletion pop-up and update label.
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

# Add a Chat Label to active message.
# Detects Edit Label option from the active message
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

#Checking for new message and respond
# check_for_new_messages()

#Follow Up Message module
# fl.follow_up_message()

data ={
    "key1":{
        'response_type': 1,
        'response': "Hello World",
        'image_path': r"C:\Users\sajid\Pictures\Family\ayrin_1.jpg",
    }
}

if(data["key1"]["response_type"]) == 1:
    print("True")

image_path = r"C:\Users\sajid\Pictures\Family\ayrin_1.jpg"
message = fl.latest_message_from_author()
if "wisholize" in message:
    position = pt.locateOnScreen(data.paperclip, confidence='.7')
    if position is not None:
        print("Paper clip located")
        pt.moveTo(position)
        pt.click()
        sleep(.5)
        image_upload_position = pt.locateOnScreen(data.upload_image, confidence='.9')
        pt.moveTo(image_upload_position)
        pt.click()
        sleep(1.5)
        pt.typewrite(str(image_path), interval=.01)
        pt.hotkey('enter')
        sleep(1.5)
        pt.hotkey('enter')


