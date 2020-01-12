import itchat
import threading

def send_qr_code(uuid, status, qrcode):
    with open('1.png', 'wb') as f:
        f.write(qrcode)
    print('send qr code')

def login_success():
    print('login_success')

sentences = ['aaa', 'bbbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']

itchat.auto_login(qrCallback=send_qr_code, loginCallback=login_success, hotReload=True)

def sender(counter=0):
    if counter < len(sentences):
        itchat.send(sentences[counter], toUserName='filehelper')
        counter += 1
    else:
        itchat.send('finish', toUserName='filehelper')
        return
    t = threading.Timer(1, sender, (counter,))
    t.start()

sender()
