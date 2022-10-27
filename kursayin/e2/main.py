def fibonacci(n):
    ml = []
    o1 = 0
    o2 = 1
    summ = 0
    while summ <= n:
        ml.append(summ) 
        summ = o1 + o2
        o1 = o2
        o2 = summ
    return ml

def create_matrix(n):
    ml = [[int(input("mutqagreq matrici elementy: ")) for j in range(n)] for i in range(n)]
    return(ml)

def find_max(matrix):
    maxx = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > maxx:
                maxx = matrix[i][j]   
    return maxx

if __name__ == "__main__":
    n = int(input("mutqagreq matrixi chapsy: "))
    matrix = create_matrix(n)
    maxx = find_max(matrix)
    fib_ml = fibonacci(maxx)
    zero_count = n
    print(fib_ml)
    for i in range(n):
        for j in range(n):
            if matrix[j][i] not in fib_ml:
                zero_count -= 1
                print("bob") 
    
    for i in range(zero_count):
        for el in matrix:
            el.append(0)            
    print(matrix)       
           