#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

struct activityInfo{
int activityNum , start , finish; // Struct to store activity number , start time and end time
};

vector<activityInfo> ActivityList;
vector<int> all_Activities;


bool compare( activityInfo activity1,activityInfo activity2)
{
    if (activity1.finish < activity2.finish) return true;  // Used to sort as per activity end time
    return false;
}


void select_This_Activity(int num_Of_Activities)
{
    int i = 0,total_Act_Selected = 0;
    total_Act_Selected++;               // Total count of the activities selected from all the activities provided in the act.txt file

    // Select the first activity
    all_Activities.resize(total_Act_Selected);
    all_Activities[total_Act_Selected-1] = ActivityList[0].activityNum;

    // Continue with other activities
    for (int j = 1; j < num_Of_Activities; j++)
    {
                    /* If activity's start time greater than or
                     equal to the finish time of previously selected
                     activity, then select it */
    if (ActivityList[j].start >= ActivityList[i].finish)
    {
    total_Act_Selected++;
    all_Activities.resize(total_Act_Selected);
    all_Activities[total_Act_Selected-1] = ActivityList[j].activityNum;
    i = j;

}}}

void PrintOutput(int setNum)  // To print the output as per assignment instructions
{
    if(all_Activities[0] != 0)
    {
    int total_Act_Selected = all_Activities.size();
    cout << "Set " << setNum << endl;
    cout << "Number of activities selected = " << total_Act_Selected << endl;
    cout << "Activities:";
    for (int i = 0; i < total_Act_Selected; ++i)
    {
    cout << " " << all_Activities[i];
    }
    cout << endl<<endl;
    }
}

int main()
{

    string filename = "act.txt";
    ifstream inFile(filename);
    if (inFile.is_open())
    {
    int num_Of_Activities = 0; // Number of Activities
    int setNum = 1; // for each set of activities


    while(!inFile.eof())
    {
    ActivityList.resize(0);
    inFile >> num_Of_Activities;
    for (int i = 0; i < num_Of_Activities; ++i)
    {
    ActivityList.resize(i+1);
    inFile >> ActivityList[i].activityNum;
    inFile >> ActivityList[i].start;
    inFile >> ActivityList[i].finish;
    }

    sort(ActivityList.begin(), ActivityList.end(), compare);

    select_This_Activity(num_Of_Activities);

    PrintOutput(setNum++);

    }
    inFile.close();
    }
    else
    {
    cout << "File not found";
    }
    return 0;
}
