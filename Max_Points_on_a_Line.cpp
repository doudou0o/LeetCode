/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        int max=0;
    	map<double,int> M;
    	int len = points.size();
    	
    	if(points.size() <= 2)return points.size();
    
    	for(int i=0; i<len;i++){
    		int same=0,maxi=0,wuqiu=0;
    		M.clear();
    		for(int j=i+1;j<len;j++){
    			if ( points[i].x == points[j].x && points[i].y == points[j].y){
    				same++;
    			}
    			else if( points[i].x == points[j].x){
    				wuqiu++;
    				if( wuqiu>maxi ) maxi=wuqiu;
    			}
    			else{
    				double xielv=(double)(points[j].y - points[i].y)/(points[j].x-points[i].x);
    				M[xielv]++;
    				if( M[xielv]>maxi ) maxi=M[xielv];
    			}
    		}
    		maxi += same+1;
    		if( maxi>max )max=maxi;
    	}
    	return max;
    }
};