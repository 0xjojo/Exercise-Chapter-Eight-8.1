def chop (t):
    x = len(t)
    #x = x-2 we can try also this and remove line 4
    del t [(x-1)]
    del t [0]
    #del t [(x-2)]
def middle (t):
    x = len (t)
    del t [0]
    del t [x-2]
    return t
t = [1,2,3,4,5,6]
y = [2,3,4,5,6,7,8,9,11,23]
chop(t)
new =[]
new = middle (y)
print (t)
print (new)# to check 
