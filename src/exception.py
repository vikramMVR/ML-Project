import sys  # sys module gives access to exception details like traceback
from src.logger import logging  # importing logging from your custom logger module (make sure logger is set up correctly)

def error_message_detail(error, error_detail: sys):
    # This function formats a detailed error message including filename, line number, and error text

    _, _, exc_tb = error_detail.exc_info()
    # exc_info() returns a tuple of (exception type, exception value, traceback object)
    # We only need the traceback (exc_tb), so we use _ for the unused values

    file_name = exc_tb.tb_frame.f_code.co_filename
    # Get the filename from the traceback where the exception occurred

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # Format a readable message with: file name, line number, and the actual error message

    return error_message  # Return the complete custom error message


    
class CustomException(Exception):  # Inheriting from the built-in Exception class
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the parent Exception class constructor with error message

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
        # Create a detailed error message using the above function
        # and store it in the instance variable `self.error_message`

        logging.error(self.error_message)
        # Log the error using your custom logger (saved in a log file if configured)

    def __str__(self):
        return self.error_message
        # Override __str__ method so when print() or str() is called on the exception,
        # it returns the detailed error message instead of default text






    


        