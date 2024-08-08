#include <iostream>
int next_smaller_coin(int m)
{
    if(m==50)
    {
	        return 20;
	    }
    if(m==20)
    {
	        return 10;
	    }
    if(m==10)
    {
	        return 5;
	    }
	if(m == 5)
	{
       return 1;
	}
    else return -1;
}
int count_partitions(int total,int largest)
{
    if(total == 0)
    {
	    return 1;
    }
    if(total < 0|| largest == -1)
    {
	    return 0;
	}
	else
    {
	       int with_largest = count_partitions(total-largest,largest);
	       int without_largest = count_partitions(total,next_smaller_coin(largest));
	        return  with_largest+without_largest;
	}
}
int count(int total,int largest)
{
    return count_partitions(total,largest);
}
int main()
{
    int total,largest;
    std::cin>>total>>largest;
	int result = count(total,largest);
	std::cout<<result<<std::endl;
	return 0;
}
