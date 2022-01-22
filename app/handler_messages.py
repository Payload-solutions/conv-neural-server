
from typing import Any


def response_conv_handler(message: str,
                  type: str = "SUCESS", **content):
    print(content)
    if type == "ERROR":
        return {
            "type": "ERROR",
            "description":message
        }
    
    return {
        "type":"SUCESS",
        "description":message,
        "content": {
            "low_prediction":content["low"],
            "non_prediction":content["non"],
            "reg_prediction":content["reg"]
        }

    }
