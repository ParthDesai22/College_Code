class set_operate:
    def __init__(self):
        data=set()
        data1=set()
        data2=set()

    def add_elem(self,data):
        print("Enter Number of Element You Want To Add In Set: ")
        n=int(input())
        for i in range(n):
            elem=input("Enter The Element: ")
            data.add(elem)
        print(data)    
        
    def del_elem(self,data):
        print(data)
        delem=input("Enter The Element To Remove: ")
        data.remove(delem)
        print(data)
        
    def size_of_set(self,data):
        print("Size Of Set Is : ",len(data))
        
    def intersection(self,data1,data2):
        print("Intersection Of Set Are: ",data1.intersection(data2))
        
    def union(self,data1,data2):
        print("Union Of Sets Are: ",data1.union(data2))
        
    def difference(self,data1,data2):
        print("Difference Of Set Are: ",data1.difference(data2))
        
    def sub_set(self,data1,data2):
        if(data1.issubset(data2)):
            print("SET 1 Is Subset Of SET 2")
        if (data2.issubset(data1)):
            print("SET 2 Is Subset Of SET 1")
        else:
            print("No Subset Are Present")
a=True
s=set_operate()
data1=set()
data2=set()
while(a==True):
    c=int(input("Enter Operation You Want To Carry On Set: \n 1.Add Element \n 2.Delete Element \n 3.Display Size Of Set \n 4.Intersection \n 5.Union \n 6.Difference \n 7.Sub-Set Checker \n 8.End \n"))
    if(c==1):
        d=int(input("Enter Set In Which You Want To Add Element: \n 1.SET 1 \n 2.SET 2 \n"))
        if (d==1):
            s.add_elem(data1)
        else:
            s.add_elem(data2)
    if(c==2):
        d=int(input("Enter Set From Which You Want To Delete Element: \n 1.SET 1 \n 2.SET 2 \n"))
        if (d==1):
            s.del_elem(data1)
        else:
            s.del_elem(data2)
    if(c==3):
        d=int(input("Enter The Set You Want To Display The Size Of : \n 1.SET 1 \n 2.SET 2 \n"))
        if(d==1):
            s.size_of_set(data1)
        else:
            s.size_of_set(data2)
    if(c==4):
        s.intersection(data1,data2)
    if(c==5):
        s.union(data1,data2)
    if(c==6):
        d=int(input("Enter Difference You Want To Perform: \n 1.SET 1 - SET 2 \n 2.SET 2 - SET 1 \n"))
        if(d==1):
            s.difference(data1,data2)
        else:
            s.difference(data2,data1)
    if(c==7):
        s.sub_set(data1,data2)
    if(c==8):
        a=False
        print("Thank You!!")
        break
        