'''
Compute Jobs offest from documents JSON data
'''
RESULTS_PER_PAGE = 1000


def get_number_of_docs(documents_data):
    '''
    Return total number of records
    '''
    number_of_docs = documents_data.get("totalNumRecords")
    return number_of_docs


def compute_jobs(documents_data):
    '''
    Computing Jobs offset for Documents endpoint
    '''
    number_of_docs = get_number_of_docs(documents_data)

    jobs = []

    for page_offset in range(0, number_of_docs, RESULTS_PER_PAGE):
        job = page_offset  # Line will be used to create DocsJob object
        jobs.append(job)

    return jobs
