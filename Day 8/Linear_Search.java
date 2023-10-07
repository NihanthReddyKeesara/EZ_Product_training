import java.util.*;

class Linear_Search{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int i;
        System.out.print("Enter the size:");
        int size=sc.nextInt();
        System.out.println("Enter the elements:");
        int nums[]=new int[size];
        for(i=0;i<size;i++){
            System.out.printf("nums[%d]=",i);
            nums[i]=sc.nextInt();
            
        }
        System.out.println("Enter search element:");
        int search=sc.nextInt();
        int c=0;
        for(i=0;i<size;i++){
            if(search==nums[i]){
               c=1;
                break;
            }
            
        }
        if(c==1){
            System.out.printf("%d Element found at index %d",search,i);
        }
        else{
            System.out.printf("%d Element not found in the array",search);
        }
    }
}