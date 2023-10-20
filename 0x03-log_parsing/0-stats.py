#!/usr/bin/python3
"""
   Log parsing: reads stdin line by line and computes metrics (file size
   and status code
   format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
   <status code> <file size>
   data printed after every 10 lines and/or a keyboard interruption (CTRL + C)
"""


import re
import fileinput


def printData(data, file_size):
    """
       print the data in a specific format:
       File size: <total size>
       Number of lines by status code: <status code>: <number>
    """
    print("File size: {:d}".format(file_size))
    for key, value in data.items():
        if (value != 0):
            print("{:d}: {:d}".format(key, value))
            data[key] = 0


def read_stdin():
    data = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0}
    file_size = 0
    form = "^([0-9]{1,3}\.){3}[0-9]{1,3} - (\[[0-9]{4}-[0-9]{2}-[0-9]{2} (\
[0-9]{2}:){2}[0-9]{2}\.[0-9]{6}\]) \"GET \/projects\/260 HTTP\/1\.1\" (\
200|301|400|401|403|404|405|500) [0-9]+$"
    cycle = 0
    try:
        for line in fileinput.input():
            if (re.search(form, line)):
                collect = line.split('"')[-1].strip().split(" ")
                data[int(collect[0].strip())] += 1
                file_size += int(collect[1])
                cycle += 1

            if (cycle == 10):
                printData(data, file_size)
                cycle = 0
    except KeyboardInterrupt:
        printData(data, file_size)


read_stdin()
