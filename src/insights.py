from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    unique_jobs_list = []
    for job in list:
        existsInList = False
        for index in unique_jobs_list:
            if job["job_type"] == index:
                existsInList = True
        if existsInList is False:
            unique_jobs_list.append(job["job_type"])

    return unique_jobs_list


def filter_by_job_type(jobs, job_type):
    jobsFilteredByJobType = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobsFilteredByJobType.append(job)

    return jobsFilteredByJobType


def get_unique_industries(path):
    jobs_list = read(path)
    totalList = []
    unique_industries_list = []
    for job in jobs_list:
        if job["industry"] != "":
            totalList.append(job["industry"])
    for type in totalList:
        if type not in unique_industries_list:
            unique_industries_list.append(type)

    return unique_industries_list


def filter_by_industry(jobs, industry):
    jobsFilteredByIndustry = []
    for job in jobs:
        if job["industry"] == industry:
            jobsFilteredByIndustry.append(job)

    return jobsFilteredByIndustry


def get_max_salary(path):
    list = read(path)
    salary_list = []
    for job in list:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"], 10))

    return max(salary_list)


def get_min_salary(path):
    list = read(path)
    salary_list = []
    for job in list:
        if job["min_salary"].isdigit():
            salary_list.append(int(job["min_salary"], 10))

    return min(salary_list)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
