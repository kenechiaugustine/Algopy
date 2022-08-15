from itertools import permutations
def allpermutations(str):
    permList = permutations(str)
    for perm in permList:
        print(''.join(perm))

if __name__ == '__main__':
    str = input('Enter a string: ')
    allpermutations(str)