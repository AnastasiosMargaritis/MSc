package com.leader_election;

import java.util.ArrayList;
import java.util.List;

public class HS {

    private List<Node> nodes = new ArrayList<>();
    private boolean isLeaderElected = false;

    public HS(int bound) {

        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
            this.nodes.get(i).setLeader(true);
        }
    }

    public HS(List<Node> nodes){
        this.nodes = nodes;
        for(int i = 0; i < this.nodes.size(); i++){
            this.nodes.get(i).setLeader(true);
        }
    }

    public void setNodes(List<Node> nodes) {
        this.nodes = nodes;
    }

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
