import random
import copy
from collections import Counter


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        self.contents_save = []

        for color in kwargs:
            for x in range(kwargs[color]):
                self.contents.append(str(color))
                self.contents_save.append(str(color))

    def draw(self, sample_size):
        result = []
        self.contents = self.contents_save.copy()

        if sample_size >= len(self.contents):
            result = self.contents.copy()
            del self.contents[:]
        else:
            for _ in range(sample_size):
                index = random.randint(0, len(self.contents)-1)
                result.append(self.contents[index])
                del self.contents[index]
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0.0
    success_counter = 0

    for _ in range(num_experiments):
        sample = hat.draw(num_balls_drawn)
        dict_sample = dict(Counter(sample))
        success = True
        # print("Sample: " + str(dict_sample), end=" -> ")

        for exp_color in expected_balls:
            try:
                if expected_balls[exp_color] <= dict_sample[exp_color]:
                    success &= True
                else:
                    success &= False
                    break
            except:
                success &= False
                break
        # print(success)
        if success:
            success_counter += 1
    return success_counter / num_experiments
