import random
score=0;
while True:
    guess=int(input("choose lane\n 1.right\n 2.left\n"))
    if guess not in[1,2]:
        print("choose 1 or 2")
        continue
    ob=random.randint(1,2)
    print("obstacle in line:",ob)
    if ob==guess:
        print("game over")
        break
    else:
         print("you are safe")
         score=score+1;
print("your score is",score)
    
