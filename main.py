from typing import List
import itertools
import statistics
import doctest

def res_of_median(fixed_list, citizen_votes: List[List] = None):
    res=[]
    for i in range(len(citizen_votes[0])):
        t=[]
        for citizen in citizen_votes:
            t.append(citizen[i])
        for f in fixed_list:
            t.append(f)
        res.append(statistics.median(t))
    return res
def binary_search(left,right,citizen_votes: List[List],total_budget,i=1):
    while right>=left:
        t=(left+right)/2
        fixed_lst=[total_budget*min(1,i*t) for i in range(1,len(citizen_votes))]
        result=res_of_median(fixed_lst,citizen_votes)
        sum_of_result=sum(result)
        if sum_of_result>total_budget:
            right=t
        elif  sum_of_result<total_budget:
            left=t
        else:
            return result
    else:
        return -1



def compute_budget(total_budget: float = None, citizen_votes: List[List] = None) -> List[float]:
    """

    :param total_budget:
    :param citizen_votes:
    :return:
    >>> citizen_votes = [[0, 0, 6, 0, 0, 6, 6, 6, 6], [0, 6, 0, 6, 6, 6, 6, 0, 0], [6, 0, 0, 6, 6, 0, 0, 6, 6]]
    >>> compute_budget(30, citizen_votes)
    [2.0, 2.0, 2.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100]]
    >>> compute_budget(100, citizen_votes)
    [50.0, 0, 50.0]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100], [0, 0, 100]]
    >>> compute_budget(100, citizen_votes)
    [33.333333333333336, 0, 66.66666666666667]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100], [0, 50, 50],[30,70,0]]
    >>> compute_budget(100, citizen_votes)
    [30, 35.00000000000001, 35.00000000000001]
    """
    return binary_search(0,1,citizen_votes,total_budget)


if __name__ == '__main__':
  
    failures, tests = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
