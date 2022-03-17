# oneliner
# ['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(n,m)]

def fizzbuzz(n: int, m: int):
    while not (1 <= n < m <= 1000):
        print('Please, input n, m to satisfy '
              'the condition 1 <= n <m <= 1000')
        n = int(input('Enter n: '))
        m = int(input('Enter m: '))
    f = n % 3
    b = n % 5
    f = 3 if f == 0 else f
    b = 5 if f == 0 else b
    for num in range(n, m+1):
        if f == 3 and b != 5:
            f = 0
            print('Fizz')
        elif f != 3 and b == 5:
            b = 0
            print('Buzz')
        elif f == 3 and b == 5:
            f, b = 0, 0
            print('FizzBuzz')
        else:
            print(num)
        b += 1
        f += 1


if __name__ == '__main__':
    fizzbuzz(3, 16)
