#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream infile("data.txt");
string myArray[5];
void merge(int arr[],int s , int e)
{
    int mid = (s+e)/2;
    int i = s;
    int j = mid+1;
    int k = s;

    /* create temp arrays */
    int temp[100];
    while(i <= mid && j <= e)
    {
            // If the first value of left array is less than first value of right value
            if(arr[i]<arr[j])
            {
                temp[k++] = arr[i++];  // Do this
            }
            else
            {
                temp[k++] = arr[j++]; // Else do this
            }
    }

    // To copy the remaining number after comparing both the arrays and exhausting(Completing) one of them
    while(i<=mid)
    {
        temp[k++] = arr[i++];
    }
    while(j<=e)
    {
        temp[k++] = arr[j++];
    }

    for(i=s ; i<=e ; i++ )
    {
        /* Copy data to temp array to our array */
        arr[i] = temp [i];
    }


}


void mergeSort(int arr[], int s , int e)
{

 if(s>=e)
 {
     return;
 }
     // Same as (s+e)/2
    int mid = s+(e-s)/2;

    mergeSort(arr,s,mid);
    mergeSort(arr,mid+1,e);

    merge(arr,s,e);

}



int main(){

    if(!infile)
    {
        cout<< "File does not exist" <<endl;
    }

    char str[255];
    ifstream file("data.txt");
    if(file.is_open())
    {

       for(int i = 0 ; i<5; i++)
       {
           file >> str;
           cout<<str[0];
       }
       cout<<endl;
    }


    int arr[] = {2,5,6,3,3,5,3,3};
    int size = sizeof(arr)/sizeof(arr[1]);
    int start = 0;
    int end = size;

    mergeSort(arr,start,end-1);

    for(int i= 0 ; i<size ; i++)
    {
        cout<<arr[i];
    }



    return 0;
}
