import hashlib
def pres():
    if __name__ == "__main__":
        print("1 -Reverse Text")
        print("2 -MD5")
        print("3 -sha512")
        print("4 -Key encryption")
        print("5 -Exit")
    else:
        pass
def reverse():
        ch = input("Enter text to crypt : ")
        ch_crypt = ch[::-1]
        print("the crypted message is : %s"% ch_crypt)
def key():
    key = input("Enter Fernet key : ")
    msg = input("Enter message to crypt : ")
    crypt = ""
    for i in key:
        for j in msg:
            c = i + j
            crypt += c
    print("the crypted message is : %s"% crypt)
def md5():
    msg = input("enter msg to crypt: ")
    hash = hashlib.md5(msg.encode())
    crypt = hash.hexdigest()
    print("Crypted message => ",crypt)
def sha512():
    txt = input("enter msg to crypt: ")
    hash = hashlib.sha512(txt.encode())
    crypt = hash.hexdigest()
    print("Crypted message => ",crypt)
def choose():
    h = 1
    if h > 0:
        pres()
    ok = True
    while ok:
        try:
            choice = int(input("Your Choice :> "))
            if choice == 1:
                reverse()
            elif choice == 2:
                md5()
            elif choice == 3:
                sha512()
            elif choice == 4:
                key()
            elif choice == 5:
                print("Exiting the program...")
                break
            else:
                print("404 Not Found!!!")
        except:
            pass
            print("Invalid input form!!!")
if __name__ == "__main__":
    choose()
