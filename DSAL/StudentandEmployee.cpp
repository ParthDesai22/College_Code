#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
class tel
 {

 public:
 int rollNo,roll1;
 char name[10];
 char div;
 char address[20];
 void accept()
 {
  cout<<"\n\tEnter Roll Number : ";
  cin>>rollNo;
  cout<<"\n\tEnter the Name : ";
  cin>>name;
  cout<<"\n\tEnter the Division:";
  cin>>div;
  cout<<"\n\tEnter the Address:";
  cin>>address;
 }
        void accept2()
        {
               cout<<"\n\tEnter the Roll No. to modify : ";
               cin>>rollNo;
        }
        void accept3()
        {
              cout<<"\n\tEnter the name to modify : ";
              cin>>name;
        }
        int getRollNo()
        {
         return rollNo;
        }
  void show()
  {

  cout<<"\n\t"<<rollNo<<"\t\t"<<name<<"\t\t"<<div<<"\t\t"<<address;
  }
};
int main()
{
 int ch,ch1,rec; 
 bool w=true;
 char name[20],name2[20];
 tel t1;
 fstream g,f;
 do
 {
  cout<<"\n>>>>>>>>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<<<<<";
  cout<<"\n1.Insert and overwrite\n2.Show\n3.Search\n4.Delete a Student Record\n5.Exit\n\tEnter the Choice\t:";
  cin>>ch;
  switch(ch)
  {
  case 1:
   f.open("StuRecord.txt",ios::out);
   x:t1.accept();
   f.write((char*) &t1,(sizeof(t1)));
   cout<<"\nDo you want to enter more records?\n1.Yes\n2.No";
   cin>>ch1;
    if(ch1==1)
     goto x;
    else
    {
     f.close();
     break;
    }
  case 2:
   f.open("StuRecord.txt",ios::in);
   f.read((char*) &t1,(sizeof(t1)));
   //cout<<"\n\tRoll No.\t\tName \t\t Division \t\t Address";
   while(f)
   {
    t1.show();
    f.read((char*) &t1,(sizeof(t1)));
   }
   f.close();
   break;
  case 3:
   cout<<"\nEnter the roll number you want to find";
   cin>>rec;
   f.open("StuRecord.txt",ios::in);
   while(f.read((char*)&t1,(sizeof(t1))))
   {
    if(rec==t1.rollNo)
    {
     cout<<"\nRecord found";
     f.close();
     break;
    }
    else{
        cout<<"\nRecord Not Found";
        f.close();
        break;
    }
    }
   break;
  case 4:
      int roll;
      cout<<"Please Enter the Roll No. of Student Whose Info You Want to Delete: ";
     cin>>roll;
     f.open("StuRecord.txt",ios::in);
     g.open("temp.txt",ios::out);
     f.read((char *)&t1,sizeof(t1));
     while(!f.eof())
     {
        if (t1.getRollNo() != roll)
           g.write((char *)&t1,sizeof(t1));
         f.read((char *)&t1,sizeof(t1));
     }
    cout << "The record with the roll no. " << roll << " has been deleted " << endl;
     f.close();
     g.close();
     remove("StuRecord.txt");
     rename("temp.txt","StuRecord.txt");
      break;
    case 5:
       cout<<"\n\tThank you";
       w=false;
       break;
        }
  }while(w==true);
}