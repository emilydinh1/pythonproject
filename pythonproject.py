import re
import collections
import datetime
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

##local_copy = r"\Users\emily\Documents\http_access_log.txt"
totalrequests_lastyear = 0
totalrequests = 0

# This line opens the log file
f=open('local_copy.log', "r")

# This line takes each line in the log file and stores it as an element in the list
lines = f.readlines()

#Creates dictionaries for dates and months
date_counts = {}
months_counts = {}

#Loop to read each line and split based off of spaces
#Checks to see that each line has 9 elements and then checks to see that in the third item there are at least 19 characters
#Takes string and replaces the square bracket with a space
#Looks at date and months
for line in lines:
   line = line.split(" ")
   str1 = " "
   if len(line) == 9:
      if len(line[3]) >= 19:
         str1 = line[3].replace('[', '')
         str1 = str1[0:11]
         date_obj = datetime.datetime.strptime(str1, '%d/%b/%Y').date()
         month_obj = date_obj.month

         #Loops through to count how many files were made in each day
         if str1 in date_counts:
            date_counts[str1] += 1
         else:
            date_counts[str1] = 1

         #Loops through to count how many file were made in each month
         if month_obj in months_counts:
            months_counts[month_obj] += 1
         else:
            months_counts[month_obj] = 1

         
#Prints out how many were made in each day and each month
print(date_counts)
print(months_counts)

#Creates a dictionary for the files
files = {}

#Checks to see that each line has 9 items then checks to see that in the 6th item, there are at least 3 characters
for line in lines:
   line = line.split(" ")
   str1 = " "
   if len(line) == 9:
      if len(line[6]) >= 3:
         str1 = line[6].replace('"', '').replace('>', '')
         #if str1 == 'index.html':
         #   print(str1)
         
         #Loops to count different types of files
         if str1 in files:
            files[str1] += 1
         else:
            files[str1] = 1

#Sorts files to take first and last element for the least and most requested files
#print(files)
sorted_files = sorted(files)
print("The least requested file:", sorted_files[0])
print("The most requested file:", sorted_files[len(sorted_files)-1])

#Declares variables 
notsuccess_requests = 0
redirected_requests = 0


#Reads through each line and if there is anytime 4xx (x being wildcards) then it adds to counter
for line in lines:   
   notsuccess_requests +=1
   for i in range(400, 499):
      if line.find(str(i)) != -1:
         notsuccess_requests += 1

#Reads through each line and if there is anytime 3xx (x being wildcards) then it adds to counter
for line in lines:   
   redirected_requests +=1
   for i in range(300, 399):
      if line.find(str(i)) != -1:
         redirected_requests += 1

   


for line in lines:
   totalrequests +=1
   if line.find("1995") != -1:
      totalrequests_lastyear += 1


#Declares my variables
#Also finds the percentage of successful and redirected requests out of total requests
percentsuc = 0
percentsuc = notsuccess_requests / totalrequests
percentredir = 0
percentredir = redirected_requests / totalrequests

f.close() 
#Prints out information
print("\nLast Year Requests: ", totalrequests_lastyear)
print("Total Requests: ", totalrequests)
print("Not successful requests with 4xx status code in percentage:  ", (percentsuc))
print("Redirected requests with 3xx status code in percentage: ", (percentredir))


