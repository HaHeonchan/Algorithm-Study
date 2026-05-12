import java.util.*;

class Solution {
    public static int solution(int n, int[][] computers) {
        List<Set<Integer>> net = new ArrayList<>();
        Set<Integer> network = new HashSet<>();
        for(int i = 0; i < n; i++){
            if(!network.contains(i)){
                network.add(i);
                Deque<Integer> link = new ArrayDeque<>();
                link.add(i);

                while(!link.isEmpty()){
                    int popping = link.remove();
                    for(int j = 0; j < n; j++){
                        if(popping != j && computers[popping][j] == 1 && !network.contains(j)){
                            network.add(j);
                            link.add(j);
                        }
                    }
                }

                net.add(network);

            }
        }
        return net.size();
    }
}