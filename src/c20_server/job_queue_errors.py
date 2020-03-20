"""
Errors for job-queue class
"""


class NoJobsAvailableException(Exception):
    """
    Thrown exception for an empty unassigned_jobs_list.
    """
