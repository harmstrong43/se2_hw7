def leap(x):
    if(x % 4 == 0):
        return True
    else:
        if(x % 100 == 0):
            return True
        else:
            return False