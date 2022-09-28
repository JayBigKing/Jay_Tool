import os
import logging
import time
import colorlog
from enum import Enum

class WhichHandler(Enum):
   STRRAM_HANDLER = 0,
   FILE_HANDLER = 1

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
messageTypeSet = {
    logging.ERROR,
    logging.WARNING,
    logging.INFO,
    logging.DEBUG
}

consoleLogger = None
fileLogger = None

def myLogger_Init(level = logging.INFO, loggerFileName : str = ""):
    if loggerFileName == "":
        loggerFileName = r'../logs/%s%s.log' % ("log", str(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())))

    global consoleLogger
    global fileLogger
    consoleLogger = logging.getLogger("consoleLogger")
    fileLogger = logging.getLogger("fileLogger")
    consoleLogger.setLevel(level)
    fileLogger.setLevel(level)

    consoleLoggerFmt = colorlog.ColoredFormatter(
        fmt = '%(log_color)s%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-12s : %(lineno)s line - %(message)s',
        datefmt = "%Y-%m-%d %H:%M:%S",
        log_colors = log_colors_config
    )
    fileLoggerFmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-12s : %(lineno)s line - %(message)s")

    consoleLoggerHandler = logging.StreamHandler()
    if os.path.exists(loggerFileName[:loggerFileName.rfind('/')]) is False:
        os.mkdir(loggerFileName[:loggerFileName.rfind('/')])
    fileLoggerHandler = logging.FileHandler(filename=loggerFileName, mode='w', encoding = 'UTF-8')
    consoleLoggerHandler.setFormatter(consoleLoggerFmt)
    fileLoggerHandler.setFormatter(fileLoggerFmt)

    consoleLogger.addHandler(consoleLoggerHandler)
    fileLogger.addHandler(fileLoggerHandler)



def myLogger_PushOutMessageBase(messageType, whichHandler, message : str = ""):
    global consoleLogger
    global fileLogger
    try:
        if consoleLogger is None or fileLogger is None:
            raise AttributeError('Logger has not initial')
        if whichHandler != WhichHandler.STRRAM_HANDLER and  whichHandler != WhichHandler.FILE_HANDLER:
            raise KeyError('error handler, there are only console or file handler served.')
        if messageType in messageTypeSet is False:
            raise KeyError('error messageType, there are only error, warn, info and debug message served.')
    except (AttributeError, KeyError) as e:
        print(r'%s' % repr(e))
    else:
        if whichHandler == WhichHandler.STRRAM_HANDLER:
            pushOutLogger = consoleLogger
        else:
            pushOutLogger = fileLogger

        if messageType == logging.ERROR:
            pushOutLogger.error(message)
        elif messageType == logging.WARNING:
            pushOutLogger.warning(message)
        elif messageType == logging.INFO:
            pushOutLogger.info(message)
        else:
            pushOutLogger.debug(message)



def myLogger_ConsoleError(message : str = ""):
    myLogger_PushOutMessageBase(logging.ERROR, WhichHandler.STRRAM_HANDLER, message)

def myLogger_ConsoleWarning(message : str = ""):
    myLogger_PushOutMessageBase(logging.WARNING, WhichHandler.STRRAM_HANDLER, message)

def myLogger_ConsoleInfo(message : str = ""):
    myLogger_PushOutMessageBase(logging.INFO, WhichHandler.STRRAM_HANDLER, message)

def myLogger_ConsoleDebug(message : str = ""):
    myLogger_PushOutMessageBase(logging.DEBUG, WhichHandler.STRRAM_HANDLER, message)

def myLogger_FileError(message : str = ""):
    myLogger_PushOutMessageBase(logging.ERROR, WhichHandler.FILE_HANDLER, message)

def myLogger_FileWarning(message : str = ""):
    myLogger_PushOutMessageBase(logging.WARNING, WhichHandler.FILE_HANDLER, message)

def myLogger_FileInfo(message : str = ""):
    myLogger_PushOutMessageBase(logging.INFO, WhichHandler.FILE_HANDLER, message)

def myLogger_FileDebug(message : str = ""):
    myLogger_PushOutMessageBase(logging.DEBUG, WhichHandler.FILE_HANDLER, message)

def myLogger_Error(message : str = ""):
    myLogger_ConsoleError(message)
    myLogger_FileError(message)

def myLogger_Warning(message : str = ""):
    myLogger_ConsoleWarning(message)
    myLogger_FileWarning(message)

def myLogger_Info(message : str = ""):
    myLogger_ConsoleInfo(message)
    myLogger_FileInfo(message)

def myLogger_Debug(message : str = ""):
    myLogger_ConsoleDebug(message)
    myLogger_FileDebug(message)


myLogger_Init()