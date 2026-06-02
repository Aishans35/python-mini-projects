import random
rand=random.randint(1,100)
i=0;
while True:
    guess=int(input("guess a number"));
    i=i+1;
    if rand == guess:
        print("your prediction is crct");   
        print("your prediction correct at ",i,"th try");
        break
    elif guess < rand:    
        print("your prediction is small");    
    else :    
        print("your prediction is high ");
    
