package com.simulation;

import java.util.Scanner;

public class Simulation {

    public static int Q_LIMIT = 1000;
    public static int BUSY = 1;
    public static int IDLE = 0;

    public static int next_event_type, num_progs_delayed, num_delays_required, num_events, num_in_q, server_status;
    public static double seed1, seed2, yy1, yy2, yy;
    public static double area_num_in_q, area_server_status, mean_interarrival, mean_service, time, time_last_event, total_of_delays;
    public static double[] time_arrival = new double[Q_LIMIT + 1];
    public static double[] time_next_event = new double[3];

    public static void main(String[] args) {

        /* Specify the number of events for the timing function. */
        num_events = 2;
        seed1 = 99275.0;
        seed2 = 48612.0;

        mean_interarrival = 5;
        mean_service = 1;
        num_delays_required = 1000;

        /* Initialize the simulation. */
        initialize();

        /* Run the simulation while more delays are still needed. */
        while (num_progs_delayed < num_delays_required) {
            /* Determine the next event. */
            timing();

            /* Update time-average statistical accumulators. */
            update_time_avg_stats();

            /* Invoke the appropriate event function. */
            switch (next_event_type) {
                case 1:
                    arrive();
                    break;
                case 2:
                    depart();
                    break;
            }
        }

        /* Invoke the report generator and end the simulation. */
        report();

    }

    public static void initialize(){

        /* Initialize the simulation clock. */
        time = 0.0;

        yy1 = seed1;
        yy2 = seed2;

        /* Initialize the state variables. */
        server_status = IDLE;
        num_in_q = 0;
        time_last_event = 0.0;

        /* Initialize the statistical counters. */
        num_progs_delayed = 0;
        total_of_delays = 0.0;
        area_num_in_q = 0.0;
        area_server_status = 0.0;

        /* Initialize event list. */
        time_next_event[1] = time + expon(mean_interarrival, yy1);
        yy1=yy;
        time_next_event[2] = 1.0e+30;
    }

    public static void timing(){
        int i;
        double min_time_next_event;

        min_time_next_event = 1.0e+29;
        next_event_type = 0;

        /* Determine the event type of the next event to occur. */
        for (i = 1; i <= num_events; ++i) {
            if (time_next_event[i] < min_time_next_event) {
                min_time_next_event = time_next_event[i];
                next_event_type = i;
            }
        }

        /* Check to see whether the event list is empty. */
        if (next_event_type == 0) {
            /* The event list is empty, so stop the simulation. */
            System.out.println("Event list empty at timeL " + time);
        }

        /* The event list is not empty, so advance the simulation clock. */
        time = min_time_next_event;
    }

    public static void update_time_avg_stats(){

        double time_since_last_event;

        /* Compute time since last event, and update last-event-time marker. */
        time_since_last_event = time - time_last_event;
        time_last_event = time;

        /* Update area under number-in-queue function. */
        area_num_in_q += num_in_q * time_since_last_event;

        /* Update area under server-busy indicator function. */
        area_server_status += server_status * time_since_last_event;

    }

    public static void arrive() {
        /* Schedule next arrival. */
        time_next_event[1] = time + expon(mean_interarrival, yy1);
        yy1=yy;

        /* Check to see whether server is busy. */
        if (server_status == BUSY) {
            /* Server is busy, so increment number of customers in queue. */
            ++num_in_q;

            /* Check to see whether an overflow condition exists. */
            if (num_in_q > Q_LIMIT) {
                /* The queue has overflowed, so stop the simulation. */
                System.out.println("Overflow of the array time_arrival at: " + time);
            }

            /* There is still room in the queue */
            time_arrival[num_in_q] = time;
        }else {
            /* Server is idle, so arriving customer has a delay of zero. */
        /* Increment the number of customers delayed, and make server
        busy. */
            ++num_progs_delayed;
            server_status = BUSY;

            /* Schedule a departure (service completion). */
            time_next_event[2] = time + expon(mean_service, yy2);
            yy2=yy;
        }
    }

    public static void depart(){
        int i;
        double delay;

        /* Check to see whether the queue is empty. */
        if (num_in_q == 0) {
        /* The queue is empty so make the server idle and eliminate the
        departure (service completion) event from consideration. */
            server_status = IDLE;
            time_next_event[2] = 1.0e+30;
        }
        else {
        /* The queue is nonempty, so decrement the number of customers
        in queue. */
            --num_in_q;

        /* Compute the delay of the customer who is beginning service
        nd update the total delay accumulator. */

            delay = time - time_arrival[1];
            total_of_delays += delay;

        /* Increment the number of customers delayed, and schedule
        departure. */
            ++num_progs_delayed;
            time_next_event[2] = time + expon(mean_service, yy2);
            yy2=yy;

            /* Move each customer in queue (if any) up one place. */
            for (i = 1; i <= num_in_q; ++i)
                time_arrival[i] = time_arrival[i + 1];
        }
    }

    public static void report(){
        System.out.println("Average delay in queue: " + total_of_delays / num_progs_delayed + " minutes.");
        System.out.println("Average number in queue: " + area_num_in_q / time);
        System.out.println("Server utilization: " + area_server_status / time);
        System.out.println("Time simulation ended: " + time + " minutes.");
    }

    public static double random1(double ygen){
        double A = 455470314.0, B = 2147483647.0;
        double r;
        ygen = A * ygen;
        ygen = ygen % B;
        r = ygen / B;
        yy = ygen;
        return r;
    }

    public static double expon(double mean, double ygen){

        double U = random1(ygen);
        return -mean * Math.log(U);
    }
}
