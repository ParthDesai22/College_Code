import java.text.ParseException;
import java.util.Scanner;
class FCFS{
static void WaitingTime(int processes[], int n, int bt[] ,int wt[]){
wt[0] = 0;
for (int i=1;i<n;i++){
wt[i] = bt[i-1] + wt[i-1];
}
}
static void TurnAroundTime(int processes[], int n, int bt[], int wt[], int tat[]){
for (int i=0;i<n;i++){
tat[i] = bt[i] + wt[i];
}
}
static void AverageTime(int processes[], int n, int bt[]){
int wt[] = new int[n] , tat[] = new int[n];
int total_wt=0,total_tat=0;
WaitingTime(processes,n,bt,wt);
TurnAroundTime(processes,n,bt,wt,tat);
System.out.printf("Processes Burst time Waiting"+" time Turn around time\n");
for (int i=0;i<n;i++){
total_wt = total_wt + wt[i];
total_tat = total_tat + tat[i];
System.out.printf("  %d  ",(i+1));
System.out.printf("          %d ",bt[i]);
System.out.printf("          %d", wt[i]);
System.out.printf("       %d\n",tat[i]);
}
float s = (float)total_wt / (float) n;
int t= total_tat / n;
System.out.printf("Average Waiting  Time Is = %f",s);
System.out.printf("\n");
System.out.printf("Average Turn Around Time Is = %d",t);
}
public static void main(String[] args) throws ParseException{
Scanner sc = new Scanner(System.in);
System.out.print("Enter the number of processes: ");      
int n = sc.nextInt();
int processes[] =new int[20];
int burst_time[] = new int[20];
System.out.println("\nEnter the Process Name And Burst Time For Each Process.");       
for (int i = 0; i < n; i++) {
System.out.print("\nFor Process " + (i + 1));
System.out.print("Process Name : ");
processes[i] = sc.nextInt();
System.out.print("Process Burst Time : ");
burst_time[i] = sc.nextInt(); 
} 
AverageTime(processes,n,burst_time);
}
}