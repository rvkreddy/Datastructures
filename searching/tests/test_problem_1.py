
import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\searching\\source')

from problems_1 import orderedLinearSearch,duplicateexist_sorting,MaxRepititionsWithHash,findMissingNumber_xor
import pytest


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print(" =>> Executing test ")



def test_orderedLinearSearch():
    listB  = [34,46,93,127,277,321,454,565,12201]
    number = 321
    assert orderedLinearSearch(listB, number) == 5

def test_orderedLinearSearch_numberdoesnotexist():
    listB  = [34,46,93,127,277,321,454,565,12201]
    number = 400
    assert orderedLinearSearch(listB, number) == -1

def test_duplicatesexist():
    duplicatelist = [1, 2, 2, 3, 4]
    assert duplicateexist_sorting(duplicatelist) == True

def test_MaxRepititionsWithHash():
    A = [3, 2, 1, 2, 2, 3, 2, 1, 3]
    elem, elemno =  MaxRepititionsWithHash(A)
    assert elem == 2
    assert elemno == 4

def test_findMissingNumber():
    A = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    assert findMissingNumber_xor(A) == 5