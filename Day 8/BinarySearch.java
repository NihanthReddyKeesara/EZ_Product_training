import java.util.*;

class BinarySearch{
    
    public static void binary_Search(int nums[],int low,int high,int search){
        int mid;
        
        if(high>=low){
            
            mid=(low+high)/2;
        
            if(nums[mid]==search){
                System.out.println("Element Found");
            }
            else if(search<nums[mid]){
                binary_Search(nums,low,mid-1,search);
            }
            else if(search>nums[mid]){
                binary_Search(nums,mid+1,high,search);
            }
           
        }
        
        
    }
    
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
        
        int low=0,high=size-1;
        
        binary_Search(nums,low,high,search);
        
    }
}