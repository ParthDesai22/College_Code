//burst time problem else good
import java.util.*;

public class SJF{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		System.out.println("\nEnter number of process:");
		int n=sc.nextInt();
		int pid[]=new int [n];
		int at[]=new int[n];
		int bt[]=new int[n];
		int ct[]=new int[n];
		int ta[]=new int[n];
		int wt[]=new int[n];
		int flag[]=new int[n];
		int rbt[]=new int[n];
		
		int st=0,total=0;
		float avgwt=0,avgta=0;
		
		for(int i=0;i<n;i++){
			pid[i]=i+1;
			System.out.println("\nEnter process:"+(i+1)+"Arrival time:");
			at[i]=sc.nextInt();
			System.out.println("\nEnter process:"+(i+1)+"Burst time:");
			bt[i]=sc.nextInt();
			rbt[i]=bt[i];
			flag[i]=0;
		}
		while(true){
			int min=99,temp=n;
			if(total==n){
				break;
			}
			for(int i=0;i<n;i++){
				if((at[i]<=st)&&(flag[i]==0)&&(bt[i]<min)){
					min=bt[i];
					temp=i;
				}
			}
			if(temp==n){
				st++;
			}
			else{
				bt[temp]--;
				st++;
				if(bt[temp]==0){
					ct[temp]=st;
					flag[temp]=1;
					total++;
				}
			}
		}
		for(int i=0;i<n;i++){
			ta[i]=ct[i]-at[i];
			wt[i]=ta[i]-rbt[i];
			avgwt+=wt[i];
			avgta+=ta[i];
		}
		System.out.println("\nPID\t\tArrivalT\t\tBurstT\t\tCompletionT\t\tTurnAT\t\tWaitingT");
		for(int i=0;i<n;i++){
			System.out.println(pid[i]+"\t\t"+at[i]+"\t\t"+bt[i]+"\t\t"+ct[i]+"\t\t"+ta[i]+"\t\t"+wt[i]);
		}
		System.out.println("\nAverage Waiting time is:"+(avgwt/n));
		System.out.println("\nAverage Turn around time is:"+(avgta/n));
		sc.close();
	}
}
