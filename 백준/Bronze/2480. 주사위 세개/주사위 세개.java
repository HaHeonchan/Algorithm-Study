import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inp = br.readLine().split(" ");

        int count = 0;
        int equalNum = 0;
        int maxNum = 0;
        for(int i = 0; i < 3; ++i){
            if(inp[i%3].equals(inp[(i+1)%3])){
                count++;
                equalNum = Integer.parseInt(inp[i]);
            } else if (Integer.parseInt(inp[i]) > maxNum) {
                maxNum = Integer.parseInt(inp[i]);
            }
        }
        switch (count){
            case 0:
                bw.write(String.valueOf(maxNum*100));
                break;
            case 1:
                bw.write(String.valueOf(1000+equalNum*100));
                break;
            case 3:
                bw.write(String.valueOf(10000+equalNum*1000));
                break;
        }
        bw.close();
    }
}