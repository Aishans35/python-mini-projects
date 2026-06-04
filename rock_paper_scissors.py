import random
coscore=0;
yourscore=0;
while True:
    print("1.rock 2.paper 3.scissor")
    user=int(input(" choose \n1.rock\n 2.paper\n 3.scissor\n 4.exit\n"))
    if user not in[1,2,3,4]:
        print("choose any of the 3 option")
        continue
    if user==4:
    	break
    computer=random.randint(1,3)
    print("computer choose",computer)
    if user==1 and computer==2:
        coscore+=1
        print("computer score 1  point")
    elif user==2 and computer==1:
        yourscore+=1
        print("you score one point")
    elif user==3 and computer==1:
        coscore+=1
        print("computer score one point")
    elif user==1 and computer==3:
        yourscore+=1
        print("you score one point")
    elif user==2 and computer==3:
        coscore+=1
        print("computer score one point")
    elif user==3  and computer==2:
        yourscore+=1
        print("you score one point")
    else:
        print("draw")
print("your score is", yourscore)
print("computer score is", coscore)
if yourscore>coscore:
    print("you won at score",yourscore)
elif yourscore<coscore:
    print("computer win at score",coscore)
else:
	print("draw:")

    
