#Count Digits

i = 9
c = 10
d = 1
def count_digits (n):
  global i
  global c
  global d
  if n > i:
    d += 1
    i += 9*c
    c *= 10
    count_digits (n)
  else:
    print(d)

#Find Max
def list_find_max(n):
  lst = [int(item) for item in n.split()]
  find_max(lst, 0, 0)

def find_max(lst, i, maxValue):
  if len(lst) == 0:
    print(None)
    return None
  if len(lst) == 1:
    print(lst[0])
    return lst[0]
  if i >= len(lst):
    print(maxValue)
  else:   
    if lst[i] > maxValue:
      maxValue = lst[i]
      find_max(lst, i+1, maxValue)
    else:
      find_max(lst, i+1, maxValue)


#count tags
def count_tags(code,tag,i,s):
  if i >= len(code):
    print(s)
  else:
    splits = len(code[i].split("<%s"%tag)) - 1
    if splits == 0:
      count_tags(code,tag,i+1,s)
    elif splits >= 1:
      s = s + splits
      count_tags(code,tag,i+1,s)
  
#main
def main():
  print("1. Count Digits")
  print("2. Find Max")
  print("3. Count Tags")
  print("4. Exit")
  print("---------------------------------------")
  ch = int(input("Enter a number for corrisponding choice: "))
  if (ch == 1):
    n = int(input("Enter Integer number to count digits: "))
    count_digits (n)
  if (ch == 2):
    n = input("Enter Integer numbers separated by spaces: ")
    list_find_max (n)
  if (ch == 3):
    code = []
    print("Enter your HTML code to count tags (type 'done' to finish): ")
    while True:
      line = input()
      if line.lower() == 'done': 
        break
      code.append(line)
    tag = input("Enter the tag name: ")
    count_tags (code,tag, 0, 0)
  if (ch == 4):
    print("Thank you")
    
main()