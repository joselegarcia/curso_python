abc=['a','b','c','d','f','g','h','i','j','k','l','m','n','ñ']

for i in range(abc):
    abc.remove([i%3==0])
    print (abc)
