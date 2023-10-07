//counting sort

import java.util.Scanner;

class Count_Sort{
    
    public static void countSort(int nums[],int max){
        int i,count=0,ele,ele1,ind;
        //int maxi=max+1;
        //count array
        int count_Array[]=new int[max+1];
        for(i=0;i<nums.length;i++){
            ele=0;
            ele=nums[i];
            if(count_Array[ele]==0){
                count_Array[ele]=1;
            }
            else if(count_Array[ele]==1 || count_Array[ele]>1){
                count_Array[ele]=count_Array[ele]+1;
            }
            
        }
        
        /*System.out.println("Count Array:");
        
        for(i=0;i<max+1;i++){
            System.out.print(count_Array[i]+" ");
        }*/
       
        //updated array
        int updated_Array[]=new int[max+1];
        for(i=0;i<max+1;i++){
            if(i==0){
                updated_Array[i]=count_Array[i];
            }
            else if(i>0){
                updated_Array[i]=updated_Array[i-1]+count_Array[i];
            }
        }
        /*System.out.println("Updated Array:");
        for(i=0;i<max+1;i++){
            System.out.print(updated_Array[i]+" ");
        }*/
        
        //Resultant array
        int result_Array[]=new int[nums.length];
        for(i=nums.length-1;i>=0;i--){
            ele1=0;
            ele1=nums[i];
            updated_Array[ele1]=updated_Array[ele1]-1;
            ind=0;
            ind=updated_Array[ele1];
            result_Array[ind]=nums[i];
        }
        
        System.out.println("Resultant Array:");
        
        for(i=0;i<nums.length;i++){
            System.out.print(result_Array[i]+" ");
        }
        
        
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int i;
        System.out.println("Enter size:");
        int size=sc.nextInt();
        int nums[]=new int[size];
        System.out.println("Enter elements:");
        for(i=0;i<size;i++){
            System.out.printf("Nums[%d]=",i);
            nums[i]=sc.nextInt();
        }
        
        System.out.println("Given Array:");
        for(i=0;i<size;i++){
            System.out.print(nums[i]+" ");
            
        }
        System.out.println();
        int max=nums[0];
        for(i=0;i<size;i++){
            if(max<=nums[i]){
                max=nums[i];
            }
        }
        System.out.println("Max element is="+max);
        countSort(nums,max);
    }
}