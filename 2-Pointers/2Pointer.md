1) When we want to make comparisions between 2 or more elements, we would write a nested for loop. This is o(n^2). 
2) This approach doesnt take advantage of "Predictable dynamics". 
3) Predictable Dynamics is when we can predict the nature of the comparisions going to be had, like in a SORTED array the value to the right will always be equal or greater than the element to its left and so on. 

4) There are 3 main approach for 2 Pointer problems: 
    a) Inward traversal: The pointers start at opposite ends and move inwards to each other till they meet or cross over or a condition is met.
    b) Unidirectional traversal: The pointers start from the same end and move in same direction depending on condition met till condition is satisfied or till end of array. The right pointer tries to find information and the left tries to store the information generally.
    c) Staged traversal: In this we traverse with one pointer and when that pointer lands on an element that meets a certain condition the we traverse with the second pointer. The first pointer finds something and the second pointer is used to find additional information relation to the element found. They are generally in unidirectional also.

5) When to use 2 pointer approach: 
    a) When its a linear data strucuture 
    b) When its sorted and follows a predictable dynamic. 

6) POTENTIAL indicator for 2 pointer approach is when problem asks for a pair of values or a result that can be generated from a pair of values. 

7) Real world usecase: In memory compaction algorithm used in garbage collector. There are 2 pointers free and scan. The free pointer keeps track of the next avaialble space to where live objects should be relocated. The scan pointer skips over the dead objects and shifts live objects to the location pointed by the free pointer. This groups up live objects togehter and frees up continous blocks of memory. 

8) 

