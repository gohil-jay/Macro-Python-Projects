#Sum Should always be : n(n^2 + 1)/2 ==>  e.g for n=3 ---> Sum = 15 
#Magic Square is being obtained in case of n = odd, for n=even the probability of obtaining a magic square is least

def magic_square(n):
    magicSquare=[[0 for i in range(n)] for j in range(n)]

    col=n-1
    row=(n//2)
    num=n*n
    count=1
    
    while(count<=num):
        if(row==-1 and col==n): #rows and cols both exceeding
            col=n-2
            row=0
        else:
            if(col==n): #col exceeding
                col=0
            if(row<0): #row exceeding
                row=n-1
        if(magicSquare[row][col]!=0): #already number is present at the pos
            col=col-2
            row=row+1
            continue
        else:
            magicSquare[row][col]=count 
            count+=1
        
        row=row-1
        col=col+1
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end="\t")
        print()
    print("The Sum of ", n," x ",n," Matrix is ", (n*(n**2+1))/2)

c=int(input("Enter N : "))
magic_square(c)
