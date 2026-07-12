class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        
        for (String val : strs){
            char[] unsorted = val.toCharArray();
            Arrays.sort(unsorted);
            String srtedString = new String(unsorted);
            res.putIfAbsent(srtedString, new ArrayList<>());
            res.get(srtedString).add(val);
            
        }
        return new ArrayList<>(res.values()); 
    }
}
