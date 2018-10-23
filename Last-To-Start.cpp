
#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

ifstream infile("act.txt");
vector<int> brr;


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



	return 0;
}
