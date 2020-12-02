package com.leader_election;

import java.util.UUID;

public class Node {

    private UUID uuid;
    private boolean isLeader = false;
    private static int leaderNode;

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
}
