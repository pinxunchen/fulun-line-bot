class FlexMessages:
    def __init__(self):
        self.google_message = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": "Google", "weight": "bold", "size": "xl"},
                    {"type": "text", "text": "https://www.google.com/", "color": "#0072C6", "size": "sm", "wrap": True},
                ],
                "action": {"type": "uri", "label": "Google", "uri": "https://www.google.com/"}
            },
        }
        
        self.yahoo_message = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": "Yahoo", "weight": "bold", "size": "xl"},
                    {"type": "text", "text": "https://www.yahoo.com/", "color": "#720e9e", "size": "sm", "wrap": True},
                ],
                "action": {"type": "uri", "label": "Yahoo", "uri": "https://www.yahoo.com/"}
            },
        }
    
    def get_message(self, text):
        if text == "google":
            return self.google_message
        elif text == "yahoo":
            return self.yahoo_message
        else:
            return None
