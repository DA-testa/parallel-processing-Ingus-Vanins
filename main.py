# python3 Ingus Vaņins 7.grupa

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    
    for i in range(m):
        time = data[i]
        start_time, thread_idx = heapq.heappop(threads)
        output.append((thread_idx, start_time))
        heapq.heappush(threads, (start_time + time, thread_idx))
        
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    
     n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    
     print(thread_idx, start_time)



if __name__ == "__main__":
    main()
