# if an exception is a subclass lets say B -> C -> D
# and we raise exception B first, then C and D
# Every thing will be B,B,B
# Specific block exception first

import sys
import logging
# Although it is not used, importing the logger file will apply its configuration
import logger


def error_message_detail(error, error_detail:sys):
    _,_,exception_traceback = error_detail.exc_info()
    file_name = exception_traceback.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}].format()".format(
        file_name,exception_traceback.tb_lineno, str(error)
    )
    return error_message 

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a= 1/0
#     except Exception as e:
#         # Logging info is 
#         # Longging message with severity level info
#         logging.info("Divide zero error")
#         raise CustomException(e,sys)
