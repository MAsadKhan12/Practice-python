example="example.txt"
#file1=open(example,'r')
#w=file1.read()
#print(w)


with open(example,'r') as file1:
   w=file1.read()
   print(w)


#converts the file lines into list
with open(example,'r') as file2:
   p=file2.readlines()
   print(p[1])
   #Remember to Learn Indent properly....



