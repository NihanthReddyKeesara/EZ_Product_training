import java.util.*;
class Otp{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int i;
		System.out.print("Enter size:");
		int size=sc.nextInt();
		System.out.print("Enter the numbers:");
		int nums[]=new int[size];
		String dnums="";
		for(i=0;i<size;i++){
			System.out.printf("nums[%d]=",i);
			nums[i]=sc.nextInt();
		}
		for(i=0;i<size;i++){
			if(i%2!=0){
				dnums=dnums+nums[i];
			}
		}
		int DNums[]=new int[dnums.length()];
		for(i=0;i<dnums.length();i++){
			//DNums[i]=Integer.parseInt(dnums.charAt(i));
			/*The issue here is that you're trying to convert a character 
			to an integer using Integer.parseInt(), which is meant for 
			converting strings to integers. To fix this, 
			you should convert the character to a string first, 
			and then parse it to an integer.*/
			DNums[i] = Integer.parseInt(String.valueOf(dnums.charAt(i)));
		}
		
		for(i=0;i<DNums.length;i++){
			System.out.print(DNums[i]+" ");
		}
		System.out.print("Squares: ");
		for(i=0;i<DNums.length;i++){
			System.out.print(DNums[i]*DNums[i]+",");
		}
		
		String s1="";
		for(i=0;i<DNums.length;i++){
			s1=s1+DNums[i]*DNums[i];
		}
		
		
		System.out.println("Enter the length for OTP:");
		int len=sc.nextInt();
		for(i=0;i<len;i++){
			System.out.print(s1.charAt(i));
		}
		
	}
	
}