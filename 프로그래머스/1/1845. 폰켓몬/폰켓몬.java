import java.util.*;

class Solution {
    public static int solution(int[] nums) {
        int len = nums.length / 2;


        Set<Integer> pokemonType = new HashSet<>();
        for(int i : nums){
            pokemonType.add(i);
        }

        return Math.min(len, pokemonType.size());
    }
}