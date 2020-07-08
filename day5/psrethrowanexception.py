def read(filename):
    try:
        open(filename)
    except (FileNotFoundError, IOError) as err:
        print(err)
        raise   # throwing the exception


try:
    read('passwd')
except FileNotFoundError as err:
    print(err)
