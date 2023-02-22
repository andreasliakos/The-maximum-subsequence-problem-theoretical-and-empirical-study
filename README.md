# The-maximum-subsequence-problem-theoretical-and-empirical-study

1 Introduction

The maximum subarray problem is a problem in which a sequence of values (negative,
positive or zero) is given a sequence of values (negative, positive or zero) and the problem is to
find the continuous sequence of values in the sequence that gives the largest possible sum. In
this paper, the algorithmic investigation of the problem is requested. In addition, it is
requested to implement algorithms for solving the problem with different computational
complexity, to write down and present the execution times.

2 Problem description

Let A be a sequence A with n integers. The maximum subsequence problem asks for the
identification of the indices i and j with 1 ≤ i ≤ j ≤ n for which the sum  ∑j
x=i A[x].

2.1 Simplistic way of solving

A simple way to compute the maximum subsequence is using 3 nested iteration loops and
an adder

2.2 Improved maximum subsequence algorithm

The previous method "wastes" time as it recalculates all the sub-column sums. The
algorithm can be improved by computing in advance all the propositional sums of the
sequence, which are all sums of t integers of A for t = 1, 2, ..., n. Given the propositional sums,
we can compute the sum of any subsequence by performing subtraction between two already
computed values of propositional sums.

2.3 Kadane's algorithm

The basic idea of Kadane's algorithm is that it computes maximum aggressive sums, i.e. it
creates a sequence whose each element at position t contains the maximum sub-sum among
all subsequences ending at t. If the computed value is negative then it is replaced by zero.
