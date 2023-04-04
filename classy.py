import re
import psutil
import glob, os

procstat = {"R": "Running", "S": "Sleeping", "D": "Waiting", "Z": "Zombie", "T": "Stropped", "I": "Idle"}
attribs = {1: 'pid', 2: 'name', 3: 'state', 22: 'starttime', 24: 'rss', 25: 'rsslim', 26: 'start_code', 27:'end_code', 28: 'start_stack', 45: 'start_data', 46: 'end_data', 47: 'start_brk', 48: 'arg_start', 49: 'arg_end', 50: 'start_env', 51: 'end_env' }

class LinuxProcess:
    def __init__(self, path):
        self.path = path
        ab = []
        with open(path) as fh:
            content = fh.read()
            ab1 = re.split('\(|\)', content)
            ab.extend(ab1[0:2])
            ab2 = ab1[2].split()
            ab.extend(ab2)
            
            for value in attribs.items():
                val_attr = ab[value[0]-1]
                if value[0] == 3:
                    val_attr = procstat[ab[2]]
                self.linsetattr(value[1],val_attr)
               
                
    def linsetattr(self, attr, value):
        setattr(self, attr, value)
        print('\t\t\t',attr,":", value)
        
    def lingetattr(self, attr):
        return getattr(self, attr, None)
        

def get_psutil_data(inputs, user):
        if inputs == 'children':
            procs = psutil.Process().children()
            print(procs)
        if inputs == 'cmdline':
            for p in psutil.process_iter():
                print (p.cmdline())
                print (' '.join(p.cmdline()))
        if inputs == 'connections':
           print(psutil.net_connections())                
        if inputs == 'create_time':
            p = psutil(os.getpid)
            print(p.create_time())

        
pid = []  
count = 0      
for dir in glob.glob('/proc/[0-9]*/'):
    num = dir.split('/')[2]
    pid.append(int(num))
for x in pid:
    count += 1
    print('{:5d}'.format(x), end=(' ' if count < 10 else "\n"))
    if count == 10:
        count = 0
    
user = input("\n\nPlease select one of the PID provided above: ")
path = '/proc/'+ user + '/stat'
new1 = LinuxProcess(path)
inputs = input("If you want to quit press CTRL+C, If you want to get more result enter(children, cmdline, connections or create_time): ")

new2 = get_psutil_data(inputs, user)

