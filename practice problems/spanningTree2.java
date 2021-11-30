import java.util.*;

public class spanningTree2 {
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

    private static int INF = (int) 1e9;

    public static long Prim(int s, List<List<Node>> graph) {
        Queue<Node> pq = new PriorityQueue<Node>();
        List<Integer> cost = new ArrayList<Integer>();
        List<Boolean> visited = new ArrayList<Boolean>();

        for(int i = 0; i < graph.size(); i++) {
            cost.add(INF);
            visited.add(false);
        }

        cost.set(s, 0);
        pq.add(new Node(s, 0));
        visited.set(s, true);

        while(!pq.isEmpty()) {
            Node top = pq.remove();
            int u = top.id;
            int w = top.w;
            visited.set(u, true);

            int minimumId = 0;
            int minimumW = 0;
            for(int i = 0; i < graph.get(u).size(); i++) {
                Node neighbor = graph.get(u).get(i);
                int v = neighbor.id;
                int neighborW = neighbor.w;
                // node 1: 60 50 40
               
                if(!visited.get(v) && neighborW < cost.get(v)) {
                    // cost.set(v, neighborW);
                    // pq.add(new Node(v, neighborW));
                    minimumId = v;
                    minimumW = neighborW;
                    
                }
                
            }
            visited.set(minimumId, true);
            pq.add(new Node(minimumId, minimumW));
            cost.set(minimumId, minimumW);
        }

        long total = 0;
        System.out.println(cost);
        for(int i = 1; i < graph.size(); i++) {
            total = cost.get(i) + total;
        }

        return total;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Node>> graph = new ArrayList<List<Node>>();

        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node>());
        }

        for(int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            graph.get(u).add(new Node(v, w));
            graph.get(v).add(new Node(u, w));
        }

        long ans = Prim(0, graph);
        System.out.println(ans);
    }
}
