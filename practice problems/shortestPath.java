import java.util.*;

public class shortestPath {
    private static class Node implements Comparable<Node> {
        public Integer id;
        public Integer w;

        public Node(Integer id, Integer w) {
            this.id = id;
            this.w = w;
        }

        public int compareTo(Node other) {
            return this.w.compareTo(other.w);
        }
        
    }

    public static List<Integer> dijkstra (List<ArrayList<Node>> graph, int s, int n){
        List<Boolean> visited = new ArrayList<Boolean>();
        List<Integer> dj = new ArrayList<Integer>();

        for (int i=0; i<n;i++){
            visited.add(false);
            dj.add(9999);
        }
        dj.set(s,0);
        
        
        int count = 0;
        while (count < n){
            int current = 10000;
            for (int i=0; i < dj.size(); i++) {
                if (!visited.get(i) && dj.get(i)<current){
                    current = i;
                }
            }

            count ++;
            visited.set(current, true);
            

            for (Node node: graph.get(current)){
                if (!visited.get(node.id)){
                    int distance = dj.get(current) + node.w;
                    if (distance < dj.get(node.id)){
                        dj.set(node.id, distance);
                    }
                }
            }
        }

        return dj;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int q = sc.nextInt();
            int s = sc.nextInt();

            if (n==0){break;}
            
            List<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
            for (int i=0; i<n;i++){
                graph.add(new ArrayList<Node>());
            }
            for (int i=0; i<m;i++){
                int u = sc.nextInt();
                int v = sc.nextInt();
                int w = sc.nextInt();

                graph.get(u).add(new Node(v, w));
                // graph.get(v).add(new Node(u, w));
            }

            List<Integer> queries = new ArrayList<Integer>();
            for (int i=0; i<q;i++){
                queries.add(sc.nextInt());
            }

            List<Integer> dj = dijkstra(graph, s, n);
            for (int i: queries){
                if (dj.get(i) > 1000){
                    System.out.println("Impossible");
                } 
                else {
                    System.out.println(dj.get(i));
                }
            }
            System.out.println();
        }
        
    }
}
