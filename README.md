# README: Understanding Univariate and Multivariate Estimation of Distribution Algorithms (EDAs)

## Overview

This document provides an introduction to Estimation of Distribution Algorithms (EDAs), focusing on the concepts of univariate and multivariate EDAs. It explains how these algorithms work, their differences, and their applications in real-world scenarios.

## What is EDA?

Estimation of Distribution Algorithms (EDAs) are optimization algorithms that use probabilistic models to guide the search for optimal solutions. They can be likened to a smart helper that assists in finding the best way to solve a problem by making educated guesses and learning from past attempts.

## How does EDA work?

1. **Guessing**: The algorithm makes an initial guess about a potential solution.
2. **Checking**: It evaluates the quality of this solution. Using a fitness function.
3. **Learning**: If the solution is good, it updates its knowledge to remember what worked well and .
4. **Trying Again**: The algorithm uses this information to generate a new generation which is assumed to be atleast equally perform with the previous generations.

## Types of EDAs

### 1. Univariate EDAs

- **Definition**: Univariate EDAs focus on evaluating one variable (or component) at a time, treating each variable independently.

- **Process**:
    - **Exploration**: These algorithms assess each variable independently to determine its contribution to the overall solution. One variable does not contribute to or affect any other.
    - **Fitness Evaluation**: The fitness of each variable is evaluated separately, without considering interactions with other variables.
    - **Learning and Updating**: The algorithm updates its probabilistic model based on the fitness evaluations of individual variables, refining its understanding to improve future generations of solutions.

- **Example**:
    - In the context of the Traveling Salesman Problem (TSP), a univariate EDA would evaluate the distance between individual cities one at a time, without considering the overall route. For example, it would assess the distance from iCog Lab to Mexico, then from Mexico to 4 Kilo, and so on, independently. The distance between iCog Lab and Mexico does not contribute to the distance between Mexico and 4 Kilo.

- **Applications**:
    - **Simple Optimization Problems**: Univariate EDAs are suitable for problems where variables can be evaluated independently without significant interactions.
    - **Basic Genetic Algorithms**: In genetic algorithms, univariate EDAs can be used to optimize individual genes without considering their interactions with other genes.

Univariate EDAs are effective for simpler optimization problems where variable interactions are minimal or non-existent. They provide a straightforward approach to finding optimal solutions by focusing on one variable at a time.

### 2. Multivariate EDAs

- **Definition**: Multivariate EDAs evaluate multiple variables (or components) simultaneously, considering their interactions and dependencies to find optimal solutions.

- **Process**:
    - **Exploration**: These algorithms explore combinations of variables to identify interactions that lead to better solutions. Unlike univariate EDAs, multivariate EDAs do not treat variables independently but rather evaluate them in the context of other variables.
    - **Fitness Evaluation**: The fitness of a variable is assessed based on its interaction with other variables. This holistic approach allows the algorithm to capture complex relationships and dependencies between variables.
    - **Learning and Updating**: The algorithm updates its probabilistic model based on the fitness evaluations, refining its understanding of variable interactions to improve future generations of solutions.

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

