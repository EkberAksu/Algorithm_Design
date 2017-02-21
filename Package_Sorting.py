def flip(a,ArrayIndex):
    reverseList =[]
    for i in range(ArrayIndex,-1,-1):
        reverseList.append(a[i])
    for i in range(len(reverseList)):
        a[i] = reverseList[i]    
    
def pancakeSorting(a):
    arraylist =[]
    while len(a)>1:
        maxIndex = a.index(max(a))
        flip(a,maxIndex)
        flip(a,len(a)-1)
        arraylist.insert(0,a[-1])
        a.pop()
    print arraylist    
def main():
    array= [45,7,3,89,123,56]
    pancakeSorting(array)
if __name__ == '__main__':
    main()