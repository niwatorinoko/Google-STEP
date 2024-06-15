#!/usr/bin/env python3

#----------------------------------------------------#
#                                                    #
# 最初にgreedyでルートを見つける                         #
# その後、2-optアルゴリズムで既存のルートをもっと最適化する。 #
#                                                    #
#----------------------------------------------------#

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    # 2点間の距離を求める公式
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities) # N = 全都市の数

    dist = [[0] * N for i in range(N)] # 2つ都市の距離を保存するリスト
    for i in range(N):
        for j in range(i, N):
            # 2つ都市の距離を計算しdistの距離を更新する
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0 # 都市0からスタート
    unvisited_cities = set(range(1, N)) # 未訪問の都市を保存するセット
    tour = [current_city] # 実際に辿った都市を保存するリスト

    # 未訪問の都市がある間行う処理
    while unvisited_cities:
        # 未訪問の都市から一番近い都市を次に訪問する都市とする
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # 2-optアルゴリズムでルートを改善する
    tour = two_opt(tour, dist)
    
    return tour


def two_opt(tour, dist):
    def calculate_total_distance(tour):
        return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + dist[tour[-1]][tour[0]]

    # 現時点での距離を計算する
    best_distance = calculate_total_distance(tour)
    improved = True

    # whileループのうち、改善する箇所が1個も出てこない場合にwhileを抜ける
    # -> 68行目のif文に入ってimprovedがTrueになるともう一度whileループに入る
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):

                # 隣同士の場合、スキップ
                if j - i == 1:
                    continue

                # スタート地点からゴール地点の間を逆順にしたルートを全通り見ていき、
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_total_distance(new_tour)
                # 距離が改善できる場合、ルートを更新する。
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True

    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
