#include <iostream>
int m = 0;
void print_proces(int start,int end)
{
	std::cout<<"把该柱子上最上面的一个从"<< start <<"移动到"<< end <<std::endl;
}
void move(int n,int start, int end)

{
	int spare = 0;
	m++;
	if (n==1)
	{
		print_proces(start,end);
	}
	else
	{
		spare = 6 - start -end;
		move(n-1,start,spare);
		print_proces(start,end);
		move(n-1,spare,end);
	}
}
int main()
{
	int n,start,end;
	std::cout<<"请输入盘子数目：";
	std::cin>>n;
	std::cout<<"请输入起始位置和终止位置：";
	std::cin>>start>>end;
	move(n,start,end);
	std::cout<<"共移动"<<m<<"次"<<std::endl;
}
