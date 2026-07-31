def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened..")

        print(f"File offset is : {fobj.tell()}")

        Data = fobj.read(10)
        print(Data)
        
        print(f"File offset is : {fobj.tell()}")

        

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory..")
    
if __name__=="__main__":
    main()