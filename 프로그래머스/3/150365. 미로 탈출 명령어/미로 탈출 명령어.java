import java.util.*;

public class Solution {

    static Map<Integer, String> dirChar = new HashMap<>(){{
        put(0, "d");
        put(1, "l");
        put(2, "r");
        put(3, "u");
    }};

    int[][] moveDir = new int[][]{{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
    int[] target;
    int[] range;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        target = new int[]{r, c};
        range = new int[]{n, m};
        String result = dfs("", x, y, k);
        if(result == null){
            result = "impossible";
        }
        return result;
    }

    private String dfs(String ways, int cx, int cy, int k){
        if(ways.length() >= k){
            if(cx == target[0] && cy == target[1]){
                return ways;
            } else{
                return null;
            }
        }
        if(!canArrive(cx, cy, ways.length(), k)){
            return null;
        }

        String answer = null, result;
        for(int i = 0; i < 4; i++){
            int nx = cx + moveDir[i][0], ny = cy + moveDir[i][1];
            if(canMove(nx, ny)){
                result = dfs(ways.concat(dirChar.get(i)), nx, ny, k);

                if(result != null){
                    answer = result;
                    break;
                }
            }
        }
        return answer;
    }

    private boolean canMove(int nx, int ny){
        return nx >= 1 && nx <= range[0] && ny >= 1 && ny <= range[1];
    }

    private boolean canArrive(int cx, int cy, int moveCount, int k){
        int shortestDis = Math.abs(cx - target[0]) + Math.abs(cy - target[1]);
        if(shortestDis > (k - moveCount) || ((k - moveCount) - shortestDis) % 2 == 1){
            return false;
        }
        return true;
    }
}