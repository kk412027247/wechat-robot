import itchat
import threading


def send_qr_code(uuid, status, qrcode):
    with open('1.png', 'wb') as f:
        f.write(qrcode)
    print('send qr code')


def login_success():
    print('login_success')


sentences = [
    {'type': 'string', 'content': 'aaa'},
    {'type': 'image', 'content': 'cat.jpg'},
    {'type': 'string', 'content': 'ccc'},
    {'type': 'video', 'content': 'v.mp4'},
]

itchat.auto_login(qrCallback=send_qr_code, loginCallback=login_success, hotReload=True)

def sender(counter=0):
    if counter < len(sentences):
        if(sentences[counter]['type'] == 'string'):
            itchat.send(sentences[counter]['content'], toUserName='filehelper')
        elif (sentences[counter]['type'] == 'image'):
            itchat.send_image(sentences[counter]['content'], toUserName='filehelper')
        elif (sentences[counter]['type'] == 'video'):
            itchat.send_video(sentences[counter]['content'], toUserName='filehelper')
        else:
            pass
        counter += 1
    else:
        itchat.send('finish', toUserName='filehelper')
        return
    t = threading.Timer(1, sender, (counter,))
    t.start()

sender()
