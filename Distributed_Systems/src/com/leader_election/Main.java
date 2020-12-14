package com.leader_election;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Main class for our semester project.
// In the first step, we choose the number of nodes we want to have in our distributed system.
// In the second step a menu is created. Each option will demonstrate the election algorithm of your choice.
public class Main {

    public static void main(String[] args) {

        System.out.print("Give the number on nodes you want your distributed system to have: ");
        Scanner scanner = new Scanner(System.in);
        int numberOfNodes = scanner.nextInt();
        List<Node> nodes = new ArrayList<>();

        for(int i = 0; i < numberOfNodes; i++){
          nodes.add(new Node());
        }

        boolean exit = false;

        while(!exit){
            System.out.println("Choose a leader election algorithm: ");
            System.out.println("1. LCR.");
            System.out.println("2. HS.");
            System.out.println("3. FloodMax.");
            System.out.println("4. Bully.");
            System.out.println("5. Exit.");

            System.out.println();
            System.out.print("Your option is: ");
            int choice = scanner.nextInt();

            switch (choice){
                case 1:
                    //--------------------------- LCR ----------------------------
                    LCR lcr = new LCR(numberOfNodes);
                    lcr.electLeader();
                    break;
                case 2:
                    //--------------------------- HS ------------------------------
                    HS hs = new HS(numberOfNodes);
                    hs.electLeader();
                    break;
                case 3:
                    //----------------------- FLOODMAX-----------------------------
                    FloodMax floodMax = new FloodMax(numberOfNodes);
                    floodMax.electLeader();
                    break;
                case 4:
                    //----------------------- BULLY ---------------------------
                    Bully bully = new Bully(numberOfNodes);
                    bully.syncMonitoring();
                    break;
                case 5:
                    System.out.println("System exited.");
                    exit = true;
                    break;
            }
        }







    }
}
