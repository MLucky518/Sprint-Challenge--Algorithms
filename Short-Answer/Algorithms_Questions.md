# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): # O(n)
      a = a + n * n #O(n)
      
      # O(n) + O(n) -- drop constant == O(n) LINEAR 
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


I would start by cutting n in half throwing an egg off of that floor which would be in the middle. If the egg breaks then i know the answer is underneath me so i can set my new top story to the halfway point and divide again to checkif an egg breaks and using that to determine whether i am going down a floor or up. if the initial egg does not break i would set my new halfway point by setting my new start point to the prior halfway point dividing by 2 again to find the new middle each time Because i am halving n each time i am expecting my algorithim to perform at O(logn) complexity 