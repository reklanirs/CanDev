#!/usr/local/bin/python3
# -*- coding: utf-8 -*- 
import os,re,sys,time
import math,random
import csv
import numpy as np


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sys.stdin=open('in.txt','r')

file_path = '../Hackathon_CanDev2018-10-20-master/OHIDataSet.csv'
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
    print(len(data))
    print(data[-1])


def _2b_1():
    '''
    2. valuable
    In the case of self-describing digital datasets, is the format either JSON (preferred) or XML-based using a well-known schema (or accompanied by the schema employed)?
    '''
    # Your code here
    
    return 0,'No one in dataset conflict against this checklist'



def main():
    load_dataset()
    pass

if __name__ == '__main__':
    main()
    