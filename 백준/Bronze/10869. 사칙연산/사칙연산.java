import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inp = br.readLine().split(" ");
        int[] results = new int[5];
        results[0] = Integer.parseInt(inp[0]) + Integer.parseInt(inp[1]);
        results[1] = Integer.parseInt(inp[0]) - Integer.parseInt(inp[1]);
        results[2] = Integer.parseInt(inp[0]) * Integer.parseInt(inp[1]);
        results[3] = Integer.parseInt(inp[0]) / Integer.parseInt(inp[1]);
        results[4] = Integer.parseInt(inp[0]) % Integer.parseInt(inp[1]);

        for(int i = 0; i < results.length; i++){
            bw.write(String.valueOf(results[i]));
            bw.newLine();
        }
        bw.close();
    }
}