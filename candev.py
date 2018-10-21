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
    print('A sample line:', data[0])
    


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
    2. valuable
    Are the filenames consistent, descriptive, and informative (clearly indicates content) to humans?
    '''
    ans, reason = 0,'The question is subjective, so it would be better to double check it by humans.'
    return Answer[ans], reason

def _2b_17():
    '''
    3. desirable
    Do the filenames follow the convention: less than 70 characters; most unique content at start of filename; no acronyms; no jargon; no organization name?
    '''
    ans, reason = 0, ''
    filename = os.path.splitext(file_path)[-2]
    if(len(filename)>70):
        ans, reason = 1, 'File name should not be longer than 70 characters.'
    else:
        #if there are two or more continuous capitals, there might be acronyms in file name
        has_continuous_capital = False
        for i in range(1,len(filename)):
            if filename[i].isupper() and filename[i-1].isupper():
                has_continuous_capital = True
                break
        if has_continuous_capital == True:
            ans, reason = 1, 'There might be acronyms in file name.'
    return Answer[ans], reason


def _2b_18():

    return Answer[ans], reason



def main():
    load_dataset()
    print(_2b_17())
    pass

if __name__ == '__main__':
    main()
    