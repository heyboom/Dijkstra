#!/usr/bin/env python3
# -*- coding: utf-8 -*-

M = 10000

def dijkstra_core(city, weight, start, end):    #算法核心！！
    n = len(city)
    new_weight = []
    for i in range(0, len(weight)):
        new_weight.append(weight[i].copy())
        path, distance, visit = [], [], []
    for i in range(0, n):
        distance.append(new_weight[start][i])
        visit.append(0)
        if new_weight[start][i] != M:
            path.append(city[start] + "-->" + city[i])
        else:
            path.append("不可达")
    visit[start] = 1

    for i in range(1, n):   #除了start到start的最短路径，还需要找到start到其余n - 1个点的最短路径
        k = -1          #找出U集合中最小距离路径的那个点，将它的距离放到short_path对应的位置，并将visit对应位置标1
        dmin = 2 * M
        for j in range(0, n):
            if visit[j] == 0 and new_weight[start][j] < dmin:
                dmin = new_weight[start][j]
                k = j
        distance[k] = dmin
        visit[k] = 1

        for j in range(0, n):   #将某个点，如D，放到S集合后，更改其他点     加了判断，自身无中转点才可以以D做中转，已经有中转则排除
            if visit[j] == 0 and new_weight[start][k] + new_weight[k][j] < new_weight[start][j] and path[j].count("-->") <= 1:
                new_weight[start][j] = new_weight[start][k] + new_weight[k][j]
                path[j] = path[k] + "-->" + city[j]

    return path[end], distance[end]


def dijkstra(start_city, end_city):
    city = ["A", "B", "C", "D", "E"]
    weight = [
        [0, 4, M, 2, M],
        [4, 0, 4, 1, M],
        [M, 4, 0, 1, 3],
        [2, 1, 1, 0, 7],
        [M, M, 3, 7, 0]
    ]
    start = city.index(start_city)
    end = city.index(end_city)
    count = 0
    result = ""
    while(True):
        path, distance = dijkstra_core(city, weight, start, end)
        if path.count("-->") != 2:  #如果不是中转1次，结束循环    舍弃直达和中转多次
            break
        count += 1  #能执行到这一步，说明始有中转方案的，处理本次方案数据，准备下次继续探索
        result += "方案" + str(count) + "\n" \
                 + "\t路径:" + path + "\n" \
                 + "\t距离:" + str(distance) + "\n"
        city_list = path.split("-->")
        transfer_city = city_list[1]
        transfer = city.index(transfer_city)
        weight[start][transfer] = M
        weight[transfer][start] = M

    return result if result != "" else "无中转方案"

if __name__ == '__main__':
    print("起点：")
    start_city = input()
    print("终点：")
    end_city = input()
    print(dijkstra(start_city,end_city))