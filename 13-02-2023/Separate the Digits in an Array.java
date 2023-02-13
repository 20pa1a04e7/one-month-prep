class Solution {
    public int[] separateDigits(int[] nums) {
        
        String s = "";
        for(int i=0 ;i< nums.length;i++){
            s +=nums[i];
        }
        int len = s.length();
        int [] arr = new int[len];
        for(int i=0 ;i<len ;i++){
            arr[i] = s.charAt(i) -'0';
        }
        return arr;
    }
}
