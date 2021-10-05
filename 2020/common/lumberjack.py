import logging
import os

# Most of this has evolved through play and following elements of the basic
# tutorial found here :
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

# It was discussed that the 'best practice' would be a call to
# "configure_logger" function at the entry point to your code. e.g. main()
# before calling any other code.
# We  /haven't/ done this here because we wanted to experiment with setting up 2
# independent logger configurations and playing with them.

def main():

    # Gotcha 1 : The following call to logging was commented out because it
    # effectively sets up a 'root' logger with default handlers and then
    # subsequent attempts to use logging.basicConfig have no effect.
    #logging.info("Starting....")
    toms_place()
    emmas_house()
    #logging.info("Collapsing....")

    
def configure_emmas_logger():

    # create a logger
    logger = logging.getLogger()

    # setup a file handler for this logger
    file_handler = logging.FileHandler("Emmas.log", "w")

    # Set the logging level for this file handler
    file_handler.setLevel(logging.INFO)

    # Setting up a formatting object for a file handler.
    logger_format = "Emma says : %(levelname)s : %(funcName)s :"\
        " %(asctime)s : %(message)s"
    file_formatter = logging.Formatter(logger_format, datefmt="%s")
    # Actually set the formatter of the file handler
    file_handler.setFormatter(file_formatter)
    # for more info on formatting fun see :
    # https://docs.python.org/3.6/library/logging.html#logrecord-attributes

    # Finally add the configured file handler to the logger.
    logger.addHandler(file_handler)

def configure_toms_logger():
    logger_format = "%(levelname)s : %(filename)s : %(funcName)s :"\
        " %(asctime)s : %(message)s"
    # Sets up a basic logger which writes to file all messages at DEBUG or above
    logging.basicConfig(filename="Toms.log", level=logging.DEBUG, filemode='w',
        format=logger_format, datefmt="%M %S")
    

def emmas_house():
    configure_emmas_logger()
    # we've passede "__name__" here as it's a good way to implement module level
    # logger. For more details see : 
    # https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
    logger = logging.getLogger(__name__)
    logger.info("Hello Emma")

    logger.warning("Awooga awooga Emma")

def toms_place():
    configure_toms_logger()
    logger = logging.getLogger(__name__)
    logger.info("Hello Tom")

    logger.warning("Awooga awooga Tom")


if __name__ == '__main__':
    main()


#=====================================================================
# Further reading :
# Tom says : example for configuring other modules:
# https://stackoverflow.com/questions/11029717/how-do-i-disable-log-messages-from-the-requests-library
#
# Rhiannon says : example for loging in cylc:
# https://web.yammer.com/main/threads/eyJfdHlwZSI6IlRocmVhZCIsImlkIjoiMTM5NTEwNTkwMTM1NTAwOCJ9
