#!/usr/local/bin/python3
# -*- coding: utf-8 -*- 
import os,re,sys,time
import math,random
import csv
import numpy as np
import re


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sys.stdin=open('in.txt','r')

file_path = './OHIDataSet.csv'
header = []
data = []
Answer = ['yes','no','not applicable','I don\'t know']

def load_dataset(f = file_path):
    global header,data
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)[:-1]
        for row in reader:
            data.append(row[:-1])
    print(header)
    print('Total lines in this dataset:', len(data))
    print('A sample line:', data[-1])
    


def _2b_1():
    '''
    2. valuable
    In the case of self-describing digital datasets, is the format either JSON (preferred) or XML-based using a well-known schema (or accompanied by the schema employed)?
    '''
    ans, reason = 1,''
    with open(file_path, 'r') as unknown_file:
        # Remove tabs, spaces, and new lines when reading
        data = re.sub(r'\s+', '', unknown_file.read())
        if (re.match(r'^<.+>$', data)):
            ans,reason = 0, 'This file is XML'
        if (re.match(r'^({|[).+(}|])$', data)):
            ans, reason = 0, 'This file is JSON'
        ans, reason = 1, 'This file is either not XML nor JSON'
    return Answer[ans], reason



def main():
    load_dataset()
    print(_2b_1())
    pass

if __name__ == '__main__':
    main()
    