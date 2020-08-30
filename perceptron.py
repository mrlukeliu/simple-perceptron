import random


class Perceptron():
    weights = []
    learning_rate = 0.1
    # Assign random weights
    def __init__(self):
        
        i = 0
        while i < 3:
            self.weights.append(random.randint(-1, 1))
            i += 1
    

    def guess(self, inputs):
        sum_of_inputs = 0
        i = 0
        while i < len(inputs):
            sum_of_inputs += inputs[i]*self.weights[i]
            i += 1

        return sign(sum_of_inputs)

    def train(self, inputs, target):
        guessed_int = self.guess(inputs)
        error = target - guessed_int

        # # with zip
        # for weight, input in zip(self.weights, inputs):
        #     weight += error*input*self.learning_rate

        # with while loop
        i = 0
        while i < len(inputs):
            self.weights[i] += error*inputs[i]*self.learning_rate
            i += 1
        
    # activation function
def sign(sum):
    return 1 if sum >= 0 else -1