#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<int> arr;

void merge(vector<int> &arr, int s, int e)
{
    int mid = (s + e) / 2;
    int i = s;
    int j = mid + 1;
    int k = s;

    /* create temp arrays */
    int temp[100];
    while (i <= mid && j <= e)
    {
        // If the first value of left array is less than first value of right value
        if (arr[i] < arr[j])
        {
            temp[k++] = arr[i++]; // Do this
        }
        else
        {
            temp[k++] = arr[j++]; // Else do this
        }
    }

    // To copy the remaining number after comparing both the arrays and exhausting(Completing) one of them
    while (i <= mid)
    {
        temp[k++] = arr[i++];
    }
    while (j <= e)
    {
        temp[k++] = arr[j++];
    }

    for (i = s; i <= e; i++)
    {
        /* Copy data to temp array to our array */
        arr[i] = temp[i];
    }
}

void mergeSort(vector<int> &arr, int s, int e)
{

    if (s >= e)
    {
        return;
    }
    // Same as (s+e)/2
    int mid = s + (e - s) / 2;

    mergeSort(arr, s, mid);
    mergeSort(arr, mid + 1, e);

    merge(arr, s, e);
}

int main()
{

    ifstream file("data.txt");

    int a;
    while (file >> a)
    {
        arr.push_back(a);
    }

    int size = arr[0];
    arr.erase(arr.begin());

    int start = 0;
    int end = size;

    mergeSort(arr, start, end - 1);

    ofstream myfile;
    myfile.open("insert.out");
    for (int i = 0; i < size; i++)
    {
        myfile << arr[i] << " ";
    }
    myfile.close();

    return 0;
}
