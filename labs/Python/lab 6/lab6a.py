def sortlist(x):#function defintion named last that takes single parameter "x"
    return x[-1]# "x[-1]" it returns last element in i/o parameter x
def sort(tuples):
    return sorted(tuples, key=sortlist)
s=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("Sorted:")
print(sort(s))
