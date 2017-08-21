

def perm(number,couples=0):
   if(couples==len(number)):
      print (number)
   else:
      for i in range(couples,len(number)):
         number[couples],number[i] = number[i],number[couples]
         perm(number, couples+1)
         number[couples],number[i] = number[i],number[couples]

print(perm([1,2]))

