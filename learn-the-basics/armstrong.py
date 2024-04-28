bool checkArmstrong(int n){
	int count = int(log10(n) + 1);
	int temp = n;
	int sum = 0;
	while (temp>0){
		int digit = temp%10;
		sum += pow(digit,count);
		temp /= 10;
	}
	if (sum == n){
		return true;
	}
	return false;
}
