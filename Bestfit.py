def best_fit_allocation(block_sizes, process_sizes):
    n = len(process_sizes)
    m = len(block_sizes)
    allocation = [-1] * n

    for i in range(n):
        best_block_index = -1
        for j in range(m):
            if block_sizes[j] >= process_sizes[i]:
                if best_block_index == -1 or block_sizes[best_block_index] > block_sizes[j]:
                    best_block_index = j
        
        if best_block_index != -1:
            allocation[i] = best_block_index
            block_sizes[best_block_index] -= process_sizes[i]

    print("Process\tSize\t\tAllocated Block")
    for i in range(n):
        block_num = allocation[i]
        result = block_num + 1 if block_num != -1 else "Not Allocated"
        print(f"P{i+1}\t{process_sizes[i]}\t\t{result}")

if __name__ == "__main__":
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]
    
    best_fit_allocation(blocks, processes)
