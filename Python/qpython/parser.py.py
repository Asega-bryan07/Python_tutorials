# #1. Open a log file, read contents in it and, find IP addresses.
# #2. Count requests from IPs
# #3. Write data to CSV File

# import re
# import csv
# from collections import counter
# import analysis


# def reader(filename):
#     with open(filename) as f:
#         log = f.read()

#         regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.'

#         ips_list = re.find(regexp,log)

#         return(ips_list)


# def count(ips_list):
#     return counter(ips_list)


# def write_csv(counter):
#     with open('output.csv','w') as csvfile:
#         writer = csv.writer(csvfile)

#         header = ['IP','Frequency'.__iter__(csvfile)]

#         writer.writerow(header)

#         for item in counter:
#             writer.writerow(item)
# #4. For try and except:
# try:
#     log == Counter [:9]
# except FrequencyError:
#     print('Frequency error occured')

# #5. For if and else
# if __name__ == '__main__':
#     write_csv(count(reader('log')))
# else:
#     print('Error')


length = 10
witdth = 20

area = length * witdth
# == != (> or < =), <>
if area == 200:
    print("Area is equal to 200")
else:
    print(f'The area of the reactengle is: {area}')



































