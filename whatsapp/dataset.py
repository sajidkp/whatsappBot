import cv2

#PATHS
temp_path = r"D:\Applications\whatsappBot\assets\temp"

#------------------------------Image Assets-------------------------------------------------

img_smiley_and_paperclip = cv2.imread(r"D:\Applications\whatsappBot\assets\smiley_and_paperclip.png")
green_circle = cv2.imread(r"D:\Applications\whatsappBot\assets\green_circle.png")
chat_and_menu = cv2.imread(r"D:\Applications\whatsappBot\assets\chat_and_menu.png")
labels = cv2.imread(r"D:\Applications\whatsappBot\assets\labels.png")
message_menu = cv2.imread(r"D:\Applications\whatsappBot\assets\message_menu.png")
edit_label = cv2.imread(r"D:\Applications\whatsappBot\assets\edit_label.png")
bottom_label_star = cv2.imread(r"D:\Applications\whatsappBot\assets\bottom_label-star.png")
todo_label = cv2.imread(r"D:\Applications\whatsappBot\assets\todo.png")
save_btn = cv2.imread(r"D:\Applications\whatsappBot\assets\save.png")
reply_label = cv2.imread(r"D:\Applications\whatsappBot\assets\reply.png")
yesterday_label = cv2.imread(r"D:\Applications\whatsappBot\assets\yesterday.png")
mic = cv2.imread(r"D:\Applications\whatsappBot\assets\mic.png")
paperclip = cv2.imread(r"D:\Applications\whatsappBot\assets\paperclip.png")
upload_image = cv2.imread(r"D:\Applications\whatsappBot\assets\upload_image.png")
archive_chat = cv2.imread(r"D:\Applications\whatsappBot\assets\archive_chat.png")

# Images for messages
KCMini_models = r"D:\Applications\whatsappBot\assets\message_images\KCMini_Models.jpg"
BikeShape1 = r"D:\Applications\whatsappBot\assets\message_images\BikeShape1.png"

#----------------------------- Image Assets End ----------------------------------------------

instagram_keychain_links = [
    "https://instagram.com/CA4fBx9A-CH",
    "TESTDATASET"
]


instagram_link_response_message = [
    "*Keychains Link:*",
    "  ",
    "https://www.wisholize.com/collections/personalised-key-chain-online.",
    "   ",
    "Please choose the keychain model from the link above and share here. We can do vehicle logos on any of the models above."]

offer_message = [
    "\n"
    "Limited Period Offer!",
    "Buy any 2 keychains, Get 2 personalised face masks free!",
    "    ",
    "Reply YES if interested.",
    "Masks link: https://www.wisholize.com/collections/face-mask"
]

no_action_response = "Thanks for reaching out. We shall get back to you shortly. Meanwhile, please visit our website www.wisholize.com to check out our offerings."

follow_up_message = "Limited Period Offer!"

#---------------------------FOLLOW UPS ------------------------------------------------
# Follow up comparison messages and its responses to be added here.

# Response Types
FOLLOW_UP = 1
RESPOND_IMAGE = 2
ARCHIVE_CHAT = 3

#Data Set
author_compare_message = {
    "Limited Period Free Masks Offer" : {
        'response_type': FOLLOW_UP,
        'response': "Have you selected the keychain model needed from the link above sir?",
    },
    "Please check the link above and share the keychain model needed" : {
        'response_type': FOLLOW_UP,
        'response': "Have you selected the keychain model needed from the link above sir?",
    },
    "If you are interested, i will share the poster here" : {
        'response_type': FOLLOW_UP,
        'response': "Are you interested in this offer sir?",
    },
    "The back side of the keychain can be engraved with your name or phone number" : {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Number plate design can be done only on the front side" : {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Rs 239" : {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Rs 233" : {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Rs 333": {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Mob number:" : {
        'response_type': FOLLOW_UP,
        'response': "Please share the details to proceed with the order.",
    },
    "Upon payment confirmation, I will create the order and share order details.": {
        'response_type': FOLLOW_UP,
        'response': "Please share to proceed with the order.",
    },
    "Vehicle shape keychains - ₹333": {
        'response_type': FOLLOW_UP,
        'response': "Which one do you need sir?",
    },
    "May I know which product category you are interested in so that I can provide the details": {
        'response_type': FOLLOW_UP,
        'response': ['Please visit our website', 'www.wisholize.com', 'to view all products with details. You can share the product here so that we can proceed further.', '', 'Category page link:', 'https://www.wisholize.com/pages/product-categories'],
    },
    "We appreciate your efforts in finding only the best for you and your loved ones": {
        'response_type': FOLLOW_UP,
        'response': ['Guarantee:', '', 'We promise to keep the authenticity of the product as described on the product page. As told, it will be personalized with your desired content and delivered to  your doorstep.', '', 'We currently work in association with courier partners (DTDC, Professional Courier & Speed Post) with whom we shall follow-up closely and ensure the products reach you on time. Tracking details also shall be made available to you once shipped. ', '', 'A refund or replacement as eligible will be provided if the product does not get delivered or is damaged in transit.'],
    },
    "Have you selected the keychain model needed from the link above sir": {
        'response_type': RESPOND_IMAGE,
        'response': ["", ""],
        'image_path': [KCMini_models, BikeShape1],
    },
    " We can do vehicle logos on any of the models above": {
        'response_type': RESPOND_IMAGE,
        'response': ["", ""],
        'image_path': [KCMini_models, BikeShape1],
    },
    "Please share to proceed with the order":{
        'response_type': ARCHIVE_CHAT,
    },
    "Please share the details to proceed with the order":{
        'response_type': ARCHIVE_CHAT,
    },
    "Thank you for your time":{
        'response_type': ARCHIVE_CHAT,
    },
    "Mini Number Plate Keychain Models!":{
        'response_type': ARCHIVE_CHAT,
    },
    "Which one do you need sir": {
        'response_type': ARCHIVE_CHAT,
    },
    "Do you wish to proceed with the order sir":{
        'response_type': ARCHIVE_CHAT,
    },
    "https://www.wisholize.com/pages/product-categories":{
        'response_type': ARCHIVE_CHAT,
    },
    "A refund or replacement as eligible will be provided if the product doesn't get delivered or is damaged in transit.":{
        'response_type': ARCHIVE_CHAT,
    },
    "Hi Sir":{
        'response_type': ARCHIVE_CHAT,
    },
    "Are you interested in this offer sir":{
        'response_type': ARCHIVE_CHAT,
    },
    "Please let me know if you have any queries or need any help.": {
        'response_type': ARCHIVE_CHAT,
    },
    "DEMO SAMPLE DATA":{
        'response_type': ARCHIVE_CHAT,
    },
    "TEST_DATA" : {
        'response_type': RESPOND_IMAGE,
        'response': ["FIRST VALUE", "TEST 2"],
        'image_path': [KCMini_models, KCMini_models],
    },
    "TEST_DATA_ONE": {
        'response_type': RESPOND_IMAGE,
        'response': "FIRST VALUE2",
        'image_path': KCMini_models,
    },
    "MULTI_LINE": {
        'response_type': FOLLOW_UP,
        'response': ['test line 1', 'test linew2'],
    }
}

#-----------------------FOLLOW UPS END--------------------------------------------------
