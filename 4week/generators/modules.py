def squares(current, n):
    while current <= n:
        yield current**2
        current += 1
def downtoZero(n):
    num = n
    while num>=0:
        yield num
        num -= 1
