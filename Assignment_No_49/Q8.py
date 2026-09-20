# 8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:
#
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
#
# Display all four values.

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    tp=tn=fp=fn = 0

    for a,p in zip(actual,predicted):
        if a==1 and p==1:
            tp += 1

        elif a==0 and p==0:
            tn+=1

        elif a==1 and p==0:
            fn+=1

        elif a==0 and p==1:
            fp+=1

    print("TP = ",tp)
    print("TN = ",tn)
    print("FP = ",fp)
    print("FN = ",fn)

if __name__=="__main__":
    main()