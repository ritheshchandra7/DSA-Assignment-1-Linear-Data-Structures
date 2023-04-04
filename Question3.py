# Q3. Write a program to check if two strings are a rotation of each other?

str1 = input("Enter orignal string: ")
str2 = input("Enter test string: ")
str1_str2 = "".join([str1, str2])
if str1 == str2 or len(str1) != len(str2):
  print("Strings are not rotations of each other")
else:
  if str2 in str1_str2:
    print("Strings are rotations of each other")
  else:
    print("Strings are not rotations of each other")