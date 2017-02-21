def Arrange_Disks(A):
    length=len(A)
    moves=0
    for i in xrange(length):
        minn=i
        for j in xrange(i+1,length):
            if A[j]<A[minn]:
                minn=j
        moves+=minn-i       
        A[i],A[minn]=A[minn],A[i]
    return A,moves                #returns a tuple containing both A and moves


def main():

    n=input("Please enter a number between 2 to 10: ")
    A=[]
    for disk in range (1,(2*n+1)):
        if (disk%2) != 0:
            A.append("1")
        else:
            A.append("0")
    print "This is the original array: ", A

    A,moves=Arrange_Disks(A)

    print "This is the sorted array: ", A
    print "This is the number of moves required: ", moves

main()