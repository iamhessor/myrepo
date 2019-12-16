  GNU nano 4.3                                                         telegram.py                                                                  
import requests
import socket

sock = socket.socket()
sock.bind(('', 10000))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break

def send_telegram(text: str ):
    token = "1040086308:AAHn8tkAFzbA-d6W_xUm8F-evaXLcz8tILc"
    url = "https://api.telegram.org/bot"
    channel_id = "491256943"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("I am alive!")
conn.close()
