#1. Open a log file, read contents in it and, find IP adresses.
#2. Count requests from IPs
#3. Write data to a CSV File

import re
import csv
from collections import counter


def reader(filename):
    with open(filename) as f:
        log = f.read()

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.'

        ips_list = re.findall(regexp,log)

        return(ips_list)


def count(ips_list):
    return counter(ips_list)


def write_csv(counter):
    with open('output.csv','w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP','Frequency']

        writer.writerow(header)

        for item in counter:
            writer.writerow(item,counter[item])



if __name__ == '__main__':
    write_csv(count(reader('log')))

