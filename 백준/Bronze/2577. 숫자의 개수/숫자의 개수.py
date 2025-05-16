a=int(input())
b=int(input())
c=int(input())

n = str(a*b*c)

count = [0] * 10

for i in n :
    count[int(i)] += 1

for j in count :
    print(j)