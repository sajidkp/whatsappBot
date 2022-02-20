import pyautogui as pt
import dataset as data
from time import sleep

LIVE = 0
DEBUG = -1


# Function to press Control + a key stroke
def controlPress( value):
    with pt.hold('ctrl'):
        pt.press(value)

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


def send_image(response, image_path):
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
        pt.typewrite(str(image_path), interval=.02)
        pt.hotkey('enter')
        sleep(2)
        pt.typewrite(str(response), interval=.02)
        pt.hotkey('enter')
        sleep(.5)
        return True

# Post Image Response
def post_image_response(response_message, image_path):

    if type(response_message) == list and type(image_path) == list:
        print("Both items are list")
        for response, path in zip(response_message, image_path):
            print(response, path)
            send_image(response, path)
            sleep(1)
    elif type(response_message) == list:
        for response in response_message:
            send_image(response, image_path)
    elif type(image_path) ==list:
        for path in image_path:
            send_image(response_message, path)
    else:
        send_image(response_message, image_path)

# Post Image Response
def post_catalog_response(response_message, image_path):

    if type(response_message) == list and type(image_path) == list:
        print("Both items are list")
        for response, path in zip(response_message, image_path):
            print(response, path)
            send_image(response, path)
            sleep(1)
    elif type(response_message) == list:
        for response in response_message:
            send_image(response, image_path)
    elif type(image_path) ==list:
        for path in image_path:
            send_image(response_message, path)
    else:
        send_image(response_message, image_path)



def archive_chat(location):
    pt.moveTo(location, duration=.5)
    pt.mouseDown(button='right')
    pt.mouseUp(button='right')
    sleep(1.5)
    l = pt.locateOnScreen(data.archive_chat, confidence='.9')
    print("ARCHIVE LOCATION : ", l)
    pt.moveTo(l, duration=.5)
    pt.click()
    sleep(1)
    return True
