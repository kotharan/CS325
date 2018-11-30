// C++ code to implement stooge sort
#include <iostream>
#include <vector>
#include <fstream>
#include <time.h>
#include <ctime>
#include <cstdlib>

using namespace std;

vector<int> arr;
int rand();
clock_t tStart = clock();
ifstream infile("data.txt");

void srand(int seed); // Seeding in time for randomizing

// Function to implement stooge sort
void stoogesort(vector<int> &arr, int first, int last)
{

    // If first element is smaller than last, swap them
    if (arr[first] > arr[last])
        swap(arr[first], arr[last]);

    // If there are more than 2 elements in the array
    if (last - first + 1 > 2)
    {
        int t = (last - first + 1) / 3;

        // Recursively sort first 2/3 elements
        stoogesort(arr, first, last - t);

        // Recursively sort last 2/3 elements
        stoogesort(arr, first + t, last);

        // Recursively sort first 2/3 elements again to confirm
        stoogesort(arr, first, last - t);
    }
}

vector<int> generateArray(vector<int> &arr, int n)
{

    arr.clear();
    srand((unsigned)time(NULL));

    int arrNum = 0;
    int range = 10000;
    for (int i = 0; i < n; i++)
    {
        arrNum = (rand() % range) + 1;
        arr.push_back(arrNum);
    }
    return arr;
}

/* void calculateTimeTaken(int range)
{
     n = (rand() % range) + 1 <<endl;
    cout << "Time taken: " << ((double)(clock() - tStart)/CLOCKS_PER_SEC);
    return n;
}
   */

// Main Code
int main()
{

    int size[] = {100, 5000, 10000, 15000, 20000};
    int n = 0;
    for (int j = 0; j < (sizeof(size) / sizeof(*size)); j++)
    {

        n = size[j];
        generateArray(arr, n);

        // Calling Stooge Sort function to sort the array
        stoogesort(arr, 0, n - 1);
        double time = ((double)(clock() - tStart) / CLOCKS_PER_SEC);
        cout << "Time taken: " << time << endl;
    }

    // Print the Output in stooge.out
    //printFinal(arr,n);

    return 0;
}
