def optimal_summands(n):

 summands = [] # array to store pairwise distinct positive integers
 k = n # marked the upper part
 m = 1 # marked the lower part

 if n == 2 or n == 1:
     summands.append(n)
 else:
     for i in range(1,k):
         if k <= 2*m:
             summands.append(k)
             break
         else:
             summands.append(m)
             k = k - m
             m = m + 1

 return summands
 
 
 def main():
     n = int(input())
     print(optimal_summands(n))
 
 
 if __name__ == '__main__':
     main()
