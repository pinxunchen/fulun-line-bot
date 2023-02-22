from linebot.models import (
    FlexSendMessage, BubbleContainer, BoxComponent, TextComponent,
    ButtonComponent, SeparatorComponent, URIAction
)
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, FlexSendMessage
import json


def handle_message(event):
    message = event.message.text
    if message == '我要預約':
        # 建立BubbleContainer
        bubble = BubbleContainer(
            size='kilo',
            header=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='請選擇您的區域', size='xl', weight='bold')
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    ButtonComponent(
                        action=URIAction(uri='https://docs.google.com/forms/d/e/1FAIpQLSd_ll8O23_KXjSfT0CagFJc56iL_6HvTnrdbFBYLCnZ9CFqxQ/viewform',
                                         label='台北長照'),
                        height='sm',
                        offsetBottom='sm'
                    ),
                    SeparatorComponent(margin='xs'),
                    ButtonComponent(
                        action=URIAction(uri='http://linecorp.com/', label='新北長照'),
                        offsetTop='md'
                    ),
                    SeparatorComponent(margin='md'),
                    ButtonComponent(
                        action=URIAction(uri='http://linecorp.com/', label='桃園長照'),
                        offsetTop='md'
                    )
                ],
                alignItems='center'
            ),
            styles={
                'body': {'separator': True}
            }
        )

        # 建立FlexSendMessage
        flex_message = FlexSendMessage(alt_text='請選擇您的區域', contents=bubble)

        # 回覆訊息
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