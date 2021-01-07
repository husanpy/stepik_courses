def find_pis(n, m):
    """this func exactly returns Pisano sequence"""
    pisano = []
    pisano.append(0)
   
    if m == 1:
        return pisano
    pisano.append(1)
    
    #if m>0
    if n <= 1:
        return pisano
    
    n0 = 0
    n1 = 1
    for _ in range(6 * m + 1):
        #here we don't calculate numbers of Fibonacci sequence, but Pisano sequence
        #by appending result of division by mod m
        
        n0, n1 = n1, (n0 + n1) % m
        pisano.append(n1 % m)
        
        #in case of repeating 0,1 sequence we get the constant period and break cycle
        if pisano[-1] == 1 and pisano[-2] == 0: #cycle ends here :-)
            return pisano[:-2]
        if len(pisano) == (n + 1): #in case if period of pisano sequence is more than fib sequence
            return pisano[:]  


def fib_mod(n, m):
    #defining mod of fib(n) by m
    pisano = find_pis(n, m)
    if len(pisano) < (n + 2):
        return pisano[n % len(pisano)]
    return pisano[-1]
    

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
