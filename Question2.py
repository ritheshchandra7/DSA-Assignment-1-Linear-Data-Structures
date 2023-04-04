# Q2. Write a program to reverse an array in place? In place means you cannot create a new array.You have to update the original array.

def ReverseArray(array):
    return "The Reverse Array is:",array[::-1]
array = ["R","i","t","h","e","s","h"]
print("Original Array:", array)
print(ReverseArray(array))
print("*"*30)
array1 = [0,2,4,6,8]
print("Original Array:", array1)
print(ReverseArray(array1))