class Solution {
    public void moveZeroes(int[] nums) {
        int ptr1 = 0;
        int ptr2 = 0;
        
        while (ptr2 < nums.length) {
            if (nums[ptr2] != 0) {
                int temp = nums[ptr1];
                nums[ptr1] = nums[ptr2];
                nums[ptr2] = temp;
                ptr1++;
            }
            ptr2++;
        }
    }
}
