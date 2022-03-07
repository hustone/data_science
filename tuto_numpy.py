import numpy as np

random_values = np.random.randint(0, 10, 100)
expectation = np.mean(random_values)
std = np.std(random_values)

if __name__ == "__main__":
    print(expectation)
    print(std)