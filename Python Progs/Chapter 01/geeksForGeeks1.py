def check_status(a, b, flag):
    if (a>=0 and b<0) and flag == False:
        return True
    if (a<0 and b>=0) and flag == False:
        return True
    if (a<0 and b<0) and flag == True:
        return True
    else:
        return False


a = int(input())
b = int(input())
flag = bool(input())
value = check_status(a, b, flag)
print(value)