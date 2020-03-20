
"""
Test class for Job-Queue Class.
"""
import pytest
from c20_server.job_queue import JobQueue
from c20_server.job import Job
from c20_server import job_queue_errors


def test_one_job_added_is_returned_by_get():
    job_queue = JobQueue()
    job = Job(1234)

    assert job_queue.get_num_unassigned_jobs() == 0
    job_queue.add_job(job)
    assert job_queue.get_num_unassigned_jobs() == 1
    assert job_queue.get_job() == job
    assert job_queue.get_num_unassigned_jobs() == 0


def test_add_two_jobs_then_remove_them():
    job_queue = JobQueue()
    job1 = Job(123411)
    job2 = Job(56722)

    job_queue.add_job(job1)
    job_queue.add_job(job2)
    assert job_queue.get_num_unassigned_jobs() == 2

    assert job_queue.get_job() == job1
    assert job_queue.get_job() == job2
    assert job_queue.get_num_unassigned_jobs() == 0


def test_get_one_job_from_empty_list():
    job_queue = JobQueue()
    with pytest.raises(job_queue_errors.NoJobsAvailableException):
        job_queue.get_job()
