#include<stdio.h>
int check(int,int);
int main(){
	int argv1,argv2;
	scanf("%d",argv1);
	scanf("%d",argv2);	
	check(argv1,argv2);
	printf("%d",argv1);
	return 0;
}
