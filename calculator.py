def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b    
def division(a,b):
    return a/b
    
a=int(input("Enter a number:"));
b=int(input("Enter a number"));
op=int(input("choose operation \n 1. Addition \n 2.Subtraction\n  3.Multiply  \n  4. Division\n"));

if op==1:
	result= add(a,b)
	print("Result",result);
	

elif op==2:
	result=subtract(a,b)
	print("Result:",result);


elif op==3:
	result=multiply(a,b)
	print("Result:",result);
	

elif op==4:
	result=division(a,b)
	print("Result:",result);
else:
    print("invalid");
    
