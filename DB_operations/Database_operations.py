'''
Created on Mar 5, 2015

@author: Nitin
'''
import psycopg2
import MySQLdb
import time
# import os

class Database():
    host =""
    port = 0
    database_name = ""
    uname = ""
    pwd = ""
    connector = ''
    con=True
    data = []
    table = ''
    def getDbdetails(self):
        global host,port,database_name,uname,pwd
        print""
        print "In dbdetails"
        print "************"
        
        try:
            host = raw_input("Please enter the host name:: ")
            #port = raw_input("Please enter the port number :: ")
            database_name = raw_input("Please enter the database name :: ")
            uname = raw_input("Please enter user name :: ")
            pwd = raw_input("Please enter password ::  ")
            return 1            
        except Exception,err:
            print"Bad input:: ",err
            return 0
    def getConnection(self):
        global host,port,database_name,uname,pwd,connector,con
        print ""
        print "Requesting connection....."
        print "**************************"
        try:
            '''con = psycopg2.connect(database=database_name,
                                   user=uname,
                                   password=pwd,
                                   host=host,
                                   port=port)'''
            #print connector
            con = connector.connect(host=host,                                    
                                   user=uname,
                                   password=pwd,
                                   database=database_name)
           # con = connector.connect("host=%s,user=%s,password=%s,dbname=%s" ,(host,uname,pwd,database_name))
           
            return con   
            
        except Exception,err:
            print"Error in getting connection :: ",err
            return 0
        
    def choice_of_operations(self):
        global con,database_name,table,data
        data= []
        cursor = con.cursor()
        sql = """SELECT table_name FROM information_schema.tables WHERE table_schema='public';"""
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            i=0
            max_rows = len(results)
            print"Number of tables got:: ",max_rows
            
            for row in results:
                if(i>(max_rows-1)): 
                    break
                else:
                    tablename = str(row).strip("(''),")
                    data.append(tablename)
                    print "Table ",i," :: ",data[i]
                    i=i+1               
            num=int(raw_input("Select table number :: "))
            print "Table selected  :: ",data[num] 
            print"ok..."
            print ""
            table = data[num]
            #-----Lets see the description of the table selected
            obj4 = Database()
            print "Table description "
            print "******************"
            print ""
            obj4.table_desc(table)
            
            print ""          
        except Exception ,err:
            print"Message from db -- error fetching data",err
            con.rollback()
            con.close()
            return 0
            
        
        print ""
        print "In choice_of_operation"
        print "**********************"
        print"1.Select"
        print"2.Insert"
        print"3.Update"
        print"4.Delete"
        while(True):
            try:
                choice = int(raw_input("Enter your choice number:: "))
                obj3=Database()
                status = obj3.done_operation(choice)
                if(status==1):
                    print"Operation done successfully"
                else:
                    print "Execution error"
                break
            except Exception,err:
                print "Bad input ",err
                
        return choice
    def table_desc(self,name):
        global table,con
        cursor = con.cursor()
        sql = """select column_name,data_type,character_maximum_length from information_schema.columns where table_name='%s';""" %(table)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print "column_name||data_type||character_maxlength"
            print"*********************************************"
            for row in results:
                column_name = row[0]
                column_data_type = row[1]
                character_max_len = row[2]
                print column_name,"||",column_data_type,"||",character_max_len
        except Exception,err:
            print "Error in fetchting data from table :: ",table
            print err
            con.close()
            return 0
        
        pass
    def done_operation(self,operation):
        global con,table
        print""
        print"In done_operation"
        print "****************"
        try:
            if(operation == 1):
                cursor = con.cursor()
                sql="""select * from %s;""" % (table)
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    print "Printing the table contents...."
                    print "*******************************"
                    time.sleep(3)
                    count=1
                    for row in results:
                        print "Row ",count," :: ", row
                        count+=1
                        
                    print "total rows printed :: ",count-1
                    return 1
                except Exception ,err:
                    print"Message from db -- error inserting data",err
                    con.rollback()
                    return 0
                    con.close()
                return 1
            if(operation == 2):
                print "do insert"
                return 1
            if(operation == 3):
                print "do update"
                return 1
            if(operation == 4):
                print "do delete"
                return 1
        except Exception,err:
            print"Exception in desired operation :: ",err
            return 0
    def main(self):
        print ""
        print "In main"
        obj1 = Database()
        status1 = obj1.getDbdetails()
        if(status1==1):
            print"Database information collected successfully"
            print""
            while(True):
                status2 = obj1.getConnection()
                if(status2 == 0):
                    print "Database connection error...."
                    print""
                    print "Please enter the details again..."
                    print ""
                    status2 = obj1.getDbdetails()
                    continue
                else:
                    print"Connected to database successfully........"
                    print""
                    break
            operation = obj1.choice_of_operations()
            '''print "***************************"
            print "Choice entered :: ",operation
            print "***************************"
            status4 = obj1.done_operation(operation)
            if(status4 == 0):
                print"Operation not performed successfully"
            if(status4 == 1):
                print"Operation performed successfully" '''
                 
        return 1
print"JARVIS Utility 1 Version 0.1"
print"****************************"
print "It  is for developers to make database operations,"
print"and currently it works for postgreSQL...."
print ""
try: 
    print ""
    choice = raw_input("(P).PostgreSQL :: ")
    if (choice.lower() == "p"):
        connector = psycopg2
    if (choice.lower() == "m"):
        connector = MySQLdb
except Exception,err:
    print "Bad RDBMS choice :: ",err
    
obj2 = Database()

while(True):
    final_status = obj2.main()
    if(final_status == 1):
        print "All operations done successfully!!"
        print ""
        break
    else:
        print "Operations not performed successfully"
        print ""
        choice =raw_input("Do you want to continue ?? Y/N :: " )
        print ""
        if(choice.lower() == "y"):
            print "Continuing "
            print ""
            continue
        else:
            print "Exiting operation"
            print""
            break
print "********************************"
print "Thanks for using my application"
print ""
print "Application stopped"
print ""
print "If you want to run the application run it again.."

        