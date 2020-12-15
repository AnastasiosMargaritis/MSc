package com.leader_election;

import java.util.*;

public class FloodMax {

    List<Node> nodes = new ArrayList<>();
    private boolean leaderElected = false;
    int[][] graph;

    //    Constructor of FloodMax class. Accepts as arguments the number of nodes
    //    and created a List of nodes.
    public FloodMax(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
        }

        this.graph = new int[bound][bound];
    }

    // Creates a randomly generated graph as a representation of a 2D array.
    public void createGraph(){
        Random random = new Random();

        for (int i = 0; i < this.nodes.size(); i++){
            int edges = random.nextInt(this.nodes.size()) + 1;
            for(int j = 0; j < edges; j++){
                int node = random.nextInt(this.nodes.size());
                while(node == i){
                    node = random.nextInt(this.nodes.size());
                }
                this.graph[i][node] = node;
                this.graph[node][i] = i;
            }
        }
        this.printGraph();
    }

    // Prints the graph.
    public void printGraph(){
        for(int i = 0; i < this.nodes.size(); i++){
            for(int j = 0; j < this.nodes.size(); j++){
                System.out.print(this.graph[i][j] + " ");
            }

            System.out.println();
        }
    }

    // Check if our election procedure is done. We take as an argument a list of UUID's and
    // we push all the values of the list to a Set. If the size of the set equals to 1 -> which means
    // that only one value is sent by each node -> our election algorithm is completed.
    public boolean checkElection(List<UUID> leader){
        Set<UUID> unique = new HashSet<>();

        for(int i = 0; i < this.nodes.size(); i++){
            unique.add(leader.get(i));
        }

        System.out.println("Check election " + unique.size());

        if(unique.size() == 1){
            return true;
        }else{
            return false;
        }
    }

    // In each phase, all nodes communicate with the nodes they are connected and exchage UUID's. In the end of
    // each step, all nodes store the max UUID value among them.
    public void electLeader(){
        this.createGraph();

        List<UUID> leaders = new ArrayList<>();
        for(int i = 0; i < this.nodes.size(); i++){
            leaders.add(this.nodes.get(i).getUuid());
        }

        System.out.println();

        while(!checkElection(leaders)){
            for(int i = 0; i < this.nodes.size(); i++){
                UUID max = this.nodes.get(i).getUuid();

                for(int j = 0; j < this.nodes.size(); j++){
                    if(this.graph[i][j] != 0 && max.compareTo(this.nodes.get(j).getUuid()) <0){
                        max = this.nodes.get(j).getUuid();
                    }
                }

                leaders.set(i, max);
                for(int j = 0; j < this.nodes.size(); j++){
                    if(this.graph[i][j] != 0){
                        this.nodes.get(j).setUuid(max);
                    }
                }
                for(int k = 0; k < this.nodes.size(); k++){
                    System.out.println("Node " + k + " has UUID " + this.nodes.get(k).getUuid() + ".");
                }
                System.out.println("===================================");
                System.out.println();
            }
        }
        for(int k = 0; k < this.nodes.size(); k++){
            System.out.println("Node " + k + " has UUID " + this.nodes.get(k).getUuid() + ".");
        }
        System.out.println("===================================");
        System.out.println();
    }
}
