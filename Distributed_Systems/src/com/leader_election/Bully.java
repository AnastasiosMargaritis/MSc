package com.leader_election;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.UUID;

public class Bully {

    private List<Node> nodes = new ArrayList<>();
    private boolean leaderElected = false;

    public Bully(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
        }
    }

    public void setNodes(List<Node> nodes) {
        this.nodes = nodes;
    }

    public void election(){

        UUID maxUUID = UUID.randomUUID();

        for(Node node: nodes){
            if(node.isActive()){
                maxUUID = node.getUuid();
                break;
            }
        }

        for(Node node: nodes){
            if(node.isActive() && node.getUuid().compareTo(maxUUID) > 0){
                maxUUID = node.getUuid();
            }
        }

        int counter = 0;

        for(Node node: this.nodes){
            if(node.getUuid().compareTo(maxUUID) == 0 && node.isActive()){
                node.setLeader(true);
                break;
            }
            counter ++;
        }

        int index = 0;
        for(Node node: this.nodes){
            if(!node.isActive()){
                System.out.println("Node " + index + " is de-activated.");
            }
            else if(node.getUuid().compareTo(maxUUID) == 0 && node.isActive()){
                System.out.println("Node " + counter + " is the Leader.");
            }else{
                System.out.println("Node " + index + " knows that the leader is node " + counter + ".");
            }
            index++;
        }
        System.out.println();
    }

    public void syncMonitoring(){
        this.election();
        boolean exit = false;


        while(!exit){
            System.out.println("Bully Algorithm Options: ");
            System.out.println("1. De-Activate Leader.");
            System.out.println("2. Re-Activate Leader.");
            System.out.println("3. Exit.");
            Scanner scanner = new Scanner(System.in);
            System.out.print("Your option is: ");
            int choice = scanner.nextInt();

            switch (choice){
                case 1:
                    for(Node node: nodes){
                        if(node.isLeader()){
                            node.setActive(false);
                        }
                    }
                    this.election();
                    break;
                case 2:
                    for(Node node: nodes){
                        node.setActive(true);
                    }
                    this.election();
                    break;
                case 3:
                    System.out.println("Bully Algorithm terminated.");
                    exit = true;
                    break;
            }
        }
    }
}
