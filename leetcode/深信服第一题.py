T=int(input())

out=[]
for _ in range(T):
    N,M=map(int,input().split())
    picture=[input() for _ in range(N)]
    feature=[input() for _ in range(M)]

    def check_submatrix(x, y):
        for i in range(M):
            for j in range(M):
                if picture[x+i][y+j]!=feature[i][j]:
                    return False
        return True

    founded=False
    for i in range(N-M+1):
        for j in range(N-M+1):
            if check_submatrix(i,j):
                founded=True
                break
        if founded:
            break
    out.append('Yes' if founded else 'No')
for i in range(len(out)):
    print(out[i])