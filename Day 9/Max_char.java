import java.util.*;
class Max_char
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int i;
		System.out.println("Enter string:");
		String s1=sc.nextLine();
		String ct="";
		for(i=0;i<s1.length();i++){
		    if(s1.charAt(i)=='@'||s1.charAt(i)=='#'){
		        ct=ct+s1.charAt(i);
		    }
		}
		String s2=s1.replace(ct,"");
		int ind=s1.indexOf(ct);
		String s3="";
		for(i=s2.length()-1;i>=0;i--){
		    s3=s3+s2.charAt(i);
		}
		StringBuilder s4=new StringBuilder(s3);
		s4.insert(ind,ct);
		System.out.println(s4);
	}
}
