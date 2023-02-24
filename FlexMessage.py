from linebot.models import (
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, URIAction, MessageAction
)

class FlexMessage:
    def __init__(self):
        self.google_flex_message = self.create_google_flex_message()
        self.yahoo_flex_message = self.create_yahoo_flex_message()

    def create_google_flex_message(self):
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                size='full',
                aspect_ratio='16:5',
                aspect_mode='cover'
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='Google', weight='bold', size='xl'),
                    TextComponent(text='Click to visit Google', wrap=True),
                ]
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    URIAction(
                        uri='https://www.google.com',
                        label='Visit Google'
                    )
                ]
            )
        )

        return FlexSendMessage(alt_text='Google', contents=bubble)

    def create_yahoo_flex_message(self):
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='Yahoo', weight='bold', size='xl'),
                    TextComponent(text='Click to visit Yahoo', wrap=True),
                ]
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    URIAction(
                        uri='https://www.yahoo.com',
                        label='Visit Yahoo'
                    )
                ]
            )
        )

        return FlexSendMessage(alt_text='Yahoo', contents=bubble)

    def get_flex_message(self, message_text):
        if message_text == 'google':
            return self.google_flex_message
        elif message_text == 'yahoo':
            return self.yahoo_flex_message
        else:
            return None
