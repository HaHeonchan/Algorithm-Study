import java.util.*;


class Solution {
    public static int solution(int n, int[][] edge) {
        Map<String, Set<Integer>> arrived = new HashMap<>();
        arrived.put("arrived", new HashSet<>(List.of(1)));

        Set<Integer> allEdge = new HashSet<>();
        for (int i = 2; i <= n; i++){
            allEdge.add(i);
        }
        arrived.put("notArrived", allEdge);
        
        int level = 2;
        int count = 0;
        while(arrived.get("arrived").size() != n){
            Set<Integer> temp = new HashSet<>();
            for(int[] e: edge){
                if(arrived.get("arrived").contains(e[0]) && arrived.get("notArrived").contains(e[1])){
                    temp.add(e[1]);
                } else if (arrived.get("arrived").contains(e[1]) && arrived.get("notArrived").contains(e[0])) {
                    temp.add(e[0]);
                }
            }

            arrived.get("notArrived").removeAll(temp);
            arrived.get("arrived").addAll(temp);
            level++;
            count = temp.size();
        }

        return count;
    }
}