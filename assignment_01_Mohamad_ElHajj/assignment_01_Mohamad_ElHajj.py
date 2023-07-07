#1
def factorial():
  m = int(input("Enter an integer number: "))
  c = 1
  n = 1
  while (c <= m):
    n = n * c
    c+=1
  print(n)

#2
def divisors():
  m = int(input("Enter an integer number: "))
  c = 1
  l = []
  while (c <= m):
    if (m%c == 0):
      l.append(c)
    c += 1 
  print(l)

#3
def reverseString():
  m = input("Enter a string to reverse: ")
  c = len(m)
  r = ""
  while (c <= len(m) and c >= 1):
    r = r + m[c-1]
    c-=1
  print(r)

#4
def evenNumbers():
  m = input("Enter a list of integer numbers separated by spaces: ")
  e = m.split()
  l=[int(element) for element in e]
  nl = []
  c = 0
  while (c < len(l)):
    if (l[c] % 2 == 0):
      nl.append(l[c])
    c+=1
  print(nl)

#5
def password():
  m = input("Enter a new password: ")
  upper = False
  lower = False
  digit = False
  l = False
  sc = False
  for c in m:
    if (c.isupper()):
      upper = True
    elif (c.islower()):
      lower = True
    elif (c.isdigit()):
      digit = True
  if (len(m) >= 8):
    l = True
  sc = ["?", "#", "$", "!"]
  for c in m:
    if c in sc:
      sc = True
      break
  if (upper and lower and digit and l and sc):
    print("Strong password")
  else:
    print("Weak password")

#6
def validIp():
  m = input("Enter an IPv4 address: ")
  n = m.split(".")
  l = False
  v = False
  for c in n:
    c=int(c)
    if (c >= 0 and c < 255):
      v = True
    else:
      v = False
      break
    if (len(n) == 4):
      l = True
  if (v and l):
    print("VALID")
  else:
    print("NOT VALID")
  
validIp()
  

      
    
    
    
    
    
  
  
  