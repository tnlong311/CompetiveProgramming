import java.util.*;

public class gold {
    public static int getGold(ArrayList<ArrayList<String>> map, int pR, int pC){
        int result = 0;
        ArrayList<ArrayList<Integer>> q = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> t = new ArrayList<Integer>();
        t.add(pR);
        t.add(pC);
        q.add(t);

        while (!q.isEmpty()){
            ArrayList<Integer> square = q.remove(0);
            int col = square.get(1);
            int row = square.get(0);

            // position of map
            String s = map.get(row).get(col);

            if (s.equals("G")){
                result++;

            }
            // if (square.equals("D") || !isValid(map.size(), map.get(0).size(), i, j) || square.equals("#")){
            //     continue;
            // } 
            s = "#";
        }
        return result;
    }
    // public static ArrayList<ArrayList<Integer>>  neighbours (ArrayList<ArrayList<String>> map, int i, int j){
    //     ArrayList<ArrayList<Integer>> neighbours = new ArrayList<ArrayList<Integer>>();
    //     String square = map.get(i).get(j);

    //     if (square.equals("D") || !isValid(map.size(), map.get(0).size(), i, j) || square.equals("#")){
    //         return neighbours;
    //     } 
    //     else {
            // ArrayList<Integer> t = new ArrayList<Integer>();
            // t.add(i);
            // t.add(j);
            // neighbours.add(t);
    //     }
    //     return neighbours;
    // }
    public static Boolean isValid(int w, int h, int r, int c){
        return (w>r || 0<r) && (h>c || 0<c);
    }
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int w = inp.nextInt();
        int h = inp.nextInt();

        int pC = 0, pR =0;
        ArrayList<ArrayList<String>> map = new ArrayList<ArrayList<String>>();
        ArrayList<ArrayList<Integer>> trap = new ArrayList<ArrayList<Integer>>();
        for (int i=0; i<h; i++){
            ArrayList<String> arr = new ArrayList<String>();
            String line = inp.next();
            for (int j=0; j<w; j++){
                String square = Character.toString(line.charAt(j));
                if (square.equals("T")){
                    ArrayList<Integer> t = new ArrayList<Integer>();
                    t.add(i);
                    t.add(j);
                    trap.add(t);
                    square = "#";
                } 
                else if (square.equals("P")){
                    pC=j;
                    pR=i;
                }
                arr.add(square);
            }
            map.add(arr);
        }
        

        for (int i=0; i<trap.size(); i++){
            int r = trap.get(i).get(0);
            int c = trap.get(i).get(1);
            if(isValid(w,h,r-1,c) && !map.get(r-1).get(c).equals("#")){
                map.get(r-1).set(c, "D");
            }
            if(isValid(w,h,r+1,c) && !map.get(r+1).get(c).equals("#")){
                map.get(r+1).set(c, "D");
            }
            if(isValid(w,h,r,c-1) && !map.get(r).get(c-1).equals("#")){
                map.get(r).set(c-1, "D");
            }
            if(isValid(w,h,r,c+1) && !map.get(r).get(c+1).equals("#")){
                map.get(r).set(c+1, "D");
            }            
        }
        inp.close();
       
        System.out.println(getGold(map, pR, pC));
        System.out.println(map.toString());
    }

}
