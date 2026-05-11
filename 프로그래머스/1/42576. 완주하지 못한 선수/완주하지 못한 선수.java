import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> result = new HashMap<>();
        for(String p : participant){
            if(result.containsKey(p)){
                result.replace(p, result.get(p)+1);
            }else{
                result.put(p, 1);
            }
        }

        String answer = "";

        for(String c : completion){
            result.replace(c, result.get(c)-1);
        }

        for(String name : result.keySet()){
            if(result.get(name) > 0){
                answer = name;
            }
        }
        return answer;
    }
}