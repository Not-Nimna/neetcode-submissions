class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> store = new HashSet<>();
        for (int val : nums ){
            if (store.contains(val)){
                
                return true;
            }
            else{
                store.add(val);
            }

        }
        return false;
    }
}