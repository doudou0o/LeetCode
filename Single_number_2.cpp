class Solution {
public:
    int singleNumber(int A[], int n) {
    	int ans=0;
    	map<int,int>m;
    	for(int i=0;i<n;i++){
    		m[A[i]]++;
    	}
    	map<int,int>::iterator it=m.begin();
    
    	while(it!=m.end()){
    		if(it->second != 3)return it->first;
    		it++;
    	}
    
    	return ans;
    }
};