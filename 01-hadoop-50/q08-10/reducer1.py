#!/usr/bin/env python
import sys

if __name__ == '__main__':

    current_key = None
    same_letter = []

    for line in sys.stdin:

        key, date, value = line.split ( ',' )

        if key == current_key:
            same_letter.append ( float ( value.replace ( '\n', '' ) ) )

        else:
            if current_key is not None:
                sys.stdout.write ( current_key + '       ' + str ( float(sum ( same_letter ) )) + '	' + str (
                    sum ( same_letter ) / len ( same_letter ) ) + '\n' )
            same_letter = []

            current_key = key
            same_letter.append ( int ( value.replace ( '\n', '' ) ) )

    sys.stdout.write ( current_key + '       ' + str ( float(sum ( same_letter ) )) + '	' + str (
        round(sum ( same_letter ) / len ( same_letter ),3 )) + '...\n' )
