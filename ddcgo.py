#!/usr/bin/env python3

import csv
import os
import shutil
import sys
from time import sleep as sleep
# 000 Computer science, information & general works
# 100 Philosophy & psychology
# 200 Religion
# 300 Social sciences
# 400 Language
# 500 Science
# 600 Technology
# 700 Arts & recreation
# 800 Literature
# 900 History & geography
# All other categories will be organized below this in a heirarchy.
# The categorical heirerarchy herein contained is based on the 3 digit code in
# each category's respective title.
# 001 002 025 476, etc.  Starting with the first digit and proceeding to the
# next digit and then the last.
#
# Here we go.
#
# Stage one.  Create primary directories for 10 super-categories
ppath = os.path.abspath(os.path.dirname(sys.argv[0]))


if os.path.exists("dds"):
    shutil.rmtree("dds")
    sleep(0.1)
    os.mkdir("dds")
else:
    os.mkdir("dds")


with open('DDSGORun0.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        x = (f'{row[0]} - {row[1]}')
        os.mkdir(f'dds\{x}')

with open('DDSGORun1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # this number will be 010 or 020 check first digit and change into 000
        # or 100 or 200 etc
        a = row[0]
        b = row[1]
        x = (f'{a} - {b}')
        #print(x)
        prefix = (f'{a[:1]}00')
        os.chdir('dds')
        lst = os.listdir()
        path = [x for x in lst if prefix in x]
        os.chdir(path[0])
        x = (f'{row[0]} - {row[1]}')
        os.mkdir(x)
        os.chdir(ppath)


with open('DDSGORun2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        a = row[0]
        b = row[1]
        x = (f'{a} - {b}')
        # print(x)
        os.chdir(f'{ppath}\dds')
        prefix = (f'{a[:1]}00')
        lst = os.listdir()
        firstpath = [x for x in lst if prefix in x]
        os.chdir(firstpath[0])
        #print(firstpath[0])
        prefix2 = (f'{a[:2]}0')
        lst = os.listdir()
        secondpath = [x for x in lst if prefix2 in x]
        os.chdir(secondpath[0])
        print(secondpath[0])
        os.mkdir(x)
