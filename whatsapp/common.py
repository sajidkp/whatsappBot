import pyautogui as pt
import dataset as data

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
