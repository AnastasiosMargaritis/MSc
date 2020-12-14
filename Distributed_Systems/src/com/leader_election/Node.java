package com.leader_election;

import java.util.UUID;

// Node class represents a node in our distributed system.
// Each node has 3 characteristics: a randomly generated UUID,
// an isLeader boolean value represents if a Node is leader of the distributed
// system or not and an isActivate boolean value represent if a current node is
// active or not.
public class Node {

    private UUID uuid;
    private boolean isLeader = false;
    private boolean isActive = true;

    public Node() {
        this.uuid = UUID.randomUUID();
    }

    public UUID getUuid() {
        return uuid;
    }

    public void setUuid(UUID uuid) {
        this.uuid = uuid;
    }

    public boolean isLeader() {
        return isLeader;
    }

    public void setLeader(boolean leader) {
        isLeader = leader;
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }
}
