# Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a list (`list = []`). You can perform the following commands:   

1. `insert i e`: Insert integer $e$ at position $i$.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer $e$.
4. `append e`: Insert integer $e$ at the end of the list.  
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of the $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.  

**Example**  
$N = 4$  
$\text{append 1}$  
$\text{append 2}$  
$\text{insert 1 3}$  
$\text{print}$   
</br >
</br >
   
- $\text{append 1}$: Append $1$ to the list, $arr = [1]$.  
- $\text{append 2}$: Append $2$ to the list, $arr = [1, 2]$.  
- $\text{insert 1 3}$: Insert $3$ at index $1$, $arr = [1, 3, 2]$.  
- $\text{print}$: Print the array.  
</br >
Output:
<pre>
[1, 3, 2]
</pre>

**Input Format**

The first line contains an integer, $n$, denoting the number of commands.	
Each line $i$ of the $n$ subsequent lines contains one of the commands described above.


**Constraints**

- The elements added to the list must be *integers*.

**Output Format**

For each command of type `print`, print the list on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T15:33:49.225Z  

```py
if __name__ == '__main__':
    N = int(input())
    my_list = []

    for i in range(N):
        command = input().split()

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-lists/problem)