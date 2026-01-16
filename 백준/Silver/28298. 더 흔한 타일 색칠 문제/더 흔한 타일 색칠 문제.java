import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

// hashMap (getOrDefault)

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] items = br.readLine().split(" ");
        int N = Integer.parseInt(items[0]);
        int M = Integer.parseInt(items[1]);
        int K = Integer.parseInt(items[2]);

        String[][] tileMatrix = new String[N][M];
        String[][] resultTile = new String[K][K];
        int resultChance = 0;
        for (int i = 0; i < N; i++) {
            tileMatrix[i] = br.readLine().split("");
        }


        for(int x = 0; x < K; x++){
            for(int y = 0; y < K; y++){
                int maxCount = 0;
                String maxColor = "";
                Map<String, Integer> colorMap = new HashMap<>();

                for(int i = x; i < N; i+=K){
                    for(int j = y; j < M; j+=K){
                        colorMap.put(tileMatrix[i][j], colorMap.getOrDefault(tileMatrix[i][j], 0) + 1);
                    }
                }

                for (Map.Entry<String, Integer> entry : colorMap.entrySet()) {
                    if (entry.getValue() > maxCount) {
                        maxCount = entry.getValue();
                        maxColor = entry.getKey();
                    }
                }

                resultTile[x][y] = maxColor;
                resultChance += (N*M)/(K*K) - maxCount;
            }
        }

        bw.write(String.valueOf(resultChance));
        bw.newLine();
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                bw.write(resultTile[i%K][j%K]);
            }
            bw.newLine();
        }
        bw.close();
    }
}