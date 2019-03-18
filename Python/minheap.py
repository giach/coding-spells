class MinHeap:

    def __init__(self):
        self.arr = []
        self.size = 0


    def add_node(self, value):
        self.arr.append(value)

        idx = len(self.arr) - 1
        self.bubble_up(idx)

    def bubble_up(self, idx):
        if idx == 0 or idx == 1:
            return

        p_idx = int((idx - 1) / 2)
        if self.arr[idx] >= self.arr[p_idx]:
            return

        tmp = self.arr[p_idx]
        self.arr[p_idx] = self.arr[idx]
        self.arr[idx] =  tmp

        self.bubble_up(p_idx)

    def remove_min(self):
        s = len(self.arr)

        if s <= 0:
            print("The heap is empty")
            return

        first = self.arr[0]
        print("Remove the min element ", self.arr[0])
        tmp = self.arr[s - 1]
        self.arr[0] = tmp
        self.arr = self.arr[1:]
        self.bubble_down(0)

        return first

    def bubble_down(self, idx):
        size = len(self.arr)
        if idx >= size:
            return

        left_idx = (2 * idx + 1) if (2 * idx + 1) < size else None
        right_idx = (2 * idx + 2) if (2 * idx + 2) < size else None


        nidx = -1
        if left_idx and right_idx:
            if self.arr[left_idx] < self.arr[right_idx]:
                if self.arr[idx] > self.arr[left_idx]:
                    nidx = left_idx
            else:
                    nidx = right_idx
        elif left_idx:
            if self.arr[idx] > self.arr[left_idx]:
                nidx = left_idx
        elif right_idx:
            if self.arr[idx] > self.arr[right_idx]:
                nidx = right_idx

        if nidx != -1:
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[nidx]
            self.arr[nidx] = tmp
            self.bubble_down(nidx)

        return


    def print(self):
        print(self.arr)

def main():
    heap = MinHeap()
    heap.add_node(3)
    heap.add_node(7)
    heap.add_node(10)
    heap.add_node(4)
    heap.print()

    heap.remove_min()
    heap.print()
    heap.remove_min()
    heap.print()

    heap.remove_min()
    heap.print()

    heap.remove_min()
    heap.print()

main()
