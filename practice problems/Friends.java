import java.util.*;

public class Friends {
    public static String check(int[][] relation) {
        for(int i = 0; i < 3; i++) {
            for(int j = i + 1; j < 4; j++) {
                for(int k = j + 1; k < 5; k++) {
                    if(relation[i][j] == 1 && relation[i][k] == 1 && relation[j][k] == 1) {
                        return "WIN";
                    }
                    if(relation[i][j] == 0 && relation[i][k] == 0 && relation[j][k] == 0) {
                        return "WIN";
                    }
                }
            }
        }

        return "FAIL";
    }

    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);
        int m = input.nextInt();
        int[][] relation = new int[5][5];
        for(int i = 0; i < m; i++) {
            int x = input.nextInt() - 1;
            int y = input.nextInt() - 1;
            relation[x][y] = 1;
            relation[y][x] = 1;
        }
        input.close();
        System.out.println(check(relation));
    }
}
