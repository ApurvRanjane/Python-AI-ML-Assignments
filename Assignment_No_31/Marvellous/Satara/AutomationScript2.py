import sys

def main():
    if(len(sys.argv)==2):
        DirctoryName = sys.argv[1]
        print("Directory name is: ",DirctoryName)
        
    else:
        print("INvalid number of arguments.")
    
if __name__=="__main__":
    main()
