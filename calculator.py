#python code for calculator
#1 for addition
#2 for subtraction
#3 for multiplication
#4 for division

operation_no = int(input('Enter the operation id: '))
n1= float(input('Enter value: '))
n2= float(input('Enter value: '))

if (operation_no==1):
    print('Addition Result: ', n1+n2)

if (operation_no==2):
    print('Subtraction Result: ', n1-n2)


if (operation_no==3):
    print('Multiplication Result: ', n1*n2)


if (operation_no==4):
    print('Division Result: ', n1/n2)
