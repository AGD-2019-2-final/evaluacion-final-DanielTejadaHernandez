import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    current_key = None
    max_mount = 0
    min_mount = 0

    for line in sys.stdin:

        #key = porpouse
        #value= mount

        key, value = line.split("\t")
        value = float(value)

        if key == current_key:

            if max_mount > value:
                max_mount = max_mount
            else:
                max_mount = value

            if min_mount < value:
                min_mount = min_mount
            else:
                min_mount = value

        else:
            if current_key is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(current_key, max_mount, min_mount ) )

            current_key = key
            max_mount = value
            min_mount = value

    sys.stdout.write("{}\t{}\t{}\n".format( current_key, max_mount, min_mount))