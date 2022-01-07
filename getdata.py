import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=smartnxt;"
                      "Trusted_Connection=yes;")
    
   
  
   
    #cursor.execute('SELECT * FROM smartnxtProductDetails')
    
cursor = cnxn.cursor()
cursor.execute('select title, price,popularity from [dbo].[smartnxtProductDetails] order by popularity desc')
 

for i in cursor:
    print('[title, price,popularity]') 
  
    print(i[0]) 
    print(i[1]) 
    print(i[2])  
    
  #  print(i[0],i[1],i[2]) 
    
    
   
  

    
 
       
        