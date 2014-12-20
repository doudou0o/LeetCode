typedef struct child_s{
	int pos;
	int rate;
}child;

int cmp(const void *a , const void *b){
	child ac=*(child*)a;
	child bc=*(child*)b;
	if( ac.rate>bc.rate )return 1;
	else return -1;
	return 0;
}
class Solution {
public:
	int candy(vector<int> &ratings){
		int len=ratings.size();
		child* children = (child*)malloc(len*sizeof(child));
		for(int i=0;i<len;i++){
			children[i].pos=i;
			children[i].rate=ratings[i];
		}

		qsort(children,len,sizeof(children[0]),cmp);

		int* candy_num=(int*)malloc(len*sizeof(int));
		//memset(candy_num,0,sizeof(int)*len);
	    	fill(candy_num , candy_num + len , 0);
		int ans=0;
		for(int i=0;i<len;i++){
			int leftpos_candy=0,rightpos_candy=0;

			if(children[i].pos -1 < 0 ) leftpos_candy=0;
			else if(children[i].rate==ratings[children[i].pos -1])leftpos_candy=0;
			else leftpos_candy=candy_num[children[i].pos-1];
			if(children[i].pos +1 >= len)rightpos_candy=0;
			else if(children[i].rate==ratings[children[i].pos +1])rightpos_candy=0;
			else rightpos_candy=candy_num[children[i].pos+1];

			if(rightpos_candy>=leftpos_candy)
				candy_num[children[i].pos]=rightpos_candy+1;
			else
				candy_num[children[i].pos]=leftpos_candy+1;

			ans+=candy_num[children[i].pos];
		}
		free(candy_num);
		free(children);
		return ans;
	}
};
