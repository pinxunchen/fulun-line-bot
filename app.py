from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, FlexSendMessage

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


    if event.message.text == '常見問題':
        flex_message = FlexSendMessage(
            alt_text='常見問題',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/question.png"
          },
          {
            "type": "text",
            "text": "查詢常見問題",
            "margin": "md",
            "weight": "bold",
            "size": "lg",
            "offsetTop": "md",
            "offsetStart": "md"
          }
        ]
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
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "如何預約",
                    "size": "lg",
                    "align": "center",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "如何預約"
                    }
                  }
                ],
                "paddingAll": "sm"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "交通收費相關",
                    "align": "center",
                    "size": "lg",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "交通收費"
                    }
                  }
                ],
                "paddingAll": "xl"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "爬梯機相關",
                    "align": "center",
                    "size": "lg",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "爬梯機相關"
                    }
                  }
                ],
                "paddingAll": "sm"
              }
            ],
            "paddingAll": "md"
          }
        ],
        "spacing": "md",
        "offsetBottom": "sm",
        "paddingAll": "xs"
      },
      "styles": {
        "body": {
          "separator": true
        }
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": []
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": []
      }
    }
  ]
}
            )
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