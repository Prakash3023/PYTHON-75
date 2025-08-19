#Out of the String we should remove all the special character and print the alphabet and capitalize it
a=input("Enter any string:")
res=""
for i in a:
    if i.isalpha():
        res=res+i
    res1=res.capitalize()
print(res1)
