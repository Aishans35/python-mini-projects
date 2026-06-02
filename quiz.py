capital=input("Enter the capital of india");
capital=capital.lower()
score=0
if capital=="delhi":
	print("your answer is correct");
	score=score+1;
else:
	print("your answer is wrong");
python=input("Who created Python?");
python=python.lower()
if python=="guido van rossum":
	print("your answer is correct");
	score=score+1;
else:
	print("your answer is wrong");
planet=input("Which planet is known as the Red Planet?");
planet=planet.lower()
if planet=="mars":
    print("your answer is correct");
    score=score+1;
else:
	print("your answer is wrong");	
print("your score is",score);
if score==3:
    print("Excellent");
elif score==2:
	print("Good");
else:
	print("Need improvement");
