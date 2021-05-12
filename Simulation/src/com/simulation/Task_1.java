package com.simulation;

import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Task_1 {

    public static int Q_LIMIT = 100000000;
    public static int BUSY = 1;
    public static int IDLE = 0;

    public static int next_event_type, num_progs_delayed_1, num_progs_delayed_2, num_progs_delayed, num_delays_required, num_events, num_in_q_1, num_in_q_2, server_status_1, server_status_2, counter_arr_1, counter_arr_2, counter_dep_1, counter_dep_2;
    public static double seed1, seed2, yy1, yy2, yy;
    public static double area_num_in_q_1, area_num_in_q_2, area_server_status_1, area_server_status_2, mean_interarrival, mean_service_1, mean_service_2, time, time_last_event, total_of_delays_1, total_of_delays_2, mean_response_time;
    public static double[] time_arrival_1 = new double[Q_LIMIT + 1];
    public static double[] time_arrival_2 = new double[Q_LIMIT + 1];
    public static double[] time_next_event = new double[4];

    public static void main(String[] args) {

        /* Specify the number of events for the timing function. */
        num_events = 3;
        seed1 = 99275.0;
        seed2 = 48612.0;

        mean_interarrival = 1;
        mean_service_1 = 2;
        mean_service_2 = 1;
        num_delays_required = 40000;

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
                    depart_1();
                    counter_dep_1++;
                    mean_response_time += time;
                    break;
                case 3:
                    depart_2();
                    counter_dep_2++;
                    mean_response_time += time;
                    break;
            }
        }

        /* Invoke the report generator and end the simulation. */
        report();
        System.out.println("Arrival 1: " + counter_arr_1);
        System.out.println("Departs 1: " + counter_dep_1);
        System.out.println("Arrival 2: " + counter_arr_2);
        System.out.println("Departs 2: " + counter_dep_2);
    }

    public static void initialize(){

        /* Initialize the simulation clock. */
        time = 0.0;

        yy1 = seed1;
        yy2 = seed2;

        /* Initialize the state variables. */
        server_status_1 = IDLE;
        server_status_2 = IDLE;
        num_in_q_1 = 0;
        num_in_q_2 = 0;
        time_last_event = 0.0;

        /* Initialize the statistical counters. */
        num_progs_delayed = 0;
        total_of_delays_1 = 0.0;
        total_of_delays_2 = 0.0;
        area_num_in_q_1 = 0.0;
        area_num_in_q_2 = 0.0;
        area_server_status_1 = 0.0;
        area_server_status_2 = 0.0;
        counter_dep_1 = 0;
        counter_dep_2 = 0;
        counter_arr_1 = 0;
        counter_arr_2 = 0;
        mean_response_time = 0;

        /* Initialize event list. */
        time_next_event[1] = time + ThreadLocalRandom.current().nextDouble(0.8, 1.2);
        System.out.println(time_next_event[1]);
        time_next_event[2] = 1e+30;
        System.out.println(time_next_event[2]);
        yy1 = yy;
        time_next_event[3] = 1e+30;
        System.out.println(time_next_event[3]);
        yy2 = yy;
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
        area_num_in_q_1 += num_in_q_1 * time_since_last_event;
        area_num_in_q_2 += num_in_q_2 * time_since_last_event;

        /* Update area under server-busy indicator function. */
        area_server_status_1 += server_status_1 * time_since_last_event;
        area_server_status_2 += server_status_2 * time_since_last_event;

    }

    public static void arrive() {

        Random random = new Random();
        double prob = random.nextDouble();

        if(prob <= 0.65){
            counter_arr_1++;
            /* Schedule next arrival. */
            time_next_event[1] = time + ThreadLocalRandom.current().nextDouble(0.8, 1.2);

            /* Check to see whether server is busy. */
            if (server_status_1 == BUSY) {
                /* Server is busy, so increment number of customers in queue. */
                ++num_in_q_1;

                /* Check to see whether an overflow condition exists. */
                if (num_in_q_1 > Q_LIMIT) {
                    /* The queue has overflowed, so stop the simulation. */
                    System.out.println("Overflow of the array time_arrival at: " + time);
                }

                /* There is still room in the queue */
                time_arrival_1[num_in_q_1] = time;
            }else {
                counter_arr_2++;
                /* Server is idle, so arriving customer has a delay of zero. */
             /* Increment the number of customers delayed, and make server
             busy. */
                ++num_progs_delayed;
                ++num_progs_delayed_1;
                server_status_1 = BUSY;

                /* Schedule a departure (service completion). */
                time_next_event[2] = time + expon(mean_service_1, yy1);
                yy1=yy;
            }
        }else{
            /* Schedule next arrival. */
            time_next_event[1] = time + ThreadLocalRandom.current().nextDouble(0.8, 1.2);

            /* Check to see whether server is busy. */
            if (server_status_2 == BUSY) {
                /* Server is busy, so increment number of customers in queue. */
                ++num_in_q_2;

                /* Check to see whether an overflow condition exists. */
                if (num_in_q_2 > Q_LIMIT) {
                    /* The queue has overflowed, so stop the simulation. */
                    System.out.println("Overflow of the array time_arrival at: " + time);
                }

                /* There is still room in the queue */
                time_arrival_1[num_in_q_2] = time;
            }else {
                /* Server is idle, so arriving customer has a delay of zero. */
             /* Increment the number of customers delayed, and make server
             busy. */
                ++num_progs_delayed;
                ++num_progs_delayed_2;
                server_status_2 = BUSY;

                /* Schedule a departure (service completion). */
                time_next_event[3] = time + expon(mean_service_2, yy2);
                yy2=yy;
            }
        }

    }

    public static void depart_1(){
        int i;
        double delay;

        /* Check to see whether the queue is empty. */
        if (num_in_q_1 == 0) {
        /* The queue is empty so make the server idle and eliminate the
        departure (service completion) event from consideration. */
            server_status_1 = IDLE;
            time_next_event[2] = 1.0e+30;
        }
        else {
        /* The queue is nonempty, so decrement the number of customers
        in queue. */
            --num_in_q_1;

        /* Compute the delay of the customer who is beginning service
        nd update the total delay accumulator. */

            delay = time - time_arrival_1[1];
            total_of_delays_1 += delay;

        /* Increment the number of customers delayed, and schedule
        departure. */
            ++num_progs_delayed;
            time_next_event[2] = time + expon(mean_service_1, yy1);
            yy1=yy;

            /* Move each customer in queue (if any) up one place. */
            for (i = 1; i <= num_in_q_1; ++i)
                time_arrival_1[i] = time_arrival_1[i + 1];
        }
    }

    public static void depart_2(){
        int i;
        double delay;

        /* Check to see whether the queue is empty. */
        if (num_in_q_2 == 0) {
        /* The queue is empty so make the server idle and eliminate the
        departure (service completion) event from consideration. */
            server_status_2 = IDLE;
            time_next_event[2] = 1.0e+30;
        }
        else {
        /* The queue is nonempty, so decrement the number of customers
        in queue. */
            --num_in_q_2;

        /* Compute the delay of the customer who is beginning service
        nd update the total delay accumulator. */

            delay = time - time_arrival_2[1];
            total_of_delays_2 += delay;

        /* Increment the number of customers delayed, and schedule
        departure. */
            ++num_progs_delayed;
            time_next_event[2] = time + expon(mean_service_2, yy2);
            yy2=yy;

            /* Move each customer in queue (if any) up one place. */
            for (i = 1; i <= num_in_q_2; ++i)
                time_arrival_2[i] = time_arrival_2[i + 1];
        }
    }

    public static void report(){
        System.out.println("Mean response time: " + mean_response_time / num_delays_required + " minutes.");
        System.out.println("Average jobs in system: " + ((area_num_in_q_1 + area_num_in_q_2)/2) / time);
        System.out.println("Average delay in queue 1: " + total_of_delays_1 / num_progs_delayed_1 + " minutes.");
        System.out.println("Average delay in queue 2: " + total_of_delays_2 / num_progs_delayed_2 + " minutes.");
        System.out.println("Average jobs in queue 1: " + area_num_in_q_1 / time);
        System.out.println("Average jobs in queue 2: " + area_num_in_q_2 / time);
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