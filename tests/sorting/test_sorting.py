from src.sorting import sort_by
from pytest import raises


jobs = [
    {"date_posted": "2020-05-08", "max_salary": "190", "min_salary": "2"},
    {"date_posted": "2020-05-04", "max_salary": "100", "min_salary": "24"},
    {"date_posted": "2020-05-03", "max_salary": "200", "min_salary": "12"},
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
]

jobsPatched = [
    {"max_salary": "100", "min_salary": "24"},
    {"date_posted": "2020-05-03", "max_salary": "190", "min_salary": "2"},
    {"max_salary": "200", "min_salary": "12"},
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
]

expect_jobs_sorted_by_date_posted_patched = [
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
    {"date_posted": "2020-05-03", "max_salary": "190", "min_salary": "2"},
    {"max_salary": "100", "min_salary": "24"},
    {"max_salary": "200", "min_salary": "12"},
]

expect_jobs_sorted_by_max_salary = [
    {"date_posted": "2020-05-03", "max_salary": "200", "min_salary": "12"},
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
    {"date_posted": "2020-05-08", "max_salary": "190", "min_salary": "2"},
    {"date_posted": "2020-05-04", "max_salary": "100", "min_salary": "24"},
]

expect_jobs_sorted_by_date_posted = [
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
    {"date_posted": "2020-05-08", "max_salary": "190", "min_salary": "2"},
    {"date_posted": "2020-05-04", "max_salary": "100", "min_salary": "24"},
    {"date_posted": "2020-05-03", "max_salary": "200", "min_salary": "12"},
]

expect_jobs_sorted_by_min_salary = [
    {"date_posted": "2020-05-08", "max_salary": "190", "min_salary": "2"},
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
    {"date_posted": "2020-05-03", "max_salary": "200", "min_salary": "12"},
    {"date_posted": "2020-05-04", "max_salary": "100", "min_salary": "24"},
]

expect_jobs_sorted_by_min_salary_reverse = [
    {"date_posted": "2020-05-04", "max_salary": "100", "min_salary": "24"},
    {"date_posted": "2020-05-03", "max_salary": "200", "min_salary": "12"},
    {"date_posted": "2020-05-09", "max_salary": "199", "min_salary": "11"},
    {"date_posted": "2020-05-08", "max_salary": "190", "min_salary": "2"},
]

criteria_keys = ["min_salary", "max_salary", "date_posted"]

invalid_criteria_keys = ["secret", None, True]


def test_sort_by_criteria():
    assert type(jobs) == list

    sort_by(jobs, "min_salary")
    assert jobs == expect_jobs_sorted_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == expect_jobs_sorted_by_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == expect_jobs_sorted_by_date_posted

    # O teste rejeita implementações que aceitam critérios não definido.
    for key in invalid_criteria_keys:
        with raises(ValueError, match=f"invalid sorting criteria: {key}"):
            sort_by(jobs, key)
