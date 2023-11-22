import pprint


def isDifferent(v, color, ver):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == ver:
            return False
    return True


def mapColoring(c, color, cur_ver):
    if cur_ver + 1 == V:
        return True

    for i in range(0, c):
        if isDifferent(cur_ver, color, i):
            color[cur_ver] = i
            if mapColoring(c, color, cur_ver + 1):
                return True

            color[cur_ver] = -1


def printColor(color, c):
    color = [0] * V

    if mapColoring(c, color, 0) is None:
        print("\nNO")
        return False
    else:
        print("\n")
        for i in range(V):
            print(color[i])

    return True


if __name__ == '__main__':
    a = input()
    a = a.split(' ')
    V = int(a[0])
    E = int(a[1])
    arr = []
    n = 2
    row_num = E
    col_num = E
    adj_mat = []
    for i in range(row_num):
        row = []
        for j in range(col_num):
            row.append(0)
        adj_mat.append(row)
    edges = list(tuple(map(int, input(int()).split())) for r in range(row_num))
    for edge in edges:
        row = edge[0]
        col = edge[1]
        adj_mat[row - 1][col - 1] = 1
        adj_mat[col - 1][row - 1] = 1

    c = int(input())

    # print("edges:")
    # print(edges)
    # print("adjacency matrix:")
    # pprint.pprint(adj_mat)
    graph = adj_mat

    printColor(graph, c)
