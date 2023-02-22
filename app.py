from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, FlexSendMessage

app = Flask(__name__)

# 設定 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi(
    "mlQ7oqRMEbtzdaO0lG6BmHe2TxMyNv/nEn75lwpOZE0HR3W+nMB8PjBbrhlqOO5Ic7nie1aVaZZAjbDL4MJsz2jo+cMuPs2v/up2vmoIqv7RBxEx8VR9456FmZqjNc5k5I5j/Cwn3OzbLS5CT+4/BAdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("fa1fd1143b0de6b63018eda97d4dcbea")


# 定義處理用戶訊息的函數
def handle_message(event):
    if event.message.text == "我要預約":
        # 建立 FlexMessage
        flex_msg = FlexSendMessage(
            alt_text="長照預約",
            contents={
                "type": "bubble",
                "size": "kilo",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "請選擇您的區域",
                            "size": "xl",
                            "weight": "bold"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "台北長照",
                                "uri": "https://docs.google.com/forms/d/e/1FAIpQLSd_ll8O23_KXjSfT0CagFJc56iL_6HvTnrdbFBYLCnZ9CFqxQ/viewform"
                            },
                            "height": "sm",
                            "offsetBottom": "sm"
                        },
                        {
                            "type": "separator",
                            "margin": "xs"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "新北長照",
                                "uri": "http://linecorp.com/"
                            },
                            "offsetTop": "md"
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "桃園長照",
                                "uri": "http://linecorp.com/"
                            },
                            "offsetTop": "md"
                        }
                    ],
                    "alignItems": "center"
                },
                "styles": {
                    "body": {
                        "separator": true
                    }
                }
            }
        )

# 設定 Webhook 路由，接收 Line 平台發送的事件
@app.route('/callback', methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except:
        return 'Error'
    return 'OK'

# 設定處理用戶訊息的路由
@handler.add(MessageEvent, message=TextMessage)
def handle_message_event(event):
    handle_message(event)

if __name__ == '__main__':
    app.run()