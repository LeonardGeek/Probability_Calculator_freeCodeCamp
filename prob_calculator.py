import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = [color for color,nballs in balls.items() for i in range(nballs)]
  
  def draw(self, dballs):
    if dballs <= len(self.contents):
        return [self.contents.pop(random.randrange(len(self.contents))) for i in range(dballs)]
    
    else:
        return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0  # how many times m you get at least expected_balls
    for i in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        balls_drawn = experiment_hat.draw(num_balls_drawn)
        check_balls_drawn = sum([1 for color, num_balls in expected_balls.items() if balls_drawn.count(color) >= num_balls])
        if check_balls_drawn == len(expected_balls):
            m += 1
    return m / num_experiments
