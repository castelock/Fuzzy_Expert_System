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
            row = [self.getId(), self.getFramework(), self.getModel(), self.getOptimizer(), self.getLearning_rate(), self.getEpsilon(), self.getEpochs(), self.getLoss_function(), self.getNum_gestures(), self.getGesture_names(), self.getNum_videos()]
            writer.writerow(row)

    def append_row(self, filename):
        # Open file in append mode
        with open(filename,'a+', newline='') as csvfile:
            # Create a writer object from csv module
            writer = csv.writer(csvfile, delimiter=';')
            # Add contents of list as last row in the csv file
            row = [self.getId(), self.getFramework(), self.getModel(), self.getOptimizer(), self.getLearning_rate(), self.getEpsilon(), self.getEpochs(), self.getLoss_function(), self.getNum_gestures(), self.getGesture_names(), self.getNum_videos()]
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

    def writeNewFile(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Id', 'Gesture', 'Precision', 'Recall', 'F1_score', 'Support']
            writer = csv.writer(csvfile, delimiter=';')
            # Writing the header
            writer.writerow(fieldnames) 
            # Writing the gestures
            gestures_list = self.getGestures()
            for gesture in gestures_list:
                row = [gesture.getId(), gesture.getName(), gesture.getPrecision(), gesture.getRecall(), gesture.getF1_score(), gesture.getSupport()]
                writer.writerow(row)            

    def append_row(self, filename):
        # Open file in append mode
        with open(filename,'a+', newline='') as csvfile:
            # Create a writer object from csv module
            writer = csv.writer(csvfile, delimiter=';')
            # Writing the gestures
            gestures_list = self.getGestures()
            for gesture in gestures_list:
                row = [gesture.getId(), gesture.getName(), gesture.getPrecision(), gesture.getRecall(), gesture.getF1_score(), gesture.getSupport()]
                writer.writerow(row) 

class Gesture:

    def __init__(self, id, name, precision, recall, f1_score, support):
        
        self.id = id
        self.name = name
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
        self.support = support

    def getId(self):
        return self.id
    
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

# Adding the metrics gesture
stop_sign1 = Gesture("1", "stop_sign", "1.0", "0.3", "0.46", "90.0")
swipe_left1 = Gesture("1", "swipe_left", "0.92", "0.89", "0.9", "123.0")
thumb_up1 = Gesture("1", "thumb_up", "0.55", "0.99", "0.71", "86.0")
gestures_1 = [stop_sign1, swipe_left1, thumb_up1]

stop_sign4 = Gesture("4", "stop_sign", "0.82", "0.72", "0.77", "90.0")
swipe_left4 = Gesture("4", "swipe_left", "0.82", "0.95", "0.88", "123.0")
thumb_up4 = Gesture("4", "thumb_up", "0.88", "0.79", "0.83", "86.0")
gestures_4 = [stop_sign4, swipe_left4, thumb_up4]

stop_sign7 = Gesture("7", "stop_sign", "0.06", "0.04", "0.05", "90.0")
swipe_left7 = Gesture("7", "swipe_left", "0.0", "0.0", "0.0", "123.0")
thumb_up7 = Gesture("7", "thumb_up", "0.26", "0.72", "0.39", "86.0")
gestures_7 = [stop_sign7, swipe_left7, thumb_up7]

stop_sign11 = Gesture("11", "stop_sign", "1.0", "0.22", "0.36", "90.0")
swipe_left11 = Gesture("11", "swipe_left", "0.68", "0.87", "0.76", "123.0")
thumb_up11 = Gesture("11", "thumb_up", "0.61", "0.86", "0.71", "86.0")
gestures_11 = [stop_sign11, swipe_left11, thumb_up11]

stop_sign15 = Gesture("15", "stop_sign", "0.36", "0.97", "0.52", "90.0")
swipe_left15 = Gesture("15", "swipe_left", "0.23", "0.03", "0.06", "88.0")
thumb_up15 = Gesture("15", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_15 = [stop_sign15, swipe_left15, thumb_up15]

stop_sign22 = Gesture("22", "stop_sign", "0.93", "0.97", "0.95", "90.0")
swipe_left22 = Gesture("22", "swipe_left", "0.88", "0.98", "0.92", "88.0")
thumb_up22 = Gesture("22", "thumb_up", "0.96", "0.8", "0.87", "86.0")
gestures_22 = [stop_sign22, swipe_left22, thumb_up22]

stop_sign24 = Gesture("24", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left24 = Gesture("24", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up24 = Gesture("24", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_24 = [stop_sign24, swipe_left24, thumb_up24]

stop_sign27 = Gesture("27", "stop_sign", "0.99", "0.97", "0.98", "90.0")
swipe_left27 = Gesture("27", "swipe_left", "0.98", "0.99", "0.98", "123.0")
thumb_up27 = Gesture("27", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_27 = [stop_sign27, swipe_left27, thumb_up27]

stop_sign30 = Gesture("30", "stop_sign", "0.02", "0.01", "0.02", "90.0")
swipe_left30 = Gesture("30", "swipe_left", "0.32", "0.81", "0.46", "88.0")
thumb_up30 = Gesture("30", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_30 = [stop_sign30, swipe_left30, thumb_up30]

stop_sign33 = Gesture("33", "stop_sign", "0.34", "1.0", "0.51", "90.0")
swipe_left33 = Gesture("33", "swipe_left", "0.0", "0.0", "0.0", "88.0")
thumb_up33 = Gesture("33", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_33 = [stop_sign33, swipe_left33, thumb_up33]

stop_sign34 = Gesture("34", "stop_sign", "0.36", "0.39", "0.38", "90.0")
swipe_left34 = Gesture("34", "swipe_left", "1.0", "0.08", "0.15", "88.0")
thumb_up34 = Gesture("34", "thumb_up", "0.34", "0.63", "0.44", "86.0")
gestures_34 = [stop_sign34, swipe_left34, thumb_up34]

stop_sign37 = Gesture("37", "stop_sign", "0.38", "0.03", "0.06", "90.0")
swipe_left37 = Gesture("37", "swipe_left", "1.0", "0.01", "0.02", "88.0")
thumb_up37 = Gesture("37", "thumb_up", "0.32", "0.94", "0.48", "86.0")
gestures_37 = [stop_sign37, swipe_left37, thumb_up37]

stop_sign38 = Gesture("38", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left38 = Gesture("38", "swipe_left", "0.4", "0.92", "0.56", "123.0")
thumb_up38 = Gesture("38", "thumb_up", "0.37", "0.08", "0.13", "86.0")
gestures_38 = [stop_sign38, swipe_left38, thumb_up38]

stop_sign41 = Gesture("41", "stop_sign", "0.38", "0.06", "0.1", "90.0")
swipe_left41 = Gesture("41", "swipe_left", "1.0", "0.11", "0.2", "88.0")
thumb_up41 = Gesture("41", "thumb_up", "0.34", "0.94", "0.5", "86.0")
gestures_41 = [stop_sign41, swipe_left41, thumb_up41]

stop_sign42 = Gesture("42", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left42 = Gesture("42", "swipe_left", "0.18", "0.05", "0.07", "88.0")
thumb_up42 = Gesture("42", "thumb_up", "0.32", "0.87", "0.47", "86.0")
gestures_42 = [stop_sign42, swipe_left42, thumb_up42]

slide_2_fingers_right51 = Gesture("51", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
stop_sign51 = Gesture("51", "stop_sign", "0.88", "0.84", "0.86", "90.0")
swipe_down51 = Gesture("51", "swipe_down", "1.0", "0.03", "0.07", "87.0")
swipe_left51 = Gesture("51", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up51 = Gesture("51", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_51 = [slide_2_fingers_right51, stop_sign51, swipe_down51, swipe_left51, thumb_up51]

slide_2_fingers_right54 = Gesture("54", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign54 = Gesture("54", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down54 = Gesture("54", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left54 = Gesture("54", "swipe_left", "1.0", "1.0", "1.0", "87.0")
thumb_up54 = Gesture("54", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_54 = [slide_2_fingers_right54, stop_sign54, swipe_down54, swipe_left54, thumb_up54]

slide_2_fingers_right56 = Gesture("56", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
stop_sign56 = Gesture("56", "stop_sign", "0.24", "0.16", "0.19", "90.0")
swipe_down56 = Gesture("56", "swipe_down", "0.0", "0.0", "0.0", "87.0")
swipe_left56 = Gesture("56", "swipe_left", "0.44", "0.29", "0.35", "87.0")
thumb_up56 = Gesture("56", "thumb_up", "0.23", "0.84", "0.36", "86.0")
gestures_56 = [slide_2_fingers_right56, stop_sign56, swipe_down56, swipe_left56, thumb_up56]

slide_2_fingers_right59 = Gesture("59", "slide_2_fingers_right", "0.96", "0.53", "0.68", "89.0")
stop_sign59 = Gesture("59", "stop_sign", "0.95", "0.89", "0.92", "90.0")
swipe_down59 = Gesture("59", "swipe_down", "1.0", "0.21", "0.34", "87.0")
swipe_left59 = Gesture("59", "swipe_left", "0.69", "0.84", "0.76", "87.0")
thumb_up59 = Gesture("59", "thumb_up", "0.47", "0.99", "0.63", "86.0")
gestures_59 = [slide_2_fingers_right59, stop_sign59, swipe_down59, swipe_left59, thumb_up59]

pull_hand_in69 = Gesture("69", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right69 = Gesture("69", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up69 = Gesture("69", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign69 = Gesture("69", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down69 = Gesture("69", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left69 = Gesture("69", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up69 = Gesture("69", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers69 = Gesture("69", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_69 = [pull_hand_in69, slide_2_fingers_right69, slide_2_fingers_up69, stop_sign69, swipe_down69, swipe_left69, thumb_up69, zoom_in_with_2_fingers69]

pull_hand_in71 = Gesture("71", "pull_hand_in", "0.25", "0.44", "0.32", "90.0")
slide_2_fingers_right71 = Gesture("71", "slide_2_fingers_right", "0.22", "0.21", "0.21", "89.0")
slide_2_fingers_up71 = Gesture("71", "slide_2_fingers_up", "0.33", "0.22", "0.26", "88.0")
stop_sign71 = Gesture("71", "stop_sign", "0.33", "0.29", "0.31", "90.0")
swipe_down71 = Gesture("71", "swipe_down", "0.55", "0.13", "0.21", "86.0")
swipe_left71 = Gesture("71", "swipe_left", "0.22", "0.52", "0.31", "88.0")
thumb_up71 = Gesture("71", "thumb_up", "0.0", "0.0", "0.0", "86.0")
zoom_in_with_2_fingers71 = Gesture("71", "zoom_in_with_2_fingers", "0.4", "0.42", "0.41", "91.0")
gestures_71 = [pull_hand_in71, slide_2_fingers_right71, slide_2_fingers_up71, stop_sign71, swipe_down71, swipe_left71, thumb_up71, zoom_in_with_2_fingers71]

pull_hand_in73 = Gesture("73", "pull_hand_in", "0.97", "0.39", "0.56", "90.0")
slide_2_fingers_right73 = Gesture("73", "slide_2_fingers_right", "1.0", "0.11", "0.2", "89.0")
slide_2_fingers_up73 = Gesture("73", "slide_2_fingers_up", "0.67", "0.66", "0.66", "88.0")
stop_sign73 = Gesture("73", "stop_sign", "0.91", "0.43", "0.59", "90.0")
swipe_down73 = Gesture("73", "swipe_down", "1.0", "0.02", "0.05", "86.0")
swipe_left73 = Gesture("73", "swipe_left", "0.67", "0.91", "0.77", "88.0")
thumb_up73 = Gesture("73", "thumb_up", "0.22", "1.0", "0.36", "86.0")
zoom_in_with_2_fingers73 = Gesture("73", "zoom_in_with_2_fingers", "1.0", "0.23", "0.38", "91.0")
gestures_73 = [pull_hand_in73, slide_2_fingers_right73, slide_2_fingers_up73, stop_sign73, swipe_down73, swipe_left73, thumb_up73, zoom_in_with_2_fingers73]


pull_hand_in75 = Gesture("75", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
slide_2_fingers_right75 = Gesture("75", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
slide_2_fingers_up75 = Gesture("75", "slide_2_fingers_up", "0.98", "0.99", "0.98", "88.0")
stop_sign75 = Gesture("75", "stop_sign", "0.99", "0.99", "0.99", "90.0")
swipe_down75 = Gesture("75", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left75 = Gesture("75", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up75 = Gesture("75", "thumb_up", "1.0", "0.99", "0.99", "86.0")
zoom_in_with_2_fingers75 = Gesture("75", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_75 = [pull_hand_in75, slide_2_fingers_right75, slide_2_fingers_up75, stop_sign75, swipe_down75, swipe_left75, thumb_up75, zoom_in_with_2_fingers75]

pull_hand_in76 = Gesture("76", "pull_hand_in", "0.99", "0.96", "0.97", "90.0")
slide_2_fingers_right76 = Gesture("76", "slide_2_fingers_right", "0.99", "0.99", "0.99", "89.0")
slide_2_fingers_up76 = Gesture("76", "slide_2_fingers_up", "1.0", "0.94", "0.97", "88.0")
stop_sign76 = Gesture("76", "stop_sign", "0.91", "0.99", "0.95", "90.0")
swipe_down76 = Gesture("76", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left76 = Gesture("76", "swipe_left", "0.95", "1.0", "0.97", "88.0")
thumb_up76 = Gesture("76", "thumb_up", "1.0", "0.93", "0.96", "86.0")
zoom_in_with_2_fingers76 = Gesture("76", "zoom_in_with_2_fingers", "0.99", "1.0", "0.99", "91.0")
gestures_76 = [pull_hand_in76, slide_2_fingers_right76, slide_2_fingers_up76, stop_sign76, swipe_down76, swipe_left76, thumb_up76, zoom_in_with_2_fingers76]

pull_hand_in82 = Gesture("82", "pull_hand_in", "0.82", "0.97", "0.89", "90.0")
slide_2_fingers_right82 = Gesture("82", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
slide_2_fingers_up82 = Gesture("82", "slide_2_fingers_up", "0.95", "0.95", "0.95", "88.0")
stop_sign82 = Gesture("82", "stop_sign", "0.7", "0.97", "0.81", "90.0")
swipe_down82 = Gesture("82", "swipe_down", "0.98", "0.64", "0.77", "86.0")
swipe_left82 = Gesture("82", "swipe_left", "0.92", "0.88", "0.9", "88.0")
thumb_up82 = Gesture("82", "thumb_up", "0.97", "0.9", "0.93", "86.0")
zoom_in_with_2_fingers82 = Gesture("82", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand82 = Gesture("82", "zoom_in_with_full_hand", "0.94", "0.88", "0.91", "90.0")
zoom_out_with_2_fingers82 = Gesture("82", "zoom_out_with_2_fingers", "0.89", "0.85", "0.87", "88.0")
gestures_82 = [pull_hand_in82, slide_2_fingers_right82, slide_2_fingers_up82, stop_sign82, swipe_down82, swipe_left82, thumb_up82, zoom_in_with_2_fingers82, zoom_in_with_full_hand82, zoom_out_with_2_fingers82]

pull_hand_in85 = Gesture("85", "pull_hand_in", "0.99", "1.0", "0.99", "90.0")
slide_2_fingers_right85 = Gesture("85", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up85 = Gesture("85", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign85 = Gesture("85", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down85 = Gesture("85", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left85 = Gesture("85", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up85 = Gesture("85", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers85 = Gesture("85", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand85 = Gesture("85", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "90.0")
zoom_out_with_2_fingers85 = Gesture("85", "zoom_out_with_2_fingers", "1.0", "0.99", "0.99", "88.0")
gestures_85 = [pull_hand_in85, slide_2_fingers_right85, slide_2_fingers_up85, stop_sign85, swipe_down85, swipe_left85, thumb_up85, zoom_in_with_2_fingers85, zoom_in_with_full_hand85, zoom_out_with_2_fingers85]

pull_hand_in88 = Gesture("88", "pull_hand_in", "0.62", "0.81", "0.7", "90.0")
slide_2_fingers_right88 = Gesture("88", "slide_2_fingers_right", "1.0", "0.37", "0.54", "89.0")
slide_2_fingers_up88 = Gesture("88", "slide_2_fingers_up", "0.65", "0.68", "0.67", "88.0")
stop_sign88 = Gesture("88", "stop_sign", "0.89", "0.53", "0.67", "90.0")
swipe_down88 = Gesture("88", "swipe_down", "1.0", "0.1", "0.19", "86.0")
swipe_left88 = Gesture("88", "swipe_left", "0.76", "0.77", "0.77", "88.0")
thumb_up88 = Gesture("88", "thumb_up", "0.47", "0.87", "0.61", "86.0")
zoom_in_with_2_fingers88 = Gesture("88", "zoom_in_with_2_fingers", "1.0", "0.46", "0.63", "91.0")
zoom_in_with_full_hand88 = Gesture("88", "zoom_in_with_full_hand", "1.0", "0.3", "0.46", "87.0")
zoom_out_with_2_fingers88 = Gesture("88", "zoom_out_with_2_fingers", "0.32", "0.94", "0.48", "89.0")
gestures_88 = [pull_hand_in88, slide_2_fingers_right88, slide_2_fingers_up88, stop_sign88, swipe_down88, swipe_left88, thumb_up88, zoom_in_with_2_fingers88, zoom_in_with_full_hand88, zoom_out_with_2_fingers88]


pull_hand_in89 = Gesture("89", "pull_hand_in", "0.98", "0.98", "0.98", "90.0")
slide_2_fingers_right89 = Gesture("89", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
slide_2_fingers_up89 = Gesture("89", "slide_2_fingers_up", "0.99", "1.0", "0.99", "88.0")
stop_sign89 = Gesture("89", "stop_sign", "0.97", "0.99", "0.98", "90.0")
swipe_down89 = Gesture("89", "swipe_down", "0.99", "0.98", "0.98", "86.0")
swipe_left89 = Gesture("89", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up89 = Gesture("89", "thumb_up", "0.47", "0.87", "0.61", "86.0")
zoom_in_with_2_fingers89 = Gesture("89", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand89 = Gesture("89", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "90.0")
zoom_out_with_2_fingers89 = Gesture("89", "zoom_out_with_2_fingers", "0.98", "0.94", "0.96", "88.0")
gestures_89 = [pull_hand_in89, slide_2_fingers_right89, slide_2_fingers_up89, stop_sign89, swipe_down89, swipe_left89, thumb_up89, zoom_in_with_2_fingers89, zoom_in_with_full_hand89, zoom_out_with_2_fingers89]

# Adding the experiments metrics 

exp1_metrics = Experiment_Metrics("1", gestures_1)
exp4_metrics = Experiment_Metrics("4", gestures_4)
exp7_metrics = Experiment_Metrics("7", gestures_7)
exp11_metrics = Experiment_Metrics("11", gestures_11)
exp15_metrics = Experiment_Metrics("15", gestures_15)
exp22_metrics = Experiment_Metrics("22", gestures_22)
exp24_metrics = Experiment_Metrics("24", gestures_24)
exp27_metrics = Experiment_Metrics("27", gestures_27)
exp30_metrics = Experiment_Metrics("30", gestures_30)
exp33_metrics = Experiment_Metrics("33", gestures_33)
exp34_metrics = Experiment_Metrics("34", gestures_34)
exp37_metrics = Experiment_Metrics("37", gestures_37)
exp38_metrics = Experiment_Metrics("38", gestures_38)
exp41_metrics = Experiment_Metrics("41", gestures_41)
exp42_metrics = Experiment_Metrics("42", gestures_42)
exp51_metrics = Experiment_Metrics("51", gestures_51)
exp54_metrics = Experiment_Metrics("54", gestures_54)
exp56_metrics = Experiment_Metrics("56", gestures_56)
exp59_metrics = Experiment_Metrics("59", gestures_59)
exp69_metrics = Experiment_Metrics("69", gestures_69)
exp71_metrics = Experiment_Metrics("71", gestures_71)
exp73_metrics = Experiment_Metrics("73", gestures_73)
exp75_metrics = Experiment_Metrics("75", gestures_75)
exp76_metrics = Experiment_Metrics("76", gestures_76)
exp82_metrics = Experiment_Metrics("82", gestures_82)
exp85_metrics = Experiment_Metrics("85", gestures_85)
exp88_metrics = Experiment_Metrics("88", gestures_88)
exp89_metrics = Experiment_Metrics("89", gestures_89)


# Writing the experiments
exp_1.writeNewFile(filenameExp_path)
exp_4.append_row(filenameExp_path)
exp_7.append_row(filenameExp_path)
exp_11.append_row(filenameExp_path)
exp_15.append_row(filenameExp_path)
exp_22.append_row(filenameExp_path)
exp_24.append_row(filenameExp_path)
exp_27.append_row(filenameExp_path)
exp_30.append_row(filenameExp_path)
exp_33.append_row(filenameExp_path)
exp_34.append_row(filenameExp_path)
exp_37.append_row(filenameExp_path)
exp_38.append_row(filenameExp_path)
exp_41.append_row(filenameExp_path)
exp_42.append_row(filenameExp_path)
exp_51.append_row(filenameExp_path)
exp_54.append_row(filenameExp_path)
exp_56.append_row(filenameExp_path)
exp_59.append_row(filenameExp_path)
exp_69.append_row(filenameExp_path)
exp_71.append_row(filenameExp_path)
exp_73.append_row(filenameExp_path)
exp_75.append_row(filenameExp_path)
exp_76.append_row(filenameExp_path)
exp_82.append_row(filenameExp_path)
exp_85.append_row(filenameExp_path)
exp_88.append_row(filenameExp_path)
exp_89.append_row(filenameExp_path)

# Writing the experiments metrics
exp1_metrics.writeNewFile(filenameMetrics_path)
exp4_metrics.append_row(filenameMetrics_path)
exp7_metrics.append_row(filenameMetrics_path)
exp11_metrics.append_row(filenameMetrics_path)
exp15_metrics.append_row(filenameMetrics_path)
exp22_metrics.append_row(filenameMetrics_path)
exp24_metrics.append_row(filenameMetrics_path)
exp27_metrics.append_row(filenameMetrics_path)
exp30_metrics.append_row(filenameMetrics_path)
exp33_metrics.append_row(filenameMetrics_path)
exp34_metrics.append_row(filenameMetrics_path)
exp37_metrics.append_row(filenameMetrics_path)
exp38_metrics.append_row(filenameMetrics_path)
exp41_metrics.append_row(filenameMetrics_path)
exp42_metrics.append_row(filenameMetrics_path)
exp51_metrics.append_row(filenameMetrics_path)
exp54_metrics.append_row(filenameMetrics_path)
exp56_metrics.append_row(filenameMetrics_path)
exp59_metrics.append_row(filenameMetrics_path)
exp69_metrics.append_row(filenameMetrics_path)
exp71_metrics.append_row(filenameMetrics_path)
exp73_metrics.append_row(filenameMetrics_path)
exp75_metrics.append_row(filenameMetrics_path)
exp76_metrics.append_row(filenameMetrics_path)
exp82_metrics.append_row(filenameMetrics_path)
exp85_metrics.append_row(filenameMetrics_path)
exp88_metrics.append_row(filenameMetrics_path)
exp89_metrics.append_row(filenameMetrics_path)

# READING THE FILES

# Reading the experiments features
with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)
    # Initializing the list of experiments
    list_exp = []
    for row in reader:
        experiment = Experiment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        list_exp.append(experiment)

# Reading the experiments metrics
with open(filenameMetrics_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)
    # Initializing the list of experiments
    list_metrics = []
    list_gestures = []
    prev_id = -1
    for row in reader:
        # Check if current gesture id is the same than the previous one
        if row[0] == prev_id or prev_id == -1:
            # Adding a new gesture
            gesture = Gesture(row[0], row[1], row[2], row[3], row[4], row[5])
            list_gestures.append(gesture)
            prev_id = row[0]
        else:
            if list_gestures is not None:
                # Creating a new metric
                metric = Experiment_Metrics(prev_id, list_gestures)
                list_metrics.append(metric)
                # Adding the current gesture
                list_gestures = []
                gesture = Gesture(row[0], row[1], row[2], row[3], row[4], row[5])
                list_gestures.append(gesture)
                prev_id = row[0]
            else:
                print("ERROR: The gestures list is empty")
    # Including the last metric
    metric = Experiment_Metrics(prev_id, list_gestures)
    list_metrics.append(metric)
    
print("READING is over")
# Reading the file
"""with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in reader:
        print("New row: ", row)
        for item in row:
            print("New item: ", item)"""
        
