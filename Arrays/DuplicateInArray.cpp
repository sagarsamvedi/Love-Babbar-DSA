// QUESTION LINK
// https://www.codingninjas.com/studio/problems/duplicate-in-array_893397?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1

#include <vector>;
using namespace std;

int findDuplicate(vector<int> &arr) {
  // WE CAN USE FORMULA FOR SUM OF N TERMS
  int sum = 0;
  int size = arr.size();
  for (int index = 0; index < size; index++){
      sum += arr[index];
  }

  return (sum - ((size)*(size-1))/2);
}
