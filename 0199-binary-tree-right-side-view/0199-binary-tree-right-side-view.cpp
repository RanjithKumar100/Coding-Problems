/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
   vector<int> ans;
   if(root == NULL){
       return {};
   }
   q.push(root);
   while(!q.empty()){
       int level = q.size();
       for(int i = 0; i< level; i++){
           TreeNode* front = q.front();
           q.pop();
           if (i==0 ){
               ans.push_back(front->val);
           }
           if(front->right != NULL){
               q.push(front->right) ;
           }
            if(front->left != NULL){
               q.push(front->left) ;
           }
       }
   }
   return ans;
    }
};