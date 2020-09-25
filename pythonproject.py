from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

# This line opens the log file
f=open('local_copy.log', "r")

# This line takes each line in the log file and stores it as an element in the list
lines = f.readlines()

linesplit = line.split()
for line in lines:
   if line.find("1995") = 1:
    print lines
    
    
    #print(line.split())
##sfsafdsafsafsafs ssfdsdf testing