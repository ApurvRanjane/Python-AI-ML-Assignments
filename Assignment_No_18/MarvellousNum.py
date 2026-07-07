def chkPrime(No):
    count = 0
    if(No<2):
        return False
    for i in range(1,No+1):
        if (No % i == 0):
            count = count +1
    if(count == 2):
        return True
    else:
        return False

