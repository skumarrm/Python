pairs = ['one','two','three']
pairs.sort(key=lambda x: x)
print(pairs)
print(globals())

def a(b):
    a.__setattr__("ids1","2")
    a.__setattr__("ids2","4")
    print(a.__getattribute__("ids2"),b)

if __name__=="__main__":
    a("hello")