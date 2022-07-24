#SOURCE CODE
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database='hospital_management')
mycursor=mydb.cursor()
def addrecord():
    while True:
        try:
            print("In Which Table You Want To Add Record?\n1. Current Patient\n2. Discharged Patient\n3. Doctor_List\n4.\
Doctor Details\n5. Exit To Main Menu")
            choice=int(input("Select One Of The Above Option:"))
            if choice==1:
                P_ID=int(input("Enter The ID Of New Patient(It Must Be Unique):"))
                P_NAME=str(input("Enter The Name Of Patient:"))
                AGE=int(input("Enter Age Of Patient:"))
                DOA=input("Enter The Date Of Admission(yyyy-mm-dd):")
                t=int(input("Enter The Treatement The Patient Will Undergo or Problem Related To \n1. Respiratory\
\n2. Immune System\n3. Kidneys\n4. Joints,Muscles,Bones\n5. Ear,Nose,Throat\n6. General\n7. Glands and Harmones\n8.\
Cancer\n9. Surgery\n10. Skin\n11. Urinary System\n12. Nerves and Nervous\n13. Children\n14. Eye Care\n15. \
Psychological Problem\n16. Pregnancy \nPlease Enter Your Choice(1-16)"))
                if t==1:
                     TREATEMENT='Respiratory'
                elif t==2:
                     TREATEMENT='Immune_System'
                elif t==3:
                     TREATEMENT='Kidneys'
                elif t==4:
                     TREATEMENT='Joints,Muscles,Bones'
                elif t==5:
                     TREATEMENT='Ear,Nose,Throat'
                elif t==6:
                     TREATEMENT='General'
                elif t==7:
                     TREATEMENT='Glands_and_Harmones'
                elif t==8:
                     TREATEMENT='Cancer'
                elif t==9:
                     TREATEMENT='Surgery'
                elif t==10:
                     TREATEMENT='Skin'
                elif t==11:
                     TREATEMENT='Urinary_System'
                elif t==12:
                     TREATEMENT='Nerves_and_Nervous'
                elif t==13:
                     TREATEMENT='Children'
                elif t==14:
                     TREATEMENT='Eye_Care'
                elif t==15:
                     TREATEMENT='Psychological_Problem'
                elif t==16:
                     TREATEMENT='Pregnancy'
                else:
                     print("Wrong Choice")
                     break
                ROOM_NO=int(input("Enter The Room Number Where Patient Will Be Accomodated:"))
                adddata='INSERT INTO curr_patient VALUES(%s,%s,%s,%s,%s,%s)'
                value=[P_ID,P_NAME,AGE,DOA,TREATEMENT,ROOM_NO]
                mycursor.execute(adddata,value)
                mydb.commit()
                print("The Record Has Been Added Succesfully")
            elif choice==2:
                P_ID=int(input("Enter The Patient Unique ID:"))
                P_NAME=str(input("Enter The Name Of Patient:"))
                AGE=int(input("Enter Age Of Patient:"))
                DOS=input("Enter The Date Of DISCHARGING(yyyy-mm-dd):")
                BILL=int(input("Enter The Bill:"))
                print('1. Respiratory \n2. Immune System\n3. Kidneys\n4. Joints,Muscles,Bones\n5. Ear,Nose,Throat\n6. \
General\n7. Glands and Harmones\n8. \Cancer\n9. Surgery\n10. Skin\n11. Urinary System\n12. Nerves and Nervous\n13.\
Children\n14. Eye Care\n15. Psychological Problem\n16. Pregnancy')
                t=int(input("Enter The Treatement or Problem The Patient Faced:"))
                if t==1:
                     TREATEMENT='Respiratory'
                elif t==2:
                     TREATEMENT='Immune_System'
                elif t==3:
                     TREATEMENT='Kidneys'
                elif t==4:
                     TREATEMENT='Joints,Muscles,Bones'
                elif t==5:
                     TREATEMENT='Ear,Nose,Throat'
                elif t==6:
                     TREATEMENT='General'
                elif t==7:
                     TREATEMENT='Glands_and_Harmones'
                elif t==8:
                     TREATEMENT='Cancer'
                elif t==9:
                     TREATEMENT='Surgery'
                elif t==10:
                     TREATEMENT='Skin'
                elif t==11:
                     TREATEMENT='Urinary_System'
                elif t==12:
                     TREATEMENT='Nerves_and_Nervous'
                elif t==13:
                     TREATEMENT='Children'
                elif t==14:
                     TREATEMENT='Eye_Care'
                elif t==15:
                     TREATEMENT='Psychological_Problem'
                elif t==16:
                     TREATEMENT='Pregnancy'
                else:
                     print("Wrong Choice")
                DOC_ASSISTED=input("Enter The Name Of The Doctor Who Treated The Patient:")
                adddata='INSERT INTO old_patient VALUES(%s,%s,%s,%s,%s,%s,%s)'
                value=[P_ID,P_NAME,AGE,DOS,BILL,TREATEMENT,DOC_ASSISTED]
                mycursor.execute(adddata,value)
                mydb.commit()
                print("The Record Has Been Added Succesfully")
            elif choice==3:
                ID=int(input("Enter The ID Of Doctor:"))
                D_NAME=input("Enter The Name Of Doctor:")
                TYPE=input("Enter The Type Of The Doctor:")
                SPECIALITY=input("Enter The Speciality Of Doctor:")
                AGE=int(input("Enter The Age Of Doctor:"))
                ROOM_NO=int(input("Enter The Room Number Of Doctor:"))
                adddata='INSERT INTO doctor_list VALUES(%s,%s,%s,%s,%s,%s)'
                value=(ID,D_NAME,TYPE,SPECIALITY,AGE,ROOM_NO)
                mycursor.execute(adddata,value)
                mydb.commit()
                print("The Record Has Been Added Succesfully")
            elif choice==4:
                ID=int(input("Enter The ID Of Doctor:"))
                D_NAME=input("Enter The Name Of Doctor:")
                DOJ=input("Enter The Date Of Joining:")
                DOB=input("Enter The Date Of Birth Of Docotor:")
                ADDRESS=input("Enter The Address Of Doctor:")
                SALARY=int(input("Enter The Salary Of Doctor:"))
                statement=("INSERT INTO doc_info VALUES(%s,%s,%s,%s,%s,%s)")
                value=(ID,D_NAME,DOJ,DOB,ADDRESS,SALARY)
                mycursor.execute(statement,value)
                mydb.commit()
                print("The Record Has Been Added Succesfully")
            elif choice==5:
                print('You Have Chosen To Exit To Main Menu')
                break
            else:
                print('Wrong Input! Please Try Again:')
                addrecord()
        except Exception as e:
            print(e)
            addrecord()
def deleterecord():
    try:
        while True:
            print("In Which Table You Want To Delete Record?\n1. Current Patient\n2. Discharged Patient\n3.\
Doctor_List\n4. Doctor Details\n5. Exit To Main Menu")
            choice=int(input("Enter Your Choice:"))
            if choice==1:
                ID=int(input("Enter The ID Of Current Patient You Want To Delete:"))
                mycursor.execute("SELECT * FROM curr_patient Where P_ID=%d"%(ID,))
                record=mycursor.fetchall()
                for i in record:
                    print('The Record Is:',i)
                mycursor.execute("DELETE FROM curr_patient where P_ID=%d"%(ID,))
                mydb.commit()
                print('The Record Has Been Deleted Succesfully!')
            elif choice==2:
                ID=int(input("Enter The ID Of Discharged Patient You Want To Delete:"))
                mycursor.execute("SELECT * FROM old_patient Where P_ID=%d"%(ID,))
                record=mycursor.fetchall()
                for i in record:
                    print('The Record Is:',i)
                mycursor.execute("DELETE FROM old_patient where P_ID=%d"%(ID,))
                mydb.commit()
                print('The Record Has Been Deleted Succesfully!')
            elif choice==3:
                ID=int(input("Enter The ID Of Doctor You Want To Delete:"))
                mycursor.execute("SELECT * FROM doctor_list Where ID=%d"%(ID,))
                record=mycursor.fetchall()
                for i in record:
                    print('The Record Is:',i)
                mycursor.execute("DELETE FROM doctor_list where ID=%d"%(ID,))
                mydb.commit()
                print('The Record Has Been Deleted Succesfully!')
            elif choice==4:
                ID=int(input("Enter The ID Of Doctor Whose Data You Want To Delete:"))
                mycursor.execute("SELECT * FROM doc_info Where ID=%d"%(ID,))
                record=mycursor.fetchall()
                for i in record:
                    print('The Record Is:',i)
                mycursor.execute("DELETE FROM doc_info where ID=%d"%(ID,))
                mydb.commit()
                print('The Record Has Been Deleted Succesfully!')
            elif choice==5:
                print('You Have Chosen To Exit To Main Menu')
                break
            else:
                print('Wrong Choice! Please Try Again.')
                deleterecord()
    except Exception as e:
            print(e)
def display():
    while True:
        try:
            print("Which Table You Want To Show?\n1. Current Patient\n2. Discharged Patient\n3.\
Doctor_List\n4. Doctor Details\n5. Exit To Main Menu")
            choice=int(input("Enter Your Choice:"))
            if choice==1:
                statement='Select * from curr_patient'
                mycursor.execute(statement)
                Value=mycursor.fetchall()
                print('The data are as Follows :-')
                for data in Value:
                    Patient_ID=data[0]
                    Patient_Name=data[1]
                    Age=data[2]
                    Date_Of_Admission=data[3]
                    Treatement=data[4]
                    Room_No=data[5]
                    print('Patient_ID - %s,Patient Name - %s,  Age - %s, Date Of Admission - %s, \
Treatement - %s,  Room No. - %s' %(Patient_ID,Patient_Name,Age,Date_Of_Admission,Treatement,Room_No))
            elif choice==2:
                statement='Select * from old_patient'
                mycursor.execute(statement)
                Value=mycursor.fetchall()
                print('The Records Are as Follows:')
                for data in Value:
                    Patient_ID=data[0]
                    Patient_Name=data[1]
                    Age=data[2]
                    Date_Of_Admission=data[3]
                    Bill=data[4]
                    Treatement=data[5]
                    print("ID - %s , Name - %s , Age - %s , Date Of Admission - %s , Bill-%s,Treatement - \
%s "%(Patient_ID,Patient_Name,Age,Date_Of_Admission,Bill,Treatement))
            elif choice==3:
                statement='Select * from doctor_list'
                mycursor.execute(statement)
                Value=mycursor.fetchall()
                print('The data are as Follows')
                for data in Value:
                    Doctor_ID=data[0]
                    Doctor_Name=data[1]
                    Type=data[2]
                    Speciality=data[3]
                    Age=data[4]
                    Room_No=data[5]
                    print('ID - %s , Name - %s , Type - %s , Speciality - %s , Age - %s , Room_No. - %s\
' %(Doctor_ID,Doctor_Name,Type,Speciality,Age,Room_No))
            elif choice==4:
                statement='Select * from Doc_info'
                mycursor.execute(statement)
                Value=mycursor.fetchall()
                print('The data are as Follows')
                for data in Value:
                    Doc_ID=data[0]
                    Doc_Name=data[1]
                    DOJ=data[2]
                    DOB=data[3]
                    ADDRESS=data[4]
                    Salary=data[5]
                    print(' ID - %s,Name - %s, Date Of Joining - %s,  Date Of Birth - %s,Address - %s,  Salary -\
%s' %(Doc_ID,Doc_Name,DOJ,DOB,ADDRESS,Salary))
            elif choice==5:
                print('You Have Chosen To Exit To Main Menu')
                break
            else:
                print('Wrong Choice!! Please Try Again.')
                display()
        except Exception as e:
            print(e)
            
def edit():
    while True:
        try:
            print('Which Table You Want To Edit \n1. Current Patient\n2. Discharged Patient\n3. Doctor_List\n4. \
Doctor Details\n5. Exit To Main Menu')
            choice=int(input('Enter Your Choice(1-5):'))
            if choice==1:
                ID=int(input('Enter The ID Of Patient Whose Data You Want To Update'))
                echoice=int(input("Which Field You Want To Edit?\n1.Age \n2.Treatement \n3.Room Number \n Enter \
Your Choice(1-3):"))
                if echoice==1:
                    column='AGE'
                elif echoice==2:
                    column='TREATEMENT'
                elif echoice==3:
                    column='ROOM_NO'
                else:print('Wrong Choice')
                updated_value=str(input('Enter The Updated Value:'))
                statement='update curr_patient set %s="%s" where P_ID=%s'%(column,updated_value,ID)
                mycursor.execute(statement)
                print("The Record Has Been Updated")
            elif choice==2:
                ID=int(input('Enter The ID Of Patient Whose Data You Want To Update'))
                echoice=int(input("Which Field You Want To Edit?\n1.Age \n2.Bill \n3.TREATMENT \n4.DOCTOR-ASSISTED \n\
Enter Your Choice(1-4):"))
                if echoice==1:
                    column='AGE'
                elif echoice==2:
                    column='BILL'
                elif echoice==3:
                    column='PROBLEM_or_TREATMENT'
                elif echoice==4:
                    column='DOC_ASSISTED'
                else:print('Wrong Choice')
                updated_value=str(input('Enter The Updated Value:'))
                statement='update old_patient set %s="%s" where P_ID=%s'%(column,updated_value,ID)
                mycursor.execute(statement)
                print("The Record Has Been Updated")
            elif choice==3:
                ID=int(input('Enter The ID Of Doctor Whose Data You Want To Update'))
                echoice=int(input("Which Field You Want To Edit?\n1.Type \n2.Speciality \n3.Age \n4.Room No. \n\
Enter Your Choice(1-4):"))
                if echoice==1:
                    column='TYPE'
                elif echoice==2:
                    column='SPECIALITY'
                elif echoice==3:
                    column='AGE'
                elif echoice==4:
                    column='ROOMNO'
                else:print('Wrong Choice')
                updated_value=str(input('Enter The Updated Value:'))
                statement='update Doctor_list set %s="%s" where ID=%s'%(column,updated_value,ID)
                mycursor.execute(statement)
                print("The Record Has Been Updated")
            elif choice==4:
                ID=int(input('Enter The ID Of Doctor Whose Data You Want To Update'))
                echoice=int(input("Which Field You Want To Edit?\n1.Address \n2.Salary \nEnter Your Choice(1/2):"))
                if echoice==1:
                    column='ADDRESS'
                elif echoice==2:
                    column='SALARY'
                else:print('Wrong Choice')
                updated_value=input('Enter The Updated Value:')
                statement='update Doc_info set %s="%s" where ID=%s'%(column,updated_value,ID)
                mycursor.execute(statement)
                print("The Record Has Been Updated")
            elif choice==5:
                print('You Have Chosen To Exit To Main Menu')
                break
        except :
            print('An Unexpected Error Occured Please Try Again')
            edit()
        mydb.commit()
print("--------------------------------\nWELCOME TO HOSPITAL MANAGEMENT\n--------------------------------")
while True:
    fchoice=int(input("Which Function You Want To Perform? \n1.Add Record \n2.Delete Record\
\n3.Display Record \n4.Edit Record \n5.Exit \nEnter Your Choice(1-5):"))
    if fchoice==1:
        addrecord()
    elif fchoice==2:
        deleterecord()
    elif fchoice==3:
        display()
    elif fchoice==4:
        edit()
    elif fchoice==5:
        print('Thank You For Using Hospital Management System.....')
        break
    else:
        print("Wrong Choice! Please Try Again..")
        pass
        
        


