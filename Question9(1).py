# Q9. Write a program to reverse a stack.

stack = list(map(int, input("enter values of stack separated by space : ").split()))
rev_stack = []
for _ in range(len(stack)):
  rev_stack.append(stack.pop())
print("reversed stack is",*rev_stack)