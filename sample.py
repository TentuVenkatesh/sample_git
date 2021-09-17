# sample python program
# prime number b/t [m,n], m<n
m=10
n=20
for i in range(m,n+1):
    for j in range(2,i):
        if (i%j == 0): # % gvies remainder
            break
    else:
        print(i)
