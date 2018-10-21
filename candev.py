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


def _2b_2():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_3():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_4():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_5():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_6():
    '''
    0.Yes 1.No
    make sure the header is in the first line.

    '''
    ans, reason = 1,'The header is in line '
    metadata=['scenario', 'goals', 'long_goal', 'dimension', 'region_id', 'region_name', 'value']
    if(metadata==header):
        ans=0
        reason = 'The header is in the first line'
    else:
        ans=1
        for index,i in enumerate(data):
            if i==metadata:
                reason += str(index)

    return Answer[ans], reason


def _2b_7():
    '''
    3. I don\'t know
    '''
    ans, reason = 3,''
    #Your code here

    return Answer[ans], reason
def _2b_8():
    '''
    0.Yes 1.No
    get the extension from the path. if it's .csv, then it can be understand easily both by humans and machines.
    '''
    ans, reason = 1,''
    extension = os.path.splitext(file_path)[1]
    if extension == '.csv':
        ans = 0
        reason = 'this is a .csv'
    else:
        reason ='because this is a '+ extension
    return Answer[ans], reason


def _2b_9():
    '''
    2.not applicable 3. I don\'t know
    '''
    ans, reason = 3,''
    #Your code here

    return Answer[ans], reason
def _2b_10():
    '''
    0.Yes 1.No
    Check if columns in the header equal to ''
    '''
    ans, reason = 1,'Columns'
    marker=[]
    for index, i in enumerate(header):
        if (i==''):
            ans = 1
            marker.append(index)
    if (len(marker)!=0):
        if(len(marker) ==1):
            reason = 'Column '
        for index, i in enumerate(marker):
            marker[index] += 1
            reason += str(marker[index])
            reason += str(',')
        if(len(marker)==1):
            reason += ' is empty'
        else:
            reason +=' are empty'
    else:
        ans = 0
        reason = 'all the columns have a column name.'

    return Answer[ans], reason


def _2b_11():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_12():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_13():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_14():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_15():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_16():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_17():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_18():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason




def main():
    load_dataset()
    print(_2b_1())
    pass

if __name__ == '__main__':
    main()
    