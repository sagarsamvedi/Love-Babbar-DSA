// QUESTION LINK
// https://www.codingninjas.com/studio/problems/sum-of-max-and-min_1081476?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=SUBMISSION

#include <bits/stdc++.h> 
#include <iostream>
using namespace std;

int sumOfMaxMin(int arr[], int n){
	
	int min = INT_MAX;
	int max = INT_MIN;
	for (int i = 0; i < n; i++){
		if(arr[i] > max){
			max = arr[i];
		}
		if(arr[i] < min){
			min = arr[i];
		}
	}
	return min + max;
}

int main() {
    const int n = 5;  // You can change the size of the array as needed
    int arr[n];

     cout << "Enter " << n << " elements for the array:" <<  endl;

    for (int i = 0; i < n; ++i) {
         cin >> arr[i];
    }

    int result = sumOfMaxMin(arr, n);

     cout << "Sum of maximum and minimum elements: " << result <<  endl;

    return 0;
}
