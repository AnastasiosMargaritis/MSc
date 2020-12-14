package com.leader_election;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.UUID;

public class Bully {

    private List<Node> nodes = new ArrayList<>();
    private boolean leaderElected = false;

//    Constructor of Bully class. Accepts as arguments the number of nodes
//    and created a List of nodes.
    public Bully(int bound) {
        for(int i = 0; i < bound; i++){
            this.nodes.add(new Node());
        }
    }

    public void setNodes(List<Node> nodes) {
        this.nodes = nodes;
    }

//    Leader election for Bully Algorithm class. Each time it is called,
//    elects leader the node which is currently active and has the max UUID.
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

//    Real time representation of synchronous behavior of Bully Algorithm.
//    A menu of 3 options is presented. In each step we can De-Activate the current leader node,
//    reactivate all nodes or eti the menu. When we either de-activate or reactivate nodes
//    leader election is executed.
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
