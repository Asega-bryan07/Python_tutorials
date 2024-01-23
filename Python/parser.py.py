#1. Open a log file, read contents in it and, find IP addresses.
#2. Count requests from IPs
#3. Write data to CSV File


import re
import pdf
from collections import counter
import analysis


def reader(log):
   csv_file=CSV.reader(open['C:/Users/HERLAB26/Documents/Desktop/log.csv','r'])
   for data in pdf_file:

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.'

        ips_list = re.find(regexp,log.pdf)

        return(ips_list)


def count(ips_list):
    return counter(ips_list[:9])


def write_csv(counter):
    with open('output.csv','w') as csvfile:
        writer = csv.writer(csv_file)

        header = ['IP','Frequency'.__iter__(csvfile)]

        writer.writerow(header)

        for item in counter:
            writer.writerow(item)
#4. For try and except:
try:
    log == (log.pdf[:9])
except FrequencyError:
    print('Frequency error occured')

#5. For if and else
if __name__ == '__main__':
    write_csv(count(reader('log.pdf')))
else:
    print('Error')

