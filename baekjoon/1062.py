import sys
import itertools

n,k = list(map(int, sys.stdin.readline().split()))
words = []
re = 0
target = ''
for _ in range(n):
	word = sys.stdin.readline().split()[0].split('anta')[1].split('tica')[0]
	new_word = []
	for ch in word:
		if ch not in ['a', 'n', 't', 'i', 'c']:
			if ch not in new_word:
				new_word.append(ch)
			if ch not in target:
				target += ch
	if len(new_word) == 0:
		re += 1
		continue
	word_num = 0
	for ch in new_word:
		word_num += 2**(ord(ch)-ord('a'))
	words.append(word_num)

if k < 5:
	print(0)
	exit()
k -= 5
if k == 0:
	print(re)
	exit()

target = list(target)
target.sort()
target = ''.join(target)

if len(target) < k:
	k = len(target)
comb_list = list(map(''.join, itertools.combinations(target, k)))
comb_re = 0
for comb in comb_list:
	comb_num = 0
	for ch in comb:
		comb_num += 2**(ord(ch)-ord('a'))
	chk = 0
	for word in words:
		if word|comb_num <= comb_num:
			chk += 1
	if comb_re < chk:
		comb_re = chk

print(re + comb_re)