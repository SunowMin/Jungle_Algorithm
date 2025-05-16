a,b = input().split()
reverseA = ' '
reverseB = ' '
for i in a:
    reverseA = i + reverseA
for j in b:
    reverseB = j + reverseB
if reverseA >= reverseB:
    print(reverseA)
else :
    print(reverseB)