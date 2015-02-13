/*Given a string, find the length of the longest substring without repeating characters. 
* For example, the longest substring without repeating letters for "abcabcbb" is "abc",
* which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
*
*/
    int lengthOfLongestSubstring(string s) {
     	map<int,int> map;
     	if(s.size() == 0)return 0;
    	int ans = 0;
    	int start=0;
    	map.insert(make_pair(s[0],0));
    	for(int i=1;i<s.size();i++){
    		int v = s[i];
    		if( map.count(v) && map[v]>=start  ){
    			int t = i-start;
    			ans = t>ans?t:ans;
    			start = map[v]+1;
    			map[v]=i;
    		}
    		else{
    			if( map.count(v) )
    				map[v]=i;
    			else
    				map.insert(make_pair(v,i));
    		}
    	}
    	int last = s.size() - start;
    	ans = last>ans?last:ans;
    	return ans;       
    }