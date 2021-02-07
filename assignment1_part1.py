class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):

    counter = 0

    if isinstance(numbers, list) == False:
        raise ListDivideException("This is not a list of numbers")
    elif isinstance(numbers, str) == True:
        raise ListDivideException("This is not a list of numbers")

    try:
        for i in numbers:
            if i % divide == 0:
                counter += 1
    except ListDivideException:
        pass

    print(counter)

if __name__ == "__main__":
    listDivide([1, 2, 3, 4, 5])
    listDivide([2, 4, 6, 8, 10])
    listDivide([30, 54, 63, 98, 100], divide=10)
    listDivide([])
    listDivide([1, 2, 3, 4, 5], 1)