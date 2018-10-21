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
    2. valuable
    In the case where the data reside in a relational database, is the database in 3rd normal form?
    '''
    ans, reason = 1,''
    #Your code here
    with open(file_path,'r') as unknown_file:

     return Answer[ans], reason


def _2b_3():
    '''
    1. essential
    In the case where the data do not reside in a relational database, are the data files tabular?
    i.e. There is one rectangular table per file, systematically arranged in rows and columns with the headers (column names) in the 1st row.
    Every record (row) has the same column name. Every column contains the same type of data, and only one type of data.
    How: Check the csv file has a header by using has_header from csv package; By checking the number of columns for each row is equal to the column numbers for header;
         By checking
    '''
    ans, reason = 1,''
    with open(file_path,'r') as unknown_file:
        sniffer = csv.Sniffer()
        has_header = sniffer.has_header(unknown_file.read(2048))
        unknown_file.seek(0)

        has_rowcols = False
        reader = csv.reader(unknown_file,delimiter=',')
        num_cols = len(next(reader))
   
        for row in data:
            if num_cols != len(row):
                has_rowcols = True
                break

        # num_rowcols = False
        # num_cols = len(header)
        # print('num_cols', num_cols)
        # print(data[0])
        # for row in data:
        #     print(len(row))
        #     # print(row)
        #     if not len(row) == num_cols:
        #         num_rowcols = True
        #         break

        All = all(isinstance(column,(int, str, float)) for column in unknown_file)

        if (has_header == True & has_rowcols == True & All == True):
            ans, reason = 0, 'This data file is tabular.'
        else:
            ans, reason = 1, 'This data is not tabular.'

    return Answer[ans], reason

def _2b_3_test():
    num_rowcols = False
    num_cols = len(header)
    print('num_cols',num_cols)
    print(data[0])
    for row in data:
        print(len(row))
        #print(row)
        if not len(row) == num_cols:
            num_rowcols = True
    return num_rowcols


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
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_7():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_8():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def _2b_9():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason
def _2b_10():
    '''
    '''
    ans, reason = 1,''
    #Your code here

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
    print(_2b_3())
    pass

if __name__ == '__main__':
    main()
    