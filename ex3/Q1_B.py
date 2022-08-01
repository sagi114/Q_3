from itertools import permutations
def permute(A):
    print(list(list(''.join(p)) for p in permutations(A)))
if __name__ == '__main__':
    print(permute('abc'))