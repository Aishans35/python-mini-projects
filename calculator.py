num1=int(input("Enter a number:"));
num2=int(input("Enter a number:"));
op=int(input("choose operation\n 1.Addition\n 2.subtraction\n 3.multiplication \n4.division\n 5.remainder\n 6.power"));
if op==1:
    Result=num1+num2;
    print("Result=",Result);
elif op==2:
    Result=num1-num2;
    print("Result=",Result);
elif op==3:
    Result=num1*num2;
    print("Result=",Result);
elif op==4:
    Result=num1/num2;    
    print("Result=",Result);
elif op==5:
	Result=num1%num2;
	print("Result=",Result);
elif op==6:
	Result=num1**num2;
	print("Result=",Result);
else:
	print("invalid operation");

