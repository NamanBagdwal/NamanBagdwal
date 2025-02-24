import mysql.connector
print("""
____________________________________________________
Welcome To Sales And Inventory Management System
____________________________________________________
""")
mydb=mysql.connector.connect(host="localhost",user='root',password='12345')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sales_manage")
mycursor.execute("use sales_manage")
mycursor.execute("create table if not exists login (username varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(odate date not null,name varchar(25) not null,pcode int not null,amount int not null)")
mycursor.execute("create table if not exists stock(pcode int not null,pname varchar(25) not null,quantity int not null,price int not null)")
mydb.commit()
z=0
mycursor.execute("select* from login")
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('usernamr','pass_')")
    mydb.commit()
while True:
    print("""1.Admin
2.Customer
3.Exit
""")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        passs=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor:
             username,password=i
        if(passs==password):
            print("Welcome")
            loop2='y'
            while(loop2=='y'or loop2=='Y'):
                 print("""    1.Add New Item
         2.updating price
         3.Deleting Item
         4.Display All Items
         5.To change the password
         6.Log Out
""")
                 ch=int(input("Enter your choice:"))
                 if(ch==1):
                     loop3='y'
                     while(loop3=='y'or loop3=='Y'):
                          pcode=int(input("Enter product code:"))
                          pname=input("Enter product name:")
                          quantity=int(input("Enter product quantity:"))
                          price=int(input("Enter product price:"))
                          mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                          mydb.commit()
                          print("Record Successfully Inserted...")
                          loop3=input("Do you want to enter more items(y/n):")
                     loop2=input("Do you want to continue editing stock(y/n):")
                 elif(ch==2):
                     loop3='y'
                     while(loop3=='y' or loop3=='Y'):
                          pcode=int(input("Enter product code:"))
                          new_price=int(input("Enter new price:"))
                          mycursor.execute("update stock set price='"+str(new_price)+"'where pcode='"+str(pcode)+"'")
                          mydb.commit()
                          print("Record successfully Updated...")
                          loop3=input("Do you want to update price of any other item(y/n):")
                     loop2=input("Do you want to continue editing stock(y/n):")
                 elif(ch==3):
                     loop3='y'
                     while(loop3=='y' or loop3=='Y'):
                          pcode=int(input("Enter product code:"))
                          mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                          mydb.commit()
                          print("Record Successfully Deleted...")
                          loop3=input("Do you want to delete any other data(y/n):")
                     loop2=input("Do you want to continue editing stock(y/n):")  
                 elif(ch==4):
                     mycursor.execute("select * from stock")
                     print("pcode||pname||quantity||price")
                     for i in mycursor:
                         t_code,t_name,t_quan,t_price=i
                         print(f"{t_code}||{t_name}||{t_quan}||{t_price}")
                 elif(ch==5):
                     old_passs=input("Enter old password:")
                     mycursor.execute("select * from login")
                     for i in mycursor:
                          username,password=i
                     if(old_passs==password):
                         new_passs=input("Enter new Password:")
                         mycursor.execute("update login set password='"+new_passs+"'")
                         mydb.commit()
                         print("Password Successfully Changed...")
                 elif(ch==6):
                     break
        else:
            print("Wrong password")
########################################Customer Section
    elif(ch==2):
         print("""1.Item Bucket
2.Payment
3.View Available Items
4.Go Back
""")
         ch2=int(input("Enter your choice:"))
         if(ch2==1):
             name=input("Enter your name:")
             pcode=int(input("Enter product code:"))
             quantity=int(input("Enter product quantity:"))
             mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
             for i in mycursor:
                 t_code,t_name,t_quan,t_price=i
             amount=t_price*quantity
             net_quan=t_quan-quantity
             mycursor.execute("update stock set quantity='"+str(net_quan)+"'where pcode='"+str(pcode)+"'")
             mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"')")
             mydb.commit()
         elif(ch2==2):
             print(f"amount to be paid{amount}")
         elif(ch2==3):
             print("CODE||NAME||PRICE")
             mycursor.execute("select * from stock")
             for i in mycursor:
                 t_code,t_name,t_quan,t_price=i
                 print(f"{t_code}||{t_name}||{t_price}")
         elif(ch2==4):
             break
    elif(ch==3):
        break

                        
       
                          
                     
                     
                    
                    
                     
                 
            
            
                
           
           
                
                
                
                
           
              
                
               
                
                                   
                
           
                
       
        
        
        
    
 
