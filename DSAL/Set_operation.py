class set_operate:
    def __init__(self):
        self.data1=set()
        self.data2=set()
        
    def se1(self):
        print("Enter Number of Element You Want To Add In Set: ")
        n=int(input())
        for i in range(n):
            elem=input("Enter The Elment: ")
            self.data1.add(elem)
            
    def add_elem(self):
        aelem=input("Enter Element To Add in Set")
        self.data1.add(aelem)
        print(self.data1)
        
    def del_elem(self):
        print(self.data1)
        delem=input("Enter The Element To Remove: ")
        self.data1.remove(delem)
        print(self.data1)
        
    def size_of_set(self):
        print("Size Of Set Is : ",len(self.data1))
        
    def se2(self):
        m=int(input("Enter The Number Of Element To Store In Second Set"))
        for i in range(m):
            elem2=input("Enter The Element To Store: ")
            self.data2.add(elem2)
        print(self.data2)  
        
    def intersection(self):
        print("Intersection Of Set Are: ",self.data1.intersection(self.data2))
        
    def union(self):
        print("Union Of Sets Are: ",self.data1.union(self.data2))
        
    def difference(self):
        print("Difference Of Set Are: ",self.data1.difference(self.data2))
        
    def sub_set(self):
        if(self.data1.issubset(self.data2)):
            print("SET 2 Is Subset Of SET 1")
        if (self.data2.issubset(self.data1)):
            print("SET1 Is Subset Of SET 2")
        else:
            print("No Subset Are Present")
            
s=set_operate()
s.se1()
s.se2()
s.add_elem()
s.del_elem()
s.size_of_set()
s.intersection()
s.union()
s.difference()
s.sub_set()