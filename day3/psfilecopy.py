import sys


def usage():
    print('Usage:')
    print(f'{sys.argv[0]} src-file dest-file')
    exit(1)


def copy(src, dest):
    with open(src) as fp, open(dest, 'w') as fw:
        fw.write(fp.read())


if len(sys.argv) != 3:
    usage()


copy(*sys.argv[1:])
