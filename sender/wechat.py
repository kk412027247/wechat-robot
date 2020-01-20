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


toUserName =  '@@b75736b44727b142f8789ae3ac4eaab4babbef84b2f2bf85b14d1fc9532a1481'

def sender(counter=0):
    if counter < len(sentences):
        if(sentences[counter]['type'] == 'string'):
            itchat.send(sentences[counter]['content'], toUserName=toUserName)
        elif (sentences[counter]['type'] == 'image'):
            itchat.send_image(sentences[counter]['content'], toUserName=toUserName)
        elif (sentences[counter]['type'] == 'video'):
            itchat.send_video(sentences[counter]['content'], toUserName=toUserName)
        else:
            pass
        counter += 1
    else:
        itchat.send('finish', toUserName=toUserName)
        return
    t = threading.Timer(1, sender, (counter,))
    t.start()

sender()
