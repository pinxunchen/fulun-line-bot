from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, FlexSendMessage
from flex_message import create_google_flex_message

app = Flask(__name__)

# 設定 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('mlQ7oqRMEbtzdaO0lG6BmHe2TxMyNv/nEn75lwpOZE0HR3W+nMB8PjBbrhlqOO5Ic7nie1aVaZZAjbDL4MJsz2jo+cMuPs2v/up2vmoIqv7RBxEx8VR9456FmZqjNc5k5I5j/Cwn3OzbLS5CT+4/BAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fa1fd1143b0de6b63018eda97d4dcbea')

# 定義處理用戶訊息的函數
def handle_message(event):
    
    # 如果接收到的訊息是「我要預約」，則回覆一個 FlexMessage，包含訂車網址的超連結
    if event.message.text == '我要預約':
        flex_message = FlexSendMessage(
            alt_text='訂車網址',
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
            "weight": "bold",
            "margin": "none",
            "offsetStart": "md",
            "offsetTop": "sm"
            }
            ],
            "offsetTop": "md",
            "offsetStart": "xs"
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "text",
            "text": "台北長照",
            "size": "lg",
            "align": "center",
            "margin": "xl",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
            },
            {
            "type": "separator",
            "margin": "lg"
            },
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "新北長照",
                "size": "lg",
                "align": "center",
                "margin": "xl",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "separator",
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "桃園長照",
                    "margin": "xl",
                    "size": "lg",
                    "align": "center",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://linecorp.com/"
                    }
                  }
                ],
                "paddingBottom": "sm"
                }
                ]
                } ]}]} })
        line_bot_api.reply_message(event.reply_token, flex_message)

    elif event.message.text == 'google':
        flex_message = FlexSendMessage(alt_text='Google', contents=create_google_flex_message())
        line_bot_api.reply_message(event.reply_token, flex_message)










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