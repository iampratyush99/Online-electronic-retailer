
import mysql.connector
import matplotlib.pyplot as plt
mysqlconn=mysql.connector.connect(host="localhost",user="root",password="root",database="onlineretailer")#Set connection
  
def show(dstring):
    print(dstring)


def drawGraph():
    Shopperid = []
    Ratingid = []
    query='SELECT * FROM reviews group by shopperid'
    mysqlCursor=mysqlconn.cursor()#Create cursor object
    mysqlCursor.execute(query)#Run query 
    rs=mysqlCursor.fetchall() #get all record
    irow=0
    for tRow in rs:
        Shopperid.append(tRow[1])
        Ratingid.append(tRow[2])
        irow=irow+1
    # close connection
    mysqlconn.close()
  
  
    plt.plot(Shopperid, Ratingid, color='red', marker='o')
    plt.title(' shopper Vs Rating', fontsize=14)
    plt.xlabel('Shopperid', fontsize=14)
    plt.ylabel('Rating', fontsize=14)
    plt.grid(True)
    plt.show()

def Vender_Menu():
    show('\n\n*****************************************************');
    show('\n 1.	show all product in a category');
    show('\n 2.	Add a new Product');
    show('\n 3.	Edit the status of Product');
    show('\n 4.	Remove a Product'); 
    show('\n 5.	Analysis'); 
    show('\n 6.	Quit');
    show('\n******************************************************');


def WelcomeScreen():
   
    show('\n SHOPPER  MENU');
    show('\n******************************************************');
   

def GetVenderProductList():
    VenderProductcategory=[]
    VenderProductVenderProductcategoryID=[]

    mysqlCursor=mysqlconn.cursor()#Create cursor object
    try:  
       query='SELECT * FROM products order by Productdescription'
       mysqlCursor.execute(query)#Run query 
       rs=mysqlCursor.fetchall() #get records
       irow=0
       #  Reading info rowwise and close the connection
    
       for tRow in rs:
            VenderProductcategory.append(tRow[2])
            VenderProductVenderProductcategoryID.append(tRow[0])
            show(str(irow+1) + ") " + tRow[2])
            irow=irow+1
    except:   
       print('Err :unable to get record')  
    mysqlconn.close()#close connection 
   
   


  

    VenderProductCategoryegory=int(input('\nEnter product anme  category :'))

    show('\n VenderProducts in the ' + VenderProductcategory[(VenderProductCategoryegory)-1])
    VenderProductcategoryesNoinfoStautusame=VenderProductcategory[int(VenderProductCategoryegory)-1]
    VenderProductcategoryID=VenderProductVenderProductcategoryID[int(VenderProductCategoryegory)-1]
    irow=0
    query='SELECT * FROM Products where Productcode  =' + str(VenderProductcategoryID)
    mysqlCursor.execute(query)#Run query 
    rs=mysqlCursor.fetchall() #get all record
    for tRow in rs:
        show(str(irow+1) + ") " + tRow[3])
        irow=irow+1
    # close connection
    mysqlconn.close()
    return VenderProductcategoryesNoinfoStautusame,VenderProductcategoryID

def getItemID():
    ItemID=''
  
    mysqlCursor=mysqlconn.cursor()#Create object
    try:  
       mysqlCursor.execute('SELECT max(Productid) FROM Products')#Run query 
       rs=mysqlCursor.fetchall() #get records
       for tRow in rs:    
           ItemID=tRow[0] 
    except:   
       print('Err :unable to get record')  
    mysqlconn.close()#close connection 
  
     
 
    return ItemID
  

def showChoises():
    VenderProductcategory=[]
    VenderProductVenderProductcategoryID=[]
   #**********-Fetch data********************
    # Create mysql connection object
    mysqlCursor=mysqlconn.cursor()#Create cursor object
    try:  
       irow=0
       mysqlCursor.execute('SELECT * FROM products order by Productdescription')#Run query 
       rs=mysqlCursor.fetchall() #get records
       for tRow in rs:    
          VenderProductcategory.append(tRow[2])
          VenderProductVenderProductcategoryID.append(tRow[0])
          show(str(irow+1) + ") " + tRow[2])
          irow=irow+1 
    except:   
       print('Err :unable to get record')  
    mysqlconn.close()#close connection 
  

  

    VenderProductCategoryegoryIndex=int(input('\nEnter the name of the Products you wish to select:'))

    show('\n VenderProducts in the ' + VenderProductcategory[(VenderProductCategoryegoryIndex)-1])

    VenderProductcategoryID=VenderProductVenderProductcategoryID[int(VenderProductCategoryegoryIndex)-1]
    irow=0
    try:  
   
        mysqlCursor.execute('SELECT * FROM Products where Productcode=' + str(VenderProductcategoryID))#Run query 
        rs=mysqlCursor.fetchall() #get records
        for tRow in rs:    
           show(str(irow+1) + ") " + tRow[3])
           irow=irow+1
    except:   
        print('Err :unable to get record')  
    mysqlconn.close()#close connection 

  



def updatedRecord(MysqlQuery,info):
       
    #mysqlconn=mysql.connector.connect(host="localhost",user="root",password="",infobase="mysqlpython")#established connection between your infobase  
    mysqlCursor=mysqlconn.cursor()#Create cursor object
    try:  
       mysqlCursor.execute(MysqlQuery)#Run query
       mysqlconn.commit() #Finalize change and make commit 
       print('Record updated successfully...')   
    except:   
       #Rollback  when error occure  
       mysqlconn.rollback()  
    show(info)
    mysqlconn.close()#close connection 


def InsertRecord(MysqlQuery,info):
    #mysqlconn=mysql.connector.connect(host="localhost",user="root",password="",infobase="mysqlpython")#established connection between your infobase  
    mysqlCursor=mysqlconn.cursor()#Create cursor object
    try:  
       mysqlCursor.execute(MysqlQuery)#Run query
       mysqlconn.commit() #Finalize change and make commit 
       print('Record add successfully...')   
    except:   
       #Rollback  when error occure  
       mysqlconn.rollback()  
    show(info)
    mysqlconn.close()#close connection 
    
def showListOfOnlineSeller():
    MYSQLOnlineSelleraccount=[]
    MYSQLOnlineSellerID=[]
   #**********-Fetch data********************
    # Create mysql connection object
 

    mysqlCursor = mysqlconn.cursor()
    irow=0
    show("OnlineSellerID 	OnlineSelleraccount 	OnlineSellername 	OnlineSelleraddressline1 	OnlineSelleraddressline2 	OnlineSelleraddressline3 	OnlineSellercounty 	OnlineSellerpostcode 	OnlineSelleremailaddress");
    query='SELECT * FROM seller order by Sellername'
    try:  
   
        mysqlCursor.execute(query)#Run query 
        rs=mysqlCursor.fetchall() #get records
        for tRow in rs:    
          MYSQLOnlineSelleraccount.append(tRow[1])
          MYSQLOnlineSellerID.append(tRow[0])
     
          show(str(irow+1) + ") " + str(tRow).replace(",","     " ))
          irow=irow+1
    except:   
        print('Err :unable to get record')  
    mysqlconn.close()#close connection 


    returnMYSQLOnlineSellerID,mysqlOnlineSelleraccount

def ModifyVenderProductinfoStautus():
    VenderProductcategory=[]
    VenderProductVenderProductcategoryID=[]
    VenderProductinfoStautus=[]
    ItemID=[]
    VenderProductcategoryesNoinfoStautusamed=[]
   #**********-Fetch data********************
    query='SELECT * FROM products order by Productdescription'
    i=0
    try:  
   
        mysqlCursor.execute(query)#Run query 
        rs=mysqlCursor.fetchall() #get records
        for tRow in rs:    
            VenderProductcategory.append(tRow[2])
            VenderProductVenderProductcategoryID.append(tRow[0])
            show(str(i+1) + ") " + tRow[2])
            i=i+1
    except:   
        print('Err :unable to get record')  
    mysqlconn.close()#close connection 
    

    VenderProductCategory=int(input('\nPlease enter category :'))

    show('\n VenderProducts in the ' + VenderProductcategory[(VenderProductCategory)-1])
    a=VenderProductcategory[int(VenderProductCategory)-1]
    VenderProductcategoryID=VenderProductVenderProductcategoryID[int(VenderProductCategory)-1]
    irow=0

    query='SELECT * FROM RProducts where RProduct_id=' + str(VenderProductcategoryID)
    i=0
    try:  
   
        mysqlCursor.execute(query)#Run query 
        rs=mysqlCursor.fetchall() #get records
        for tRow in rs:    
           show(str(irow+1) + ") " + tRow[3])
           s=str(tRow[3])
           VenderProductcategoryesNoinfoStautusamed=s
           VenderProductinfoStautus=tRow[5]
           ItemID=tRow[0]
           irow=irow+1
    except:   
        print('Err :unable to get record')  
    mysqlconn.close()#close connection 

   
    return VenderProductcategory,VenderProductcategoryID,VenderProductinfoStautus,VenderProductCategory,ItemID,VenderProductcategoryesNoinfoStautusamed


def VerifyOrders(ID):
    IsPresent=False
   #**********-Fetch data********************
    query='SELECT * FROM Products'
    i=0
    try:  
   
        mysqlCursor.execute(query)#Run query 
        rs=mysqlCursor.fetchall() #get records
        for tRow in rs:    
          if(ID==tRow[0]):
           IsPresent=True
    except:   
        print('Err :unable to get record')  
    mysqlconn.close()#close connection 

    return IsPresent

def Removeinfo(MysqlQuery):
    
    mysqlCursor=mysqlconn.cursor()#Create cursor object 
    try:   
       mysqlCursor.execute(MysqlQuery)#Execute SQL Query to detete a record   
       mysqlconn.commit() #Finalize change and make commit 
       print('Record deteted successfully...')  
    except:  
       #Rollback  when error occure  
       mysqlconn.rollback()  
    mysqlconn.close()#close connection
    
def getinfo():
     return input("Enter the number of the infoStautus you wish to change the VenderProduct to : ");
def getinfoStatus():
     infoStautus=''
     if(infoStautus=='Available'):
                show("\n 1. Temporarily Unavailable")
                show("\n 2. Discontinued")
                MYSQLStat=getinfo()
                if(mysqlStat=="1"):
                   MYSQLinfoStautus="Temporarily Unavailable"
                else: 
                   MYSQLinfoStautus="Discontinued"
     elif(infoStautus=='Temporarily Unavailable'):
        show("\n 1. Available")
        show("\n 2. Discontinued")
        MYSQLStat=getinfo()
        if(mysqlStat=="1"):
           MYSQLinfoStautus="Available"
        else: 
           MYSQLinfoStautus="Discontinued"
     elif(infoStautus=='Discontinued'):
        show("\n 1. Available")
        show("\n 2. Temporarily Unavailable")
        MYSQLStat= getinfo() 
        if(mysqlStat=="1"):
           MYSQLinfoStautus="Available"
        else: 
           MYSQLinfoStautus="Temporarily Unavailable"
     return infoStautus   
 
def Choise_Selection():
     while(True):
        Vender_Menu()
        show('\n Select the Choise :')
        mChoice=input()
        if(mChoice=='1'):
            VenderProductcategory=[]
            show('\nChoise 1 – show all VenderProducts in a VenderProductcategory')
            showChoises()
        elif(mChoice=='2'):
            show('\nChoise 2 – Add  new VenderProduct')
            VenderProductcategoryesNoinfoStautusame,VenderProductcategoryID=GetVenderProductList()
            VenderProductcode=input("Enter code of VenderProduct: ");
            VenderProductdescription=input("Enter description of VenderProduct: ");
            VenderProductmanufacturer=input("Enter  manufacturer of VenderProduct: ");
            VenderProductmodel=input("Enter  model of VenderProduct : ");
            ItemID=getItemID()
            ItemID=str(int(ItemID)+1)
           
            MysqlQuery="INSERT INTO Products VALUES (" + str(ItemID) + ",'" + str(VenderProductcategoryID) +"','" + VenderProductdescription +"','" + VenderProductmanufacturer + "','" + VenderProductmodel +"','Available')";
            InsertRecord(MysqlQuery,"Records inserted........")
            MYSQLOnlineSellerID,mysqlOnlineSelleraccount=showListOfOnlineSeller()
            userSellernumber=int(input('\nHow many seller do you want to add:'))

            show('\n OnlineSeller number is ' + str(mysqlOnlineSellerID[(userSellernumber)-1]))

            OnlineSellerID=str(mysqlOnlineSellerID[(userSellernumber)-1])
            VenderProductCost=input("Enter  VenderProduct Cost : ");
            MysqlQueryOnlineSeller="INSERT INTO ProductSeller VALUES (" + str(ItemID) + "," + str(OnlineSellerID) +"," + str(VenderProductCost) +")"
            InsertRecord(MysqlQueryOnlineSeller,"New VenderProduct added to the infobase")
        elif(mChoice=='3'):
            show('\nChoise 3 – Change the info Status of an existing VenderProduct')
            VenderProductcategoryesNoinfoStautusame,VenderProductcategoryID,VenderProductinfoStautus,VenderProductCategory,ItemID,VenderProductCategorYesNoinfoStautusame=ModifyVenderProductinfoStautus()

            VenderProductCategory=input("\nHow many VenderProduct wants to change: ")
            infoStautus=VenderProductinfoStautus #[int(VenderProductCategory)-1]
            cVenderProductID=ItemID#[int(VenderProductCategory)-1]
            VenderProductcategoryesNoinfoStautusame=VenderProductCategorYesNoinfoStautusame#[int(VenderProductCategory)-1]

            show('\n VenderProduct ' + str(VenderProductcategoryesNoinfoStautusame) + ' is  : ' + infoStautus )
            MYSQLinfoStautus= getinfoStatus()

            MysqlQueryUpdate="Update Products set Productstatus='" + str(mysqlinfoStautus) + "' where Productid=" + str(VenderProductcategoryID)  + " and RProduct_code=" + str(cVenderProductID);  
            info="Updated - VenderProduct " + str(VenderProductcategoryesNoinfoStautusame) + " is now " + str(mysqlinfoStautus);
            updatedRecord(MysqlQueryUpdate,info)


        elif(mChoice=='4'):
            show('\nChoise 4.	Delete Product ')
      
            VenderProductcategoryesNoinfoStautusame,VenderProductcategoryID,VenderProductinfoStautus,VenderProductCategory,ItemID,VenderProductCategorYesNoinfoStautusame=ModifyVenderProductinfoStautus()

            VenderProductCategory=input("\nEnter the proudctID: ")
       
            cVenderProductID=ItemID
            VenderProductcategoryesNoinfoStautusame=VenderProductCategorYesNoinfoStautusame

            YesNoinfoStautus=input('\nDo you really want to delete press  (Y or N)?   : ')
            if(YesNoinfoStautus.upper()=='Y'):
                if(VerifyOrders(cVenderProductID)):
                    show('Product can not delete')
                else:
                    Removeinfo("Delete from products where Productid=" + cVenderProductID)

        elif(mChoice=='5'):
            show('\nChoise 5.	Show graph ')
      
            drawGraph()

        else:
            show('\nChoise 6 – Exit')
            break

def  MAINPROG():
    Choise_Selection();

   


WelcomeScreen()
MAINPROG()


