import mysql.connector as ms
ms=ms.connect(user="root",host="localhost",password="",database="user")
from tabulate import tabulate
from PIL import Image
import sys,time,os
def typewriter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char!="\n":
            time.sleep(0.03)
        else:
            time.sleep(0.4)

c=ms.cursor()
if ms.is_connected():
    print("connection extablished")
os.system("cls")
print("1>Sign up by creating a new user")
print("2>Login into exixting account")
choice=input("Enter your choice: ")
if(choice=="1"):
    username=input("Enter user name:").lower()
    password=input("Enter password:")
    cls=input("Enter class:")
    querry='insert into user_info(name,password,class) values("{}","{}","{}")'.format(username,password,cls)
    c.execute(querry)
    ms.commit()
elif(choice=="2"):
    username=input("Enter user name:").lower()
    password=input("Enter password:")
    querry='SELECT EXISTS(SELECT * from user_info WHERE name="{}" and password="{}");'.format(username,password)
    c.execute(querry)
    exsit=c.fetchall()
    for i in exsit:
        if(1 in i):
            print("You are successfully logged in")
            while(True):
                print("do you want to move on or quit y/n:")
                choice=input()
                if(choice=="y"):
                    print("concepts available:")
                    querry1="select t_name ,application from math_fun"
                    c.execute(querry1)
                    topics=c.fetchall()
                    print(tabulate(topics,headers=["Topics","Applicatoin"],tablefmt="fancy_grid"))
                    print('''Enter the Maths concept or Application of the maths concept you need''')
                    search=input()
                    querry1='SELECT EXISTS(SELECT * from math_fun WHERE t_name="{}");'.format(search)
                    c.execute(querry1)
                    querry1_d=c.fetchall()
                    querry1_d=querry1_d[0]
                    querry2='SELECT EXISTS(SELECT * from math_fun WHERE application="{}");'.format(search)
                    c.execute(querry2)
                    querry2_d=c.fetchall()
                    querry2_d=querry2_d[0]
                    while True:
                        if (1 in querry1_d):
                            print("The topic name you asked for is:")
                            print(search)
                            q3="select t_brief from math_fun where t_name='{}'".format(search)
                            c.execute(q3)
                            q3_d=c.fetchall()
                            typewriter(q3_d[0][0])
                            choice2=input("Enter do you want to continue further y/n: ")
                            if(choice2=="y"):
                                q3="select eg_prob from math_fun where t_name='{}'".format(search)
                                c.execute(q3)
                                q3_d=c.fetchall()
                                typewriter("Here is a example problem for your required concept:\n")
                                typewriter(q3_d[0][0])
                                choice2=input("Enter do you want to continue further y/n: ")
                                if(choice2=="y"):
                                    q3="select soln from math_fun where t_name='{}'".format(search)
                                    c.execute(q3)
                                    q3_d=c.fetchall()
                                    q3_d=q3_d[0][0]
                                    im = Image.open(q3_d)
                                    im.show()
                                    choice2=input("Enter do you want to continue further y/n: ")
                                    if(choice2=="y"):
                                        q3="select application from math_fun where t_name='{}'".format(search)
                                        c.execute(q3)
                                        q3_d=c.fetchall()
                                        q3_d=q3_d[0][0]
                                        print("This Concept is used in ",q3_d)
                                        choice2=input("Enter do you want to continue further y/n: ")
                                        if(choice2=="y"):
                                            q3="select app_brief from math_fun where t_name='{}'".format(search)
                                            c.execute(q3)
                                            q3_d=c.fetchall()
                                            q3_d=q3_d[0][0]
                                            typewriter(q3_d)
                                            break
                                        else:
                                            print("Enter a right option")
                                    elif(choice2=="n"):
                                        break
                                    else:
                                        print("Enter a right option")

                                elif(choice2=="n"):
                                    break
                                else:
                                    print("Enter a right option")
                            elif(choice2=="n"):
                                break
                            else:
                                print("Enter a right option")

                        elif(1 in querry2_d):
                            typewriter("The topic name corresponding to the application you asked for is:")
                            q3="select t_name from math_fun where application='{}'".format(search)
                            c.execute(q3)
                            q3_d=c.fetchall()
                            print(q3_d[0][0])
                            q3="select t_brief from math_fun where application='{}'".format(search)
                            c.execute(q3)
                            q3_d=c.fetchall()
                            typewriter(q3_d[0][0])
                            choice2=input("Enter do you want to continue further y/n: ")
                            if(choice2=="y"):
                                q3="select eg_prob from math_fun where application='{}'".format(search)
                                c.execute(q3)
                                q3_d=c.fetchall()
                                typewriter("Here is a example problem for your required concept:\n")
                                typewriter(q3_d[0][0])
                                choice2=input("Enter do you want to continue further y/n: ")
                                if(choice2=="y"):
                                    q3="select soln from math_fun where application='{}'".format(search)
                                    c.execute(q3)
                                    q3_d=c.fetchall()
                                    q3_d=q3_d[0][0]
                                    im = Image.open(q3_d)
                                    im.show()
                                    choice2=input("Enter do you want to continue further y/n: ")
                                    break
                                else:
                                    print("Enter a right option")
                            elif(choice2=="n"):
                                break
                            else:
                                print("Enter a right option")
                        else:
                            print("Topic or application not available in the database")
                            break
                elif(choice=="n"):
                    break
                else:
                    print("Enter a correct option")
                
        else:
            print("your credentials are incorrect")

else:
    print("Enter the correct choice")
    



