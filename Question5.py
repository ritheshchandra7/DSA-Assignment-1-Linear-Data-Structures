# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def print_instruction(n, st1, st2):
  print(f"move disk no {n} from rod {st1} to rod {st2}")

def tower_of_hanoi(n, start, end):
  if n == 1:
    print_instruction(n, start, end)
  else:
    other = 6 - (start + end)
    tower_of_hanoi(n-1, start, other)
    print_instruction(n, start, end)
    tower_of_hanoi(n-1, other, end)

n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 1, 3)