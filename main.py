#!/usr/bin/python
# -*- coding: utf-8 -*-
from tasks import ExecuteCommands, CopyFilesPatternCommand, SendAFile
from os import path
from os import sep

CURR_PATH = path.dirname(path.realpath(__file__))

if __name__ == '__main__':
    #ec = ExecuteCommands("ls command", "10.81.80.12", "ericsson", "ericsson", "ls ~", "free -m")
   #ec.execute()
    
    #cfp = CopyFilesPatternCommand("copy logs", "146.250.180.201","ericsson", "ericsson", "/home/ericsson/*.log", CURR_PATH + sep + "logs")
    #cfp.execute()
    
    #saf = SendAFile("Send file","146.250.180.201","ericsson", "ericsson", "/home/rcls/FITec/MrRobot/tasks.py", "/home/ericsson/tasks.py")
    #saf.execute()
    
    ec = ExecuteCommands("ls command", "52.34.50.54", "ec2-user", "/home/rcls/FITec/MrRobot/ADOTrail.pem", "ls ~", "free -m")
    ec.execute()
    print "".center(50,'-')
    #Check SVN MACHINE    
    redmine = ExecuteCommands("BACKUP REDMINE", "146.250.180.201", "ericsson", "ericsson", "ls -lh /srv/backup-redmine/files", "free -m", "df -h" ,"date")
    redmine.execute()
    svn = ExecuteCommands("BACKUP SVN", "146.250.180.201", "ericsson", "ericsson", "ls -lh /srv/backup-svn/svn", "date")
    svn.execute()
    
    print "".center(50,'-')
    #Check AOP MACHINE
    aop = ExecuteCommands("AOP STATS", "146.250.180.202", "aop", "aop", "free -m", "df -h" ,"date")
    aop.execute()
    