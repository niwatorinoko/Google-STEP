#!/usr/bin/env python3

from common import format_tour, read_input

import two_opt as two_opt

CHALLENGES = 6


def generate_sample_output():
    for i in range(CHALLENGES):
        cities = read_input(f'tsp/sample_input/input_{i}.csv')
        tour = two_opt.solve(cities)
        with open(f'tsp/output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_sample_output()
