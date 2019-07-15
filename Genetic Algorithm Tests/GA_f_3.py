# Matthew Powell's 14034684

import numpy as np
from random import randrange, random, uniform
import math
import csv

# This GA Carries out the minimisation task on a floating point set.

POPULATION_SIZE = 500
GENE_SIZE = 10
MUTATION = 1
# This class designates Individuals as having a Gene variable and a fitness variable
class Individual:
    def __init__(self, gene, fitness):
        self.gene = gene
        self.fitness = fitness

# This function creates a list of individuals and randomly populates them with floating point numbers.
# It then assigns a fitness value to the random string.


def populate_population_floats():

    population_list = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    gene = [None] * GENE_SIZE
    x = 0.00

    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            gene[j] = np.random.uniform(0, 5.12)
        population_list[i].gene = gene
        population_list[i].fitness = calculate_fitness_e3(population_list[i].gene)
        gene = [None] * GENE_SIZE

    return population_list

# This function carries out a mathematical function using each value in the gene string


def calculate_fitness_e3(gene):
    x = sum([(x ** 2 - 10 * np.cos(2 * math.pi * x)) for x in gene])
    y = 10 * len(gene)
    fitness = x + y
    return fitness

# this function adds up all the fitness values and divides it by the population size to get the average


def calculate_mean_fitness(population_list):
    mean_fitness = 0

    for i in range(POPULATION_SIZE):
        mean_fitness += population_list[i].fitness

    return mean_fitness / POPULATION_SIZE

# this function sets a value to find the best fitness  and if a value is higher than it the the
# # best fitness gets that fitness set to it, however as this is a minimisation function this finds the worst value.


def calculate_best_fitness(population_list):
    best_fitness = 0
    indexes = 0

    for i in range(POPULATION_SIZE):
        if best_fitness < population_list[i].fitness:
            best_fitness = population_list[i].fitness

    return best_fitness

# this function sets a value to find the worst fitness  and if a value is lower than it then the
# # worst fitness gets that fitness set to it, however as this is a minimisation function this finds the best value.


def calculate_worst_fitness(population_list):
    worst_fitness = 0

    for i in range(POPULATION_SIZE):
        if worst_fitness > population_list[i].fitness:
            worst_fitness = population_list[i].fitness

    return worst_fitness


# this function selects the best individual from two random parents by comparing fitness values. So for this function
# best is the lowest of the two parents.

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


# this function finds a random position and then swaps the tails of the gene from that random
# position. It then finds the lowest fitness of the switched genes to set the lowest value to the offspring.


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

        if calculate_fitness_e3(temp_gene1) <= calculate_fitness_e3(temp_gene2):
            offspring[i].gene = temp_gene1
        else:
            offspring[i].gene = temp_gene2

        offspring[i].fitness = calculate_fitness_e3(offspring[i].gene)

    return offspring

# This function can change one value of a gene  by creeping if a random value is below a set mutation rate. If the value
# is above 0 it subtracts 1 if it is below 0 it adds 1.


def mutation2(population_list):
    offspring = [Individual(None, None) for _ in range(POPULATION_SIZE)]
    for i in range(POPULATION_SIZE):
        for j in range(GENE_SIZE):
            if random() < MUTATION:
                if population_list[i].gene[j] > 0:
                    population_list[i].gene[j] = population_list[i].gene[j] -1
                else:
                    population_list[i].gene[j] = population_list[i].gene[j] + 1

            offspring[i] = population_list[i]

    return offspring

# The main then produces a population then carries out selection, crossover and mutation on the population
# It then prints out the gene string as well as the fitness of that gene as well as the mean and best value, the mean
# and best (which are the lowest) are also then written into a file to produce graphs afterwards.


def main():
    population_list = populate_population_floats()
    i =1

    f = open('Run_M__2_3.txt','w')
    f2 = open('Run_B_2_3.txt','w')
    for i in range(100):
        population_list = selection_min(population_list)
        population_list = cross_over_min(population_list)
        population_list = mutation2(population_list)
        print(" Gene: " + str(population_list[i].gene))
        print(" Fitness: " + str(population_list[i].fitness))
        print("mean fitness = " + str(calculate_mean_fitness(population_list)))
        print("Best fitness = " + str(calculate_best_fitness(population_list)))
        mean_population=  str(calculate_mean_fitness(population_list))
        f.write(str(mean_population+'\n'))
        best_fitness = str(calculate_best_fitness(population_list))
        f2.write(best_fitness +'\n')

    f.close()


if __name__ == '__main__':
    main()
