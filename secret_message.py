import os

alphabet ='abcdefghijklmnopqrstuvwxyz'
newmessage=''

os.system("cls")

count =0
while count <=0:
    do_u_want_to_play = input("\nDO YOU WANT TO WRITE SECRET CODE PRESS Y: ")
    if do_u_want_to_play =="y":
        
        message=input("ENTER MESSAGE: ")
        key = input("ENTER A KEY (1-26): ")
        key=int(key)

        for i in message:
            if i in alphabet:
                position = alphabet.find(i)
                newposition =(position + key )%26
                newi=alphabet[newposition]
                newmessage += newi
            else:
                newmessage += i
        print("YOUR NEW MESSAGE IS: ",newmessage,) 
        
    else:
        os.system("pause")
        os.system("cls")
        count+=1