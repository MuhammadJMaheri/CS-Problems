'''contains roman numerals and their equavilant arabic numbers'''
num={'V':5,'L':50,'D':500,'I':1,'X':10,'C':100,'M':1000}

rom = input("enter roman numerals: ")

def findmax(string,left_index,right_index):
    '''
    finds the smallest index that represents the 
    greatest numeral from left_index to right_index
    '''
    max_decimal=0
    for i in range(left_index,right_index+1):
        if num[string[i]]>max_decimal:
            max_decimal=num[string[i]]
            pos=i
    return pos

def calc(string,left_index,right_index):
    '''
    calculates arabic equavilant from left_index to right_index
    '''
    if(string==''or left_index>right_index):
        return 0

    max_index=findmax(string,left_index,right_index)
    if left_index==right_index:
        decimal=num[rom[left_index]]
        return decimal

    decimal=  (num[rom[max_index]]
        +calc(string,max_index+1,right_index)
        -calc(string,left_index,max_index-1))
    return decimal

arabic=calc(rom,0,len(rom)-1)
print("arabic number: ")
print(arabic)
