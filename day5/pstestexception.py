from pscustomexception import check_4_limit, RadiationError

if __name__ == '__main__':
    try:
        check_4_limit(.9)
    except RadiationError as err:
        print(err)