def swap(a, i, j):
  a[i], a[j] = a[j], a[i]
  
def is_heap(a):
  n = 0
  m = 0
  while True:
    for i in [0, 1]:
      m += 1
      if m >= len(a):
        return True
      if a[m] > a[n]:
        return False
    n += 1
    
def sift_down(a, n, max):
  while True:
    biggest = n
    c1 = 2*n + 1
    c2 = c1 + 1
    for c in [c1, c2]:
      if c < max and a[c] > a[biggest]:
        biggest = c
    if biggest == n:
      return
    swap(a, n, biggest)
    n = biggest

def heapify(a):
  i = int(len(a)-1 / 2)
  max = len(a)
  while i >= 0:
    sift_down(a, i, max)
    i -= 1

def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j > 0:
    swap(a, 0, j)
    sift_down(a, 0, j)
    j -= 1

a = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print (a)
heapsort(a)
print (a)

