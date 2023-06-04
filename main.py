import prime_finder
import math
import json

PRIMES_FILE = 'primes.json'

try:
    with open('primes.json', 'r') as f:
        primes = json.load(f)
except json.JSONDecodeError:
    print('Could not read JSON from primes.json. The file might be empty or the JSON might be malformed.')
    primes = [2, 3, 5]


limit = max(primes)
again = True

while again:
    answer = []
    print(len(primes))
    user_request = int(input("What number do you want to know the unique product of primes of?"))

    if user_request % 2 == 0:
        needed_limit = math.ceil(math.sqrt(limit))
    else:
        needed_limit = user_request

    if needed_limit > limit:
        new_primes = prime_finder.needed_primes(needed_limit, primes)
        primes.extend(new_primes)

    if prime_finder.prime_finder(user_request):
        print(f"{user_request} is Prime")
    else:
        while user_request != 1:
            for i in range(len(primes)):
                if user_request % primes[i] == 0:
                    answer.append(primes[i])
                    user_request /= primes[i]
        print(answer)

    user_answer = input("Do you want to input another number? y/n: ").lower()
    if user_answer == "n":
        again = False


with open(PRIMES_FILE, 'w') as f:
    json.dump(primes, f)
