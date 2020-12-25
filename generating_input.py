import csv
import statistics

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
                
    # Calculate the mean of the gestures metrics per experiment
    def calculateMean(self):
        gestures_list = self.getGestures()
        sum_precision = 0
        sum_recall = 0
        sum_f1score = 0
        data_precision = []
        data_recall = []
        data_f1score = []
        for gesture in gestures_list:
            """sum_precision += gesture.precision
            sum_recall += gesture.recall
            sum_f1score += gesture.f1_score"""

            data_precision.append(float(gesture.precision))
            data_recall.append(float(gesture.recall))
            data_f1score.append(float(gesture.f1_score))

        
        mean_precision = statistics.mean(data_precision)
        mean_recall = statistics.mean(data_recall)
        mean_f1score = statistics.mean(data_f1score)

        # TO DO
        # print("Mean: ",mean_precision +" "+mean_recall+" "+mean_f1score)

        return mean_precision, mean_recall, mean_f1score

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
exp_2 = Experiment("2", "Keras", "ResNet50", "Adam", "0.0001", "1.0", "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_3 = Experiment("3", "Keras", "ResNet50", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_4 = Experiment("4", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_5 = Experiment("5", "Keras", "ResNet101", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_6 = Experiment("6", "Keras", "ResNet152", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_7 = Experiment("7", "Keras", "ResNet50V2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_8 = Experiment("8", "Keras", "ResNet101V2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_9 = Experiment("9", "Keras", "ResNet152V2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_10 = Experiment("10", "Keras", "ResNet50V2", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_11 = Experiment("11", "Keras", "ResNet50", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_12 = Experiment("12", "Keras", "ResNet101", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_13 = Experiment("13", "Keras", "ResNet152", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_14 = Experiment("14", "Keras", "ResNet50V2", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_15 = Experiment("15", "Keras", "ResNet101V2", "Adam", "0.001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_16 = Experiment("16", "Keras", "ResNet50", "Adam", "0.0001", "1.0", "100", "mse", "3", gestures_3g, "10")
exp_17 = Experiment("17", "Keras", "ResNet50", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_18 = Experiment("18", "Keras", "ResNet101", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_19 = Experiment("19", "Keras", "ResNet152", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_20 = Experiment("20", "Keras", "ResNet50", "Adam", "0.01", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_21 = Experiment("21", "Keras", "ResNet101", "Adam", "0.01", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_22 = Experiment("22", "Keras", "VGG16", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_23 = Experiment("23", "Keras", "VGG16", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_24 = Experiment("24", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_25 = Experiment("25", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_26 = Experiment("26", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_27 = Experiment("27", "Keras", "VGG19", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_28 = Experiment("28", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_29 = Experiment("29", "Keras", "VGG19", "SGD", None, None, "100", "categorical_crossentropy", "3", gestures_3g, "10")
exp_30 = Experiment("30", "Keras", "InceptionV3", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_31 = Experiment("31", "Keras", "InceptionV3", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_32 = Experiment("32", "Keras", "InceptionResNetV2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_33 = Experiment("33", "Keras", "InceptionResNetV2", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_34 = Experiment("34", "Keras", "MobileNetV2", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_35 = Experiment("35", "Keras", "MobileNetV2", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_36 = Experiment("36", "Keras", "DenseNet121", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_37 = Experiment("37", "Keras", "DenseNet121", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_38 = Experiment("38", "Keras", "DenseNet169", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_39 = Experiment("39", "Keras", "DenseNet169", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_40 = Experiment("40", "Keras", "DenseNet201", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_41 = Experiment("41", "Keras", "DenseNet201", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_42 = Experiment("42", "Keras", "NasNetLarge", "SGD", None, None, "100", "mse", "3", gestures_3g, "10")
exp_43 = Experiment("43", "Keras", "NasNetLarge", "Adam", "0.001", "0.1", "100", "mse", "3", gestures_3g, "10")
exp_44 = Experiment("44", "Keras", "VGG16", "Adam", "0.001", "0.1", "150", "categorical_crossentropy", "3", gestures_3g, "10")
exp_45 = Experiment("45", "Keras", "VGG16", "Adam", "0.001", "0.1", "150", "mse", "3", gestures_3g, "10")
exp_46 = Experiment("46", "Keras", "ResNet152", "SGD", None, None, "150", "mse", "3", gestures_3g, "10")
exp_47 = Experiment("47", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "3", gestures_3g, "10")
exp_48 = Experiment("48", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "3", gestures_3g, "10")
exp_49 = Experiment("49", "Keras", "ResNet50", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_50 = Experiment("50", "Keras", "ResNet101", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_51 = Experiment("51", "Keras", "ResNet152", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_53 = Experiment("53", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_54 = Experiment("54", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "5", gestures_5g, "10")
exp_55 = Experiment("55", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
exp_56 = Experiment("56", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "5", gestures_5g, "10")
exp_57 = Experiment("57", "Keras", "ResNet50", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_58 = Experiment("58", "Keras", "ResNet101", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_59 = Experiment("59", "Keras", "ResNet152", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_60 = Experiment("60", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_61 = Experiment("61", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "mse", "5", gestures_5g, "10")
exp_62 = Experiment("62", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "5", gestures_5g, "10")
exp_63 = Experiment("63", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "5", gestures_5g, "10")
exp_64 = Experiment("64", "Keras", "ResNet50", "Adam", "0.001", "0.1", "100", "mse", "8", gestures_8g, "10")
exp_65 = Experiment("65", "Keras", "ResNet101", "Adam", "0.001", "0.1", "100", "mse", "8", gestures_8g, "10")
exp_66 = Experiment("66", "Keras", "ResNet152", "Adam", "0.001", "0.1", "100", "mse", "8", gestures_8g, "10")
exp_67 = Experiment("67", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "8", gestures_8g, "10")
exp_68 = Experiment("68", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "mse", "8", gestures_8g, "10")
exp_69 = Experiment("69", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "8", gestures_8g, "10")
exp_70 = Experiment("70", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "8", gestures_8g, "10")
exp_71 = Experiment("71", "Keras", "ResNet50", "SGD", None, None, "100", "mse", "8", gestures_8g, "10")
exp_72 = Experiment("72", "Keras", "ResNet50", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_73 = Experiment("73", "Keras", "ResNet101", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_74 = Experiment("74", "Keras", "ResNet152", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_75 = Experiment("75", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_76 = Experiment("76", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "mse", "8", gestures_8g, "10")
exp_77 = Experiment("77", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "8", gestures_8g, "10")
exp_78 = Experiment("78", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "8", gestures_8g, "10")
exp_79 = Experiment("79", "Keras", "ResNet50", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_80 = Experiment("80", "Keras", "ResNet101", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_81 = Experiment("81", "Keras", "ResNet152", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_82 = Experiment("82", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_83 = Experiment("83", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "10")
exp_84 = Experiment("84", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "10", gestures_10g, "10")
exp_85 = Experiment("85", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "10", gestures_10g, "10")
exp_86 = Experiment("86", "Keras", "ResNet50", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_87 = Experiment("87", "Keras", "ResNet101", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_88 = Experiment("88", "Keras", "ResNet152", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_89 = Experiment("89", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_90 = Experiment("90", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "mse", "10", gestures_10g, "10")
exp_91 = Experiment("91", "Keras", "VGG16", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "10", gestures_10g, "10")
exp_92 = Experiment("92", "Keras", "VGG19", "Adam", "0.001", "0.1", "200", "categorical_crossentropy", "10", gestures_10g, "10")
exp_93 = Experiment("93", "Keras", "VGG16", "Adam", "0.001", "0.1", "30", "categorical_crossentropy", "10", gestures_10g, "17")
exp_94 = Experiment("94", "Keras", "VGG16", "Adam", "0.001", "0.1", "50", "categorical_crossentropy", "10", gestures_10g, "17")
exp_95 = Experiment("95", "Keras", "VGG16", "Adam", "0.001", "0.1", "50", "mse", "10", gestures_10g, "17")
exp_96 = Experiment("96", "Keras", "VGG19", "Adam", "0.001", "0.1", "50", "categorical_crossentropy", "10", gestures_10g, "17")
exp_97 = Experiment("97", "Keras", "VGG19", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "10", gestures_10g, "17")
exp_98 = Experiment("98", "Keras", "VGG16", "Adam", "0.001", "0.1", "70", "categorical_crossentropy", "10", gestures_10g, "17")
exp_99 = Experiment("99", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "categorical_crossentropy", "10", gestures_10g, "17")
exp_100 = Experiment("100", "Keras", "VGG16", "Adam", "0.001", "0.1", "30", "mse", "10", gestures_10g, "17")
exp_101 = Experiment("101", "Keras", "VGG16", "Adam", "0.001", "0.1", "70", "mse", "10", gestures_10g, "17")
exp_102 = Experiment("102", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "10", gestures_10g, "17")
exp_103 = Experiment("103", "Keras", "VGG19", "Adam", "0.001", "0.1", "30", "categorical_crossentropy", "10", gestures_10g, "17")
exp_104 = Experiment("104", "Keras", "VGG19", "Adam", "0.001", "0.1", "70", "categorical_crossentropy", "10", gestures_10g, "17")

# Adding the metrics gesture
stop_sign1 = Gesture("1", "stop_sign", "1.0", "0.3", "0.46", "90.0")
swipe_left1 = Gesture("1", "swipe_left", "0.92", "0.89", "0.9", "123.0")
thumb_up1 = Gesture("1", "thumb_up", "0.55", "0.99", "0.71", "86.0")
gestures_1 = [stop_sign1, swipe_left1, thumb_up1]

stop_sign2 = Gesture("2", "stop_sign", "0.86", "0.53", "0.66", "90.0")
swipe_left2 = Gesture("2", "swipe_left", "0.79", "0.91", "0.85", "123.0")
thumb_up2 = Gesture("2", "thumb_up", "0.61", "0.72", "0.66", "86.0")
gestures_2 = [stop_sign2, swipe_left2, thumb_up2]

stop_sign3 = Gesture("3", "stop_sign", "0.85", "0.58", "0.69", "90.0")
swipe_left3 = Gesture("3", "swipe_left", "0.83", "0.93", "0.88", "123.0")
thumb_up3 = Gesture("3", "thumb_up", "0.79", "0.92", "0.85", "86.0")
gestures_3 = [stop_sign3, swipe_left3, thumb_up3]

stop_sign4 = Gesture("4", "stop_sign", "0.82", "0.72", "0.77", "90.0")
swipe_left4 = Gesture("4", "swipe_left", "0.82", "0.95", "0.88", "123.0")
thumb_up4 = Gesture("4", "thumb_up", "0.88", "0.79", "0.83", "86.0")
gestures_4 = [stop_sign4, swipe_left4, thumb_up4]

stop_sign5 = Gesture("5", "stop_sign", "0.82", "0.51", "0.63", "90.0")
swipe_left5 = Gesture("5", "swipe_left", "0.93", "0.93", "0.93", "123.0")
thumb_up5 = Gesture("5", "thumb_up", "0.63", "0.88", "0.74", "86.0")
gestures_5 = [stop_sign5, swipe_left5, thumb_up5]

stop_sign6 = Gesture("6", "stop_sign", "0.96", "0.56", "0.7", "90.0")
swipe_left6 = Gesture("6", "swipe_left", "0.78", "0.81", "0.79", "88.0")
thumb_up6 = Gesture("6", "thumb_up", "0.64", "0.91", "0.75", "86.0")
gestures_6 = [stop_sign6, swipe_left6, thumb_up6]

stop_sign7 = Gesture("7", "stop_sign", "0.06", "0.04", "0.05", "90.0")
swipe_left7 = Gesture("7", "swipe_left", "0.0", "0.0", "0.0", "123.0")
thumb_up7 = Gesture("7", "thumb_up", "0.26", "0.72", "0.39", "86.0")
gestures_7 = [stop_sign7, swipe_left7, thumb_up7]

stop_sign8 = Gesture("8", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left8 = Gesture("8", "swipe_left", "0.35", "0.45", "0.39", "123.0")
thumb_up8 = Gesture("8", "thumb_up", "0.31", "0.51", "0.38", "86.0")
gestures_8 = [stop_sign8, swipe_left8, thumb_up8]

stop_sign9 = Gesture("9", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left9 = Gesture("9", "swipe_left", "0.41", "1.0", "0.58", "123.0")
thumb_up9 = Gesture("9", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_9 = [stop_sign9, swipe_left9, thumb_up9]

stop_sign10 = Gesture("10", "stop_sign", "0.31", "1.0", "0.48", "90.0")
swipe_left10 = Gesture("10", "swipe_left", "0.0", "0.0", "0.0", "123.0")
thumb_up10 = Gesture("10", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_10 = [stop_sign10, swipe_left10, thumb_up10]

stop_sign11 = Gesture("11", "stop_sign", "1.0", "0.22", "0.36", "90.0")
swipe_left11 = Gesture("11", "swipe_left", "0.68", "0.87", "0.76", "123.0")
thumb_up11 = Gesture("11", "thumb_up", "0.61", "0.86", "0.71", "86.0")
gestures_11 = [stop_sign11, swipe_left11, thumb_up11]

stop_sign12 = Gesture("12", "stop_sign", "0.88", "0.48", "0.62", "90.0")
swipe_left12 = Gesture("12", "swipe_left", "0.75", "0.89", "0.81", "123.0")
thumb_up12 = Gesture("12", "thumb_up", "0.6", "0.72", "0.66", "86.0")
gestures_12 = [stop_sign12, swipe_left12, thumb_up12]

stop_sign13 = Gesture("13", "stop_sign", "0.91", "0.48", "0.63", "90.0")
swipe_left13 = Gesture("13", "swipe_left", "0.69", "0.99", "0.81", "123.0")
thumb_up13 = Gesture("13", "thumb_up", "0.81", "0.7", "0.75", "86.0")
gestures_13 = [stop_sign13, swipe_left13, thumb_up13]

stop_sign14 = Gesture("14", "stop_sign", "0.31", "0.97", "0.46", "90.0")
swipe_left14 = Gesture("14", "swipe_left", "0.29", "0.03", "0.06", "123.0")
thumb_up14 = Gesture("14", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_14 = [stop_sign14, swipe_left14, thumb_up14]

stop_sign15 = Gesture("15", "stop_sign", "0.36", "0.97", "0.52", "90.0")
swipe_left15 = Gesture("15", "swipe_left", "0.23", "0.03", "0.06", "88.0")
thumb_up15 = Gesture("15", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_15 = [stop_sign15, swipe_left15, thumb_up15]

stop_sign16 = Gesture("16", "stop_sign", "1.0", "0.03", "0.06", "90.0")
swipe_left16 = Gesture("16", "swipe_left", "0.46", "0.54", "0.49", "123.0")
thumb_up16 = Gesture("16", "thumb_up", "0.44", "0.78", "0.56", "86.0")
gestures_16 = [stop_sign16, swipe_left16, thumb_up16]

stop_sign17 = Gesture("17", "stop_sign", "0.95", "0.84", "0.89", "90.0")
swipe_left17 = Gesture("17", "swipe_left", "1.0", "0.81", "0.9", "123.0")
thumb_up17 = Gesture("17", "thumb_up", "0.7", "0.97", "0.81", "86.0")
gestures_17 = [stop_sign17, swipe_left17, thumb_up17]

stop_sign18 = Gesture("18", "stop_sign", "1.0", "0.46", "0.63", "90.0")
swipe_left18 = Gesture("18", "swipe_left", "0.94" "0.97", "0.95", "123.0")
thumb_up18 = Gesture("18", "thumb_up", "0.66", "1.0", "0.79", "86.0")
gestures_18 = [stop_sign18, swipe_left18, thumb_up18]

stop_sign19 = Gesture("19", "stop_sign", "1.0", "0.77", "0.87", "90.0")
swipe_left19 = Gesture("19", "swipe_left", "0.96", "0.91", "0.93", "123.0")
thumb_up19 = Gesture("19", "thumb_up", "0.73", "0.97", "0.83", "86.0")
gestures_19 = [stop_sign19, swipe_left19, thumb_up19]

stop_sign20 = Gesture("20", "stop_sign", "0.98", "0.56", "0.71", "90.0")
swipe_left20 = Gesture("20", "swipe_left", "0.88", "0.72", "0.79", "88.0")
thumb_up20 = Gesture("20", "thumb_up", "0.73", "0.97", "0.83", "86.0")
gestures_20 = [stop_sign20, swipe_left20, thumb_up20]

stop_sign21 = Gesture("21", "stop_sign", "1.0", "0.59", "0.74", "90.0")
swipe_left21 = Gesture("21", "swipe_left", "0.84", "1.0", "0.91", "123.0")
thumb_up21 = Gesture("21", "thumb_up", "0.86", "1.0", "0.92", "86.0")
gestures_21 = [stop_sign21, swipe_left21, thumb_up21]

stop_sign22 = Gesture("22", "stop_sign", "0.93", "0.97", "0.95", "90.0")
swipe_left22 = Gesture("22", "swipe_left", "0.88", "0.98", "0.92", "88.0")
thumb_up22 = Gesture("22", "thumb_up", "0.96", "0.8", "0.87", "86.0")
gestures_22 = [stop_sign22, swipe_left22, thumb_up22]

stop_sign23 = Gesture("23", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left23 = Gesture("23", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up23 = Gesture("23", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_23 = [stop_sign23, swipe_left23, thumb_up23]

stop_sign24 = Gesture("24", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left24 = Gesture("24", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up24 = Gesture("24", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_24 = [stop_sign24, swipe_left24, thumb_up24]

stop_sign25 = Gesture("25", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left25 = Gesture("25", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up25 = Gesture("25", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_25 = [stop_sign25, swipe_left25, thumb_up25]

stop_sign26 = Gesture("26", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left26 = Gesture("26", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up26 = Gesture("26", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_26 = [stop_sign26, swipe_left26, thumb_up26]

stop_sign27 = Gesture("27", "stop_sign", "0.99", "0.97", "0.98", "90.0")
swipe_left27 = Gesture("27", "swipe_left", "0.98", "0.99", "0.98", "123.0")
thumb_up27 = Gesture("27", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_27 = [stop_sign27, swipe_left27, thumb_up27]

stop_sign28 = Gesture("28", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left28 = Gesture("28", "swipe_left", "1.0", "1.0", "1.0", "123.0")
thumb_up28 = Gesture("28", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_28 = [stop_sign28, swipe_left28, thumb_up28]

stop_sign29 = Gesture("29", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left29 = Gesture("29", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up29 = Gesture("29", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_29 = [stop_sign29, swipe_left29, thumb_up29]

stop_sign30 = Gesture("30", "stop_sign", "0.02", "0.01", "0.02", "90.0")
swipe_left30 = Gesture("30", "swipe_left", "0.32", "0.81", "0.46", "88.0")
thumb_up30 = Gesture("30", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_30 = [stop_sign30, swipe_left30, thumb_up30]

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
list_exp = []
with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)   
    for row in reader:
        experiment = Experiment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        list_exp.append(experiment)

# Reading the experiments metrics
list_metrics = []
list_gestures = []
with open(filenameMetrics_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)
    
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
        
