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
                "uri": "https://github.com/pinxunchen/fulun-line-bot/raw/master/%E9%A6%96%E6%AC%A1%E5%88%87%E7%B5%90%E6%9B%B8.pdf"
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


    if event.message.text == '文件下載':
        flex_message = FlexSendMessage(
            alt_text='訂車網址',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "爬梯機相關文件",
            "size": "xxl",
            "weight": "bold",
            "contents": [],
            "offsetStart": "lg",
            "margin": "xl",
            "offsetBottom": "sm"
          },
          {
            "type": "text",
            "text": "點擊下方選單可下載文件",
            "offsetStart": "lg",
            "offsetBottom": "sm",
            "size": "md",
            "color": "#1E90FF",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#8B4513"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "福倫小簽單",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#BEBEBE",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "首次切結書",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#BEBEBE",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "size": "lg",
                    "align": "center",
                    "text": "輔具購買證明"
                  },
                  {
                    "type": "separator",
                    "margin": "md",
                    "color": "#BEBEBE"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "租賃紀錄表 (履帶)",
                        "size": "lg",
                        "align": "center"
                      },
                      {
                        "type": "separator",
                        "margin": "md",
                        "color": "#BEBEBE"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "租賃紀錄表 (撐桿)",
                            "size": "lg",
                            "align": "center"
                          }
                        ],
                        "margin": "md",
                        "paddingTop": "sm"
                      }
                    ],
                    "paddingTop": "lg"
                  }
                ],
                "paddingTop": "lg"
              }
            ],
            "paddingTop": "lg"
          }
        ],
        "paddingTop": "md"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "新北長照文件",
            "size": "xl",
            "weight": "bold",
            "contents": [
              {
                "type": "span",
                "text": "新北",
                "size": "xxl",
                "color": "#E680FF"
              },
              {
                "type": "span",
                "text": "  爬梯機文件"
              }
            ],
            "offsetStart": "lg",
            "margin": "xl",
            "offsetBottom": "sm"
          },
          {
            "type": "text",
            "text": "點擊下方選單可下載文件",
            "offsetStart": "lg",
            "offsetBottom": "sm",
            "size": "md",
            "color": "#1E90FF",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#8B4513"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "請款表電子檔下載",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#BEBEBE",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "請款表範例",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#BEBEBE",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "size": "lg",
                    "align": "center",
                    "text": "新北爬梯機DM",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "新北爬梯機DM"
                    }
                  },
                  {
                    "type": "separator",
                    "margin": "md",
                    "color": "#BEBEBE"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "size": "lg",
                        "align": "center",
                        "text": "預留"
                      },
                      {
                        "type": "separator",
                        "color": "#BEBEBE",
                        "margin": "md"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "size": "lg",
                            "align": "center",
                            "text": "預留"
                          }
                        ],
                        "paddingTop": "lg"
                      }
                    ],
                    "paddingTop": "lg"
                  }
                ],
                "paddingTop": "lg"
              }
            ],
            "paddingTop": "lg"
          }
        ],
        "paddingTop": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "台北長照文件",
            "size": "xl",
            "weight": "bold",
            "contents": [
              {
                "type": "span",
                "text": "台北",
                "size": "xxl",
                "color": "#FFCC00"
              },
              {
                "type": "span",
                "text": "  爬梯機文件"
              }
            ],
            "offsetStart": "lg",
            "margin": "xl",
            "offsetBottom": "sm"
          },
          {
            "type": "text",
            "text": "點擊下方選單可下載文件",
            "offsetStart": "lg",
            "offsetBottom": "sm",
            "size": "md",
            "color": "#1E90FF",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#8B4513"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "交通出勤報表",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#BEBEBE",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "收據黏貼表",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#BEBEBE",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "size": "lg",
                    "align": "center",
                    "text": "核可編號範例"
                  },
                  {
                    "type": "separator",
                    "margin": "md",
                    "color": "#BEBEBE"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "size": "lg",
                        "align": "center",
                        "text": "台北爬梯機 DM",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "台北爬梯DM"
                        }
                      },
                      {
                        "type": "separator",
                        "color": "#BEBEBE",
                        "margin": "md"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "size": "lg",
                            "align": "center",
                            "text": "預留",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "核可編號範例"
                            }
                          }
                        ],
                        "paddingTop": "lg"
                      }
                    ],
                    "paddingTop": "lg"
                  }
                ],
                "paddingTop": "lg"
              }
            ],
            "paddingTop": "lg"
          }
        ],
        "paddingTop": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "桃園爬梯機相關文件",
            "size": "xl",
            "weight": "bold",
            "contents": [
              {
                "type": "span",
                "text": "桃園",
                "size": "xxl",
                "color": "#A52A2A"
              },
              {
                "type": "span",
                "text": "  爬梯機文件"
              }
            ],
            "offsetStart": "lg",
            "margin": "xl",
            "offsetBottom": "sm"
          },
          {
            "type": "text",
            "text": "點擊下方選單可下載文件",
            "offsetStart": "lg",
            "offsetBottom": "sm",
            "size": "md",
            "color": "#1E90FF",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#8B4513"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "服務租賃請款表",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#BEBEBE",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "租賃紀錄表",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#BEBEBE",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "size": "lg",
                    "align": "center",
                    "text": "長照輔具租賃領據"
                  },
                  {
                    "type": "separator",
                    "margin": "md",
                    "color": "#BEBEBE"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "報告書範例",
                        "size": "lg",
                        "align": "center"
                      },
                      {
                        "type": "separator",
                        "margin": "md",
                        "color": "#BEBEBE"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "桃園爬梯機 DM",
                            "size": "lg",
                            "align": "center",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "桃園爬梯機DM"
                            }
                          }
                        ],
                        "margin": "md",
                        "paddingTop": "sm"
                      }
                    ],
                    "paddingTop": "lg"
                  }
                ],
                "paddingTop": "lg"
              }
            ],
            "paddingTop": "lg"
          }
        ],
        "paddingTop": "md"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "桃園爬梯機相關文件",
            "size": "xl",
            "weight": "bold",
            "contents": [
              {
                "type": "span",
                "text": "基隆",
                "size": "xxl",
                "color": "#FF4D00"
              },
              {
                "type": "span",
                "text": "  爬梯機文件"
              }
            ],
            "offsetStart": "lg",
            "margin": "xl",
            "offsetBottom": "sm"
          },
          {
            "type": "text",
            "text": "點擊下方選單可下載文件",
            "offsetStart": "lg",
            "offsetBottom": "sm",
            "size": "md",
            "color": "#1E90FF",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "md",
            "color": "#8B4513"
          }
        ],
        "paddingAll": "md"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "服務租賃紀錄表",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#BEBEBE",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "輔具購買補助證明",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#BEBEBE",
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "size": "lg",
                    "align": "center",
                    "text": "個案契約書"
                  },
                  {
                    "type": "separator",
                    "margin": "md",
                    "color": "#BEBEBE"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "輔具照片",
                        "size": "lg",
                        "align": "center"
                      },
                      {
                        "type": "separator",
                        "margin": "md",
                        "color": "#BEBEBE"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "基隆爬梯機 DM",
                            "size": "lg",
                            "align": "center",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "基隆爬梯機DM"
                            }
                          }
                        ],
                        "margin": "md",
                        "paddingTop": "sm"
                      }
                    ],
                    "paddingTop": "lg"
                  }
                ],
                "paddingTop": "lg"
              }
            ],
            "paddingTop": "lg"
          }
        ],
        "paddingTop": "md"
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