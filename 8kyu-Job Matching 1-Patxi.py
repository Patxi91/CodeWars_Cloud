def job_matching(candidate, job):
    # Check if both candidate's minimum salary and job's maximum salary are present
    if not candidate.get('min_salary'):
        raise ValueError('Candidate must have a minimum salary specified.')
    if not job.get('max_salary'):
        raise ValueError('Job must have a maximum salary specified.')

    # Calculate the adjusted minimum salary considering 10% wiggle room
    adjusted_min_salary = candidate['min_salary'] * 0.9

    # Check if the adjusted minimum salary is less than or equal to the job's maximum salary
    if adjusted_min_salary <= job['max_salary']:
        return True
    return False
