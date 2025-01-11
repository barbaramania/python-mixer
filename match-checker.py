#Un-optimized bubble method

fruits = ["mango", "orange", "grape", "pineapple", "kiwi", "pear","grape"]
length = len(fruits)
x = 0
found_match = False
while x <= length :
  j=x+1
  while j<=(length-1):
        if fruits[j] == fruits[x]:
            print(x, j)
            found_match = True
            break 
        j+=1
  x+=1
  if found_match == True:
    break 


