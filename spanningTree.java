import java.util.*;
public class spanningTree {
    private static class Branch implements Comparable<Branch>{
        public Integer id;
        public Integer weight;

        public Branch(int id, int weight) {
            this.id = id;
            this.weight = weight;
        }
        
        public int compareTo(Branch other) {
            return this.weight.compareTo(other.weight);
        }

    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int nodes = input.nextInt();
        int edges = input.nextInt();
        
        List<PriorityQueue<Branch>> tree = new ArrayList<PriorityQueue<Branch>>();
        for(int i = 0; i < nodes+1; i++) {
            tree.add(new PriorityQueue<Branch>());
        }
        
        for(int i = 0; i < edges; i++){
            int firstNode = input.nextInt();
            int secondNode = input.nextInt();
            int weight = input.nextInt();


            tree.get(firstNode).add(new Branch(secondNode,weight));
            tree.get(secondNode).add(new Branch(firstNode,weight));
        }
        List<Boolean> visited = new ArrayList<Boolean>();
        visited.add(true);
        visited.add(true);
        for(int i=1; i < nodes; i++){
            visited.add(false);
        }

        int minimumWeight = 0;

        List<Integer> treeID = new ArrayList<Integer>();
        treeID.add(1);

        int size = 1;


        while (size < nodes){
            int minW = 1000001;
            int minIdMother = 0;
            int minId = 0;
            
            for (int j = 0; j < treeID.size(); j++){
                int i = treeID.get(j);
                PriorityQueue<Branch> current = tree.get(i);

                while(!current.isEmpty() && visited.get(current.peek().id)){
                    current.remove();
                }
                
                if (!current.isEmpty()){
                    int id = current.peek().id;
                    int w =  current.peek().weight;

                    if (minW > w){
                        minW = w;
                        minId = id;
                        minIdMother = i;
                    }
                }
            }               

            minimumWeight += minW;
            size ++;
            treeID.add(minId);
            visited.set(minId,true);
            tree.get(minIdMother).remove();
            
        }
        
        input.close();

        System.out.println(minimumWeight);
    }
}
