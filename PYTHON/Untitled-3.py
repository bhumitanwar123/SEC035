class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    result = [-1] * n
    max_deadline = max(job.deadline for job in jobs)
    slot = [False] * max_deadline

    for job in jobs:
        for t in range(job.deadline - 1, -1, -1):
            if not slot[t]:
                slot[t] = True
                result[t] = job.id
                break
    
    sequence = [x for x in result if x != -1]
    return sequence

if __name__ == "__main__":
    jobs = [
        Job('J1', 4, 20),
        Job('J2', 1, 10),
        Job('J3', 1, 40),
        Job('J4', 1, 30)
    ]
    n = len(jobs)
    sequence = job_sequencing(jobs, n)
    print("Job sequence:", sequence)

# Time Complexity for Sorting the jobs: 𝑂(𝑛log𝑛)


