# Q7. Write a program to convert prefix expression to infix expression.

prefix = input("Enter prefix expression: ")
s = []
for i in reversed(prefix):
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(f"({op1}{i}{op2})")
print("infix expression is",*s)