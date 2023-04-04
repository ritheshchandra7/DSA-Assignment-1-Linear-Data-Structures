# Q10. Write a program to find the smallest number using a stack.

stack = list(map(int, input("enter values of stack separated by space : ").split()))
small_num = stack.pop()
for _ in range(len(stack)):
  i = stack.pop()
  if i < small_num:
    small_num = i
print(f"smallest number in given stack is {small_num}")