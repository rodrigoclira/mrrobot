#!/usr/bin/python
# -*- coding: utf-8 -*-
from tasks import ExecuteCommands, CopyFilesPatternCommand, SendAFile
from os import path
from os import sep

if __name__ == '__main__':
    
    #ec = ExecuteCommands("ls command", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", "ls ~", "free -m")
    #ec.execute()
    
    #copy_war = CopyFilesPatternCommand("Copy War", "146.250.180.202", "aop", "aop", "/var/lib/jenkins/workspace/new-admanager/project-web/target/new-ado.war", "./new-ado.war")
    #copy_war.execute()
    
    local_path = "/home/rcls/ADO_workspace/newADO/new-admanager-trunk/project-web/target/new-ado.war"
    nat_file = SendAFile("NAT WAR", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", local_path, "~")
    nat_file.execute()
    
    local_path = "/home/rcls/FITec/MrRobot/deploy_dev.py"
    ec = SendAFile("Copy Script to Net", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", local_path, "~")
    ec.execute()
    
    local_path = "/home/rcls/FITec/MrRobot/tasks.py"
    ec = SendAFile("Copy Script to Net", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", local_path, "~")
    ec.execute()
    
    local_path = "/home/rcls/FITec/MrRobot/util.py"
    ec = SendAFile("Copy Script to Net", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", local_path, "~")
    ec.execute()
    
    command = r'python ~/deploy_dev.py "%s" "%s" "%s" "%s" "%s"' %("11.0.1.100", "~/new-ado.war", "/home/ubuntu", "ubuntu", "/home/ec2-user/ADODev.pem")
    ec = ExecuteCommands("Execute Script", "dev.adorchestrator.ericsson.net", "ec2-user", "/home/rcls/FITec/MrRobot/ADODev.pem", command)
    ec.execute()
    