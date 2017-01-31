def exceptionhandling():
    try:
        a="aa"
        b=10
        c=0

        print(a/c)
    except ZeroDivisionError:
        print("this is wrong, cant divide by zero")
    except TypeError:
        print("cant add int to str")
        raise Exception("this is an exception")
    else:
        print("there is no exception hence else is executed")
    finally:
        print("it will print whatever happens")

exceptionhandling()
