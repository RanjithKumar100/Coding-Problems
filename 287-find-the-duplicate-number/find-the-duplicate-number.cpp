class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        set<int> s;
        for(int i=0;i<nums.size();i++){
            if(s.contains(nums[i])){
                return nums[i];
            }
            s.insert(nums[i]);
        }
        return -1;
    }
};