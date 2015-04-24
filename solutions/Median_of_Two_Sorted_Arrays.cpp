#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findKth(vector<int> A,vector<int> B,int k)
{
    int l1 = A.size();
    int l2 = B.size();
    if ( l1 > l2 )
        return findKth(B,A,k);
    if ( l1 == 0 )
        return B.at(k-1);
    if ( k == 1 )
        return std::min( A.at(0) , B.at(0));
    int pa = std::min(k/2-1,l1-1);
    int pb = k-pa-2;
    if ( A.at(pa) < B.at(pb) ) {
        A.erase(A.begin(),A.begin()+pa+1);
        return findKth(A,B,k-pa-1);
    }
    if ( A.at(pa) > B.at(pb) ) {
        B.erase(B.begin(),B.begin()+pb+1);
        return findKth(A,B,k-pb-1);
    }
    if ( A.at(pa) == B.at(pb) ) {
        return A.at(pa);
    }
    return 0;
}
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2){
    int length1 = nums1.size();
    int length2 = nums2.size();
    int total = length1 + length2;
    if ( total & 0x1 )
        return findKth(nums1,nums2,total/2 + 1);
    else{
        return ((double)(findKth(nums1,nums2,total/2)+findKth(nums1,nums2,total/2+1)))/2;
    }
}
int main(int argc, const char *argv[])
{
    std::vector<int> n1;
    std::vector<int> n2;
    n1.push_back(1);
    n1.push_back(2);
    n2.push_back(1);
    n2.push_back(2);

    double ans = findMedianSortedArrays(n1,n2);
    std::cout << ans << std::endl;
    return 0;
}
