todos=[]
def add(todos):
     user=input("what we need to do\n")
     todos.append(user)
def remove(todos):
	 re=input("what we need to remove\n")
	 todos.remove(re)
while True:
    op=int(input("1.Add \n 2.remove\n 3.exit\n "))
    if op==1:
        add(todos)
        print(todos)
    elif op==2:
	    remove(todos)
	    print(todos)
    elif op==3:
        break
print("todolist is",todos)
