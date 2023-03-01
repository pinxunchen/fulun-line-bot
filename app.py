from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pyodbc

app = Flask(__name__)

server = '192.168.1.224'
database = 'Test'
username = 'sa'
password = '31095184qweRt'
cnxn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# 設定 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('mlQ7oqRMEbtzdaO0lG6BmHe2TxMyNv/nEn75lwpOZE0HR3W+nMB8PjBbrhlqOO5Ic7nie1aVaZZAjbDL4MJsz2jo+cMuPs2v/up2vmoIqv7RBxEx8VR9456FmZqjNc5k5I5j/Cwn3OzbLS5CT+4/BAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fa1fd1143b0de6b63018eda97d4dcbea')

# 定義處理用戶訊息的函數
def handle_message_event(event):
    # 判斷接收到的事件是否為文字訊息事件
    if event.type == "message" and event.message.type == "text":
        # 使用process_text_message函式處理文字訊息
        result = process_text_message(event)
        # 將處理結果封裝成TextSendMessage物件，並回覆訊息給使用者
        if result:
            message = TextSendMessage(text=result)
            line_bot_api.reply_message(event.reply_token, message)

def process_text_message(event):
    # 取得使用者輸入的文字訊息
    user_input = event.message.text
    # 使用使用者輸入的文字訊息作為查詢條件，查詢"employees"資料表中符合條件的記錄
    cursor = cnxn.cursor()
    query = f"SELECT * FROM 叫車資料 WHERE Name='{user_input}'"
    cursor.execute(query)
    rows = cursor.fetchall()
    # 如果查詢結果不為空，則將查詢結果返回給使用者；否則，回傳一個提示訊息
    if rows:
        result = ""
        for row in rows:
            result += f"ID:{row[0]}, Name:{row[1]}, Date:{row[2]}\n"
        return result
    else:
        return "No matching records found."

    
    

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
    handle_message_event(event)

if __name__ == '__main__':
    app.run()