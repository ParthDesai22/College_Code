import java.util.*;

class FCFS{
    public static void main(String []args){
    int sum;
    int tat;
    int [] Process={1,2,3,4,5};
    int [] Arrival_Time={0,1,2,5,7};
    int [] Brust_Time={4,7,2,6,4};
    int [][]F;

    for (int i =0;i<5;i++){
        for (int j=0;j<5;j++){
            F[i][j]=0;
        }
        
    }    

    for(int i =0;i<5;i++){
        F[i][0]=(Process[i]);
        F[i][1]=(Arrival_Time[i]);
        F[i][2]=(Brust_Time[i]);
    }

    for (int i = 0;i<Brust_Time.length;i++){
        sum += Brust_Time[i];
         F[i][3] = sum; 
      }

    for(int i =0;i<5;i++){
        tat=F[i][3]-F[i][1];
        F[i][4]=(tat);
    }  
    

    for (int i =0;i<5;i++){
        System.out.print("\n");
        for (int j=0;j<5;j++){
            System.out.print(F[i][j] + "\t");
        }

    }
    }
}   }
}