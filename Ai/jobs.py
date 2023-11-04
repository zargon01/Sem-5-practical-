def printJobScheduling(arr, t):
    # Sort all jobs in decreasing order of profit
    arr.sort(key=lambda x: x[2], reverse=True)
    
    # To keep track of free time slots
    result = [False] * t
    
    # To store result (Sequence of jobs)
    job = [-1] * t

    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                break

    # Print the sequence
    print(job)

# Driver's Code
if __name__ == '__main__':
    # Example usage
    # Jobs are represented as a list of tuples (job_id, deadline, profit)
    jobs = [
        ("J1", 2, 60),
        ("J2", 1, 100),
        ("J3", 3, 20),
        ("J4", 2, 40)
    ]
    
    # Number of time slots
    time_slots = 3
    
    # Call the function
    printJobScheduling(jobs, time_slots)
