#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int len=gas.size();
		int sum=0;
		for(int i=0;i<len;i++){
			gas[i]=gas[i]-cost[i];
			sum+=gas[i];
		}
		if(sum<0)return -1;

		for(int i=0;i<len;i++){
			sum=0;
			if(gas[i]<0)continue;
			int j;
			for(j=i;j<len;j++){
				sum+=gas[j];
				if(sum<0)break;
			}
			if(j==len && sum>=0)
				return i;
		}
    }
};

int main(){
	vector<int> g;
	vector<int> c;
	g.push_back(3);c.push_back(0);
	g.push_back(0);c.push_back(2);
	g.push_back(0);c.push_back(2);
	g.push_back(1);c.push_back(0);
	g.push_back(2);c.push_back(0);
	g.push_back(0);c.push_back(2);
	int a=Solution().canCompleteCircuit(g,c);
	cout<<a;
	return 1;
}