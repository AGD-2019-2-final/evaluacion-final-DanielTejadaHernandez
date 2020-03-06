import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        value, keys = line.split ( '\t' )
        keys = keys.replace ( '\n', '' )
        keys = keys.replace ( ' ', '' )
        keys_2 = keys.split ( ',' )

        for i in keys_2:
            sys.stdout.write ( str ( i ) + ',' + value + '\n' )