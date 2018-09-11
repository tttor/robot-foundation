# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def createGenerator():
    mylist = range(3)
    print('halo')
    for i in mylist:
        print('inside for in the gen fn')
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

print('calling via for i')
for i in mygenerator:
     print(i)

print('calling via for i: B')
for i in createGenerator():
    print(i)
