def leap(x):
    if(x % 4 == 0):
        if(x % 400 == 0):
            return False
        else:
            return True
    else:
        if(x % 100 == 0):
            if(x % 400 == 0):
                return False
            else:
                return True
        else:
            return False