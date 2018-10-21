#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
Packages needed:
python3 -m pip install csv pyenchant numpy
'''
import os,re,sys,time
import math,random
import csv,re,enchant
import numpy as np
import ntpath


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sys.stdin=open('in.txt','r')

file_path = './OHIDataSet.csv'
checklist_path = './DataChecklistModules.csv'
checklist_header = []
checklist_data = {}
header = []
data = []
Answer = ['yes','no','not applicable','I don\'t know']
threshold = 60.0

finished_modules = [ '2b_%d'%i for i in range(1,20) ] + \
                    []
results_according_to_modules = []

def load_dataset(f = file_path):
    global header,data, checklist_header, checklist_data
    with open(f, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)[:-1]
        for row in reader:
            data.append(row[:-1])
    print(header)
    print('Total lines in this dataset:', len(data))
    print('A sample line:', data[-1])
    pass
    with open(checklist_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        checklist_header = next(reader)
        for row in reader:
            checklist_data[row[0].replace('-','_')] = row[1:]
    print(checklist_header)
    print('Total lines in this checklist:', len(checklist_data))
    print('A sample line:', checklist_data['9a_15'])



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


def _2b_19():
    '''
    '''
    ans, reason = 1,''
    #Your code here

    return Answer[ans], reason


def evaluate():
    global results_according_to_modules
    res = [ eval('_%s()'%i) for i in finished_modules ]
    for i in finished_modules:
        print('_%s'%i)
        print( eval("_%s()"%i) )
    print(res)
    results_according_to_modules = res


def task2_overall_rating():
    tmp = [i[0] for i in results_according_to_modules]
    count_result = [ tmp.count(Answer[i])  for i in range(len(Answer))]
    print(count_result)
    output = 'Amongst %d criteria of the checklist'%(len(finished_modules))
    for i in range(len(Answer)):
        output += '\nThere are %d answers are "%s", proportion is %.3f%%'%(count_result[i], Answer[i], count_result[i]*100.0/len(finished_modules))

    tmp = count_result[0]*100.0/len(finished_modules)
    if tmp >= threshold:
        output += '\n\nProportion of \'Yes\' is %.2f%%, which is bigger than the threshold %.2f%%. \nSo the dataset PASSED according to the checklist.'%(tmp, threshold)
    else:
        output += '\n\nProportion of \'Yes\' is %.2f%%, which is smaller than the threshold %.2f%%. \nSo the dataset FAILED according to the checklist.'%(tmp, threshold)
    print(output)
    with open('output.txt','w') as fout:
        fout.write(output)
        fout.flush()
    pass


def task3_R_markdown_report():
    dataset_name = ntpath.basename(file_path)
    summary = [ [0 for j in range(len(Answer))] for i in range(3) ]
    for indx,i in enumerate(finished_modules):
        r = int(checklist_data[i][1][0]) - 1
        col = Answer.index(results_according_to_modules[indx][0])
        summary[r][col] += 1
    for i in summary:
        print(i)

    summary_table = ''
    priority = ['essential', 'valuable', 'desirable']
    for i in range(3):
        tmp = '| x-%d  | number %s | %d |'%(i+1, priority[i], sum(summary[i]))
        for j in range(len(Answer)):
            tmp += ' %d |'%(summary[i][j])
        tmp += '\n'
        summary_table += tmp
    summary_table += '| x-4  | total | %d |'%(len(finished_modules))

    for j in range(len(Answer)):
        summary_table += ' %d |'%( sum([i[j] for i in summary]) )
    summary_table += '\n'

    total = len(finished_modules)*0.01
    for i in range(3):
        tmp = '| x-%d  | percent %s | %.1f%% |'%(i+4, priority[i], sum(summary[i])/total)
        for j in range(len(Answer)):
            tmp += ' %.1f%% |'%(summary[i][j]/total)
        tmp += '\n'
        summary_table += tmp
    summary_table += '| x-7  | total | %.1f%% |'%(len(finished_modules)/total)

    for j in range(len(Answer)):
        summary_table += ' %.1f%% |'%( sum([i[j] for i in summary])/total )
    summary_table += '\n'


    detail_table = ''
    for indx,i in enumerate(finished_modules):
        detail_table += '|%s|%s|%s|%s|%s|%s|\n'%\
        (i,checklist_data[i][0],checklist_data[i][1],checklist_data[i][2],results_according_to_modules[indx][0],results_according_to_modules[indx][1])


    markdown = '''
---
title: "%s"
output: html_document
---

The code below demonstrates an R markdown report containing:
* Overview and summary of the assessment results
* Detailed assessment results
of the given dataset %s.

##Overview and summary of the assessment results

| ID   | Category          | Questions | Answers (yes) | Answers (no) | Answers (not applicable) | Answers (I don't no) |
| ---- | ----------------- | --------- | ------------- | ------------------------ | ------------ | -------------------- |
%s


##Detailed assessment results

| ID   | Category | Priority for now | Data checklist questions | Answer | Explanation |
| ---- | -------- | ---------------- | ------------------------ | ------ | ----------- |
%s
'''%(dataset_name+' Report', dataset_name, summary_table, detail_table)

    print(markdown)
    with open('RMarkDownReport.Rmd','w') as fout:
        fout.write(markdown)
        fout.flush()
    pass

def main():
    load_dataset()
    print(_2b_5())

    evaluate()
    task2_overall_rating()
    task3_R_markdown_report()
    pass

if __name__ == '__main__':
    main()
    