// QUESTION LINK
// https://www.codingninjas.com/studio/problems/find-unique_625159?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1&leftPanelTabValue=PROBLEM

int findUnique(int *arr, int size)
{
   int ans = 0;
   for (int index = 0; index < size; index++){
       ans ^= arr[index];
   }
   return ans;
}