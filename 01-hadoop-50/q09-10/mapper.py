import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.replace('\n','')
        sys.stdout.write(line.split('   ')[0] + ',' + line.split('   ')[1]+  ',' +line.split('   ')[2].replace('\t','')+'\n')