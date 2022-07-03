#Working with Binary Files

import pickle
import os

#Create a binary file to store records and append more records
def Create_rec():
    name_rec = input("Enter the name of the record file: ")
    f = open(f"{name_rec}","ab")
    n = int(input("How many records do you want to enter? "))
    for N in range(0, n):
        rollno = int (input ("Enter the Roll No.:") )
        name = input ("Enter the Name: ")
        marks = int (input ("Enter the Marks:") )
        rec = {"Roll No.": rollno, "Name": name, "Marks": marks}
        pickle.dump(rec, f)
    f.close()

#Reading the records
def Read_rec():
    name_rec = input("Enter the name of the record file: ")
    f = open (f"{name_rec}","rb")
    while True:
        try:
            rec = pickle.load(f)
            print ("Roll No.: ", rec['Roll No.'])
            print ("Name: ", rec["Name"])
            print ("Marks: ", rec["Marks"])
            print(" ")
        except EOFError:
            break
    f.close()

#Searching for a record 
def Search(rollno_search):
    name_rec = input("Enter the name of the record file: ")
    f = open (f"{name_rec}","rb")
    found = False
    while True:
        try:
            rec = pickle.load(f)
            if rec["Roll No."] == rollno_search:
                print("Record Found")
                print ("Roll No.: ", rec['Roll No.'])
                print ("Name: ", rec["Name"])
                print ("Marks: ", rec["Marks"])
                found = True
        except EOFError:
            break
    if found == False:
        print ("Record Not Found")
    f.close()

#Modifying the marks in an existing record
def Modify_Entry(rollno_modify, marks_modify):
    name_rec = input("Enter the name of the record file: ")
    f = open(f"{name_rec}", "rb")
    record = []
    while True:
        try:
            rec = pickle.load(f)
            record.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(record)):
        if record[i]['Roll No.'] == rollno_modify:
            record[i]['Marks'] = marks_modify
    f = open(f"{name_rec}",'wb')
    for x in record:
        pickle.dump(x, f)
    f.close()

#Deleting a record 
def Delete_Entry():
    name_rec = input("Enter the name of the record file: ")
    def del_rec():
        roll_insert = int(input("Enter the Roll No. corresponding to the record that you want to delete: "))
        
        f = open (f"{name_rec}","rb")
        while True:
            try:
                rec = pickle.load(f)
                temp_data = {"Roll No.": rec['Roll No.'], "Name": rec["Name"], "Marks": rec["Marks"]}
                
                with open("temp_del.dat", 'ab') as temp:    
                    if rec["Roll No."] != roll_insert:
                        pickle.dump(temp_data, temp)
                    elif rec["Roll No."] == roll_insert:
                        pass
                        temp.flush()
                        continue
            except EOFError:
                break
        f.close()

    def rename_file():
        old_name = r"temp_del.dat"
        new_name = f"{name_rec}"
        os.rename(old_name, new_name)
        

    def Delete_original_file():
        original_file_path = os.path.dirname(os.path.abspath(f"{name_rec}"))
        remove_file_name = original_file_path + "/" +f"{name_rec}"
        os.remove(remove_file_name)

    del_rec()
    Delete_original_file()
    rename_file()

#Insert a record between existing records
def insert_record():
    name_rec = input("Enter the name of the record file: ")
    def insert_rec():
        roll_insert = int(input("Enter the Roll No. of the record after which you want to insert a new record: "))
        
        f = open (f"{name_rec}","rb")
        while True:
            try:
                print("Existing Data:")
                rec = pickle.load(f)
                print ("Roll No.: ", rec['Roll No.'])
                print ("Name: ", rec["Name"])
                print ("Marks: ", rec["Marks"])
                temp_data = {"Roll No.": rec['Roll No.'], "Name": rec["Name"], "Marks": rec["Marks"]}
                print(" ")
                
                with open("temp.dat", 'ab') as temp:    
                    if rec["Roll No."] != roll_insert:
                        pickle.dump(temp_data, temp)
                    elif rec["Roll No."] == roll_insert:
                        pickle.dump(temp_data, temp)                            
                        print("Enter the details of the record that you want to insert.")
                        insert_name = input("Enter the Name: ")
                        insert_roll = int(input("Enter the Roll No.: "))
                        insert_marks = int(input("Enter the Marks: "))
                        insert_rec = {"Roll No.": insert_roll, "Name": insert_name, "Marks": insert_marks}
                        print(" ")
                        pickle.dump(insert_rec, temp)
                        temp.flush()
                        continue
            except EOFError:
                break
        f.close()

    def rename_file():
        old_name = r"temp.dat"
        new_name = f"{name_rec}"
        os.rename(old_name, new_name)
        
    def Delete_original_file():
        original_file_path = os.path.dirname(os.path.abspath(f"{name_rec}"))
        remove_file_name = original_file_path + "/" +f"{name_rec}"
        os.remove(remove_file_name)

    insert_rec()
    Delete_original_file()
    rename_file()
    
#Permanently Delete an entire binary file 
def delete_binary_file():
    name_rec = input("Enter the name of the record file that you want to Permanently Delete: ")
    print("***")
    print("Warning: THIS ACTIONS IS GOING TO PERMANENTLY DELETE THE BINARY FILE")
    print("***")
    CHOICE = input("Do you want to procede? (yes/no): ")
    if CHOICE.upper()=="YES":
        original_file_path = os.path.dirname(os.path.abspath(f"{name_rec}"))
        remove_file_name = original_file_path + "/" +f"{name_rec}"
        os.remove(remove_file_name)
        print("File Deleted from directory")
    else:
        pass
    
#What does the user want to do?
def purpose():
    print("1. Create a binary record/Append new records to a binary file")
    print("2. Modify an Entry")
    print("3. Delete an Entry")
    print("4. Search for an Entry")
    print("5. Read a Binary Record")
    print("6. Insert a record between existing records")
    print("7. Permanently delete an entire binary file")
    purpose = int(input("What do you want to do? (Enter the number corresponding to the action available): "))
    if purpose == 1:
        Create_rec()
    if purpose == 2:
        rollno_modify = int(input("Enter the Roll No. of the record that you want to modify: "))
        marks_modify = int(input("Enter new marks: "))
        Modify_Entry(rollno_modify, marks_modify)
    if purpose == 3:
        Delete_Entry()
    if purpose == 4:
        rollno_search = int(input("Enter the Roll No. of the record you are looking for: "))
        Search(rollno_search)
    if purpose == 5:
        Read_rec()
    if purpose == 6:
        insert_record()
    if purpose == 7:
        delete_binary_file()

purpose()   