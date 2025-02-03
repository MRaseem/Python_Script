import random
x=random.randint(1,10)
dictionary={'Counter No.':'Value'}
for i in range(1,x):
    key=i
    value=random.randint(1,50)
    dictionary.update({key:value})
print(dictionary)