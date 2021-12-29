import psycopg2

from prettytable import PrettyTable

class A:
    def connection(self):
        con=psycopg2.connect(host='localhost',database='food',user='postgres',password='admin')
        return con
    def create_table(self):
        if (self.connection()):
            con=self.connection()
            sql='''CREATE TABLE sample (id INT PRIMARY KEY,food_name TEXT,location TEXT)'''
            cur=con.cursor()
            cur.execute(sql)
            con.commit()
            con.close()
            print("table created")
    def insert_10_table(self):
        if (self.connection()):
            con=self.connection()
            sql_1='''INSERT INTO  sample values(1,'biriyani','india')'''
            sql_2='''INSERT INTO  sample values(2,'dosa','china')'''
            sql_3='''INSERT INTO  sample values(3,'idly','nepal')'''
            sql_4='''INSERT INTO  sample values(4,'poori','tibet')'''
            sql_5='''INSERT INTO  sample values(5,'pongal','sri lanka')'''
            sql_6='''INSERT INTO  sample values(6,'fried rice','japan')'''
            sql_7='''INSERT INTO  sample values(7,'kfc','australia')'''
            sql_8='''INSERT INTO  sample values(8,'mcd','mexico')'''
            sql_9='''INSERT INTO  sample values(9,'burgerking','brazil')'''
            sql_10='''INSERT INTO  sample values(10,'subway','usa')'''
            cur=con.cursor()
            cur.execute(sql_1)
            cur.execute(sql_2)
            cur.execute(sql_3)
            cur.execute(sql_4)
            cur.execute(sql_5)
            cur.execute(sql_6)
            cur.execute(sql_7)
            cur.execute(sql_8)
            cur.execute(sql_9)
            cur.execute(sql_10)
            con.commit()
            con.close()
            print("value_insert")

    def insert(self,_id,name,location):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql='''INSERT INTO  sample  values({},'{}','{}');'''.format(_id,name,location)
            cur.execute(sql)
            con.commit()
            con.close()
            print("value_insert")           
    
    def delete_by_id(self,_id):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql="DELETE FROM sample WHERE id={}".format(_id)
            cur.execute(sql) 
            con.commit()
            con.close()
            print("data deleted successfully!")
    
    def update_by_id(self,_id,query,new_value):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql="UPDATE sample set {}='{}' WHERE id={};".format(query,new_value,_id)
            cur.execute(sql) 
            con.commit()
            con.close()
            print("data updated successfully!")

    def display(self):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql='''Select * from sample;'''
            cur.execute(sql)
            data=cur.fetchall()
            t = PrettyTable(['id', 'food_name','location'])
            for data in data:
             t.add_row(data)
            print(t)
            con.close()

    def display_by_id(self,_id):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql='''Select * from sample where id={};'''.format(_id)
            cur.execute(sql)
            data=cur.fetchall()
            t = PrettyTable(['id', 'food_name','location'])
            for data in data:
             t.add_row(data)
            print(t)
            con.close()
    def display_by_like(self,query,value):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql='''Select * from sample where {} like '{}';'''.format(query,value)
            cur.execute(sql)
            data=cur.fetchall()
            t = PrettyTable(['id', 'food_name','location'])
            for data in data:
             t.add_row(data)
            print(t)
            con.close()
     
    def truncate(self):
        if (self.connection()):
            con=self.connection()
            cur=con.cursor()
            sql='''truncate table sample;'''
            cur.execute(sql) 
            con.commit()
            con.close()
            print("table truncated successfully!")                        

a=A()
ans=1

while ans!=0:
    print ("1.Create table")
    print ("2.Insert all data")
    print ("3.Insert user given data")
    print ("4.Display all data")
    print("5.Display data by id")
    print ("6.Display by Like")
    print ("7.Delete by id")
    print ("8.Truncate")
    print ("9.Update by id")
    print("Press 1-9 or 0 to Exit:")
    ans=int(input())
    if(ans==1):
       a.create_table()
    elif(ans==2):
       a.insert_10_table()
    elif(ans==3):
       print("enter id:")
       _id=int(input())
       print("enter food_name:")
       food_name=input()
       print("enter location:")
       location=input() 
       a.insert(_id,food_name,location)
    elif(ans==4):
       a.display()
    elif(ans==5):
       print("enter _id:")
       _id=int(input())
       a.display_by_id(_id)
    elif(ans==6):
       print("1.food_name")
       print("2.location")
       print("enter column_num:")
       opt=int(input())
       q=['food_name','location']
       query=q[opt-1]
       print("enter value:")
       value=input() 
       a.display_by_like(query,value)
    elif(ans==7):
       print("enter _id:")
       _id=int(input())
       a.delete_by_id(_id) 
    elif(ans==8):
       a.truncate()
    elif(ans==9):             
       print("enter _id:")
       _id=int(input())
       q=['food_name','location']
       print("1.food_name")
       print("2.location")
       print("enter column_num:")
       opt=int(input())
       query=q[opt-1]
       print("enter value:")
       value=input() 
       a.update_by_id(_id,query,value)
    elif(ans==0):
      print("Goodbye") 
      ans=0
      break             
#a.create_table()
#a.display()
#a.truncate()
#a.display_by_id(1)
#a.display_by_like('food_name','b%')
#a.insert_10_table()
#a.delete_by_id(10)
#a.update_by_id(9,'food_name','burger')
#a.insert(10,"gulab_jamun","africa")