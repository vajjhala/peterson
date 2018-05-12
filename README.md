## Formal Verification of Peterson's ALgorithm

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

#### Approach 
========

I will start with the primitive algorithm for mutual exclusion, which is
the the Safe Sluice algorithm, show how it fails to address deadlock,
then extract the Petersonâs algorithm from the *safety* condition. The
algorithm I will be arguing about will be a variant of the Petersonâs
algorithm that synchronises only two components, but the general version
extends this to n components. At the end of the report I have presented
the pseudo-code for the **N**-component variant without proof. It is
this version that I have implemented.

###### More details in report/report.pdf


