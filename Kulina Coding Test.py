print("Test no 1 : Prima Number")
print("="*40)

print("Input the range number")
low = int(input("lower limit : "))
upp = int(input("upper limit : "))
prima = []
for n in range(low, upp ):
    condition = True
    if n<2 :
        condition = False
    else :
        for i in range(2, n) :
            if (n%i==0) :
                condition = False
    
    if condition == True :
        prima.append(n)
        
print(prima)

prim_index = int(input("Index prima yang di cari berdasarkan range tersebut :"))
print(prima[prim_index-1])

print("="*40)
print("Test no 2 : Fibonacci")
print("="*40)

fibo = int(input("Choose your index for Fibonacci, index start from 1 : "))

a = 0
b = 1
c = a + b
for i in range(fibo-1):
 	c = a + b
 	a = b
 	b = c
print(c)

print("="*40)
print("Test no 3")
print("="*40)
import sys
inp = str(1345679)

for i in range(len(inp)):
    sys.stdout.write(str(inp[i]))
    for j in range(i,len(inp)-1):
        sys.stdout.write(str(0))
    sys.stdout.write('\n')
