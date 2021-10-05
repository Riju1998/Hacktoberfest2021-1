#include<stdio.h>
#include<conio.h>
void main()
{
int i,a,b,c;
clrscr();
printf("enter the three given numbers :");
scanf("%d%d%d",&a,&b,&c);
for(i=c;i>=1;i--)
{
if(a%i==0&&b%i==0&&c%i==0)
break;
}
printf("the g.c.d is %d",i);
getch();
}