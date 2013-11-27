# -*- coding: cp949 -*-
from __future__ import division
import hashlib
import time
import sys
import os
import glob

def searchPatternIncludeSub(dir,patternStr, sub):
    # 우선 지금 폴더의 패턴 검색 해서 저장.
    retlist = glob.glob(os.path.join(dir, patternStr))
    if sub =="yes":
        try:
            # 하위 디렉토리 검색
            findlist = os.listdir(dir)

            for f in findlist:
                next = os.path.join(dir, f)
                if os.path.isdir(next):
                    retlist += searchPatternIncludeSub(next,patternStr)
        except:
            pass

    return retlist


try:
    sys.argv[1]
    sys.argv[2]
    sys.argv[3]
 
except:
    print '사용법: 경로명  확장자  하위폴더 검색여부'
    print "searchfile.py C:\Windows\System32 exe no"
    exit(-1)
try:
    result = searchPatternIncludeSub(str(sys.argv[1]),'*.'+ str(sys.argv[2]), str(sys.argv[3]))
    #print result

    for f in result:
        print f
        
                                   
except IOError:
    print 'no such directory'
    exit(-1)

 

