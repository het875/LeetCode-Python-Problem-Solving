n = [2,3,6,7,9]  
m = [1,4,8,10,11]

k = 5

new = n + m
new.sort()

print("The K-th Elements is " ,new[k-1])

# Time Complexity: O(nlogn)
# Space Complexity: O(n+m)
# The above code is not optimal. We can solve this problem in O(logn) time complexity using binary search.
# The idea is to divide the arrays into two parts and compare the middle elements of the two arrays. If the middle element of the first array is less than the middle element of the second array, then the k-th element must be in the right half of the first array or the left half of the second array. Otherwise, the k-th element must be in the right half of the second array or the left half of the first array. We can keep dividing the arrays into two parts until we find the k-th element.
# Let's implement the above approach in code.

n = [2,3,6,7,9]
m = [1,4,8,10,11]

k = 5

def kth_element(n, m, k):
    if len(n) > len(m):
        n, m = m, n

    if not n:
        return m[k-1]

    if k == 1:
        return min(n[0], m[0])

    i = min(len(n), k//2)
    j = min(len(m), k//2)

    if n[i-1] < m[j-1]:
        return kth_element(n[i:], m, k-i)
    else:
        return kth_element(n, m[j:], k-j)

print("The K-th Elements is " ,kth_element(n, m, k))

