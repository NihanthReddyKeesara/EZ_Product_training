/*#include<stdio.h>
void main(){
	int r,c,i=0,j=0,temp=0;
	printf("Rows: ");
	scanf("%d",&r);
	printf("cols: ");
	scanf("%d",&c);
	int m1[r][c];
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			scanf("%d",&m1[i][j]);
		}
	}
	
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			printf("%d ",m1[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			if(i==1 && j==0){
				temp=m1[i][j+2];
				m1[i][j+2]=m1[j+2][i];
				m1[j+2][i]=temp;
			}
			else if(i!=j){
				temp=m1[i][j];
				m1[i][j]=m1[j][i];
				m1[j][i]=temp;
			}
			
		}
		
	}
	
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			printf("%d ",m1[i][j]);
		}
		printf("\n");
	}
}*/


/*#include<stdio.h>

int pows(int num,int base){
	if(num<=0 || base<=0){
		return 0;
	}
	

    
    while (num % base == 0) {
        num /= base;
    }
    
    return num == 1;
	
}

void main(){
	int n,i,count=0;
	printf("size: ");
	scanf("%d",&n);
	int a[n],b[10];
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	
	printf("Even numbers: ");
	for(i=0;i<n;i++){
		if(a[i]%2==0){
			printf("%d ",a[i]);
		}
	}
	printf("Powers of 2: ");
	for(i=0;i<n;i++){
		if(pows(a[i],2)==1){
			printf(a[i]);
		}
	}
	
}*/

/*#include<stdio.h>
void main(){
	int i,n=10;
	for(i=n;i>=1;i=i/2){
		printf("%d ",i);
	}
}*/

#include<stdio.h>
struct a{
	
	char y;
	double z;
	int x;
	
	
	
};

int main(){
	struct a yes;
	printf("%d",sizeof(yes));
	return 0;
}
