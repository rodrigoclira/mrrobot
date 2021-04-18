from datetime import datetime 

ERROR = 'ERROR'
WARN = 'WARN'
INFO = 'INFO'
LOGNAME = 'mrrobot.log'

logfile = open (LOGNAME, 'a')

def tee(typeinfo , information , printable = True):
    
    line = ('[%s][%s]  ' + information) % (datetime.now(), typeinfo)
    
    if printable:
        print line
    
    if logfile:
        logfile.write(line + '\n')