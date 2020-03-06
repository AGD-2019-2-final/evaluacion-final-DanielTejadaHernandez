import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    current_key = None
    same_letter = []

    for line in sys.stdin:

        key, value = line.split ( ',' )

        if key == current_key:
            same_letter.append ( int ( value.replace ( '\n', '' ) ) )

        else:
            if current_key is not None:

                same_letter.sort ()
                sys.stdout.write ( current_key + '\t' )

                for i in range ( len ( same_letter ) ):
                    if i < len ( same_letter ) - 1:
                        sys.stdout.write ( str ( same_letter[i] ) + ',' )
                    else:
                        sys.stdout.write ( str ( same_letter[i] ) + '\n' )
                same_letter = []

            current_key = key
            same_letter.append ( int ( value.replace ( '\n', '' ) ) )

    same_letter.sort ()
    sys.stdout.write ( current_key + '\t' )

    for i in range ( len ( same_letter ) ):
        if i < len ( same_letter ) - 1:
            sys.stdout.write ( str ( same_letter[i] ) + ',' )
        else:
            sys.stdout.write ( str ( same_letter[i] ) + '\n' )
