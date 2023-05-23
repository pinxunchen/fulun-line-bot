from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    FlexSendMessage, BubbleContainer, BoxComponent,
    ButtonComponent, PostbackAction, MessageAction
)

app = Flask(__name__)

# 設定 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('mlQ7oqRMEbtzdaO0lG6BmHe2TxMyNv/nEn75lwpOZE0HR3W+nMB8PjBbrhlqOO5Ic7nie1aVaZZAjbDL4MJsz2jo+cMuPs2v/up2vmoIqv7RBxEx8VR9456FmZqjNc5k5I5j/Cwn3OzbLS5CT+4/BAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fa1fd1143b0de6b63018eda97d4dcbea')

# 定義處理用戶訊息的函數
def handle_message(event):

    # 如果接收到的訊息是「___」，則回覆一個 FlexMessage
    if event.message.text == '我要預約':
        flex_message = FlexSendMessage(
            alt_text='我要預約',
            contents={
            "type": "bubble",
            "size": "kilo",
            "hero": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "image",
                  "size": "xl",
                  "aspectMode": "cover",
                  "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/src/booking.png",
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
                  "offsetStart": "lg",
                  "weight": "bold"
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
                    "uri": "https://liff.line.me/1660683719-5mAggVBG"
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
                            "uri": "https://reurl.cc/WLle1D"
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
                              "text": "桃園長照",
                              "margin": "xxl",
                              "size": "md",
                              "align": "center",
                              "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://reurl.cc/Nq5lr5"
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
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "愛接送(交通自費)",
                                      "margin": "xxl",
                                      "size": "md",
                                      "align": "center",
                                      "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": "https://reurl.cc/14yn0D"
                                      }
                                    }
                                  ]
                                }
                              ]
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
            alt_text='文件下載',
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
                          "type": "image",
                          "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/src/document.png",
                          "size": "lg",
                          "margin": "md"
                        },
                        {
                          "type": "text",
                          "text": "爬梯機相關文件",
                          "size": "xl",
                          "weight": "bold",
                          "contents": [],
                          "offsetStart": "md",
                          "margin": "xl",
                          "offsetBottom": "lg"
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
                          "text": "新北長照文件",
                          "size": "xl",
                          "contents": [
                            {
                              "type": "span",
                              "text": "新北",
                              "size": "xxl",
                              "color": "#DA70D6"
                            },
                            {
                              "type": "span",
                              "text": "  爬梯機文件"
                            }
                          ],
                          "offsetStart": "lg",
                          "margin": "xl",
                          "offsetBottom": "sm",
                          "weight": "bold"
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
                              "align": "center",
                              "weight": "regular"
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
                              "color": "#FF9900"
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
                                  "text": "租賃紀錄表"
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
                                      "text": "購買證明"
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
                                          "text": "台北爬梯機DM",
                                          "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "台北爬梯機DM"
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

    if event.message.text == '訂車查詢':
        flex_message = FlexSendMessage(
            alt_text='訂車查詢',
            contents={
            "type": "bubble",
            "size": "kilo",
            "hero": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "image",
                  "size": "lg",
                  "aspectMode": "cover",
                  "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/src/conclusion.png",
                  "margin": "xl",
                  "offsetStart": "md"
                },
                {
                  "type": "text",
                  "text": "訂車查詢",
                  "size": "xl",
                  "weight": "bold",
                  "margin": "none",
                  "offsetTop": "md",
                  "contents": [],
                  "offsetStart": "lg"
                },
                {
                  "type": "text",
                  "text": "查詢紀錄以及個案長照資格",
                  "size": "sm",
                  "color": "#1E90FF",
                  "offsetTop": "md",
                  "offsetStart": "lg",
                  "weight": "bold"
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
                  "text": "我的趟次",
                  "size": "md",
                  "align": "center",
                  "margin": "lg",
                  "offsetBottom": "md"
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
                          "text": "歷史紀錄",
                          "size": "md",
                          "align": "center",
                          "margin": "xxl"
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
                              "text": "長照資格查詢",
                              "margin": "xxl",
                              "size": "md",
                              "align": "center"
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

    if event.message.text == '輔具額度':
        flex_message = FlexSendMessage(
            alt_text='輔具額度',
            contents={
            "type": "bubble",
            "size": "kilo",
            "hero": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "image",
                  "size": "lg",
                  "aspectMode": "cover",
                  "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/src/caculation11.png",
                  "margin": "xl",
                  "offsetStart": "xs"
                },
                {
                  "type": "text",
                  "text": "輔具額度相關",
                  "size": "xl",
                  "weight": "bold",
                  "margin": "none",
                  "offsetTop": "md",
                  "contents": [],
                  "offsetStart": "lg"
                },
                {
                  "type": "text",
                  "text": "查詢輔具預估剩餘額度及補收試算",
                  "size": "sm",
                  "color": "#1E90FF",
                  "offsetTop": "md",
                  "offsetStart": "lg",
                  "weight": "bold"
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
                  "text": "餘額查詢",
                  "size": "md",
                  "align": "center",
                  "margin": "lg",
                  "offsetBottom": "md"
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
                          "text": "補收試算",
                          "size": "md",
                          "align": "center",
                          "margin": "xxl"
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
                              "text": "待補收紀錄",
                              "margin": "xxl",
                              "size": "md",
                              "align": "center"
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

    if event.message.text == 'LINE連結':
        flex_message = FlexSendMessage(
            alt_text='LINE連結',
            contents={
            "type": "bubble",
            "size": "kilo",
            "hero": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "image",
                      "size": "lg",
                      "aspectMode": "cover",
                      "url": "https://raw.githubusercontent.com/pinxunchen/fulun-line-bot/master/src/line%20(1).png",
                      "margin": "xl",
                      "offsetStart": "xs"
                    }
                  ],
                  "paddingAll": "lg"
                },
                {
                  "type": "text",
                  "text": "Line相關連結",
                  "size": "xl",
                  "weight": "bold",
                  "margin": "none",
                  "offsetTop": "md",
                  "contents": [],
                  "offsetStart": "lg"
                },
                {
                  "type": "text",
                  "text": "點擊下方可跳轉到該Line頁面",
                  "size": "md",
                  "color": "#1E90FF",
                  "offsetTop": "md",
                  "offsetStart": "lg",
                  "weight": "bold"
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
                  "text": "台北爬梯機特約",
                  "size": "md",
                  "align": "center",
                  "margin": "lg",
                  "offsetBottom": "md",
                  "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://lin.ee/gYmP75J"
                  }
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
                          "text": "新北爬梯機特約",
                          "size": "md",
                          "align": "center",
                          "margin": "xxl",
                          "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://lin.ee/F9sIMMq",
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
                              "text": "桃園爬梯機特約",
                              "margin": "xxl",
                              "size": "md",
                              "align": "center",
                              "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://lin.ee/m0VEwln"
                              }
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
                                  "type": "text",
                                  "text": "基隆爬梯機特約",
                                  "margin": "xxl",
                                  "size": "md",
                                  "align": "center",
                                  "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://lin.ee/UhJHNZj"
                                  }
                                }
                              ]
                            }
                          ],
                          "offsetBottom": "sm"
                        }
                      ]
                    }
                  ],
                  "offsetBottom": "md"
                }
              ],
              "offsetTop": "sm"
            }
          }


            )
        line_bot_api.reply_message(event.reply_token, flex_message)

    if event.message.text == '補收試算':
        flex_message = create_flex_message()
        line_bot_api.reply_message(event.reply_token, flex_message)


def create_flex_message():
    flex_message = FlexSendMessage(
        alt_text='補收試算',
        contents=BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                contents=[
                    ButtonComponent(
                        style='primary',
                        color='#0000FF',
                        height='sm',
                        action=PostbackAction(
                            label='一般戶',
                            data='一般戶'
                        )
                    ),
                    ButtonComponent(
                        style='primary',
                        color='#FF0000',
                        height='sm',
                        action=PostbackAction(
                            label='中低收',
                            data='中低收'
                        )
                    ),
                    ButtonComponent(
                        style='primary',
                        color='#00FF00',
                        height='sm',
                        action=PostbackAction(
                            label='低收',
                            data='低收'
                        )
                    )
                ]
            )
        )
    )
    return flex_message

@app.route("/postback", methods=['POST'])
def handle_postback():
    data = request.json['events'][0]['postback']['data']
    if data == '一般戶' or data == '中低收' or data == '低收':
        flex_message = create_flex_message_floor(data)
        line_bot_api.reply_message(request.json['events'][0]['replyToken'], flex_message)
    elif data.startswith('樓層'):
        floor = int(data.split(':')[1])
        user_id = request.json['events'][0]['source']['userId']
        reply_text = f"請輸入剩餘額度（樓層：{floor}，身份別：{data.split(':')[2]}）"
        line_bot_api.push_message(user_id, TextSendMessage(text=reply_text))

def create_flex_message_floor(identity):
    flex_message = FlexSendMessage(
        alt_text='選擇樓層',
        contents=BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='vertical',
                contents=[
                    ButtonComponent(
                        style='primary',
                        color='#0000FF',
                        height='sm',
                        action=PostbackAction(
                            label='一二樓',
                            data=f'樓層:1:身份別:{identity}'
                        )
                    ),
                    ButtonComponent(
                        style='primary',
                        color='#FF0000',
                        height='sm',
                        action=PostbackAction(
                            label='三樓',
                            data=f'樓層:3:身份別:{identity}'
                        )
                    ),
                    ButtonComponent(
                        style='primary',
                        color='#00FF00',
                        height='sm',
                        action=PostbackAction(
                            label='四五樓',
                            data=f'樓層:4:身份別:{identity}'
                        )
                    )
                ]
            )
        )
    )
    return flex_message


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