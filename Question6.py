# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

postfix = input("Enter postfix expression: ")
s = []
for i in postfix:
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(i+op2+op1)
print("prefix expression is",*s)