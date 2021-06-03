from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('6D3uPq6/EcQM2HSo89EogoTUscTIk8+cwXsrOShGEI76TpOAZQmkpvL7pwQP0YAenayWQYWqrQ7S0sATZvqx5CdMQ9/qLcV5BN3D07H67Eei/chJB6d1IUCXxtrr4PMlYfhHxEjRQavohaJs6te17QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('83de04c484d27744f7e928ba03e74c9f')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    msg = msg.encode('utf-8')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(debug=True,port=80)