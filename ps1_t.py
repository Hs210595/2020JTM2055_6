def count_1s(a,b):
    i=0
    count=0
    while(i<b):
        f=int(a[i])
        if f==1:
           count+=1
        i+=1
        return(count)
A=int(input('Enter the first number: '))
B=int(input('Enter the second number: '))
A_Bin=bin(A).replace("0b", "0")
B_Bin=bin(B).replace("0b", "0")
A1s=count_1s(A_Bin,len(A_Bin))
B1s=count_1s(B_Bin,len(B_Bin))
if (A1s>B1s):
    Diff=(A1s-B1s)
else:
    Diff=(B1s-A1s)
print('A \t B \t A Binary \t B binary \t Diffrence in number of ones ')
print('{0} \t {1} \t {2} \t     {3} \t         {4} '.format(A,B,A_Bin,B_Bin,Diff))
if(Diff==0):
    print('Bit Balanced ')
else:
    print('Bit Biased ')
