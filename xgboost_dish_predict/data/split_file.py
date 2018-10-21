# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:45:03 2018

@author: shi.chao
"""

import os
import time
 
def mkSubFile(lines,head,srcName,sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()
 
def splitByLineCount(filename,count):
    fin = open(filename,'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf,head,filename,sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf,head,filename,sub)   
    finally:
        fin.close()
 
if __name__ == '__main__':
    begin = time.time()
    path_split_1516 = './/' + 'dishdetail14d_1516' + '.csv'
    path_split_1617 = './/' + 'dishdetail14d_1617' + '.csv'
#    splitByLineCount(path_split_1516, (2015486*14)/4)
    splitByLineCount(path_split_1617, (2015486*14)/4)
    end = time.time()
    print('time is %d seconds ' % (end - begin))