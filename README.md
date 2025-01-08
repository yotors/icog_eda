# README: Understanding Univariate and Multivariate Estimation of Distribution Algorithms (EDAs)

## Overview

This document provides an introduction to Estimation of Distribution Algorithms (EDAs), focusing on the concepts of univariate and multivariate EDAs. It explains how these algorithms work, their differences, and their applications in real-world scenarios.

## What is EDA?

Estimation of Distribution Algorithms (EDAs) are optimization algorithms that use probabilistic models to guide the search for optimal solutions. They can be likened to a smart helper that assists in finding the best way to solve a problem by making educated guesses and learning from past attempts.

## How does EDA work?

1. **Guessing**: The algorithm makes an initial guess about a potential solution.
2. **Checking**: It evaluates the quality of this solution using a fitness function.
3. **Learning**: If the solution is good, it updates its knowledge to remember what worked well.
4. **Trying Again**: The algorithm uses this information to generate a new generation which is assumed to perform at least equally well as the previous generations.

## Types of EDAs

### 1. Univariate EDAs

- **Definition**: Univariate EDAs focus on evaluating one variable (or component) at a time, treating each variable independently. Therefore, univariate EDAs rely only on univariate statistics, and multivariate distributions must be factorized as the product of (N) univariate probability distributions.

- **Types of Univariate EDAs**:
    - **Univariate Marginal Distribution Algorithm (UMDA)**: Generates the next population by calculating the mean of the selected individuals from the current population.
    - **Population-Based Incremental Learning (PBIL)**: Incorporates a learning rate to update the mean of the selected individuals, balancing exploration and exploitation.
    - **Compact Genetic Algorithm (CGA)**: Utilizes a probability vector to represent the population and updates it based on the performance of selected individuals, also considering the learning rate.

- **Example**:
    - In the context of the Traveling Salesman Problem (TSP), a univariate EDA would evaluate the distance between individual cities one at a time, without considering the overall route. For example, it would assess the distance from iCog Lab to Mexico, then from Mexico to 4 Kilo, and so on, independently. The distance between iCog Lab and Mexico does not contribute to the distance between Mexico and 4 Kilo.

- **Applications**:
    - **Simple Optimization Problems**: Univariate EDAs are suitable for problems where variables can be evaluated independently without significant interactions.
    - **Basic Genetic Algorithms**: In genetic algorithms, univariate EDAs can be used to optimize individual genes without considering their interactions with other genes.

Univariate EDAs are effective for simpler optimization problems where variable interactions are minimal or non-existent. They provide a straightforward approach to finding optimal solutions by focusing on one variable at a time.

### 2. Multivariate EDAs

- **Definition**: Multivariate EDAs evaluate multiple variables (or components) simultaneously, considering their interactions and dependencies to find optimal solutions. Multivariate distributions are usually represented as probabilistic graphical models (graphs), in which edges denote statistical dependencies (or conditional probabilities) and vertices denote variables.

- **Types of Multivariate EDAs**:
    - **Extended Compact Genetic Algorithm (eCGA)**: Utilizes a compact representation of the population and models dependencies between variables using a probabilistic model. It extends the compact genetic algorithm by incorporating linkage learning to identify and exploit variable interactions.
    - **Bayesian Optimization Algorithm (BOA)**: Employs Bayesian networks to model the dependencies between variables. By sampling from these networks, BOA generates new solutions that account for complex interactions, leading to more robust optimization.
    - **Factorized Distribution Algorithm (FDA)**: Decomposes the problem into smaller subproblems by factorizing the joint probability distribution. This approach allows FDA to efficiently model and optimize variable interactions.
    - **Learning Factorized Distribution Algorithm (LFDA)**: An extension of FDA that incorporates learning mechanisms to improve the factorization process. LFDA adapts the factorization based on the observed data, enhancing the optimization performance.
    - **Dependency Structure Matrix Genetic Algorithm (DSMGA)**: Uses a dependency structure matrix to capture and exploit variable dependencies. DSMGA identifies and preserves important variable interactions, leading to more effective optimization.

Multivariate EDAs leverage these advanced models to capture and utilize variable dependencies, providing powerful tools for solving complex optimization problems.
- **Example**:
    - In iCog Labs, a multivariate EDA would evaluate the entire set of robotic components by considering the interactions between different parts. For instance, it would assess the combination of sensors, actuators, and control algorithms collectively, taking into account the overall performance and efficiency of the robot rather than evaluating each component independently.

- **Modeling Dependencies**:
    - Multivariate EDAs model dependencies between variables by capturing joint distributions. This approach allows the algorithm to better represent interactions between variables, leading to more accurate and effective optimization.
    - **Example**: The Bayesian Optimization Algorithm (BOA) uses a Bayesian network to model the dependencies between variables. By sampling from this network, BOA generates solutions that account for the complex interactions between variables, leading to more robust and optimal outcomes.

- **Applications**:
    - **Robotics**: In robotics, multivariate EDAs can optimize the combination of different sensors and actuators to achieve desired behaviors. For example, a robot might learn the best combination of movements and sensor inputs to navigate through an obstacle course efficiently.
    - **Genetic Research**: In genetic research, multivariate EDAs can identify combinations of genetic markers that contribute to specific traits or diseases. By considering the interactions between multiple genes, researchers can gain deeper insights into genetic influences on health.

Multivariate EDAs are powerful tools for tackling complex optimization problems where variable interactions play a crucial role. By capturing and leveraging these interactions, they provide more accurate and effective solutions compared to univariate approaches.

## Key Differences Between Univariate and Multivariate EDAs

| Feature             | Univariate EDA                     | Multivariate EDA                 |
|---------------------|------------------------------------|----------------------------------|
| Focus               | One variable at a time             | Combinations of variables        |
| Speed               | Generally faster                   | May take more time               |
| Best for            | Simple problems                    | Complex problems with interactions|

## Conclusion

Estimation of Distribution Algorithms (EDAs) are powerful tools for optimization, akin to stacking blocks to build a tall tower. They help find optimal solutions through a process of guessing, checking, learning, and iterating. Whether used for robotics at iCog Labs or library organization at Addis Ababa University, EDAs enhance problem-solving efficiency.

## References

- [Estimation of Distribution Algorithms](https://en.wikipedia.org/wiki/Estimation_of_distribution_algorithm)
