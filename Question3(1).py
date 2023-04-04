# Q3. Write a program to check if two strings are a rotation of each other?

def StringRotationCheck(s1, s2): 
    temp = '' 
    temp = s1 + s1 
    if s2 in temp: 
        return True 
    else: 
        return False
s1 = "ABACADABC"
s2 = "CDABABACD"
if StringRotationCheck(s1, s2): 
    print("Given Strings are a rotation of each other.")
else: 
    print("Given Strings are not a rotation of each other.")
print("*"*30)
s1_1 = "ABACD"
s2_2 = "CDABA"
if StringRotationCheck(s1_1, s2_2): 
    print("Given Strings are a rotation of each other.")
else: 
    print("Given Strings are not a rotation of each other.")