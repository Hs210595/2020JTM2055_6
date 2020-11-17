def is_leap(x):
    y= (x%4)
    if y==0:
        print("you have enterd Leap year")
    else:
        print("you have enterd Non leap year")
a=int(input('Enter the value of a '))
is_leap(a)