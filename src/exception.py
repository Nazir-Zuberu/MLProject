import sys # provides variables and func to manipulate parts of a python runtime. It helps identify the source of an error and other details
import logging




def error_message_detail(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    # Locating the name of the file where the error occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
       file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # Over writing the __init__ in the parent class Exception and passing the error_message variable to it
        # Assigning the error_message extracted by error_message_detail
        # error_message gives the error message and error_details gives specifics about the source of the error
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
# A function to return the error message
    def __str__(self):
        return self.error_message
