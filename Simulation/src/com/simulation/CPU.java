package com.simulation;

public class CPU {

    private float serviceTime;
    private boolean isBusy = false;

    public CPU(float serviceTime) {
        this.serviceTime = serviceTime;
    }

    public float getServiceTime() {
        return serviceTime;
    }

    public void setServiceTime(float serviceTime) {
        this.serviceTime = serviceTime;
    }

    public boolean isBusy() {
        return isBusy;
    }

    public void setBusy(boolean busy) {
        isBusy = busy;
    }
}
