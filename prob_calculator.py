import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        contents = []
        for key, value in kwargs.items():
            for i in range(value):
                contents.append(key)
        self.contents = contents

    def draw(self, num):
        balls = []
        if num < len(self.contents):
            for i in range(num):
                selection = random.randrange(len(self.contents))
                balls.append(self.contents[selection])
                self.contents.remove(self.contents[selection])
        else:
            balls = self.contents
            self.contents = []
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        balls = temp_hat.draw(num_balls_drawn)
        counts = dict()
        for item in balls:
            counts[item] = counts.get(item, 0) + 1
        check = 0
        for key in list(expected_balls.keys()):
            if key in list(counts.keys()):
                if expected_balls[key] <= counts[key]:
                    check += 1
        if check == len(expected_balls):
            m += 1
    
    prob = m / num_experiments
    return prob
