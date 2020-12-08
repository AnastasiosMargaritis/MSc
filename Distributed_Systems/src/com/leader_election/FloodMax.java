package com.leader_election;

import java.util.*;

public class FloodMax {

    List<Node> nodes = new ArrayList<>();
    private boolean leaderElected = false;
    int[][] graph;


    public FloodMax(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
        }

        this.graph = new int[bound][bound];
    }

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

    public void printGraph(){
        for(int i = 0; i < this.nodes.size(); i++){
            for(int j = 0; j < this.nodes.size(); j++){
                System.out.print(this.graph[i][j] + " ");
            }

            System.out.println();
        }
    }

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

    public void electLeader(){
        this.createGraph();

        List<UUID> leaders = new ArrayList<>();
        for(int i = 0; i < this.nodes.size(); i++){
            leaders.add(this.nodes.get(i).getUuid());
            System.out.print(leaders.get(i) + " ");
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
                    System.out.print(leaders.get(k) + " ");
                }
                System.out.println();
            }
        }
    }
}
