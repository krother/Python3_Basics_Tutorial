from collections import Counter
from itertools import permutations


def anagram(s1: str, s2: str) -> bool:
    """clean and neat solution in O(n log n) time"""
    return sorted(s1) == sorted(s2)


def anagram(s1: str, s2: str) -> bool:
    """from scratch solution, also O(n log n) because of 'in' """
    if len(s1) == len(s2):
        for c1 in s1:
            if c1 not in s2:
                return False
        return True
    return False

def anagram(s1: str, s2: str) -> bool:
    """faster O(n) but fails for character duplicates"""
    return set(s1) == set(s2)

def anagram(s1: str, s2: str) -> bool:
    """using counter dict, covers duplicates and should be O(n)"""
    return Counter(s1) == Counter(s2)


def anagram(s1: str, s2: str) -> bool:
    """super slow, probably O(n!)"""
    return tuple(s1) in permutations(s2)
    


assert anagram("players", "parsley") is True
assert anagram("hello", "foo") is False