class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int>S;
    	while(!S.empty())S.pop();
    	
    	for(int i=0;i<tokens.size();i++){
    		string t=tokens[i];
    		if(t.length() > 1){S.push(atoi( t.c_str()));continue;}
    		switch (t[0])
    		{
    			int a,b;
    			case '*':	a=S.top();S.pop();
    						b=S.top();S.pop();
    						S.push(a*b);break;
    			case '/':	a=S.top();S.pop();
    						b=S.top();S.pop();
    						S.push(b/a);break;
    			case '+':	a=S.top();S.pop();
    						b=S.top();S.pop();
    						S.push(a+b);break;
    			case '-':	a=S.top();S.pop();
    						b=S.top();S.pop();
    						S.push(b-a);break;
    			default:	S.push(atoi( t.c_str()));
    		}	
    	}
    	return S.top();
    }
};