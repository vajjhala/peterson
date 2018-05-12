## Formal Verification of Peterson's Algorithm

#### The Problem
===========

In a distributed program, a number of different components are
simultaneously executed, but the critical section is only accessible to
one component at a time. The problem is to find a *protocol* to allow
only one of the competing components access to the critical section.
Peterson's mutual exclusion algorithm is one of the many algorithms that
solves this problem.

The properties we need to check for are:

1.  **Safety**: Only one process is in the critical section at any time.

2.  **Liveness**: Every requesting process must eventually get access to
    the critical section.


###### More details in report/report.pdf


