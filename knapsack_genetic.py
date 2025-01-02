import random

def generate_population(pop_size, chromo_len):
    return [[random.choice([0, 1]) for _ in range(chromo_len)] for _ in range(pop_size)]


def fitness(chromosome, benfits, weights, knapsak_size):
    total_benfit = sum(b * c for b, c in zip(benfits, chromosome))
    total_weights = sum(v * c for v, c in zip(weights, chromosome))
    return total_benfit if total_weights <= knapsak_size else 0

def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    probs = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, weights=probs, k=2)
    return parents

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    return [1 - gene if random.random() < mutation_rate else gene for gene in chromosome]

def genetic_algorithm(benfits, weights, knapsack_size, pop_size=20, generations=100, mutation_rate=0.1):
    chromo_len = len(benfits)
    population = generate_population(pop_size, chromo_len)

    for generation in range(generations):
        fitnesses = [fitness(chromo,benfits,weights,knapsack_size) for chromo in population]
        new_population = []
        while len(new_population) < pop_size:
            parent1, parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))

        population = new_population[:pop_size]

    fitnesses = [fitness(chromo, benfits, weights, knapsack_size) for chromo in population]
    best_index = fitnesses.index(max(fitnesses))
    best_solution = population[best_index]

    return best_solution, fitness(best_solution, benfits, weights, knapsack_size)