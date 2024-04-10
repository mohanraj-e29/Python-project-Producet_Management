from pymysql import *


temp=0
def check(username,password):      
    con = connect(host="localhost",user="root",password="",database="product_management")
    q = "select username,password from Admin_info"
    c = con.cursor()
    c.execute(q)
    result = c.fetchall()
    global temp
    for i in result:
        c=0
        if username in i:
            c+=1
            if password in i:
                c+=1
                temp=c
            else:
                pass
        else:
            pass
    con.close()  
print("--------------------------------------------------------------PRODUCT MANAGEMENT ADMIN PORTAL---------------------------------------------------------------------------")
print()
print()
username=input("Enter the username=")
password=int(input("Enter your password="))
check(username,password)
print()
print()


if(temp==2):
    print("---------------------------------------------------------PRODUCT MANAGEMENT TABLES PORTAL-------------------------------------------------------------------------------")
    chs = int(input("1.Personal Information Table\n2.customer Information Table\nselect any 1 to perform operations:"))
    print()
    print()
    print()
    #product info table
    print()
    if(chs==1):
        def add():
            try:
                productid = int(input("Enter the ProductID :"))
                productcode = int(input("Enter the Product Code :"))
                Productname = input("Enter the Product Name :")
                Productbrand = input("Enter the Product Brand:")
                Productprice = int(input("Enter the ProductPrice  :"))
                Productcolour = input("Enter the Product Colour :")
                Productdescription = input("Enter the Product Description :")
                Productspecification = input("Enter the Product Specification :")
                warranty= input("Enter the Warranty :")
                countryoforigin= input("Enter the Country of origin :")
                manufaturedetails= input("Enter the Manufacture Details :")
                packerdetails= input("Enter the Packer Details :")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "insert into product_info values('{0}',{1},'{2}','{3}',{4},'{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(productid,productcode,Productname,Productbrand,Productprice,Productprice,Productcolour,Productdescription,Productspecification,warranty,countryoforigin,manufaturedetails,packerdetails)
                c = con.cursor()
                c.execute(q)
                con.commit()
                con.close()
                print("Data Saved....")
            except Exception as e:
                print(e)

        def update():
            try:
                Productname = input("Enter the Product Name :")
                Productbrand = input("Enter the Product Brand:")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "update product_info set Productname ='{2}' where Productbrand ='{3}'".format(Productname,Productbrand)
                c = con.cursor()
                r=c.execute(q)
                con.commit()
                con.close()
                print("Data updated" if(r!=0) else "Invalid Name")
            except Exception as e:
                print(e)
                
        def delete():
            try:
                Productbrand = input("Enter the Product Brand:")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "delete from product_info where Productbrand ='{3}'".format(Productbrand)
                c = con.cursor()
                r=c.execute(q)
                con.commit()
                con.close()
                print("Data deleted" if(r!=0) else "Invalid Brand")
            except Exception as e:
                print(e)
                
        def find():
            try:
                Productname = input("Enter the Product Name :")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "select * from product_info where Productname='{2}'".format(Productname)
                c = con.cursor()
                c.execute(q)
                result = c.fetchall()
                print("Product_Id\tProduct_Code\tProduct_Name\tProduct_Branch\tProduct_Price\tProduct_Colour\tProduct_Description\tProduct_Specification\tWarranty\tCountry Of Origin\tManufacture Details\tPacker Details")
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                con.close()   
            except Exception as e:
                print(e)
                
        def printData():
            try:        
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "select * from product_info"
                c = con.cursor()
                c.execute(q)
                result = c.fetchall()
                print("Product_Id\tProduct_Code\tProduct_Name\tProduct_Branch\tProduct_Price\tProduct_Colour\tProduct_Description\tProduct_Specification\tWarranty\tCountry Of Origin\tManufacture Details\tPacker Details")
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                con.close()       
            except Exception as e:
                print(e)

        
        #choice for query
        chq = int(input("1.add\n2.update\n3.delete\n4.find\n5.print\nselect any 1:"))
        print()
        print("---------------------------------------------------------PERSONAL INFOMATION TABLE--------------------------------------------------------------------------------")
        if(chq==1):
            add()
        elif(chq==2):
            update()
        elif(chq==3):
            delete()
        elif(chq==4):
            find()
        elif(chq==5):
            printData()
        else:
            print("Invalid choice...")
        print()
        print()
    #else:
    #    print("Invalid Choice Of Number")   
        
    #customer table
    elif(chs==2):
        print("---------------------------------------------------------CUSTOMER INFOPRMATION PORTAL--------------------------------------------------------------------------------")
        print()
        print() 
        def adds():
            try:
                customerid = int(input("Enter the customerid :"))
                customercode = int(input("Enter the customercode :"))
                customerFname = input("Enter the customerFname :")
                customerLname = input("Enter the customerLname:")
                age = int(input("Enter the age  :"))
                emailId = input("Enter the emailId :")
                PhoneNumber = int(input("Enter the Product PhoneNumber :"))
                Address = input("Enter the Address :")
                Landmark= input("Enter the Landmark :")
                City= input("Enter the City :")
                country= input("Enter the country :")
                zipcode= int(input("Enter the zipcode :"))
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "insert into customer_infos values({0},{1},'{2}','{3}',{4},'{5}',{6},'{7}','{8}','{9}','{10}',{11})".format(customerid,customercode,customerFname,customerLname,age,emailId,PhoneNumber,Address,Landmark,City,country,zipcode)
                c = con.cursor()
                c.execute(q)
                con.commit()
                con.close()
                print("Data Saved....")
            except Exception as e:
                print(e)

        def updates():
            try:
                PhoneNumber = int(input("Enter the PhoneNumber :"))
                Address = input("Enter the Address :")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "update customer_infos set phoneNumber  ={6} where address  ='{7}'".format(PhoneNumber,Address)
                c = con.cursor()
                r=c.execute(q)
                con.commit()
                con.close()
                print("Data updated" if(r!=0) else "Invalid phonenumber")
            except Exception as e:
                print(e)
                
        def deletes():
            try:
                Landmark= input("Enter the Landmark :")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "delete from customer_infos where landmark ='{8}'".format(Landmark)
                c = con.cursor()
                r=c.execute(q)
                con.commit()
                con.close()
                print("Data deleted" if(r!=0) else "Invalid Landmark")
            except Exception as e:
                print(e)
                
        def finds():
            try:
                customerFname = input("Enter the customerFname :")
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "select * from customer_infos where customer_fname ='{2}'".format(customerFname)
                c = con.cursor()
                c.execute(q)
                result = c.fetchall()
                print("customerid\tcustomercode\tcustomerFname\tcustomerLname\tage\temailId\tPhoneNumber\tAddress\tLandmark\tCity\tcountry\tzipcode")
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                con.close()   
            except Exception as e:
                print(e)
                
        def printDatas():
            try:        
                con = connect(host="localhost",user="root",password="",database="product_management")
                q = "select * from customer_infos"
                c = con.cursor()
                c.execute(q)
                result = c.fetchall()
                print("customerid\tcustomercode\tcustomerFname\tcustomerLname\tage\temailId\tPhoneNumber\tAddress\tLandmark\tCity\tcountry\tzipcode")
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                con.close()       
            except Exception as e:
                print(e)
           
        print()
        print("---------------------------------------------------------CUSTOMER INFOPRMATION TABLE--------------------------------------------------------------------------------")
        #choice for query
        che = int(input("1.add\n2.update\n3.delete\n4.find\n5.print\nselect any 1:"))
        if(che==1):
            adds()
        elif(che==2):
            updates()
        elif(che==3):
            deletes()
        elif(che==4):
            finds()
        elif(che==5):
            printDatas()
        else:
            print("Invalid choice...")     
    else:
        print("Invalid Choice Of Number")
        
        
    
                    
else:
    print("Invalid Username Or Password")
    
   