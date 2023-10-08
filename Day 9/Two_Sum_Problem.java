import java.util.*;
class Two_Sum_Problem{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int i=0,sum=0;
        System.out.println("Ener the size:");
        int size=sc.nextInt();
        System.out.println("Enter the elements:");
        int nums[]=new int[size];
        for(i=0;i<size;i++){
            nums[i]=sc.nextInt();
        }
        Arrays.sort(nums);
        System.out.println("Enter target:");
        int target=sc.nextInt();
        int start=0,end=nums.length-1;
        for(i=0;i<nums.length;i++){
            
            sum=nums[start]+nums[end];
            if(sum>target){
                end--;
            }
            else if(sum<target){
                start++;
            }
            else if(sum==target){
                System.out.printf("%d,%d",start+1,end+1);
                break;
            }
            
        }
    }
}