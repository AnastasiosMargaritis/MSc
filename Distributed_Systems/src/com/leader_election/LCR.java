package com.leader_election;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.UUID;

public class LCR {

    private List<Node> nodes = new ArrayList<>();
    private boolean leaderElected = false;

    public LCR(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
        }
    }

    public void setNodes(List<Node> nodes) {
        this.nodes = nodes;
    }

    public void electLeader(){

        UUID maxUUID = this.nodes.get(0).getUuid();
        System.out.println("Node " + 0 + " starts the whole procedure with UUID " + this.nodes.get(0).getUuid() + ".");

        for(int i = 1; i < this.nodes.size(); i++){
            if (this.nodes.get(i).getUuid().compareTo(maxUUID) > 0){
                maxUUID = this.nodes.get(i).getUuid();
            }

            System.out.println("Node " + i + " with UUID " + this.nodes.get(i).getUuid().toString() + " passes " + maxUUID + " to the next.");
        }

        int counter = 0;

        for(Node node: this.nodes){
            if(node.getUuid().compareTo(maxUUID) == 0){
                node.setLeader(true);
                System.out.println("Node " + counter + " is the Leader.");
            }else{
                System.out.println("Node " + counter + " is not the Leader.");
            }

            counter ++;
        }
    }
}
