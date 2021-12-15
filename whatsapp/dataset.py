import cv2

#PATHS
temp_path = r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\temp"
##Image Assets
img_smiley_and_paperclip = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\smiley_and_paperclip.png")
green_circle = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\green_circle.png")
chat_and_menu = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\chat_and_menu.png")
labels = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\labels.png")
message_menu = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\message_menu.png")
edit_label = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\edit_label.png")
bottom_label_star = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\bottom_label-star.png")
todo_label = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\todo.png")
save_btn = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\save.png")
reply_label = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\reply.png")
yesterday_label = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\yesterday.png")
mic = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\mic.png")
paperclip = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\paperclip.png")
upload_image = cv2.imread(r"C:\Users\sajid\Documents\_SAJID\Works\Wisholize\whatsappBot\assets\upload_image.png")

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

follow_up_message = "Have you selected the keychain model from the link above sir ?"

author_compare_message = "machine learning"