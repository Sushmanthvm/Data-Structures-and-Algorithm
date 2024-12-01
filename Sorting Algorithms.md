

# Notes for Data Structures

  

## Sorting Algorithms
- [x] Selection Sort
- [x] Bubble Sort
- [x] Insertion Sort 
- [ ] Quick Sort
- [ ] Merge Sort

### 1.Selection Sort
> :memo: **Note:**  Select the ***minimum element*** and ***swap*** .

**Example :**
| **Step** | **Array State**           | **Comparison Range** |
|----------|----------------------------|-----------------------|
| Step 1   | ***9***, 46, 24, 52, 20, ***13*** | 0 → N-1              |
| Step 2   | 9, ***13***, 24, 52, 20, ***46*** | 1 → N-1              |
| Step 3   | 9, 13, ***20***, 52, ***24***, 46 | 2 → N-1              |
| Step 4   | 9, 13, 20, ***24***, ***52***, 46 | 3 → N-1              |
| Step 5   | 9, 13, 20, 24, ***46***, ***52*** | 4 → N-1              |


```Python
 def selectionSort(self, arr):
	#code here
	for i in range(0,len(arr)-1):
	    mini=i
	    for j in range(i,len(arr)):
	        if arr[mini]>arr[j]:
	            mini=j
	    
	    temp = arr[mini]
	    arr[mini]=arr[i]
	    arr[i]=temp

	return arr
```
>  :memo: **Time complexity** for the algorithm : O(n^2^)
---
### 2. Bubble Sort
> :memo: **Note:** Push the ***maximum element*** to the last by ***adjacent swapping***

**Example :**

Initial Array:  
| 13 |  46 |  24 |  50 |  20 |  9 |
|----|-----|-----|-----|-----|----|
<br>      

| **Pass** | **Array State**       | **Comparison Range in each pass** |
|----------|-----------------------|----------------------|
| Pass 1   | 13, 24, 46, 20, 9, ***52*** | 0 → N-1              |
| Pass 2   | 13, 24, 20, 9, ***46***, ***52***| 0 → N-2              |
| Pass 3   | 13, 20, 9, ***24***, ***46***, ***52***| 0 → N-3              |
| Pass 4   | 13, 9, ***20***, ***24***, ***46***, ***52***| 0 → N-4              |
| Pass 5   | 9, ***13***, ***20***, ***24***, ***46***, ***52***| 0 → N-5              |          


---

**Pass 1:**  
| Step | Compare       | Action         | Result               |
|------|---------------|----------------|----------------------|
| 1    | 13 and 46     | No Swap        | 13, 46, 24, 50, 20, 9 |
| 2    | 46 and 24     | Swap           | 13, ***24***, ***46***, 50, 20, 9 |
| 3    | 46 and 50     | No Swap        | 13, 24, 46, 50, 20, 9 |
| 4    | 50 and 20     | Swap           | 13, 24, 46, ***20***, ***50***, 9 |
| 5    | 50 and 9      | Swap           | 13, 24, 46, 20, ***9***, ***50*** |

---

**Pass 2:**
| Step | Compare       | Action         | Result               |
|------|---------------|----------------|----------------------|
| 1    | 13 and 24     | No Swap        | 13, 24, 46, 20, 9, 50 |
| 2    | 24 and 46     | No Swap        | 13, 24, 46, 20, 9, 50 |
| 3    | 46 and 20     | Swap           | 13, 24, ***20***, ***46***, 9, 50 |
| 4    | 46 and 9      | Swap           | 13, 24, 20, ***9***, ***46***, 50 |


---

**Pass 3:**
| Step | Compare       | Action         | Result               |
|------|---------------|----------------|----------------------|
| 1    | 13 and 24     | No Swap        | 13, 24, 20, 9, 46, 50 |
| 2    | 24 and 20     | Swap           | 13, ***20***, ***24***, 9, 46, 50 |
| 3    | 24 and 9      | Swap           | 13, 20, ***9***, ***24***, 46, 50 |

---

**Pass 4:**
| Step | Compare       | Action         | Result               |
|------|---------------|----------------|----------------------|
| 1    | 13 and 20     | No Swap        | 13, 20, 9, 24, 46, 50 |
| 2    | 20 and 9      | Swap           | 13, ***9***, ***20***, 24, 46, 50 |

---
**Pass 5:**
| Step | Compare       | Action         | Result               |
|------|---------------|----------------|----------------------|
| 1    | 13 and 9      | Swap           | ***9***, ***13***, 20, 24, 46, 50 |

---

**Final Sorted Array:**  
| 9 | 13 | 20 | 24 | 46 | 50 |
|---|----|----|----|----|----|

**Code:**
```Python 3.10
def bubbleSort(self,arr):
	# code here
	for i in range(len(arr)-1,-1,-1): #for(int i = n-1;i>=0;i--)
	   for j in range(0,i):			#for(int j =0; j<=i-1;j++)
	       if arr[j]>arr[j+1]:
	           temp = arr[j]
	           arr[j]=arr[j+1]
	           arr[j+1]=temp
	return arr
```
> :bulb: **Note** that after one complete round of adjacent swapping the maximum sits in it's place so in the second for loop we iterate till the i-1 ---> n-1-1, n-2-1, n-3-1,.....   and first for loop till n-1 ---> 0 **don't forget this babe**

 >  :memo: **Time complexity** for the algorithm : O(n^2^)
---
### 3.Insertion Sort
> :memo: **Note:** Takes an element and place it in it's correct position

**Example:**
Initial Array:
| 13 | 46 | 24 | 50 | 20 | 9 |
|----|-----|-----|----|-----|---|
<br>

| **Step** | **Array State**             | **Action**                                             |
|----------|------------------------------|---------------------------|
| Initial  | [ 13, 46, 24, 50, 20, 9 ]   | Start with the first element (13), it's already sorted. |
| Step 1   | [ 13, 46, 24, 50, 20, 9 ]   | 46 is already in its correct position.                |
| Step 2   | [ 13, ***24***, 46, 50, 20, 9 ]   | Insert 24 into its correct position (swap with 46).   |
| Step 3   | [ 13, 24, 46, 50, 20, 9 ]   | 50 is already in its correct position.                |
| Step 4   | [ 13, ***20***, 24, 46, 50, 9 ]   | Insert 20 into its correct position (swap with 24, 46). |
| Step 5   | [ ***9***, 13, 20, 24, 46, 50 ]   | Insert 9 into its correct position (swap with all elements before it). |

---
**Final Sorted Array:** 
| 9 | 13 | 20 | 24 | 46 | 50 |
|---|----|-----|----|-----|---| 

**Code:**
```Python 3.10
def insertionSort(self, arr):
	#code here
	for i in range(0,len(arr)):
	    j=i
	    while j>0 and arr[j-1]>arr[j]:
	        temp = arr[j-1]
	        arr[j-1]=arr[j]
	        arr[j]=temp
	        j-=1
	return arr

```
 >  :memo: **Time complexity** for the algorithm : O(n^2^)




  

