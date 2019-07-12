import heapq


class MaxHeapObj:
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


class MinHeap:
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)

    def get_min(self): return self.h[0]


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heapq.heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val

    def get_max(self): return self.h[0].val


class MedianMaintainer:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.size = 0

    def push(self, val):
        # Empty case
        if self.size == 0:
            self.max_heap.heappush(val)
            self.size += 1
            return

        if val < self.max_heap.get_max():
            self.max_heap.heappush(val)
            self.size += 1
            if len(self.max_heap) > (len(self.min_heap) + 1):
                transfer_val = self.max_heap.heappop()
                self.min_heap.heappush(transfer_val)
        else:
            self.min_heap.heappush(val)
            self.size += 1
            if len(self.min_heap) > (len(self.max_heap) + 1):
                transfer_val = self.min_heap.heappop()
                self.max_heap.heappush(transfer_val)

    def get_median(self):
        if self.size == 0:
            raise Exception('MedianMaintainer is Empty')

        if len(self.max_heap) >= len(self.min_heap):
            return self.max_heap.get_max()
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap.get_min()


def load_numbers(filename):
    arr = []
    with open(filename, 'r') as f:
        for line in f:
            arr.append(int(line))

    return arr


def main():
    filename = 'Median.txt'
    arr = load_numbers(filename)

    med_maintainer = MedianMaintainer()
    medians = []
    for val in arr:
        med_maintainer.push(val)
        medians.append(med_maintainer.get_median())
        print(med_maintainer.get_median())

    print(sum(medians))

if __name__ == '__main__':
    main()
