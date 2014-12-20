class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
    	unordered_set<string>::iterator it;
    	for(it=dict.begin();it!=dict.end();it++){
    		if(s.find(*it) == 0){
    			int len=(*it).length();
    			string substr=s;
    			substr.erase(0,len);
    			if(substr.length()==0)return true;
    			if(wordBreak(substr,dict)){
    				return true;
    			}
    		}
    	}
    	return false;
    }
};