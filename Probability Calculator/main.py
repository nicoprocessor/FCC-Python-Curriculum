import prob_calculator
from unittest import main

hat = prob_calculator.Hat(blue=3, red=2, green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={
                                         "blue": 2, "green": 1},
                                         num_balls_drawn=4, num_experiments=1000)
# print(len(hat.contents))
print("Probability:", probability)


hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
# print(len(hat.contents))
probability = prob_calculator.experiment(hat=hat, expected_balls={
                                         "yellow": 2, "blue": 3, "test": 1},
                                         num_balls_drawn=20, num_experiments=100)
print("Probability:", probability)

# Run unit tests automatically
# main(module='test_module', exit=False)
