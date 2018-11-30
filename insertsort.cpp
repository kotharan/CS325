
#include <iostream>
#include <vector>
#include <fstream>

// Ref:: https://www.geeksforgeeks.org/insertion-sort/

using namespace std;
vector<int> brr;

ifstream infile("data.txt");

void insertSort(vector<int> &arr, int n)
{
    int z, j;
    for (int i = 1; i < n; i++)
    {
        z = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > z)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = z;
    }
}

// For printing the final array
void printFinal(vector<int> &arr, int n)
{
    ofstream myfile;
    myfile.open("insert.out");
    for (int i = 0; i < n; i++)
    {
        myfile << arr[i] << " ";
    }
    myfile.close();
}

int main()
{

    if (!infile)
    {
        cout << "File does not exist" << endl;
    }

    ifstream file("data.txt");

    int a;
    while (file >> a)
    {
        brr.push_back(a);
    }

    int n = brr[0];
    brr.erase(brr.begin());

    insertSort(brr, n);
    printFinal(brr, n);

    return 0;
}
