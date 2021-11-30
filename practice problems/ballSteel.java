import java.util.*;
public class ballSteel {
    public static Boolean connected(ArrayList<Integer> balls, int k, int j){
        Boolean connected = true;
        int xJ = balls.get(2*j);
        int yJ = balls.get(2*j+1);
        for (int i=0; i<balls.size()/2; i++){
            if (i==j){
                continue;
            }
            int d = Math.abs(balls.get(2*i)-xJ)+Math.abs(balls.get(2*i+1)-yJ);
            if (d > k) return false;
        }

        return connected;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();
        for (int i=0; i<tests;i++){
            int n = sc.nextInt();
            int k = sc.nextInt();
            
            ArrayList<Integer> balls = new ArrayList<Integer>();
            for (int j = 0; j<n;j++){
                balls.add(sc.nextInt());
                balls.add(sc.nextInt());
            }

            Boolean result = true;
            for (int j = 0; j<n;j++){
                if (connected(balls, k, j)){
                    result = false;
                }
            }
            if (result){
                System.out.println("-1");
            } else{
                System.out.println("1");
            }
        }
        sc.close();
    }
}
