from collections import namedtuple
Job = namedtuple('Job', ['weight', 'length'])


def load_file(filename):
    jobs = []

    with open(filename, 'r') as f:

        for line_num, line in enumerate(f):
            if line_num == 0:
                num_jobs = int(line)
                continue
            line = str.strip(line).split(' ')
            job = Job(*map(int, line))
            jobs.append(job)

    return num_jobs, jobs



def schedule_jobs(jobs):
    scheduled_jobs = sorted(jobs, key=(lambda job: (job.weight / job.length)), reverse=True)
    return scheduled_jobs


def compute_weighted_completion_times(scheduled_jobs):
    completion_time = 0
    cost = 0
    for job in scheduled_jobs:
        completion_time += job.length
        cost += (completion_time * job.weight)
    return cost, completion_time


def main():
    filename = 'jobs.txt'
    _, jobs = load_file(filename)
    scheduled_jobs = schedule_jobs(jobs)
    cost, comletion_time = compute_weighted_completion_times(scheduled_jobs)
    print(cost, comletion_time)

if __name__ == '__main__':
    main()