#1. Open a log file, read contents in it and, find IP addresses.
#2. Count 10 requests from IPs
#3. Write data to CSV File


import re
import csv as log

def reader(log):
#Read CSV file
   data_2 = log.read_csv(open['C:/Users/HERLAB26/Documents/Desktop/log.csv', 'r'])

   for data in log:
    def count(ips_list):
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.'

        ips_list = re.find(regexp, log)

        return
if log == '__main__':
    print('log.pdf')
else:
    print('Error')


def write_csv(counter):
    with open('output.csv', 'w') as log:
        writer = log.writer(log)

        header = ['IP', 'Frequency'.__iter__(log)]

        writer.write(header)

        for item in counter:
            writer.writerow(item)
            return
try:
    log == (log[:9])
except:
    print('Error')







