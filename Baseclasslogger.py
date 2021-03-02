import logging
class Baselogger:



    def getlog(self):
        log = logging.getLogger(__name__)  # this will testfile mname

        filehandler = logging.FileHandler('logingfile.log')  # it is like filehandle object for giving path for handler
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        # to set level which n all from which level u want to print log from the given log
        log.addHandler(filehandler)
        log.setLevel(logging.DEBUG)
        return log
