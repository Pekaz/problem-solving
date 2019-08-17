import sys

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = 0
word = sys.stdin.readline().split()[0]
result += color.index(word)*10
word = sys.stdin.readline().split()[0]
result += color.index(word)
word = sys.stdin.readline().split()[0]
result *= 10**color.index(word)
print(result)