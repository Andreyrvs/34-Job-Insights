from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)

    industries = {}
    for row in jobs:
        content = row["industry"]
        if content not in industries:
            industries[content] = 0
        industries[content] += 1

    remove_empty = list(filter(None, industries))
    print(remove_empty)
    return remove_empty


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
