def prime_checker(number):
    number_of_divisions = 0
    for i in range(1, number+1):
        if number%i == 0:
            number_of_divisions += 1
    if number_of_divisions == 2:
        return "Prime number."
    else:
        return "Not a prime number."


start = int(input("Start from: "))
end = int(input("End in: "))
list_primes = []

for a in range(start, end+1):
    if prime_checker(a) == "Prime number.":
        list_primes.append(a)

print(f"Prime numbers in this range are: {list_primes}")

