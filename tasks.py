from fabric.api import *
from os import path
from os import makedirs
from util import *

class Command:
    def __init__(self, name, server, user, password):
        self.name = name
        self.server = server
        self.user = user
        self.password = password
    
    def configure_environment(self):
        env.user = self.user        
        if (path.isfile(self.password)):
            env.key_filename = self.password
        else:
            env.password = self.password

class SendAFile(Command, object):
    def __init__(self, name, server, user, password, local_path, remote_path):
        super(SendAFile, self).__init__(name, server, user, password)
        self.local_path = local_path
        self.remote_path = remote_path        
    def execute(self):
        tee(INFO, "--- Executing %s ---" % (self.name))
        with settings(host_string = self.server):
            self.configure_environment()            
            self.result = put(self.local_path, self.remote_path)              
        tee(INFO, "--- Finishing %s ---" % (self.name))
        

            
class SendATextFile(Command, object):
    def __init__(self, name, server, user, password, local_path, remote_path):
        super(SendAFile, self).__init__(name, server, user, password)
        self.local_path = local_path
        self.remote_path = remote_path
        
        if (path.exists(self.local_path)):
            local_file = open(self.local_path)
            content = local_file.read()
            
        self.file_content = """
        cat > %s  <<'EOF'
        \r%s""" % (self.remote_path, content)
        
    def execute(self):
        tee(INFO, "--- Executing %s ---" % (self.name))
        with settings(host_string = self.server):
            self.configure_environment()            
            self.result = run(self.file_content)              
        tee(INFO, "--- Finishing %s ---" % (self.name))
        
class ExecuteCommands(Command, object):
    def __init__(self, name, server, user, password, *command):
        super(ExecuteCommands, self).__init__(name, server, user, password)
        self.commands = command
        self.result = None
        
    def execute(self):
        tee(INFO, "--- Executing %s ---" % (self.name))
        with settings(host_string = self.server):
            self.results = []
            self.configure_environment()
            for command in self.commands:                
                result = run(command)
                self.results.append(result)
        tee(INFO, "--- Finishing %s ---" % (self.name))

    def __str__(self):
        return self.result
            
class CopyFilesPatternCommand(Command, object):
    def __init__(self, name, server, user, password, pattern, destination):
        super(CopyFilesPatternCommand, self).__init__(name, server, user, password)        
        self.pattern = pattern
        self.result = None
        self.destination = destination
        
    def execute(self):
        tee(INFO, "--- Executing %s ---" % (self.name))
        with settings(host_string = self.server):
            self.configure_environment()
            
            if not path.exists(self.destination):
                makedirs(self.destination)
                
            self.result = get(self.pattern, self.destination)
            print self.result
        tee(INFO, "--- Finishing %s ---" % (self.name))
