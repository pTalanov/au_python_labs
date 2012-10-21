__author__ = 'Pavel'

class Primes:
    def __init__(self, n):
        self.n = n
        self.sieve = self.init_sieve()
        self.cur_prime = 1

    def init_sieve(self):
        sieve = []
        for i in range(0, self.n):
            sieve.append(0)
        return sieve

    def calculate(self):
        while True:
            p = self.next_prime()

            if p is None:
                return

            self.cur_prime = p

            self.update_sieve(p)

    def next_prime(self):
        for i in range(self.cur_prime + 1, self.n):
            if self.sieve[i] == 0:
                return i
        return None

    def update_sieve(self, p):
        i = 2
        while i * p < self.n:
            current = i * p
            self.sieve[current] += 1
            if i % p == 0:
                self.sieve[current] += 1
            if i % (p * p) == 0:
                self.sieve[current] += 1
            i += 1

    def print(self):
        for i in range(2, self.n):
            if self.sieve[i] == 2:
                print(str(i) + " "),


if __name__ == '__main__':
    primes = Primes(1000)
    primes.calculate()
    primes.print()

