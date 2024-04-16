import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, cache=None):
	if cache is None:
			cache = {}

	if (S, T) in cache:
			return cache[(S, T)]

	if not S:
			cache[(S, T)] = len(T)
	elif not T:
			cache[(S, T)] = len(S)
	elif S[0] == T[0]:
			cache[(S, T)] = fast_MED(S[1:], T[1:], cache)
	else:
			insert = fast_MED(S, T[1:], cache)
			delete = fast_MED(S[1:], T, cache)
			cache[(S, T)] = 1 + min(insert, delete)

	return cache[(S, T)]

def fast_align_MED(S, T, cache=None):
	if cache is None:
			cache = {}

	if (S, T) in cache:
			return cache[(S, T)]

	if not S:
			result = (len(T), (len(T) * '-', T))
	elif not T:
			result = (len(S), (S, len(S) * '-'))
	else:
			if S[0] == T[0]:
					cost, (aligned_S, aligned_T) = fast_align_MED(S[1:], T[1:], cache)
					result = (cost, (S[0] + aligned_S, T[0] + aligned_T))
			else:
					del_cost, (del_S, del_T) = fast_align_MED(S[1:], T, cache)
					ins_cost, (ins_S, ins_T) = fast_align_MED(S, T[1:], cache)
					if del_cost <= ins_cost:
							best_cost, best_align = del_cost, ('-' + del_S, T[0] + del_T)
					else:
							best_cost, best_align = ins_cost, (S[0] + ins_S, '-' + ins_T)
					sub_cost, (sub_S, sub_T) = fast_align_MED(S[1:], T[1:], cache)
					if sub_cost < best_cost:
							best_cost, best_align = sub_cost, (S[0] + sub_S, T[0] + sub_T)
					result = (1 + best_cost, best_align)

	cache[(S, T)] = result
	return result

