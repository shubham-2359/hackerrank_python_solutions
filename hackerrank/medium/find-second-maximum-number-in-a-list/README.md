# Find the Runner-Up Score!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given $n$ scores. Store them in a list and find the score of the runner-up. 




**Input Format**

The first line contains $n$. The second line contains an array $A[$ $]$ of $n$ integers each separated by a space.  



**Constraints**

+ $2 \le n \le 10$  
+ $-100 \le A[i] \le 100$



**Output Format**

Print the runner-up score.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T07:34:41.419Z  

```py
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    scores = list(set(scores))
    scores.sort()

    print(scores[-2])

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)