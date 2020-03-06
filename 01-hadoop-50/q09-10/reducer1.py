#!/usr/bin/env python
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    current_key = None
    same_letter = []

    for line in sys.stdin:
        
        key,date,value = line.split(',')
        same_letter.append([int(value.replace('\n','')),key,date])

    same_letter.sort()
    
    for i in range(6):
        sys.stdout.write(same_letter[i][1]+'   '+same_letter[i][2]+'   '+str(same_letter[i][0])+'\n')
