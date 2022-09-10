#Working with binary files

import pickle

#Create a binary record/ Append more data to an existing binary record file
def Create_rec():
    name_rec = input("Enter the name of the binary record file: ")
    f = open(f"{name_rec}", "ab")
    n = int(input("How many record do you want to add? "))
    for N in range(0, n):
        rollno = int(input("Enter the Roll No.: "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        rec = {"Roll No.": rollno, "Name": name, "Marks": marks}
        pickle.dump(rec, f)
    f.close()

#Read a binary record file
def read_rec():
    name_rec = input("Enter the name of the binary record file: ")
    f = open(f"{name_rec}", "rb")
    while True:
        try:
            rec = pickle.load(f)
            print("Roll No.:", rec["Roll No."])
            print("Name:", rec["Name"])
            print("Marks:", rec["Marks"])
            print(" ")
        except EOFError: 
            break
    f.close()

#Search for a record in a binary file
def Search():
    name_rec = input("Enter the name of the binary record file: ")
    f = open(f"{name_rec}", "rb")
    search = int(input("Enter the Roll No. of the record that you are searching for: "))
    found = 1
    while True:
        try:
            rec = pickle.load(f)
            if rec["Roll No."] == search:
                found = 0
                print("*RECORD FOUND*")
                print(" ")
                print("Roll No.:", rec["Roll No."])
                print("Name:", rec["Name"])
                print("Marks:", rec["Marks"])
                print(" ")
        except EOFError: 
            break
    if found == 1:
        print("*RECORD NOT FOUND*")
    f.close()
                
#Modify an existing record in a binary file
def Modify():
    name_rec = input("Enter the name of the binary record file: ")

    rollno_rec_modify = int(input("Enter the Roll No. of the record that you want to modify: "))
  
    print("1. Modify Name")
    print("2. Modify Roll No.")
    print("3. Modify Marks")
    print("If you want to modify multiple details, enter the required combination of corresponding numbers.")
    modify = int(input("What do you want to modify? ((1)Name, (2)Roll No., or (3)Marks)"))

    if modify == 1:
        new_name = input("Enter the new name: ")
    elif modify == 2:
        new_rollno = int(input("Enter the new Roll No.: "))
    elif modify == 3:
        new_mark = int(input("Enter the new marks: "))

    elif modify == 12 or modify == 21:
        new_name = input("Enter the new name: ")
        new_rollno = int(input("Enter the new Roll No.: "))
    elif modify == 13 or modify == 31:
        new_name = input("Enter the new name: ")
        new_mark = int(input("Enter the new marks: "))
    elif modify == 23 or modify == 32:
        new_rollno = int(input("Enter the new Roll No.: "))
        new_mark = int(input("Enter the new marks: "))
    elif modify == 123 or modify == 132 or modify == 321 or modify == 312 or modify == 213 or modify == 231:
        new_name = input("Enter the new name: ")
        new_rollno = int(input("Enter the new Roll No.: "))
        new_mark = int(input("Enter the new marks: "))
    else:
        print("*INVALID COMMAND*")

        
    f = open(f"{name_rec}", "rb")
    record = []
    while True:
        try:
            rec = pickle.load(f)
            record.append(rec)
        except EOFError:
            break
    f.close()

    for x in range(0, len(record)):
        if record[x]["Roll No."] == rollno_rec_modify:

            if modify == 1:
                record[x]["Name"]  = new_name
            elif modify == 2:
                record[x]["Roll No."]  = new_rollno
            elif modify == 3:
                record[x]["Marks"]  = new_mark
            
            elif modify == 12 or modify == 21:
                record[x]["Name"]  = new_name
                record[x]["Roll No."]  = new_rollno
            elif modify == 13 or modify == 31:
                record[x]["Name"]  = new_name
                record[x]["Marks"]  = new_mark
            elif modify == 23 or modify == 32:
                record[x]["Roll No."]  = new_rollno
                record[x]["Marks"]  = new_mark
            elif modify == 123 or modify == 132 or modify == 321 or modify == 312 or modify == 213 or modify == 231:
                record[x]["Name"]  = new_name
                record[x]["Roll No."]  = new_rollno
                record[x]["Marks"]  = new_mark

    f = open(f"{name_rec}", "wb")
    for y in record:
        pickle.dump(y, f)

    f.close()

#Delete an existing record from a binary file
def Delete():
    name_rec = input("Enter the name of the binary record file: ")
    found = False
    rollno_rec_delete = int(input("Enter the Roll No. of the record that you want to delete: "))
    f = open(f"{name_rec}", "rb")
    record = []
    while True:
        try:
            rec = pickle.load(f)
            record.append(rec)
        except EOFError:
            break
    f.close()
    f = open(f"{name_rec}", "wb")
    for x in record:
        if x["Roll No."] == rollno_rec_delete:
            print("*RECORD DELETED*")
            found = True
            continue
        pickle.dump(x, f)
        if found == False:
            print("*RECORD NOT FOUND*")
            break

    f.close()

#Insert a record between existing records
def Insert():
    name_rec = input("Enter the name of the binary record file: ")

    rollno_insert_rec = int(input("Enter the Roll No. of the record after which you want to insert a new record: "))

    f = open(f"{name_rec}", "rb")

    record = []

    while True:
        try: 
            rec = pickle.load(f)
            record.append(rec)
        except EOFError:
            break
    f.close()
    print(" ")
    print ("Enter the Details of the new record.")
    print(" ")
    rollno = int(input("Enter the Roll No.: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    insert_rec = {"Roll No.": rollno, "Name": name, "Marks": marks}
    print(" ")
    for x in range(len(record)):
        if record[x]["Roll No."] == rollno_insert_rec:
            record.insert((x+1), insert_rec)
            break
    f = open(f"{name_rec}", "wb")
    for y in record:
        pickle.dump(y, f)
    f.close()

#Purpose
def Purpose():
    print("1. Create a binary record/ Append more data to an existing binary record file")
    print("2. Read a binary record file")
    print("3. Search for a record in a binary file")
    print("4. Modify an existing record in a binary file")
    print("5. Delete an existing record from a binary file")
    print("6. Insert a record between existing records")

    purpose = int(input("What do you want to do? "))
    if purpose == 1:
        Create_rec()
    elif purpose == 2:
        read_rec()
    elif purpose == 3:
        Search()
    elif purpose == 4:
        Modify()
        print("*RECORD MODIFIED*")
    elif purpose == 5:
        Delete()  
    elif purpose == 6:
        Insert()  
        print("*RECORD INSERTED*")
    else:
        pass

Purpose()