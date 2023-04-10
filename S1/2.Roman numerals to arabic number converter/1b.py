num={'V':5,'L':50,'D':500,'I':1,'X':10,'C':100,'M':1000}
rom = input("enter roman numerals: ")
def findmax(string,a,b):
    p=0
    for i in range(a,b+1):
        if num[string[i]]>p:
            p=num[string[i]]
            pos=i
    return pos
c=0
def calc(string,a,b):
    if(string==''or a>b):
        return 0
    fm=findmax(string,a,b)
    if(a==b):
        c=num[rom[a]]
        return c
    else:
        c=num[rom[fm]]+calc(string,fm+1,b)-calc(string,a,fm-1)
        return c
arabic=calc(rom,0,len(rom)-1)
print("arabic number: ")
print(arabic)
