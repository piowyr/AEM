import sys
import os.path
from tqdm import tqdm
import numpy as np
from statistics import mean
from time import time
import random

random.seed(0)

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from tsp_router.utils.evaluator import Evaluator
from tsp_router.utils.loader import Loader
from tsp_router.utils.visualizer import Visualizer



from tsp_router.local_search.steepest_on_edges_destroy_repair import \
    SteepestOnEdges
from tsp_router.local_search.steepest_on_edges_multiple_start import \
    SteepestOnEdgesMultipleStart
# from tsp_router.local_search.steepest_on_edges import SteepestOnEdges
from tsp_router.local_search.steepest_on_edges_previous_moves import SteepestOnEdgesPreviousMoves

from tsp_router.local_search.steepest_on_edges_destroy_repair import \
    LocalSearchWithLargeScaleNeighbourhood

def run(path):
    loader = Loader(path)
    vertices = loader.load_vertices()

    matrix = loader.calculate_matrix(vertices)

    visualizer = Visualizer()
    
    # two_opt = SteepestOnEdges()
    lswlsn = LocalSearchWithLargeScaleNeighbourhood()

    all_vertices = np.arange(len(vertices))
    solutions = []
    lengths = []
    times = []

    for i in tqdm(range(10)):
        random_solution = random.sample(
            list(all_vertices), int(np.ceil(len(all_vertices)/2)))
        start = time()
        # improved_solution = two_opt.improve(random_solution, matrix, all_vertices)
        # improved_solution = two_opt.improve(matrix, all_vertices, 100)
        improved_solution, n_iterations = lswlsn.solve(
            matrix, all_vertices, 360)
        print("llll", len(improved_solution))
        print("improved_solution", improved_solution)
        print("unique",  len(np.unique(np.array(improved_solution))))
        print("n_iterations:", n_iterations)
        end = time()

        times.append(end - start)
        l = 0
        for i in range(-1, len(improved_solution)-1):
            l += matrix[improved_solution[i], improved_solution[i+1]]
        lengths.append(l)
        print("l:", l)
        solutions.append(improved_solution)

    print('min:', min(lengths))
    print('max:', max(lengths))
    print('mean:', mean(lengths))
    print('min_time:', min(times))
    print('max_time:', max(times))
    print('mean_time:', mean(times))
    best_sol = solutions[lengths.index(min(lengths))]
    visualizer.create_graph_euclidean(best_sol, matrix, vertices)


def run_all_algorithms(path):
    for algoritm in [LocalSearchWithLargeScaleNeighbourhood, ]
    loader = Loader(path)
    vertices = loader.load_vertices()

    matrix = loader.calculate_matrix(vertices)

    visualizer = Visualizer()

    # two_opt = SteepestOnEdges()
    lswlsn = LocalSearchWithLargeScaleNeighbourhood()

    all_vertices = np.arange(len(vertices))
    solutions = []
    lengths = []
    times = []

    for i in tqdm(range(10)):
        random_solution = random.sample(
            list(all_vertices), int(np.ceil(len(all_vertices) / 2)))
        start = time()
        # improved_solution = two_opt.improve(random_solution, matrix, all_vertices)
        # improved_solution = two_opt.improve(matrix, all_vertices, 100)
        improved_solution, n_iterations = lswlsn.solve(
            matrix, all_vertices, 360)
        print("llll", len(improved_solution))
        print("improved_solution", improved_solution)
        print("unique", len(np.unique(np.array(improved_solution))))
        print("n_iterations:", n_iterations)
        end = time()

        times.append(end - start)
        l = 0
        for i in range(-1, len(improved_solution) - 1):
            l += matrix[improved_solution[i], improved_solution[i + 1]]
        print("l:", l)
        lengths.append(l)
        solutions.append(improved_solution)

    print('min:', min(lengths))
    print('max:', max(lengths))
    print('mean:', mean(lengths))
    print('min_time:', min(times))
    print('max_time:', max(times))
    print('mean_time:', mean(times))
    best_sol = solutions[lengths.index(min(lengths))]
    visualizer.create_graph_euclidean(best_sol, matrix, vertices)

def main():
    # run('../data/kroA200.tsp')
    # run('../../data/kroB100.tsp')
    run_all_algorithms('../../data/kroB100.tsp')

if __name__ == '__main__':
    main()