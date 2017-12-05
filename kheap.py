class minHeap(object):
    def __init__(self, k):
        self.heap_array = []
        self.k = k

    def add_num(self, x):
        #
        # TODO: Add number to the heap array
        # while maintaining heap property
        #
        self.heap_array.append(x)
        self.heapify_up(len(self.heap_array)-1)
        pass

    def pop_min(self):
        #
        # TODO: Remove number from heap array while
        # maintaining heap property
        #
        removeValue = self.heap_array[0]
        self.heap_array[0]= self.heap_array[len(self.heap_array)-1]
        self.heap_array.pop()
        self.heapify_down(0)
        return removeValue
        pass

    def heapify_up(self, index):
        #
        # A helper function to help maintain heap property
        #
        parentIndex=(index-1)//self.k
        while (index>0 and self.heap_array[parentIndex]>self.heap_array[index]):
            #exchange
            tmp=self.heap_array[parentIndex]
            self.heap_array[parentIndex]=self.heap_array[index]
            self.heap_array[index]=tmp
            #update index
            index=parentIndex
            parentIndex=(index-1)//self.k
        pass

    def heapify_down(self, index):
        #
        # A helper function to help maintain heap property
        #
        firstChild=self.k*index+1#index to it's leftmost child, wehn j is 1
        smallest=index
        for childIndex in range (firstChild,min(self.k*index+self.k+1,len(self.heap_array))):#the range will exclude last index 
            if(self.heap_array[childIndex]<self.heap_array[smallest]):
                smallest=childIndex
        if (smallest!=index):
            temp=self.heap_array[index]
            self.heap_array[index]=self.heap_array[smallest]
            self.heap_array[smallest]=temp
            self.heapify_down(smallest)
        pass

    # This will print the heap in the requested format. You do not need to modify this function
    def __str__(self):
        # Do not sort the heap array
        s = ""
        for i in self.heap_array:
            s += str(i) + " "
        return s.strip()

# Given Starter Code for IO. You need not modify code beneath this line

[k, c] = [int(x) for x in raw_input().split()]
h = minHeap(k)
for i in range(c):
    command = raw_input().split()
    if command[0] == "add":
        h.add_num(int(command[1]))
    elif command[0] == "remove":
        print h.pop_min()
    elif command[0] == "print":
        print h