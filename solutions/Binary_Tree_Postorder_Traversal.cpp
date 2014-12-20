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
    vector<int> postorderTraversal(TreeNode *root) {
        TreeNode *a=root;
    	stack<int> s;
    	vector<int>ans;
    	if(root!=NULL)PreOrderTraversal(root,s);
    	else{};
    
    	while(!s.empty()){
    		ans.push_back(s.top());
    		s.pop();
    	}
    	return ans;
    }
    void PreOrderTraversal(TreeNode *root,stack<int> &s){
        s.push(root->val);
        if(root->right != NULL)
    		PreOrderTraversal(root->right,s);
    	if(root->left != NULL)
    		PreOrderTraversal(root->left,s);
    	return;
    }
};