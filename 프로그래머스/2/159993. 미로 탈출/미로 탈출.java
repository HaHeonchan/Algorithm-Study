import java.util.*;

class Solution {
    public static int solution(String[] maps) {
        int[] leverPos = new int[]{-1, -1};
        int[][] dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        char[][] grid = new char[maps.length][];
        for (int i = 0; i < maps.length; i++) {
            grid[i] = maps[i].toCharArray();
        }

        // 레버 찾기
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 'L'){
                    leverPos[0] = i;
                    leverPos[1] = j;
                    break;
                }
            }
            if(leverPos[0] != -1){
                break;
            }
        }

        if(leverPos[1] == -1){
            return -1;
        }

        // 레버에서 입구와 출구까지의 거리 구하기
        Deque<int[]> tripQue = new ArrayDeque<>();
        tripQue.add(new int[]{leverPos[0], leverPos[1], 0});
        int[] result = new int[]{-1, -1};
        int gxlen = grid.length;
        int gylen = grid[0].length;
        grid[leverPos[0]][leverPos[1]] = 'X';

        while(!tripQue.isEmpty()){
            int[] cPos = tripQue.remove();
            int cx = cPos[0], cy = cPos[1], dis = cPos[2];
            for(int i = 0; i < 4; i++){
                int nx = cx + dir[i][0], ny = cy + dir[i][1];
                if(!(nx >= 0 && nx < gxlen && ny >= 0 && ny < gylen && grid[nx][ny] != 'X')){
                    continue;
                }

                if(grid[nx][ny] == 'S'){
                    result[0] = dis+1;
                } else if(grid[nx][ny] == 'E'){
                    result[1] = dis+1;
                }

                if(result[0] >= 0 && result[1] >= 0){
                    tripQue.clear();
                    break;
                }

                tripQue.add(new int[]{nx, ny, dis+1});
                grid[nx][ny] = 'X';
            }
        }
        if(result[0] < 0 || result[1] < 0){
            return -1;
        }
        return result[0] + result[1];
    }
}