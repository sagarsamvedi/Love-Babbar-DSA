// QUESTION LINK
// https://www.codingninjas.com/studio/problems/pair-sum_697295?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1

#include <bits/stdc++.h>

vector<vector<int>> pairSum(vector<int> &arr, int s){
   // Write your code here.
   vector<vector<int>> ans;
   int size = arr.size();
   for (int index = 0; index < size; index++){
      for (int j = index + 1; j < size; j++){
         if (arr[index] + arr[j] == s){
            vector <int> temp;
            temp.push_back(arr[index]);
            temp.push_back(arr[j]);
            sort(temp.begin(),temp.end());
            ans.push_back(temp);
         }
      }
   }
   sort(ans.begin(),ans.end());
   return ans;
}