from flask import Flask, request, abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)

################################

from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api =('"cMvM+WpdeI8C8b0nRfWjEihrAZGt5+AsAPBEB0y6ljs3RHnVmPiCsKODBmcKfN0I7yqRC2egO6kvQP2kfqMOlxkzfNfaQNrBVKIXwTkgkYiTsJddVAaD2jDBPJr+MaiIXzbt31VAnI7F39laivITbQdB04t89/1O/w1cDnyilFU="')
# Channel Secret
handler = WebhookHandler('"789d3e1a07e119832fd17b788dcd2266"')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID

    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "想要詢問甚麼?"
    else:
        reply_text = text
#如果非以上的選項，就會學你說話

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
