import random
def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    begin = start+1
    end = stop-1
    while begin <= end:
        while begin <= end and  not pivot < seq[begin]:
            begin += 1
        while begin <= end and pivot < seq[end]:
            end -= 1
        if begin < end:
            tmp =seq[begin]
            seq[begin] = seq[end]
            seq[end] = tmp
            begin += 1
            end -= 1
    seq[pivotIndex] = seq[end]
    seq[end] = pivot
    return end

def quicksortRecursive(seq,start,stop):
    if start >= stop-1:
        return
    pivotIndex = partition(seq,start,stop)
    quicksortRecursive(seq,start,pivotIndex)
    quicksortRecursive(seq,pivotIndex+1,stop)

def quicksort(seq):
    random.shuffle(seq)
    quicksortRecursive(seq,0,len(seq))

if __name__ == "__main__":
    a = [4,6,2,1,5]
    quicksort(a)
    print(a)
    a = [4,2,3,2,7,7,8,9]
    quicksort(a)
    print(a)
    a = [1,2,3,4]
    quicksort(a)
    print(a)


