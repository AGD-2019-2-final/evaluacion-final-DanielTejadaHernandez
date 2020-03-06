import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':

    current_key = None
    max_mount = 0

    for line in sys.stdin:

        #key = porpouse
        #value= mount

        key, value = line.split("\t")
        value = int(value)

        if key == current_key:

            if max_mount > value:
                max_mount = max_mount
            else:
                max_mount = value

        else:
            if current_key is not None:
                sys.stdout.write("{}\t{}\n".format(current_key, max_mount ) )

            current_key = key
            max_mount = value

    sys.stdout.write("{}\t{}\n".format( current_key, max_mount ))
