class Experiment:

    def __init__(self, framework, model, optimizer, learning_rate, epsilon, epochs, loss_function, num_gestures, gestures, num_videos):

        self.framework = framework
        self.model = model
        self.optimizer = optimizer
        self.learning_rate  = learning_rate
        self.epsilon = epsilon
        self.epochs = epochs
        self.loss_function = loss_function
        self.num_gestures = num_gestures
        self.gestures = gestures
        self.num_videos = num_videos

    def getFramework(self):
        return self.framework
    
    def getModel(self):
        return self.model

    def getOptimizer(self):
        return self.optimizer

    def getLearning_rate(self):
        return self.learning_rate

    def getEpsilon(self):
        return self.epsilon

    def getEpochs(self):
        return self.epochs

    def getLoss_function(self):
        return self.loss_function

    def getNum_gestures(self):
        return self.num_gestures

    def getGestures(self):
        return self.gestures

    def getNum_videos(self):
        return self.num_videos
    

class Experiment_Metrics:

    def __init__(self, precision, recall, f1_score, support):
        
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
        self.support = support

    def getPrecision(self):
        return self.precision

    def getRecall(self):
        return self.recall

    def getF1_score(self):
        return self.f1_score

    def getSupport(self):
        return self.support


print("Starting the input generation")

exp1 = Experiment_Metrics("1.0", "1.0", "0.86", "98")

print(exp1.getF1_score())
