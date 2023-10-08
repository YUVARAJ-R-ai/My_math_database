import mysql.connector as ms
import os
def sep_elem(l1,ele):
    c=l1.count(ele)
    newl=[]
    emp=[]
    for i in range(len(l1)):
        if l1[i]==ele:
            emp.append(i)
    len_e=len(emp)
    for j in range (len_e-1):
        newl+=[l1[emp[j]+1:emp[j+1]]]
    return newl
os.system("cls")
ms=ms.connect(user="root",host="localhost",password="",database="user")
c=ms.cursor()
if ms.is_connected():
    print("connection extablished")
while True:
    print("1>Enter a record ")
    print("2>exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        path=r"C:\Users\sindu\Documents\python\math_fun\test.txt"
        f= open(path,"r") 
        data=f.readlines()
        new_data=sep_elem(data,"***\n")
        #print(new_data)
        t_no,t_name,t_brief,eg_prob,soln,app,app_brief=new_data
        t_no_s=""
        t_name_s=""
        t_brief_s=""
        eg_prob_s=""
        soln_s=""
        app_s=""
        app_brief_s=""

        for i in t_no:
            t_no_s+=i
        for i in t_name:
            t_name_s+=i
        for i in t_brief:
            t_brief_s+=i
        for i in eg_prob:
            eg_prob_s+=i
        for i in soln:
            soln_s+=i
        for i in app_s:
            app_s+=i
        for i in app_brief:
            app_brief_s+=i
        t_no_s=t_no_s.replace("\n","")
        t_no_s=int(t_no_s)
        querry="insert into math_fun values({},'{}','{}','{}','{}','{}','{}')".format(t_no_s,t_name_s,t_brief_s,eg_prob_s,soln_s,app_s,app_brief_s)
        querry=querry.replace("\n","\\n")
        print(querry)
        c.execute(querry)
        ms.commit()
        app_brief_s=app_brief_s.replace("\n","\\n")
    elif choice==2:
        break