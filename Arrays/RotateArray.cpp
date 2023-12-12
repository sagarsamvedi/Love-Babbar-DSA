// QUESTION LINK
// https://www.codingninjas.com/studio/problems/rotate-array_1230543?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=PROBLEM

#include<vector>
using namespace std;
vector<int> rotateArray(vector<int>arr, int k) {
    int len = arr.size();

    while ( k > 0){
        int temp = arr[0];
        for (int i = 0; i < len; i++){
            arr[i] = arr[i+1];        
        }
        arr[len-1] = temp;
    k--;
    }
    
    return arr;
}
