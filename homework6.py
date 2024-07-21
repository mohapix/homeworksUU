def is_prime(func):
    def wrapper(*args):
        res = func(*args)

        if res % 2 == 0:
            print('Составное')
        else:
            div = 3
            while div < res:
                if res % div == 0:
                    print('Составное')
                    div = 0
                    break
                div += 2
            if div != 0:
                print('Простое')

        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
