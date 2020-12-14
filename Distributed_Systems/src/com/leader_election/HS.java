package com.leader_election;

import java.util.ArrayList;
import java.util.List;

public class HS {

    private List<Node> nodes = new ArrayList<>();
    private boolean isLeaderElected = false;

    // Constructor of HS class. Accepts as arguments the number of nodes
    // and created a List of nodes. Initially, all nodes are elected as leader.
    public HS(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
            this.nodes.get(i).setLeader(true);
        }
    }

    // Election function for HS class. In a variable phase we store the value of the step we're.
    // For each node, in each phase we send to Math.pow(2, phase) nodes in both directions to compare UUID's.
    // Finally, for each step of the phase, we call the election complete function to check if our procedure is finished.
    public void electLeader(){
        int phase = 0;

        while(!isLeaderElected){

            if(phase == 0){
                System.out.println("Initially: ");
                for(int i = 0; i < this.nodes.size(); i++){
                    System.out.println("Node " + i + " is Leader.");
                }
                phase ++;
            }else{
                for(int i = 0; i < this.nodes.size(); i++) {
                    for(int j = 0; j < Math.pow(2, phase); j++){
                        if((this.nodes.get(i).getUuid().compareTo(this.nodes.get((i + j + 1) % this.nodes.size()).getUuid()) < 0
                        || this.nodes.get(i).getUuid().compareTo(this.nodes.get(Math.abs(this.nodes.size() + i - j - 1) % this.nodes.size()).getUuid()) < 0)
                        && this.nodes.get(i).isLeader()) {
                            this.nodes.get(i).setLeader(false);
                        }
                    }
                }

                System.out.println("In phase " + (phase - 1) + ": ");
                for(int i = 0; i < this.nodes.size(); i++){
                    if(this.nodes.get(i).isLeader()){
                        System.out.println("Node " + i + " is Leader.");
                    }else{
                        System.out.println("Node " + i + " is not Leader.");
                    }
                }

                if(this.electionComplete()){
                    this.isLeaderElected = true;
                }
                phase ++;
            }
        }
    }

    // Checks if our election procedure is finished. Counts the current declared leader nodes for each phase.
    public boolean electionComplete(){
        int counter = 0;
        for (Node e: this.nodes){
            if(e.isLeader()){
                counter ++;
            }
        }

        if( counter > 1 ){
            return false;
        }else{
            return true;
        }
    }

}
