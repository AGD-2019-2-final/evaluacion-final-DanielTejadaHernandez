import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    current_key = None
    same_letter = []

    for line in sys.stdin:

        key, date, value = line.split ( ',' )

        if key == current_key:
            same_letter.append ( [int( value.replace ( '\n', '' ) ), key, date] )

        else:
            if current_key is not None:
                same_letter.sort ()
                for i in same_letter:
                    sys.stdout.write ( i[1] + '   ' + i[2] + '   ' + str ( i[0] ) + '\n' )
                same_letter = []

            current_key = key
            same_letter.append ( [int ( value.replace ( '\n', '' ) ), key, date] )
    same_letter.sort ()
    for i in same_letter:
        sys.stdout.write ( i[1] + '   ' + i[2] + '   ' + str ( i[0] ) + '\n' )
