import math, queue
from collections import Counter

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-ur-ra', 'kooky-bi-rd--'), ('-ele-phant','relev--ant'), ('AAAGAATTCA', 'AAA---T-CA')]

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


def fast_MED(S, T, MED={}):
	if (S, T) in MED:
			return MED[(S, T)]
	if S == "":
			return len(T)
	elif T == "":
			return len(S)
	elif S[0] == T[0]:
			MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
	else:
			MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

	return MED[(S, T)]


def fast_align_MED(S, T, MED={}):
	if (S, T) in MED:
			return MED[(S, T)]
	if S == "":
			MED[(S, T)] = ("-" * len(T), T)
			return MED[(S, T)]
	if T == "":
			MED[(S, T)] = (S, "-" * len(S))
			return MED[(S, T)]
	if S[0] == T[0]:
			aligned_seq_S, aligned_seq_T = fast_align_MED(S[1:], T[1:], MED)
			MED[(S, T)] = (S[0] + aligned_seq_S, T[0] + aligned_seq_T)
	else:
			insert_seq_S, insert_seq_T = fast_align_MED(S, T[1:], MED)
			delete_seq_S, delete_seq_T = fast_align_MED(S[1:], T, MED)
			cost_insert = 1 + len(insert_seq_S)
			cost_delete = 1 + len(delete_seq_S)
			if cost_insert <= cost_delete:
					MED[(S, T)] = ("-" + insert_seq_S, T[0] + insert_seq_T)
			else:
					MED[(S, T)] = (S[0] + delete_seq_S, "-" + delete_seq_T)
	return MED[(S, T)]