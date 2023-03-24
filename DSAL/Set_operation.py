
class set_operate:
    def __init__(self):
        data=[]
        data1=[]
        data2=[]
        data3=[]
        data4=[]
        data5=[]

    def add_elem(self,data):
        print("Enter Number of Element You Want To Add In Set: ")
        n=int(input())
        for i in range(n):
            elem=input("Enter The Element: ")
            while(elem in data):
                print("Element Already Exist!!")
                elem=input()
            data.append(elem)    
                    
                
          
    def del_elem(self,data):
        delem=input("Enter The Element To Remove: ")
        data.remove(delem)
        
    def search_elem(self,data):
        key=input("Enter Element To Search: ")
        if(key in data):
            print("Element Is Present In SET ")
        else:
            print("Key Not Present In SET")
            
    def size_of_set(self,data):
        l=0
        iter1 = iter(data)
        for i in iter1:
            l+=1
        print("Size Of Set Is : ",l)
        
    def intersection(self,data1,data2,data3):
        for i in data1:
            if i in data2:
                data3.append(i)
                
        
    def union(self,data1,data2):
        data4=data1+data2
        for i in data1:
            if i in data2:
                data4.remove(i)
        return data4
        
    def difference(self,data1,data2,data5):
        for i in data1:
            if i not in data2:
                data5.append(i)
                
    def sub_set(self,data1,data2):
        if(all(i in data1 for i in data2)):
            print("It Is An Subset")
        else:
            print("it Is Not An Subset")
            
    def display(self,data):
        print("{",end="")
        for i in range(len(data)):
            j=i
            print(data[i],end="")
            if (j<len(data)-1):
                print(",",end="")
        print("}")        
        

a=True
s=set_operate()
data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
while(a==True):
    c=int(input("Enter Operation You Want To Carry On Set: \n 1.Add Element \n 2.Delete Element \n 3.Display Size Of Set \n 4.Intersection \n 5.Union \n 6.Difference \n 7.Sub-Set Checker \n 8.Search \n 9.End \n"))
    if(c==1):
        d=int(input("Enter Set In Which You Want To Add Element: \n 1.SET 1 \n 2.SET 2 \n"))
        if (d==1):
            s.add_elem(data1)
            s.display(data1)
        else:
            s.add_elem(data2)
            s.display(data2)
    if(c==2):
        d=int(input("Enter Set From Which You Want To Delete Element: \n 1.SET 1 \n 2.SET 2 \n"))
        if (d==1):
            s.display(data1)
            s.del_elem(data1)
            s.display(data1)
        else:
            s.display(data2)
            s.del_elem(data2)
            s.display(data2)
    if(c==3):
        d=int(input("Enter The Set You Want To Display The Size Of : \n 1.SET 1 \n 2.SET 2 \n"))
        if(d==1):
            s.size_of_set(data1)
        else:
            s.size_of_set(data2)
    if(c==4):
        s.intersection(data1,data2,data3)
        s.display(data3)
    if(c==5):
        data4 = s.union(data1,data2)
        s.display(data4)
    if(c==6):
        d=int(input("Enter Difference You Want To Perform: \n 1.SET 1 - SET 2 \n 2.SET 2 - SET 1 \n"))
        if(d==1):
            s.difference(data1,data2,data5)
            s.display(data5)
        else:
            s.difference(data2,data1,data5)
            s.display(data5)
    if(c==7):
        s.sub_set(data1,data2)
    if(c==8):
        d=int(input("Enter The Set You Want To Display The Size Of : \n 1.SET 1 \n 2.SET 2 \n"))
        if(d==1):
            s.search_elem(data1)
        else:
            s.search_elem(data2)
    if(c==9):
        a=False
        print("Thank You!!")
        break
        
        