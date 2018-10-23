
#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

ifstream infile("act.txt");
vector<int> brr;

void lastToStart(int n)
{
    int k = 0;
   for( k = 0 ; k < n*3 ; k++)
   {
        if(k%3==0)
        {
            cout<<brr[k];

        }else{
        continue;}

   }
}

int main()
{



    if(!infile)
    {
        cout<< "File does not exist" <<endl;
    }

    ifstream file("act.txt");

    int a;
    while (file >> a)
    {
        brr.push_back(a);

    }


    int n =  brr[0];
	brr.erase(brr.begin());

    lastToStart(n);

	return 0;
}
