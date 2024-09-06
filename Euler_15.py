#How many routes are there through a 20x20 grid

def count_lattice_paths(n):
    # 0...1
    # 1...11
    # 2...121
    # 3...1331
    # 4...14641
    row_new=n*[0]
    row=n*[0]
    matrix=[]
    for i in range(n):
        if i == 0:
            row_new[0]=1
        else:
            row_new=n*[0]
            for j in range(i+1):
                row_new[j]= row[j]+row[j-1]
        row=row_new
        matrix.append(row)
    return matrix

out=count_lattice_paths(21)

pascal_sum=0
for i in out[len(out)-1]:
    pascal_sum+=i**2

