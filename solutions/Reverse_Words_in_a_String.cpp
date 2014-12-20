class Solution {
public:
    void reverseWords(string &s) {
        char *p;
	    int len=s.length();
	    p=(char*)malloc((len+1)*sizeof(char));
	    s.copy(p,len,0);
	    p[len]='\0';

    	char *q=strtok(p," ");
    	string ans;
    	string k=" ";int i=0;
    	while(q != NULL){
    		if(i==0){ans= q+ans;i++;}
    		else ans= q + k +ans;
    		q=strtok(NULL," ");
    	}
    	s=ans;
    }
};