
"""
implementation of Job_Queue class

"""
from c20_server.job import Job
from c20_server import job_queue_errors


class JobQueue:

    unassigned_jobs_list = []
    job = Job

    def add_job(self, job):
        self.unassigned_jobs_list.append(job)

    def get_job(self):
        if not self.unassigned_jobs_list:
            raise job_queue_errors.NoJobsAvailableException
        return self.unassigned_jobs_list.pop(0)

    def get_num_unassigned_jobs(self):
        return len(self.unassigned_jobs_list)
