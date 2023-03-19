import random
import time


def test_sort(v):
    for i in range(len(v)-1):
        if(v[i]>v[i+1]):
            return False
    return True

def merge_sort(v):
    if len(v)>1:
        n=len(v)
        mid=n//2
        L=v[:mid]
        R=v[mid:]
        merge_sort(L)
        merge_sort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                v[k]=L[i]
                i+=1
                k+=1
            else:
                v[k]=R[j]
                j+=1
                k+=1
        while i<len(L):
            v[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            v[k]=R[j]
            j+=1
            k+=1
        return(v)

def shell_sort(v):
    n=len(v)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            j=i
            t=v[i]
            while j>=gap and v[j-gap]>t:
                v[j-gap],v[j]=v[j],v[j-gap]
                j=j-gap
            v[j]=t
        gap=gap//2
    return(v)

def counting_sort(v):
    n=max(v)+1
    v2=[0]*n
    for i in range(len(v)):
        nr=v[i]
        v2[nr]+=1
    k=0
    for i in range(n):
        while v2[i]>0:
            v[k]=i
            v2[i]=v2[i]-1
            k+=1
    return(v)

def quick_sort(v):
    n=len(v)
    if n<2:
        return v
    j=0
    for i in range(1,n):
        if v[i]<=v[0]:
            j+=1
            v[i],v[j]=v[j],v[i]
    v[0],v[j]=v[j],v[0]

    L=quick_sort(v[0:j])
    R=quick_sort(v[j+1:n])
    v=L+[v[j]]+R
    return(v)


def radix_sort(v):
    m=1
    n=max(v)
    k=0
    while(n>0):
        n=n//10
        k+=1
    buckets=[[]for i in range(10)]
    while(k>0):
        k-=1
        for i in v:
            d=(i//m)%10
            buckets[d].append(i)
        k2=0
        for i in range(10):
            while(len(buckets[i])>0):
                    v[k2]=buckets[i][0]
                    buckets[i].pop(0)
                    k2+=1
        m=m*10
    return(v)



def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def tim_sort(arr):
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array
        size *= 2
    return arr

f=open("tests.txt")
t=int(f.readline())
tests=[]
for i in range(t):
    n,Max=map(int,f.readline().split())
    t_random=[random.randint(0,Max) for i in range(n)]
    tests.append(t_random)


d = {"shell_sort":shell_sort,"quick_sort":quick_sort,"merge_sort":merge_sort,"radix_sort":radix_sort,"counting_sort":counting_sort,"timsort":tim_sort}
sorts=["shell_sort","quick_sort","merge_sort","radix_sort","counting_sort","timsort"]
for test in tests:
    print("n="+str(len(test)))
    print("Max="+str(max(test)))
    for sort in sorts:
        try:
            sort_function = d[sort]
            start_time = time.time()
            sorted_list = sort_function(test)
            end_time = time.time()
            run_time = end_time - start_time
            test_Sort= test_sort(test)
            print(sort + " timp sortare: " + str(run_time) + " secunde" + " test_Sort=" + str(test_Sort))
        except:
            print(sort + " nu poate sorta pentru o lista cu " + str(len(test)) + " elemente.")
