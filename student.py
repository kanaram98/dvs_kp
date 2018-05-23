print('enter the type of user')
print('1.admin')
print('2.student')
print('3.teacher')
print('select an operation')
a=input("select (1/2/3)")

if a=='1':
    list3=[]
    print("enter the admin details ")
    c=input()
    list3.append(c)
    print(list3)
elif a=='2':
    print("are you a existing student ")
    d=input('yes or no ')
    if d=='yes':
        print("your rank")
        print("student marks")
        print("your attendence")
    elif d=='no':
        list1=[]
        print("enter your name" )
        e=input()
        list1.append(e)
        #print(e)
        
        print("enter your address" )
        f=input()
        list1.append(f)
        #print(f)
        
        print("enter your fee" )
        g=input()
        list1.append(g)
        #print(g)
        
        print("enter your rank in your class" )
        h=input()
        #print(h)
        list1.append(h)
        print(list1)
elif a=='3':
    list2=[]
    print("enter your name" )
    i=input()
    list2.append(i)
    print(list2)
        #print(e)
    
