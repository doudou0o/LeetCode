class Solution {
public:
    bool wordBreaker(string s, unordered_set<string> &dict,stack<string> stk,vector<string> &ans,set<string> &unmatched){
    	if(s.length()==0){
    		string t="";
    		while(!stk.empty()){
    			t=stk.top()+" "+t;
    			stk.pop();
    		}
    		int len=t.length();
    		ans.push_back(t.substr(0,len-1));
    		return true;
    	}
    	bool flag=false;
    	bool finalflag=false;
    	for(int i=0;i<=s.length();i++){
    		string substr=s.substr(0,i);
    		unordered_set<string>::iterator it = dict.find(substr);
    		if( it == dict.end() )continue;//not in dictionary
    
    		stk.push(substr);
    		string suffix_str = s.substr(i);
    			set<string>::iterator unit=unmatched.find(suffix_str);
    			if(unit != unmatched.end()){stk.pop();continue;}
    		flag=wordBreaker(suffix_str,dict, stk ,ans,unmatched);
    		stk.pop();
    		if(!flag)unmatched.insert(suffix_str);
    		if(flag)finalflag=true;
    	}
    	return finalflag;
    }
    
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
    	vector<string> ans;
    	stack<string> stk;
    	set<string> unmatched;
    	wordBreaker(s,dict,stk,ans,unmatched);
    	return ans;
    }
};