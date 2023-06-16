#student database
print("\t\t\tstudent database")
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
school=client["studentDatabase123"]
db=school["StudentDetails"]
print("student database menu")
print("\t=> 0 is menu")
print("\t=> 1 is insert student data")
print("\t=> 2 is read the existing data")
print("\t=> 3 is update the existing data")
print("\t=> 4 is delete the exisitng file")
print("\t=> 5 is exit")
def insert_fun():
    name1=input("enter the name")
    age1=int(input("enther the age"))
    mark1=int(input("enter the mark"))
    details={"name":name1,"age":age1,"mark":mark1}
    result=db.insert_one(details)
    print("insert student data")
def read_fun():
    name1=input("enter the name")
    details={"name":name1}
    result=db.find_one(details)
    print(result)
        
def update_fun():
    name1=input("search the name")
    old_value={"name":name1}
    print("press 1 update the name")
    print("press 2 update the age")
    print("press 3 update the mark")
    
    def update_name():
        name2=input("update the name")
        new_value={"$set":{"name":name2}}
        db.update_one(old_value,new_value)
        print("name update complete")
    def update_age():
        age=int(input("update the age"))
        new_value={"$set":{"age":age}}
        db.update_one(old_value,new_value)
        print("age update complete")
    def update_mark():
        mark=int(input("update the mark"))
        new_value={"$set":{"mark":mark}}
        db.update_one(old_value,new_value)
        print("mark update complete")
    while True:
        selectno=int(input("choose no in update data"))
        if selectno==1:
            update_name()   
        if selectno==2:
            update_age()
        if selectno==3:
            update_mark()
            break                  
def delete_fun():
    name1=input("enter the name")
    details={"name":name1}
    db.delete_one(details)
    print("delete existing data")
while True:
    select_no=int(input("select the menu no"))
    if select_no==0:
        print("NO 1 is insert student data")
        print("NO 2 is read the existing data")
        print("NO 3 is update the existing data")
        print("NO 4 is delete the exisitng file")
        print("NO 5 is exit")  
    if select_no==1:
        insert_fun()
    if select_no==2:
        read_fun()
    if select_no==3:
        update_fun()
    if select_no==4:
        delete_fun()
    if select_no==5:
        print("exit")
        break
    


        







