import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
_rando = random.randint(0, len(friends)-1)
print(_rando)
print(f'The person paying for today\'s meal is {friends[_rando]}')

