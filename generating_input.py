import csv

class Experiment:

    def __init__(self, id, framework, model, optimizer, learning_rate, epsilon, epochs, loss_function, num_gestures, gesture_names, num_videos):

        self.id = id
        self.framework = framework
        self.model = model
        self.optimizer = optimizer
        self.learning_rate  = learning_rate
        self.epsilon = epsilon
        self.epochs = epochs
        self.loss_function = loss_function
        self.num_gestures = num_gestures
        # This attribute is a list
        self.gesture_names = gesture_names
        self.num_videos = num_videos

    def getId(self):
        return self.id

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

    def getGesture_names(self):
        return self.gesture_names

    def getNum_videos(self):
        return self.num_videos

    def writeNewFile(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Id', 'Framework', 'Model', 'Optimizer', 'Learning_rate', 'Epsilon', 'Epochs', 'Loss_function', 'Num_gestures', 'Gestures', 'Num_videos']
            writer = csv.writer(csvfile, delimiter=';')
            # Writing the header
            writer.writerow(fieldnames) 
            # Writing the content
            row = [self.getId(), self.getFramework(), self.getModel(), self.getOptimizer(), self.getLearning_rate(), self.getEpsilon(), self.getEpochs(), self.getLoss_function(), self.getNum_gestures(), self.getGestures(), self.getNum_videos()]
            writer.writerow(row)

    def append_row(self, filename, row):
        # Open file in append mode
        with open(filename,'a+', newline='') as csvfile:
            # Create a writer object from csv module
            writer = csv.writer(csvfile, delimiter=';')
            # Add contents of list as last row in the csv file
            writer.writerow(row)
    
    def print(self):
        data = "Id: " + self.id +  " " + "Framework: " + self.framework + " " + "Model: " + self.model + " " + "Optimizer: " + self.optimizer + " " + "Loss_function: " + self.loss_function
        print(data)
    

class Experiment_Metrics:

    def __init__(self, id, gestures):
        
        self.id = id
        # This attribute is a list
        self.gestures = gestures

    def getId(self):
        return self.id
    
    def getGestures(self):
        return self.gestures

class Gesture:

    def __init__(self, name, precision, recall, f1_score, support):
        
        self.name = name
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
        self.support = support

    def getName(self):
        return self.name

    def getPrecision(self):
        return self.precision

    def getRecall(self):
        return self.recall

    def getF1_score(self):
        return self.f1_score

    def getSupport(self):
        return self.support

# Input folder path
input_path = "input/"
# File to store the experiments characteristics
filename_exp = "experiments.csv"
filenameExp_path = input_path + filename_exp
# File to store the experiments metrics
filename_metrics = "experiments_metrics.csv"
filenameMetrics_path = input_path + filename_metrics


print("Starting the input generation")

# Adding the experiments
gestures_3g = ["swipe_left", "thumb_up", "stop_sign"]
gestures_5g = ["swipe_left", "thumb_up", "stop_sign", "swipe_down", "slide_2_fingers_right"]
gestures_8g = ["swipe_left", "thumb_up", "stop_sign", "swipe_down", "slide_2_fingers_right", "slide_2_fingers_up", "zoom_in_with_2_fingers", "pull_hand_in"]
gestures_10g = ["swipe_left", "thumb_up", "stop_sign", "swipe_down", "slide_2_fingers_right", "slide_2_fingers_up", "zoom_in_with_2_fingers", "pull_hand_in", "zoom_in_with_full_hand", "zoom_out_with_2_fingers"]

exp_1 = Experiment("1", "Keras", "ResNet50", "Adam", "0.001", "1.0", "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_4 = Experiment("4", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_7 = Experiment("7", "Keras", "ResNet50V2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_11 = Experiment("11", "Keras", "ResNet50", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_15 = Experiment("15", "Keras", "ResNet101V2", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_22 = Experiment("22", "Keras", "VGG16", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_24 = Experiment("24", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_27 = Experiment("27", "Keras", "VGG19", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_30 = Experiment("30", "Keras", "InceptionV3", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_33 = Experiment("33", "Keras", "InceptionResNetV2", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_34 = Experiment("34", "Keras", "MobileNetV2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_37 = Experiment("37", "Keras", "DenseNet121", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_38 = Experiment("38", "Keras", "DenseNet169", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_41 = Experiment("41", "Keras", "DenseNet201", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_42 = Experiment("42", "Keras", "NasNetLarge", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_51 = Experiment("51", "Keras", "ResNet152", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_54 = Experiment("54", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "5", gestures_5g, "10")
exp_56 = Experiment("56", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "5", gestures_5g, "10")
exp_59 = Experiment("59", "Keras", "ResNet152", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_69 = Experiment("69", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "8", gestures_8g, "10")
exp_71 = Experiment("71", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "8", gestures_8g, "10")
exp_73 = Experiment("73", "Keras", "ResNet101", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_75 = Experiment("75", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_76 = Experiment("76", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_82 = Experiment("82", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_85 = Experiment("85", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "10", gestures_10g, "10")
exp_88 = Experiment("88", "Keras", "ResNet152", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_89 = Experiment("89", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")

# Adding the metrics
swipe_left1 = Gesture("swipe_left", )





# Testing write files
exp_test.writeNewFile(filenameExp_path)

print(exp1.getF1_score())

# Reading the file
with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in reader:
        print("New row: ", row)
        for item in row:
            print("New item: ", item)
        
