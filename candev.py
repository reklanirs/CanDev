#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Packages needed:
python3 -m pip install csv pyenchant numpy
'''
import os,re,sys,time
import math,random
import csv
import numpy as np
import re
import enchant


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

def name_split(s):
    '''
    Split a string by: All possible delimiters; Uppercases; Numbers
    '''
    words = re.findall(r"[A-Za-z0-9']+", s)
    tmp = []
    for i in words:
        tmp += re.sub( r"([A-Z])", r" \1", i).split()
    ret = []
    for i in tmp:
        ret += re.findall('\d+|\D+', i)
    return ret


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
    2. valuable
    Was a logical, documented naming convention used for variables (column names)?
    Split the name into letters and numbers. Check if all words appears in the dictionary
    '''
    ans, reason = 1,''
    d = enchant.Dict("en_US")
    warning_column_names = []
    for col in header:
        words = name_split(col)
        if not all(d.check(i) for i in words):
            warning_column_names.append(col)
    if len(warning_column_names)==0:
        ans = 0
    else:
        ans = 1
        reason = '%s columns may not have logical, documented naming convention'%warning_column_names
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
    1. essential
    Are the column names consistent with the documentation?
    '''
    ans, reason = 3,'No documentation presented'
    return Answer[ans], reason

def _2b_12():
    '''
    2. valuable
    Where possible, is human understable information preferred over coded information (e.g., "cat", "dog" instead of "1", "2" to represent cat and dog, respectively).
    '''
    ans, reason = 1,''
    excldue = ['id','value','date','number','year','scenario']
    warning_columns = []
    tmp = data[random.randint(0,len(data))]
    for indx,i in enumerate(header):
        skip = False
        for j in excldue:
            if j in i:
                skip = True
        if skip or re.match("^\d+?\.\d+?$", tmp[indx]) is not None:
            continue
        if str(tmp[indx]).isdigit():
            warning_columns.append(indx)
    if len(warning_columns) == 0:
        ans, reason = 0,''
    else:
        ans, reason = 1,'The %s columns may should not be coded information'%warning_columns
    return Answer[ans], reason


def _2b_13():
    '''
    1. essential
    Does each record (row) have a unique identifier?
    '''
    ans, reason = 0,''
    if len(header)>=1: 
        s = {}
        for indx,i in enumerate(data):
            if i[0] in s:
                ans = 1
                reason = 'Identifier in row %d conflicts with row %d'%(indx+2,s[i[0]]+2)
                break
            else:
                s[i[0]] = indx
    return Answer[ans], reason


def _2b_14():
    '''
    1. essential
    Can the tables in a data collection be linked via common fields (columns)?
    '''
    ans, reason = 2,'This tool is only used for single dataset'
    return Answer[ans], reason


def _2b_15():
    '''
    1. essential
    Can the data tables be linked to the metadata via common fields (columns)?
    '''
    ans, reason = 2,'This tool is only used for single dataset'
    return Answer[ans], reason


def _2b_16():
    '''
    2. valuable
    Are the filenames consistent, descriptive, and informative (clearly indicates content) to humans?
    '''
    ans, reason = 0,'The question is subjective, so it would be better to double check it by humans.'
    return Answer[ans], reason


def _2b_():
    '''
    '''
    ans, reason = 1,''
    #Your code here

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


def _2b_19():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def main():
    load_dataset()
    print(_2b_5())
    pass

if __name__ == '__main__':
    main()
    