c= 'python'
for i in range(0,len(c)):
    for j in range(i):
        print(c[j], end='')
    print('')

for i in range(0,len(c)):
    if i%2!=0:
        continue
    print(c[i])