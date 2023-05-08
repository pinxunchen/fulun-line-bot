from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, FileSendMessage

app = Flask(__name__)

# 設定 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('mlQ7oqRMEbtzdaO0lG6BmHe2TxMyNv/nEn75lwpOZE0HR3W+nMB8PjBbrhlqOO5Ic7nie1aVaZZAjbDL4MJsz2jo+cMuPs2v/up2vmoIqv7RBxEx8VR9456FmZqjNc5k5I5j/Cwn3OzbLS5CT+4/BAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fa1fd1143b0de6b63018eda97d4dcbea')

# 定義處理用戶訊息的函數
def handle_message(event):
    
    # 如果接收到的訊息是「我想預約」，則回覆一個 FlexMessage
    if event.message.text == '我想預約':
        flex_message = FlexSendMessage(
            alt_text='訂車網址',
            contents={"type": "bubble",
            "size": "kilo",
            "hero": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
             "type": "image",
             "size": "lg",
             "aspectMode": "cover",
        "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/booking.png",
        "margin": "xl"
      },
      {
        "type": "text",
        "text": "請選擇預約區域",
        "size": "lg",
        "weight": "bold",
        "margin": "none",
        "offsetTop": "md",
        "contents": [],
        "offsetStart": "lg"
      },
      {
        "type": "text",
        "text": "填寫表單後，將由客服推播趟次",
        "size": "sm",
        "color": "#1E90FF",
        "offsetTop": "md",
        "offsetStart": "lg"
      },
      {
        "type": "separator",
        "margin": "xl",
        "color": "#BEBEBF"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "台北長照",
        "size": "md",
        "align": "center",
        "margin": "lg",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        },
        "offsetBottom": "sm"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "margin": "lg",
            "color": "#BEBEBE"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "新北長照",
                "size": "md",
                "align": "center",
                "margin": "xxl",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://linecorp.com/"
                }
              },
              {
                "type": "separator",
                "margin": "lg",
                "color": "#BEBEBE"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "僅愛接送(自費交通)",
                    "margin": "xxl",
                    "size": "md",
                    "align": "center",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://linecorp.com/"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "offsetBottom": "md"
      }
    ]
  }
}
)
        line_bot_api.reply_message(event.reply_token, flex_message)


    if event.message.text == '首次切結書':
        message = FileSendMessage(original_content_url='https://drive.google.com/drive/u/0/folders/1uNaK2F8KJC28JC3nmKUKOCPfXfJN2o0J', file_name='首次切結書.pdf')
        line_bot_api.reply_message(event.reply_token, message)


    


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