package com.leader_election;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        int numberOfNodes = 20;
        List<Node> nodes = new ArrayList<>();
        for(int i = 0; i < numberOfNodes; i++){
          nodes.add(new Node());
        }
//--------------------------- LCR ----------------------------
        LCR lcr = new LCR(numberOfNodes);
        lcr.setNodes(nodes);
        lcr.electLeader();

//-------------------------- HS ------------------------------

        HS hs = new HS(nodes);
        hs.electLeader();

    }
}
