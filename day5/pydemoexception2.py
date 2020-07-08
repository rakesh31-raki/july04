"""demo for the exception handling"""


def safe_float(value):
    try:
        result = None
        result = float(value[0])
    except (ValueError, TypeError, IndexError, KeyError) as error:
        print(error)
    except Exception as error:  # genric exception
        print('internal script error')
    finally:
        print('finally block')
        return result


print(safe_float([0]))