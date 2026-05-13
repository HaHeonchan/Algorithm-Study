import java.util.*;

class Solution {
    public static int solution(String begin, String target, String[] words) {
        List<String> wordList = new ArrayList<>(List.of(words));
        if(!wordList.contains(target)){
            return 0;
        }

        Map<String, Integer> roadMap = new HashMap<>();
        roadMap.put(begin, 0);

        Deque<String> tripPlan = new ArrayDeque<>();
        tripPlan.add(begin);

        while (!tripPlan.isEmpty()){
            String currentWord = tripPlan.remove();
            for(String word : wordList){
                if(!roadMap.containsKey(word) || roadMap.get(currentWord) + 1 < roadMap.get(word)){
                    int count = 0;
                    for (int i = 0; i < Math.min(currentWord.length(), word.length()); i++){
                        if(currentWord.charAt(i) != word.charAt(i)){
                            count++;
                        }
                    }
                    if(count == 1){
                        tripPlan.add(word);
                        roadMap.put(word, roadMap.get(currentWord) + 1);
                    }
                }
            }
        }

        return roadMap.get(target);
    }
}