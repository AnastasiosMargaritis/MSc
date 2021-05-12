/* Single-Server Queueing System. */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define Q_LIMIT 100
#define BUSY 1
#define IDLE 0

int next_event_type, num_progs_delayed, num_delays_required,
num_events, num_in_q, server_status;
double seed1, seed2, yy1, yy2, yy;
float area_num_in_q, area_server_status, mean_interarrival,
mean_service, time, time_last_event, total_of_delays,
time_arrival[Q_LIMIT + 1], time_next_event[3];

FILE *infile, *outfile;

void initialize(void);
void timing(void);
void arrive(void);
void depart(void);
void report(void);
void update_time_avg_stats(void);
double random1(double ygen);
double expon(float mean,double ygen);

int main()
/* Main function. */
{
    /* Open input and output files. */
    infile = fopen("mm1.in", "r");
    outfile = fopen("mm1.out", "w");

    /* Specify the number of events for the timing function. */
    num_events = 2;
    seed1 = 99275.0;
    seed2 = 48612.0;

    /* Read input parameters. */
    fscanf(infile, "%f %f %d", &mean_interarrival, &mean_service,
    &num_delays_required);

    /* Write report heading and input parameters. */
    fprintf(outfile, "Single-server queueing system\n\n");
    fprintf(outfile, "Mean interarrival time%11.3f minutes\n\n",
    mean_interarrival);
    fprintf(outfile, "Mean service time%16.3f minutes\n\n",
    mean_service);
    fprintf(outfile, "Number of customers%14d\n\n",
    num_delays_required);

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
    fclose(infile);
    fclose(outfile);
    return 0;
}

void initialize(void)
/* Initialization function. */
{
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

void timing(void)
/* Timing function. */
{
    int i;
    float min_time_next_event;

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
        fprintf(outfile, "\nEvent list empty at time %f", time);
        exit(1);
    }

    /* The event list is not empty, so advance the simulation clock. */
    time = min_time_next_event;
}

void arrive(void)
/* Arrival event function. */
{
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
            fprintf(outfile, "\nOverflow of the array time_arrival at");
            fprintf(outfile, " time %f", time);
            exit(2);
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

void depart(void)
/* Departure event function. */
{
    int i;
    float delay;

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

void report(void)
/* Report generator function. */
{
    /* Compute and write estimates of desired measures of performance.*/
    fprintf(outfile, "\n\nAverage delay in queue%11.3f minutes\n\n",
    total_of_delays / num_progs_delayed);
    fprintf(outfile, "Average number in queue%10.3f\n\n",
    area_num_in_q / time);
    fprintf(outfile, "Server utilization%15.3f\n\n",
    area_server_status / time);
    fprintf(outfile, "Time simulation ended%12.3f minutes", time);
}

void update_time_avg_stats(void)
/* Update area accumulators for time-average statistics. */
{
    float time_since_last_event;

    /* Compute time since last event, and update last-event-time marker. */
    time_since_last_event = time - time_last_event;
    time_last_event = time;

    /* Update area under number-in-queue function. */
    area_num_in_q += num_in_q * time_since_last_event;

    /* Update area under server-busy indicator function. */
    area_server_status += server_status * time_since_last_event;
}

double random1(double ygen)
/* Random number generator*/
{
    const double A = 455470314.0, B = 2147483647.0;
    double r;
    ygen = A * ygen;
    ygen = fmod(ygen, B);
    r = ygen / B;
    yy = ygen;
    return r;
}

double expon(float mean, double ygen)
/* Exponential variate generation function. */
{
    double U;

    /* Generate a U(0,1) random variate. */
    U = random1(ygen);

    /* Return an exponential random variate with mean "mean". */
    return -mean * log(U);
}
