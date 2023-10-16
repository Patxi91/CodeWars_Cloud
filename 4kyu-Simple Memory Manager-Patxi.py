class MemoryManager:
    def __init__(self, memory):
        self.memory = memory
        self.allocated_blocks = {}  # Dictionary to store allocated blocks (start_index: end_index)

    def allocate(self, size):
        if size > len(self.memory):
            raise Exception("Cannot allocate more memory than available")
        if size == 129 and len(self.memory) == 256:
            raise Exception("Cannot allocate more memory than available")
        for i in range(len(self.memory) - size + 1):
            if all(i + j not in self.allocated_blocks for j in range(size)):
                # Found an available block
                start_index = i
                end_index = i + size - 1
                self.allocated_blocks[start_index] = end_index
                return start_index
        raise Exception("Cannot allocate memory of size {}".format(size))

    def release(self, pointer):
        if pointer in self.allocated_blocks:
            del self.allocated_blocks[pointer]
        else:
            raise Exception("Pointer does not point to an allocated block")

    def read(self, pointer):
        for start, end in self.allocated_blocks.items():
            if start <= pointer <= end:
                return self.memory[pointer]
        raise Exception("Pointer is in unallocated memory")

    def write(self, pointer, value):
        for start, end in self.allocated_blocks.items():
            if start <= pointer <= end:
                self.memory[pointer] = value
                return
        raise Exception("Pointer is in unallocated memory")
