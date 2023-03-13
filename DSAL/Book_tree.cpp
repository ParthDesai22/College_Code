#include<iostream>
using namespace std;
struct node
{
	char lable[10];
	int ch_cnt;
	struct node*child[10];
}*root;
class booktree
{
public:
	void create_tree();
	void display(node*root);
	booktree()
	{
		root=NULL;
	}
};
void booktree::create_tree()
{
	int tbr,tch,i,j,k;
	root=new node;
	cout<<"Enter Name Of The Book"<<endl;
	cin>>root->lable;
	cout<<"Enter Number of Chapter In Book"<<endl;
	cin>>tch;
	root->ch_cnt=tch;
	for(i=0;i<tch;i++)
	{
		root->child[i]=new node;
		cout<<"Enter Chapter Name"<<endl;
		cin>>root->child[i]->lable;
		cout<<"Enter Number Of Sections"<<endl;
		cin>>root->child[i]->ch_cnt;
		for(j=0;j<root->child[i]->ch_cnt;j++)
		{
			root->child[i]->child[j]=new node;
			cout<<"Enter The Name Of Subsection "<<j+1<<endl;
			cin>>root->child[i]->child[j]->lable;
		}
	}
}
void booktree::display(node*root)
{
	int i,j,k,tch;
	if(root!=NULL)
	{
		cout<<"\nBook Tree Hierarchy";
		tch=root->ch_cnt;
		for(i=0;i<tch;i++)
		{
			cout<<"Chapters:"<<endl;
			cout<<"\t"<<i+1<<"."<<root->child[i]->lable<<endl;
			cout<<"Sections:"<<endl;
			for(j=0;j<root->child[i]->ch_cnt;j++)
			{
				cout<<"\t"<<j+1<<"."<<root->child[i]->child[j]->lable<<endl;
			}
			cout<<endl;
		}
		
	}
}
int main()
{
	booktree bt;
	bt.create_tree();
	bt.display(root);
	return 0;
}