#include<iostream>
using namespace std;
void completiontime (int n,int at[],int bt[],int q){
    int ct[n],rem[n],sam[n],t=0;
    for (int i=0;i<n;i++){ 
        rem[i]=bt[i];
        sam[i]=0;
    }
    while(a==true){
        bool a=true;
        for (int i=0;i<n;i++){
            if(rem[i]==0){ continue; }
            else{
                if(rem[i] > q){
                    t+= q;
                    ct[i]=t;
                    rem[i]-=q;
                }
                if(rem[i] < q){
                    t+=rem[i];
                    ct[i]=t;
                    rem[i]=0;
                }
    
            }
        
        }
        for(int i=0;i<n;i++){
            if(rem[i]==sam[i]){a=false;}
            else{a=true;}
        }

    }

}

void averagetime(int n,int at[],int bt[],int ct[]){
    int wt[n],int tat[n],tot_wt=0;,tot_tat=0,avg_wt,avg_tat;
    for(int i=0;i<n;i++){
        tat[i]=ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
        tot_wt+=wt[i];
        tot_tat+=tat[i];
    }
    avg_wt=tot_wt/n;
    avg_tat=tot_tat/n;
    cout<<"Pro"<<"AT"<<"BT"<<"CT"<<"WT"<<"TAT"<<endl
    for(int i=0;i<n;i++){
        cout<<i<<at[i]<<bt[i]<<ct[i]<<wt[i]<<tat[i]<<endl;
    }
}
int main{
    int n,q;
    int at[n],bt[n],wt[n],tat[n];
    cout<<"Enter Total Number Of Process";
    cin>>n;
    for(int i=0;i<n;i++){
        cout<<"For Process"<<i<<endl;
        cout<<"Arrival Time"<<endl;
        cin>>at[i];
        cout<<"Burst Time"<<endl;
        cin>>bt[i];
    }
    cout<<"Enter Quantum :";
    cin>>q;
    completiontime(n,at,bt,q);
    averagetime(n,at,bt,ct);
    return 0; 
}
