/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
    	vector<int> ans;
    	if(root != NULL)preorder(root,ans);
    	else{};
    	return ans;
    }
    
    void preorder(TreeNode *root,vector<int> &v){
    	v.push_back(root->val);
    	if(root->left != NULL)
    		preorder(root->left,v);
    	if(root->right != NULL)
    		preorder(root->right,v);
    	return;
    }
};