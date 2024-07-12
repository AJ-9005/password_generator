import random
chars="`1234567890-=~!@#$%^&*()\\_+qwertyuiop[]RWEQTYUIOP{}|asdfghjkl;'\"ASDFGHJKL:zxcvbnm,./ZXCVBNM<>?"
def passwordgen(l,n):
    print("Here are some suggested passwords:")
    while n:
        password=""
        for _ in range(0,l):
            j=random.randrange(0,len(chars))
            password+=chars[j]
        print(f"\n{password}")
        n-=1
lengthofpass=int(input("Enter length of password:"))
numofpass=int(input("\nEnter number of passwords you want:"))
passwordgen(lengthofpass,numofpass)