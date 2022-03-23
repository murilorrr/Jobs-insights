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
    try:
        if job["min_salary"] <= int(salary) <= job["max_salary"]:
            return True
        elif job["min_salary"] > job["max_salary"]:
            raise ValueError
        else:
            return False
    except (TypeError, KeyError):
        raise ValueError


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
    # lista de dicionarios como primeiro parametro ex:[{},{}]
    # inteiro como segundo parametro salary: int
    jobs_matched = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_matched.append(job)
        except ValueError:
            pass
    return jobs_matched
