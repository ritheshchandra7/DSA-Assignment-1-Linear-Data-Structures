# Q8. Write a program to check if all the brackets are closed in a given code snippet.

expression = input("Enter Brackets expression: ")
s = []
o = "{[("
c = "}])"
for i in expression:
    if i in o:
        s.append(i)
    else:
        if len(s) == 0:
            print("Not Balanced")
            break
            
        b = s.pop()
        if o.index(b) != c.index(i):
            print("Not Balanced")
            break
else:
    if len(s) == 0:
        print("Balanced")
    else:
        print("Not Balanced")