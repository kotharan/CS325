
// C++ code to implement stooge sort 
#include <iostream> 
#include <vector>
#include <fstream>
#include <time.h>

using namespace std; 
vector<int> arr ;
ifstream infile("data.txt");
// Function to implement stooge sort 
void stoogesort(vector<int> &arr, int first, int last) 
{ 
    
    // If first element is smaller than last, swap them 
    if (arr[first] > arr[last]) 
        swap(arr[first], arr[last]); 
  
    // If there are more than 2 elements in the array 
    if (last - first + 1 > 2) { 
        int t = (last - first + 1) / 3; 
  
        // Recursively sort first 2/3 elements 
        stoogesort(arr, first, last - t); 
  
        // Recursively sort last 2/3 elements 
        stoogesort(arr, first + t, last); 
  
        // Recursively sort first 2/3 elements again to confirm 
        stoogesort(arr, first, last - t); 
    } 
} 

void printFinal(vector<int>& arr, int n)
{
    ofstream myfile;
    myfile.open ("stooge.out");
    for (int i=0; i < n; i++)
    {
    // Storing the sorted array 
    myfile << arr[i]<<" ";
    }
    myfile.close();


}

  
// Main Code which passes the 
int main() 
{ 
    clock_t tStart = clock();

    if(!infile)
    {
        cout<< "File does not exist" <<endl;
    }

    ifstream file("data.txt");

    int data;
    while (file >> data)
    {
        arr.push_back(data);

    }

    int n =  arr[0];
	arr.erase(arr.begin());

    // Calling Stooge Sort function to sort 
    // the array 
    stoogesort(arr, 0, n - 1); 
    
    // Print the Output in stooge.out
    printFinal(arr,n);
    
    cout << "Time taken: " << ((double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0; 
} 
