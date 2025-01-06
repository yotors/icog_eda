import random

'''
    Knapsack Problem using Estimation of Distribution Algorithm (EDA)
'''

# Initializing Problem Parameters
capacity = random.uniform(5, 50)
population_size = 10
generations = 30
top_k = 5
n = 10
items = [(random.uniform(1, 5), random.uniform(1, 10)) for _ in range(n)]  # (weight, value) pairs

# Fitness Function: Calculate total value if within capacity, else return 0
def fitness(individual):
    total_weight = sum(items[i][0] for i in range(n) if individual[i] == 1)
    total_value = sum(items[i][1] for i in range(n) if individual[i] == 1)
    return total_value if total_weight <= capacity else 0

# Generate an individual (random binary string)
def random_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

# Generate initial population
def initialize_population(pop_size, n):
    return [random_individual(n) for _ in range(pop_size)]

# Select the top k individuals based on fitness
def select_top_individuals(population, k):
    return sorted(population, key=fitness, reverse=True)[:k]

# Learn probability distribution from selected individuals
def learn_distribution(top_individuals, n):
    probabilities = [0.0] * n
    for i in range(n):
        ones_count = sum(ind[i] for ind in top_individuals)
        probabilities[i] = ones_count / len(top_individuals)
    return probabilities

# Sample new individuals from the learned distribution
def sample_new_individual(probabilities):
    return [1 if random.random() < p else 0 for p in probabilities]

# Main EDA Loop
def eda_knapsack(population_size, generations, top_k):
    population = initialize_population(population_size, n)

    for generation in range(generations):
        top_individuals = select_top_individuals(population, top_k)
        probabilities = learn_distribution(top_individuals, n)
        population = [sample_new_individual(probabilities) for _ in range(population_size)]
        best = max(population, key=fitness)
        if sum(best) > 7:
            break
        print(f"Generation {generation+1}: Best Fitness = {fitness(best)}, Best Individual = {best}")
        print(f"Probabilities = {probabilities}")
        print('-' * 50)
    
    return max(population, key=fitness)

# Run the EDA
best_solution = eda_knapsack(population_size, generations, top_k)
print("\nFinal Best Solution:", best_solution)
print("Final Fitness:", fitness(best_solution))
