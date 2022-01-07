import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=smartnxt;"
                      "Trusted_Connection=yes;")

from urllib.request import urlopen

import json 
  

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = urlopen(url)

data_json = json.loads(response.read())
#print (data_json)
jsonstr = json.dumps(data_json)
jsonstrnew = "'" + jsonstr + "'"
#alist = json.loads(jsonstr)
#print(jsonstrnew)
alist = json.loads(jsonstr)
mydata= alist["products"]
#print (alist["products"]['6834'])
#print (mydata)




data = json.loads(jsonstr)

for i in data['products']:
   # print(i)
    test=i;

   
   # print(test);
   # print (alist["products"][test])
    subdetails=alist["products"][test]
    price= subdetails["price"]
    #print (subdetails)
    subcategory=subdetails["subcategory"]
   # print (subcategory)
 
   # print (subdetails)
   # print (subdetails["title"])
    #print (subdetails["price"])
  #  print (subdetails["popularity"])
  
 
  
    popularity=subdetails["popularity"]
    
   # print ("////////////////////")
    titleInfo=subdetails["subcategory"];
   #valInfo = (test,subcategory,subdetails['price'],subdetails['popularity'] );

    myquery="INSERT INTO smartnxtProductDetails ( productcategory,title, price,popularity) VALUES   ('{t}','{s}',{r},{p})".format(t=test, s=subcategory,r=price,p=popularity)
      
  

   # myquery = "INSERT INTO smartnxtProductDetails ( productcategory,title, price,popularity) VALUES (%s, %s,%s, %s)"
    valInfo = (test,subcategory,subdetails['price'],subdetails['popularity'] );
    
     
    cursor = cnxn.cursor()
    
    cursor.execute(myquery)

    cnxn.commit()
    #cnxn.close()  
    
   
 
         
       
        