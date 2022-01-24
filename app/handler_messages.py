
from typing import (
    Any,
    Dict
)



def response_conv_handler(message: Any=None,
        type: str = "SUCCESS", content=None):

    if type == "ERROR":
        if message is not None:
            return {
                "type": "ERROR",
                "description":message
            }
        else:
            return {
                "type":"ERROR",
                "description":"Not process"
            }
    if content is not None:
        return {
            "type":"SUCESS",
            "content":content 
        }
