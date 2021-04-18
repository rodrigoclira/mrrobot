from fabric.api import *
from os import path
from sys import argv
from tasks import ExecuteCommands, CopyFilesPatternCommand, SendAFile

if __name__ == '__main__':
    
    domain = argv[1]
    local_path = argv[2]
    remote_path = argv[3]
    user =  argv[4]
    key_file = argv[5]
    
    war_dev = SendAFile("NAT WAR", domain, user, key_file, local_path, remote_path)
    war_dev.execute()  

    stop_tomcat = ExecuteCommands("Tomcat", domain, user, key_file, "sudo service tomcat7 stop", "sudo rm -rf /var/lib/tomcat7/last-webapps/*",
                                   "sudo mv /var/lib/tomcat7/webapps/new-ado* /var/lib/tomcat7/last-webapps/",
                                   "sudo cp " + remote_path + "/new-ado.war /var/lib/tomcat7/webapps/", "sudo service tomcat7 start")
    stop_tomcat.execute()
    
