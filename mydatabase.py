import mysql.connector as m
from datetime import datetime 

conn=None
def connect():
    global conn
    conn=m.connect(host="localhost",user="root",password="root",database="schooldb")
    if conn.is_connected():
        return True
    else:
        return False
def add_record():
    if(connect()):
        cur=conn.cursor()
        r=int(input("Enter Roll"))
        n=input("Enter Name")
        c=input("Enter Course")
        ad=datetime.now().strftime("%Y-%m-%d")
        query='''insert into student(S_Roll,S_Name,S_Course,addmissionDate)
        values(%s,%s,%s,%s)'''
        value=(r,n,c,ad)
        cur.execute(query,value)
        conn.commit()
        print("Record Added Successfully")
    else:
        print("Connection Error")

def View_Record():
    if(connect()):
        cur=conn.cursor()
        query="select * from student"
        cur.execute(query)
        records=cur.fetchall()
        for rec in records:
            print(f"{rec[0]} | {rec[1]} | {rec[2]} | {rec[3]}")
        else:
            print("Record Empty")
def delete_record():
    if(connect()):
        r=int(input("Enter roll to Delete"))
        cur=conn.cursor()
        cur.execute("select * from student")
        records=cur.fetchall()
        for rec in records:
            if r==rec[0]:
                q="delete from student where S_Roll=%s"
                v=(r,)
                cur.execute(q,v)
                conn.commit()
                print("Record deleted")
                break
        else:
            print("Record does not exist")
    else:
        print("Error")

def update_record():
    if(connect()):
        r=int(input("Enter roll to update"))
        cur=conn.cursor()
        cur.execute("select *from student")
        records=cur.fetchall()
        for rec in records:
            if r==rec[0]:
                ui=int(input("What do you want to update?\n1.Name\n2.Course"))
                if ui==1:
                    n=input("Enter New Name")
                    q="update student set S_Name=%s where S_Roll=%s"
                elif ui==2:
                    n=input("Enter New Course")
                    q="update student set S_Course=%s where S_Roll=%s"
                v=(n,r)
                cur.execute(q,v)
                conn.commit()
                print("Data update")
                break
            else:
                print("Record Does Not Exit")
        else:
            print("Error")

while True:
    print("1. Add Records")
    print("2. View Records")
    print("3. Delete Records")
    print("4. Update Records")
    print("5. Exit")
    ch=int(input("Enter choise:"))
    if ch==1:
        add_record()
    elif ch==2:
        View_Record()
    elif ch==3:
        delete_record()
    elif ch==4:
        update_record() 
    elif ch==5:
        break




    

    







