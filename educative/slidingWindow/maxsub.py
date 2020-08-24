"""
time: 5 min
error: 
  maxSum, total, j = 0
  if i - j == k:

"""

def max_sub_array_of_size_k(k, arr):
  maxSum, total, j = 0, 0 ,0
  for i, n in enumerate(arr):
    total += n

    if i - j == k-1:
      maxSum = max(total, maxSum)
      total -= arr[j]
      j += 1

  return maxSum
