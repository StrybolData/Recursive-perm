def perm(number,elements=0):
   if(elements==len(number)):
      print (number)
   else:
      for i in range(elements,len(number)):
         number[elements],number[i] = number[i],number[elements]
         perm(number, elements+1)
         number[elements],number[i] = number[i],number[elements]

print(perm([1,2]))
