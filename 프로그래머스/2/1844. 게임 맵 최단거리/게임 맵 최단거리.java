import java.util.*;

class Solution {
    public static int solution(int[][] maps) {
        int[] dirX = {1, 0, -1, 0};
        int[] dirY = {0, -1, 0, 1};
        int lenX = maps.length;
        int lenY = maps[0].length;


        Deque<int[]> tripQue = new ArrayDeque<>();
        tripQue.add(new int[]{0, 0, 1});

        while (!tripQue.isEmpty()){
            int[] cPos = tripQue.remove();
            int cx = cPos[0], cy = cPos[1], disC = cPos[2];
            maps[cx][cy] = 0;

            for(int i = 0; i < 4; i++){
                int nx = cx + dirX[i], ny = cy + dirY[i];
                if((nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length && maps[nx][ny] == 1)){
                    if(nx == lenX-1 && ny == lenY-1){
                        return disC + 1;
                    }
                    maps[nx][ny] = 0;
                    tripQue.add(new int[]{nx, ny, disC + 1});
                }
            }
        }
        return -1;
    }
}