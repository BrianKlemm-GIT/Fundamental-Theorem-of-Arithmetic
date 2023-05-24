import primes

limit = max(primes.primes)
answer = []
again = True

while again:
    user_request = int(input("What number do you want to know the unique product of primes of? "
                             f"\nIf you number is odd it cannot be larger than {limit}. "
                             f"\nIf your number is even it cannot be larger than 2,363,029,320: "))
    if user_request not in primes.primes:
        while user_request != 1:
            for i in range(len(primes.primes)):
                if user_request % primes.primes[i] == 0:
                    answer.append(primes.primes[i])
                    user_request /= primes.primes[i]
        print(answer)
    else:
        print(f"{user_request} is Prime")

    user_answer = input("Do you want to input another number? y/n: ").lower()
    if user_answer == "n":
        again = False
