# Matthew Powell's 14034684

import numpy as np
from random import randrange, random
import math
import csv

POPULATION_SIZE = 100
GENE_SIZE = 10
MUTATION =111
# This class designates Individuals as having a Gene variable and a fitness variable
class Individual:
    def __init__(self, gene, fitness):
        self.gene = gene
        self.fitness = fitness

# This function creates a list of individuals and randomly populates them with 0 and 1s.
# It then assigns a fitness value to the random string.


def populate_population_max():

    population_list = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    gene = [None] * GENE_SIZE

    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            gene[j] = randrange(2)
        population_list[i].gene = gene
        population_list[i].fitness = calculate_fitness_e1(population_list[i].gene)
        gene = [None] * GENE_SIZE

    return population_list


def populate_population_min():

    population_list = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    gene = [None] * GENE_SIZE

    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            gene[j] = randrange(2)
        population_list[i].gene = gene
        population_list[i].fitness = calculate_fitness_e2(population_list[i].gene)
        gene = [None] * GENE_SIZE

    return population_list


def populate_population_floats():

    population_list = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    gene = [None] * GENE_SIZE
    x = 0.00

    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            gene[j] = np.random.uniform(0, 5.12)
        population_list[i].gene = gene
        population_list[i].fitness = calculate_fitness_e3(population_list[i].gene)
        print(gene)
        gene = [None] * GENE_SIZE

def calculate_fitness_e1(gene):
    fitness = 0
    for i in range(GENE_SIZE):
        conversion = int("".join(str(x) for x in gene), 2)
        fitness = conversion ** 2

    return fitness


def calculate_fitness_e2(gene):
    x = gene[:len(gene)//2]
    y = gene[len(gene)//2:]
    k = x.pop(0)
    z = y.pop(0)
    in_x = int("".join(str(i) for i in x), 2)
    in_y = int("".join(str(i) for i in y), 2)
    if k ==0:
        in_x = -in_x
    if z ==0:
        in_y = -in_y
    fn1 = 0.26 * ((in_x ** 2) + (in_y ** 2))
    fn2 = -0.48 * (in_x * in_y)
    fitness = fn1 + fn2
    return fitness


def calculate_fitness_e3(gene):
    gene = [5.12,5.12,5.12,5.12,5.12,5.12,5.12,5.12,5.12,5.12]
    fitness = -(10 * len(gene) + sum([(x ** 2 - 10 * np.cos(2 * math.pi * x)) for x in gene]))
    return fitness



def calculate_mean_fitness(population_list):
    mean_fitness = 0

    for i in range(POPULATION_SIZE):
        mean_fitness += population_list[i].fitness

    return mean_fitness / POPULATION_SIZE


def calculate_best_fitness(population_list):
    best_fitness = 0
    indexes = 0

    for i in range(POPULATION_SIZE):
        if best_fitness < population_list[i].fitness:
            best_fitness = population_list[i].fitness

    return best_fitness


def calculate_worst_fitness(population_list):
    worst_fitness = 0

    for i in range(POPULATION_SIZE):
        if worst_fitness > population_list[i].fitness:
            worst_fitness = population_list[i].fitness

    return worst_fitness


def selection_max(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        parent1 = randrange(POPULATION_SIZE)
        parent2 = randrange(POPULATION_SIZE)

        if population_list[parent1].fitness >= population_list[parent2].fitness:
            offspring[i] = population_list[parent1]
        else:
            offspring[i] = population_list[parent2]

    return offspring


def selection_min(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        parent1 = randrange(POPULATION_SIZE)
        parent2 = randrange(POPULATION_SIZE)

        if population_list[parent1].fitness <= population_list[parent2].fitness:
            offspring[i] = population_list[parent1]
        else:
            offspring[i] = population_list[parent2]

    return offspring


def selection_post(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    best_fitness = calculate_best_fitness(population_list)
    worst_fitness = calculate_worst_fitness(population_list)
    temp2 = 2
    for i in range(POPULATION_SIZE):
        if population_list[(i+1)< POPULATION_SIZE].fitness > population_list[i].fitness:
            offspring[i] = population_list[(i+1) < POPULATION_SIZE]
        else:
            offspring[i] = population_list[i]
    return offspring


def cross_over_max(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        temp_gene1 = [None] * GENE_SIZE
        temp_gene2 = [None] * GENE_SIZE
        parent1 = randrange(POPULATION_SIZE)
        parent2 = randrange(POPULATION_SIZE)
        cross_over_point = randrange(GENE_SIZE)

        for j in range(GENE_SIZE):
            if j > cross_over_point:
                temp_gene1[j] = population_list[parent2].gene[j]
                temp_gene2[j] = population_list[parent1].gene[j]
            else:
                temp_gene1[j] = population_list[parent1].gene[j]
                temp_gene2[j] = population_list[parent2].gene[j]

        if calculate_fitness_e1(temp_gene1) >= calculate_fitness_e1(temp_gene2):
            offspring[i].gene = temp_gene1
        else:
            offspring[i].gene = temp_gene2

        offspring[i].fitness = calculate_fitness_e1(offspring[i].gene)

    return offspring


def cross_over_min(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        temp_gene1 = [None] * GENE_SIZE
        temp_gene2 = [None] * GENE_SIZE
        parent1 = randrange(POPULATION_SIZE)
        parent2 = randrange(POPULATION_SIZE)
        cross_over_point = randrange(GENE_SIZE)

        for j in range(GENE_SIZE):
            if j > cross_over_point:
                temp_gene1[j] = population_list[parent2].gene[j]
                temp_gene2[j] = population_list[parent1].gene[j]
            else:
                temp_gene1[j] = population_list[parent1].gene[j]
                temp_gene2[j] = population_list[parent2].gene[j]

        if calculate_fitness_e2(temp_gene1) <= calculate_fitness_e2(temp_gene2):
            offspring[i].gene = temp_gene1
        else:
            offspring[i].gene = temp_gene2

        offspring[i].fitness = calculate_fitness_e2(offspring[i].gene)

    return offspring


def mutation(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            if random() < MUTATION:
                if population_list[i].gene[j] == 0:
                    population_list[i].gene[j] = 1
                else:
                    population_list[i].gene[j] = 0

            offspring[i] = population_list[i]

    return offspring


def main():
    population_list = populate_population_max()
    i =1
    f = open('Mean_Broken_1.txt','w')
    f2 = open('Best_broken_1.txt','w')
    for i in range(50):
        population_list = selection_max(population_list)
        population_list = cross_over_max(population_list)
        population_list = mutation(population_list)
        print(" Gene: " + str(population_list[i].gene))
        print(" Fitness: " + str(population_list[i].fitness))
        print("mean fitness = " + str(calculate_mean_fitness(population_list)))
        print("Best fitness = " + str(calculate_best_fitness(population_list)))
        mean_population=  str(calculate_mean_fitness(population_list))
        f.write(str(mean_population+'\n'))
        best_fitness = str(calculate_mean_fitness(population_list))
        f2.write(best_fitness +'\n')

    f.close()


if __name__ == '__main__':
    main()
