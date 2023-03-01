
def flex_massage_booking():  
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
    return  flex_message