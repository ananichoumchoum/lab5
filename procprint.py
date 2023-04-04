import re
import glob

def info1(stat_file):
    names = []
    names2 = []
    string1 = 'T'
    for dir in glob.glob('/proc/[0-9]*/' + stat_file):
        if stat_file == 'status':
            with open(dir) as fh:
                content2 = fh.readline()
                name = re.split(':',content2)
                names.append(name[1][1:-1])
                content1 = fh.read()
                name2 = re.split('\(|\)', content1)
                names2.append(name2[1])
                if name2 == 'Stopped':
                   print(names2, "FileNotFindError")
        elif stat_file == 'stat':
            with open(dir) as fh:
                content = fh.read()
                name = re.split('\(|\)', content)
                names.append(name[1])   
                if string1 in content:
                    print( names, "FileNotFindError")        
    return names

stat_file = input('please enter stat or status: ')
print (info1(stat_file))
