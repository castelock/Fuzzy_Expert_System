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
gestures_3g = ["fist", "l", "palm"]
gestures_5g = ["fist", "l", "palm", "ok", "thumb_up"]

exp_1 = Experiment("1", "Keras", "ResNet50", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_2 = Experiment("2", "Keras", "ResNet101", "Adam", "0.001", "100", "categorical_crossentropy","3")
exp_3 = Experiment("3", "Keras", "ResNet152", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_4 = Experiment("4", "Keras", "ResNet50V2", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_5 = Experiment("5", "Keras", "ResNet101V2", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_6 = Experiment("6", "Keras", "ResNet152V2", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_7 = Experiment("7", "Keras", "VGG16", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_8 = Experiment("8", "Keras", "VGG19", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_9 = Experiment("9", "Keras", "InceptionV3", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_10 = Experiment("10", "Keras", "InceptionResnetV2", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_11 = Experiment("11", "Keras", "MobileNetV2", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_12 = Experiment("12", "Keras", "DenseNet121", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_13 = Experiment("13", "Keras", "DenseNet169", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_14 = Experiment("14", "Keras", "DenseNet201", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_15 = Experiment("15", "Keras", "NasNetLarge", "Adam", "0.001", "100", "categorical_crossentropy", "3")
exp_16 = Experiment("16", "Keras", "ResNet50", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_17 = Experiment("17", "Keras", "ResNet101", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_18 = Experiment("18", "Keras", "ResNet152", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_19 = Experiment("19", "Keras", "ResNet50V2", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_20 = Experiment("20", "Keras", "ResNet101V2", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_21 = Experiment("21", "Keras", "ResNet152V2", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_22 = Experiment("22", "Keras", "VGG16", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_23 = Experiment("23", "Keras", "VGG19", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_24 = Experiment("24", "Keras", "InceptionV3", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_25 = Experiment("25", "Keras", "InceptionResNetV2", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_26 = Experiment("26", "Keras", "MobileNetV2", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_27 = Experiment("27", "Keras", "DenseNet121", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_28 = Experiment("28", "Keras", "DenseNet169", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_29 = Experiment("29", "Keras", "DenseNet201", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_30 = Experiment("30", "Keras", "NasNetLarge", "SGD", "0.001", "100", "categorical_crossentropy", "3")
exp_31 = Experiment("31", "Keras", "ResNet50", "Adam", "0.001", "100", "mse", "3")
exp_32 = Experiment("32", "Keras", "ResNet101", "Adam", "0.001", "100", "mse", "3")
exp_33 = Experiment("33", "Keras", "ResNet152", "Adam", "0.001", "100", "mse", "3")
exp_34 = Experiment("34", "Keras", "ResNet50V2", "Adam", "0.001", "100", "mse", "3")
exp_35 = Experiment("35", "Keras", "ResNet101V2", "Adam", "0.001", "100", "mse", "3")
exp_36 = Experiment("36", "Keras", "ResNet152V2", "Adam", "0.001", "100", "mse", "3")
exp_37 = Experiment("37", "Keras", "VGG16", "Adam", "0.001", "100", "mse", "3")
exp_38 = Experiment("38", "Keras", "VGG19", "Adam", "0.001", "100", "mse", "3")
exp_39 = Experiment("39", "Keras", "InceptionV3", "Adam", "0.001", "100", "mse", "3")
exp_40 = Experiment("40", "Keras", "InceptionResNetV2", "Adam", "0.001", "100", "mse", "3")
exp_41 = Experiment("41", "Keras", "MobileNetV2", "Adam", "0.001", "100", "mse", "3")
exp_42 = Experiment("42", "Keras", "DenseNet121", "Adam", "0.001", "100", "mse", "3")
exp_43 = Experiment("43", "Keras", "DenseNet169", "Adam", "0.001", "100", "mse", "3")
exp_44 = Experiment("44", "Keras", "DenseNet201", "Adam", "0.001", "100", "mse", "3")
exp_45 = Experiment("45", "Keras", "NasNetLarge", "Adam", "0.001", "100", "mse", "3")
exp_46 = Experiment("46", "Keras", "ResNet50", "SGD", "0.001", "100", "mse", "3")
exp_47 = Experiment("47", "Keras", "ResNet101", "SGD", "0.001", "100", "mse", "3")
exp_48 = Experiment("48", "Keras", "ResNet152", "SGD", "0.001", "100", "mse", "3")
exp_49 = Experiment("49", "Keras", "ResNet50V2", "SGD", "0.001", "100", "mse", "3")
exp_50 = Experiment("50", "Keras", "ResNet101V2", "SGD", "0.001", "100", "mse", "3")
exp_51 = Experiment("51", "Keras", "ResNet152V2", "SGD", "0.001", "100", "mse", "3")
exp_52 = Experiment("52", "Keras", "VGG16", "SGD", "0.001", "100", "mse", "3")
exp_53 = Experiment("53", "Keras", "VGG19", "SGD", "0.001", "100", "mse", "3")
exp_54 = Experiment("54", "Keras", "InceptionV3", "SGD", "0.001", "100", "mse", "3")
exp_55 = Experiment("55", "Keras", "InceptionResNetV2", "SGD", "0.001", "100", "mse", "3")
exp_56 = Experiment("56", "Keras", "MobileNetV2", "SGD", "0.001", "100", "mse", "3")
exp_57 = Experiment("57", "Keras", "DenseNet121", "SGD", "0.001", "100", "mse", "3")
exp_58 = Experiment("58", "Keras", "DenseNet169", "SGD", "0.001", "100", "mse", "3")
exp_59 = Experiment("59", "Keras", "DenseNet201", "SGD", "0.001", "100", "mse", "3")
exp_60 = Experiment("60", "Keras", "NasNetLarge", "SGD", "0.001", "100", "mse", "3")
exp_61 = Experiment("61", "Keras", "VGG16", "Adam", "0.0001", "100", "mse", "3")
exp_62 = Experiment("62", "Keras", "VGG19", "Adam", "0.0001", "100", "mse", "3")
exp_63 = Experiment("63", "Keras", "ResNet50V2", "Adam", "0.0001", "100", "mse", "3")
exp_64 = Experiment("64", "Keras", "InceptionV3", "Adam", "0.0001", "100", "mse", "3")
exp_65 = Experiment("65", "Keras", "DenseNet201", "Adam", "0.0001", "100", "mse", "3")
exp_66 = Experiment("66", "Keras", "VGG16", "Adam", "0.01", "100", "mse", "3")
exp_67 = Experiment("67", "Keras", "VGG19", "Adam", "0.01", "100", "mse", "3")
exp_68 = Experiment("68", "Keras", "ResNet50V2", "Adam", "0.01", "100", "mse", "3")
exp_69 = Experiment("69", "Keras", "InceptionV3", "Adam", "0.01", "100", "mse", "3")
exp_70 = Experiment("70", "Keras", "DenseNet201", "Adam", "0.01", "100", "mse", "3")
exp_71 = Experiment("71", "Keras", "VGG16", "SGD", "0.0001", "100", "mse", "3")
exp_72 = Experiment("72", "Keras", "VGG19", "SGD", "0.0001", "100", "mse", "3")
exp_73 = Experiment("73", "Keras", "ResNet50V2", "SGD", "0.0001", "100", "mse", "3")
exp_74 = Experiment("74", "Keras", "InceptionV3", "SGD", "0.0001", "100", "mse", "3")
exp_75 = Experiment("75", "Keras", "DenseNet201", "SGD", "0.0001", "100", "mse", "3")
exp_76 = Experiment("76", "Keras", "VGG16", "SGD", "0.01", "100", "mse", "3")
exp_77 = Experiment("77", "Keras", "VGG19", "SGD", "0.01", "100", "mse", "3")
exp_78 = Experiment("78", "Keras", "ResNet50V2", "SGD", "0.01", "100", "mse", "3")
exp_79 = Experiment("79", "Keras", "InceptionV3", "SGD", "0.01", "100", "mse", "3")
exp_80 = Experiment("80", "Keras", "DenseNet201", "SGD", "0.01", "100", "mse", "3")
exp_81 = Experiment("81", "Keras", "VGG16", "Adam", "0.001", "10", "mse", "3")
exp_82 = Experiment("82", "Keras", "VGG19", "Adam", "0.001", "10", "mse", "3")
exp_83 = Experiment("83", "Keras", "ResNet50V2", "Adam", "0.001", "10", "mse", "3")
exp_84 = Experiment("84", "Keras", "InceptionV3", "Adam", "0.001", "10", "mse", "3")
exp_85 = Experiment("85", "Keras", "DenseNet201", "Adam", "0.001", "10", "mse", "3")
exp_86 = Experiment("86", "Keras", "VGG16", "Adam", "0.001", "30", "mse", "3")
exp_87 = Experiment("87", "Keras", "VGG19", "Adam", "0.001", "30", "mse", "3")
exp_88 = Experiment("88", "Keras", "ResNet50V2", "Adam", "0.001", "30", "mse", "3")
exp_89 = Experiment("89", "Keras", "InceptionV3", "Adam", "0.001", "30", "mse", "3")
exp_90 = Experiment("90", "Keras", "DenseNet201", "Adam", "0.001", "30", "mse", "3")
exp_91 = Experiment("91", "Keras", "VGG16", "Adam", "0.001", "50", "mse", "3")
exp_92 = Experiment("92", "Keras", "VGG19", "Adam", "0.001", "50", "mse", "3")
exp_93 = Experiment("93", "Keras", "ResNet50V2", "Adam", "0.001", "50", "mse", "3")
exp_94 = Experiment("94", "Keras", "InceptionV3", "Adam", "0.001", "50", "mse", "3")
exp_95 = Experiment("95", "Keras", "DenseNet201", "Adam", "0.001", "50", "mse", "3")
exp_96 = Experiment("96", "Keras", "VGG16", "Adam", "0.001", "70", "mse", "3")
exp_97 = Experiment("97", "Keras", "VGG19", "Adam", "0.001", "70", "mse", "3")
exp_98 = Experiment("98", "Keras", "ResNet50V2", "Adam", "0.001", "70", "mse", "3")
exp_99 = Experiment("99", "Keras", "InceptionV3", "Adam", "0.001", "70", "mse", "3")
exp_100 = Experiment("100", "Keras", "DenseNet201", "Adam", "0.001", "70", "mse", "3")
exp_101 = Experiment("101", "Keras", "ResNet50", "Adam", "0.001", "100", "mse", "5")
exp_102 = Experiment("102", "Keras", "ResNet101", "Adam", "0.001", "100", "mse", "5")
exp_103 = Experiment("103", "Keras", "ResNet152", "Adam", "0.001", "100", "mse", "5")
exp_104 = Experiment("104", "Keras", "ResNet50V2", "Adam", "0.001", "100", "mse", "5")
exp_105 = Experiment("105", "Keras", "ResNet101V2", "Adam", "0.001", "100", "mse", "5")
exp_106 = Experiment("106", "Keras", "ResNet152V2", "Adam", "0.001", "100", "mse", "5")
exp_107 = Experiment("107", "Keras", "VGG16", "Adam", "0.001", "100", "mse", "5")
exp_108 = Experiment("108", "Keras", "VGG19", "Adam", "0.001", "100", "mse", "5")
exp_109 = Experiment("109", "Keras", "InceptionV3", "Adam", "0.001", "100", "mse", "5")
exp_110 = Experiment("110", "Keras", "InceptionResNetV2", "Adam", "0.001", "100", "mse", "5")
exp_111 = Experiment("111", "Keras", "MobileNetV2", "Adam", "0.001", "100", "mse", "5")
exp_112 = Experiment("112", "Keras", "DenseNet121", "Adam", "0.001", "100", "mse", "5")
exp_113 = Experiment("113", "Keras", "DenseNet169", "Adam", "0.001", "100", "mse", "5")
exp_114 = Experiment("114", "Keras", "DenseNet201", "Adam", "0.001", "100", "mse", "5")
exp_115 = Experiment("115", "Keras", "NasNetLarge", "Adam", "0.001", "100", "mse", "5")

# Adding the metrics gesture
fist1 = Gesture("1", fist, 0.99, 1.0, 0.99, 76.0)
l1 = Gesture("1", l, 1.0, 0.91, 0.95, 75.0)
palm1 = Gesture("1", palm, 0.91, 0.99, 0.95, 75.0)
gestures_1 = [fist1, l1, palm1]

fist2 = Gesture("2", fist, 1.0, 0.74, 0.85, 76.0)
l2 = Gesture("2", l, 1.0, 0.8, 0.89, 75.0)
palm2 = Gesture("2", palm, 0.68, 1.0, 0.81, 75.0)
gestures_2 = [fist2, l2, palm2]

fist3 = Gesture("3", fist, 0.97, 1.0, 0.99, 76.0)
l3 = Gesture("3", l, 1.0, 1.0, 1.0, 75.0)
palm3 = Gesture("3", palm, 1.0, 0.97, 0.99, 75.0)
gestures_3 = [fist3, l3, palm3]

fist4 = Gesture("4", fist, 0.0 0.0, 0.0, 76.0)
l4 = Gesture("4", l, 0.0, 0.0, 0.0, 75.0)
palm4 = Gesture("4", palm, 0.33, 1.0, 0.5, 75.0)
gestures_4 = [fist4, l4, palm4]

fist5 = Gesture("5", fist, 0.0, 0.0, 0.0, 76.0)
l5 = Gesture("5", l, 0.34, 0.35, 0.34, 75.0)
palm5 = Gesture("5", palm, 0.35, 0.69, 0.46, 75.0)
gestures_5 = [fist5, l5, palm5]

fist6 = Gesture("6", fist, 0.34, 1.0, 0.5, 76.0)
l6 = Gesture("6", l, 0.0, 0.0, 0.0, 75.0)
palm6 = Gesture("6", palm, 0.0, 0.0, 0.0, 75.0)
gestures_6 = [fist6, l6, palm6]

fist7 = Gesture("7", fist, 1.0, 1.0, 1.0, 76.0)
l7 = Gesture("7", l, 1.0, 1.0, 1.0, 75.0)
palm7 = Gesture("7", palm, 1.0, 1.0, 1.0, 75.0)
gestures_7 = [fist7, l7, palm7]

fist8 = Gesture("8", fist, 1.0, 1.0, 1.0, 76.0)
l8 = Gesture("8", l, 1.0, 1.0, 1.0, 75.0)
palm8 = Gesture("8", palm, 1.0, 1.0, 1.0, 75.0)
gestures_8 = [fist8, l8, palm8]

fist9 = Gesture("9", "stop_sign", "0.0", "0.0", "0.0", "90.0")
l9 = Gesture("9", "swipe_left", "0.41", "1.0", "0.58", "123.0")
palm9 = Gesture("9", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_9 = [fist9, l9, palm9]

fist10 = Gesture("10", "stop_sign", "0.31", "1.0", "0.48", "90.0")
l10 = Gesture("10", "swipe_left", "0.0", "0.0", "0.0", "123.0")
palm10 = Gesture("10", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_10 = [fist10, l10, palm10]

fist11 = Gesture("11", "stop_sign", "1.0", "0.22", "0.36", "90.0")
l11 = Gesture("11", "swipe_left", "0.68", "0.87", "0.76", "123.0")
palm11 = Gesture("11", "thumb_up", "0.61", "0.86", "0.71", "86.0")
gestures_11 = [fist11, l11, palm11]

fist12 = Gesture("12", "stop_sign", "0.88", "0.48", "0.62", "90.0")
l12 = Gesture("12", "swipe_left", "0.75", "0.89", "0.81", "123.0")
palm12 = Gesture("12", "thumb_up", "0.6", "0.72", "0.66", "86.0")
gestures_12 = [fist12, l12, palm12]

fist13 = Gesture("13", "stop_sign", "0.91", "0.48", "0.63", "90.0")
l13 = Gesture("13", "swipe_left", "0.69", "0.99", "0.81", "123.0")
palm13 = Gesture("13", "thumb_up", "0.81", "0.7", "0.75", "86.0")
gestures_13 = [fist13, l13, palm13]

fist14 = Gesture("14", "stop_sign", "0.31", "0.97", "0.46", "90.0")
l14 = Gesture("14", "swipe_left", "0.29", "0.03", "0.06", "123.0")
palm14 = Gesture("14", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_14 = [fist14, l14, palm14]

fist15 = Gesture("15", "stop_sign", "0.36", "0.97", "0.52", "90.0")
l15 = Gesture("15", "swipe_left", "0.23", "0.03", "0.06", "88.0")
palm15 = Gesture("15", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_15 = [fist15, l15, palm15]

fist16 = Gesture("16", "stop_sign", "1.0", "0.03", "0.06", "90.0")
l16 = Gesture("16", "swipe_left", "0.46", "0.54", "0.49", "123.0")
palm16 = Gesture("16", "thumb_up", "0.44", "0.78", "0.56", "86.0")
gestures_16 = [fist16, l16, palm16]

fist17 = Gesture("17", "stop_sign", "0.95", "0.84", "0.89", "90.0")
l17 = Gesture("17", "swipe_left", "1.0", "0.81", "0.9", "123.0")
palm17 = Gesture("17", "thumb_up", "0.7", "0.97", "0.81", "86.0")
gestures_17 = [fist17, l17, palm17]

fist18 = Gesture("18", "stop_sign", "1.0", "0.46", "0.63", "90.0")
l18 = Gesture("18", "swipe_left", "0.94", "0.97", "0.95", "123.0")
palm18 = Gesture("18", "thumb_up", "0.66", "1.0", "0.79", "86.0")
gestures_18 = [fist18, l18, palm18]

fist19 = Gesture("19", "stop_sign", "1.0", "0.77", "0.87", "90.0")
l19 = Gesture("19", "swipe_left", "0.96", "0.91", "0.93", "123.0")
palm19 = Gesture("19", "thumb_up", "0.73", "0.97", "0.83", "86.0")
gestures_19 = [fist19, l19, palm19]

fist20 = Gesture("20", "stop_sign", "0.98", "0.56", "0.71", "90.0")
l20 = Gesture("20", "swipe_left", "0.88", "0.72", "0.79", "88.0")
palm20 = Gesture("20", "thumb_up", "0.73", "0.97", "0.83", "86.0")
gestures_20 = [fist20, l20, palm20]

fist21 = Gesture("21", "stop_sign", "1.0", "0.59", "0.74", "90.0")
l21 = Gesture("21", "swipe_left", "0.84", "1.0", "0.91", "123.0")
palm21 = Gesture("21", "thumb_up", "0.86", "1.0", "0.92", "86.0")
gestures_21 = [fist21, l21, palm21]

fist22 = Gesture("22", "stop_sign", "0.93", "0.97", "0.95", "90.0")
l22 = Gesture("22", "swipe_left", "0.88", "0.98", "0.92", "88.0")
palm22 = Gesture("22", "thumb_up", "0.96", "0.8", "0.87", "86.0")
gestures_22 = [fist22, l22, palm22]

fist23 = Gesture("23", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l23 = Gesture("23", "swipe_left", "1.0", "1.0", "1.0", "123.0")
palm23 = Gesture("23", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_23 = [fist23, l23, palm23]

fist24 = Gesture("24", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l24 = Gesture("24", "swipe_left", "1.0", "1.0", "1.0", "123.0")
palm24 = Gesture("24", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_24 = [fist24, l24, palm24]

fist25 = Gesture("25", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l25 = Gesture("25", "swipe_left", "1.0", "1.0", "1.0", "123.0")
palm25 = Gesture("25", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_25 = [fist25, l25, palm25]

fist26 = Gesture("26", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l26 = Gesture("26", "swipe_left", "1.0", "1.0", "1.0", "123.0")
palm26 = Gesture("26", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_26 = [fist26, l26, palm26]

fist27 = Gesture("27", "stop_sign", "0.99", "0.97", "0.98", "90.0")
l27 = Gesture("27", "swipe_left", "0.98", "0.99", "0.98", "123.0")
palm27 = Gesture("27", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_27 = [fist27, l27, palm27]

fist28 = Gesture("28", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l28 = Gesture("28", "swipe_left", "1.0", "1.0", "1.0", "123.0")
palm28 = Gesture("28", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_28 = [fist28, l28, palm28]

fist29 = Gesture("29", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l29 = Gesture("29", "swipe_left", "1.0", "1.0", "1.0", "88.0")
palm29 = Gesture("29", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_29 = [fist29, l29, palm29]

fist30 = Gesture("30", "stop_sign", "0.02", "0.01", "0.02", "90.0")
l30 = Gesture("30", "swipe_left", "0.32", "0.81", "0.46", "88.0")
palm30 = Gesture("30", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_30 = [fist30, l30, palm30]

fist31 = Gesture("31", "stop_sign", "0.32", "0.51", "0.39", "90.0")
l31 = Gesture("31", "swipe_left", "0.26", "0.28", "0.27", "88.0")
palm31 = Gesture("31", "thumb_up", "0.24", "0.06", "0.09", "86.0")
gestures_31 = [fist31, l31, palm31]

fist32 = Gesture("32", "stop_sign", "0.0", "0.0", "0.0", "90.0")
l32 = Gesture("32", "swipe_left", "0.33", "1.0", "0.5", "88.0")
palm32 = Gesture("32", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_32 = [fist32, l32, palm32]

fist33 = Gesture("33", "stop_sign", "0.34", "1.0", "0.51", "90.0")
l33 = Gesture("33", "swipe_left", "0.0", "0.0", "0.0", "88.0")
palm33 = Gesture("33", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_33 = [fist33, l33, palm33]

fist34 = Gesture("34", "stop_sign", "0.36", "0.39", "0.38", "90.0")
l34 = Gesture("34", "swipe_left", "1.0", "0.08", "0.15", "88.0")
palm34 = Gesture("34", "thumb_up", "0.34", "0.63", "0.44", "86.0")
gestures_34 = [fist34, l34, palm34]

fist35 = Gesture("35", "stop_sign", "0.2", "0.11", "0.14", "90.0")
l35 = Gesture("35", "swipe_left", "0.4", "0.11", "0.18", "88.0")
palm35 = Gesture("35", "thumb_up", "0.29", "0.63", "0.39", "86.0")
gestures_35 = [fist35, l35, palm35]

fist36 = Gesture("36", "stop_sign", "0.0", "0.0", "0.0", "90.0")
l36 = Gesture("36", "swipe_left", "0.33", "1.0", "0.5", "88.0")
palm36 = Gesture("36", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_36 = [fist36, l36, palm36]

fist37 = Gesture("37", "stop_sign", "0.38", "0.03", "0.06", "90.0")
l37 = Gesture("37", "swipe_left", "1.0", "0.01", "0.02", "88.0")
palm37 = Gesture("37", "thumb_up", "0.32", "0.94", "0.48", "86.0")
gestures_37 = [fist37, l37, palm37]

fist38 = Gesture("38", "stop_sign", "0.0", "0.0", "0.0", "90.0")
l38 = Gesture("38", "swipe_left", "0.4", "0.92", "0.56", "123.0")
palm38 = Gesture("38", "thumb_up", "0.37", "0.08", "0.13", "86.0")
gestures_38 = [fist38, l38, palm38]

fist39 = Gesture("39", "stop_sign", "0.33", "0.64", "0.43", "90.0")
l39 = Gesture("39", "swipe_left", "1.0", "0.07", "0.14", "123.0")
palm39 = Gesture("39", "thumb_up", "0.29", "0.37", "0.32", "86.0")
gestures_39 = [fist39, l39, palm39]

fist40 = Gesture("40", "stop_sign", "0.35", "0.99", "0.52", "90.0")
l40 = Gesture("40", "swipe_left", "1.0", "0.03", "0.07", "88.0")
palm40 = Gesture("40", "thumb_up", "0.2", "0.02", "0.04", "86.0")
gestures_40 = [fist40, l40, palm40]

fist41 = Gesture("41", "stop_sign", "0.38", "0.06", "0.1", "90.0")
l41 = Gesture("41", "swipe_left", "1.0", "0.11", "0.2", "88.0")
palm41 = Gesture("41", "thumb_up", "0.34", "0.94", "0.5", "86.0")
gestures_41 = [fist41, l41, palm41]

fist42 = Gesture("42", "stop_sign", "0.0", "0.0", "0.0", "90.0")
l42 = Gesture("42", "swipe_left", "0.18", "0.05", "0.07", "88.0")
palm42 = Gesture("42", "thumb_up", "0.32", "0.87", "0.47", "86.0")
gestures_42 = [fist42, l42, palm42]

fist43 = Gesture("43", "stop_sign", "0.34", "1.0", "0.51", "90.0")
l43 = Gesture("43", "swipe_left", "0.0", "0.0", "0.0", "88.0")
palm43 = Gesture("43", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_43 = [fist43, l43, palm43]

fist44 = Gesture("44", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l44 = Gesture("44", "swipe_left", "1.0", "1.0", "1.0", "88.0")
palm44 = Gesture("44", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_44 = [fist44, l44, palm44]

fist45 = Gesture("45", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l45 = Gesture("45", "swipe_left", "1.0", "1.0", "1.0", "88.0")
palm45 = Gesture("45", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_45 = [fist45, l45, palm45]

fist46 = Gesture("46", "stop_sign", "0.95", "0.6", "0.73", "90.0")
l46 = Gesture("46", "swipe_left", "0.7", "0.91", "0.79", "88.0")
palm46 = Gesture("46", "thumb_up", "0.81", "0.87", "0.84", "86.0")
gestures_46 = [fist46, l46, palm46]

fist47 = Gesture("47", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l47 = Gesture("47", "swipe_left", "1.0", "1.0", "1.0", "88.0")
palm47 = Gesture("47", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_47 = [fist47, l47, palm47]

fist48 = Gesture("48", "stop_sign", "1.0", "1.0", "1.0", "90.0")
l48 = Gesture("48", "swipe_left", "1.0", "1.0", "1.0", "88.0")
palm48 = Gesture("48", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_48 = [fist48, l48, palm48]

fist49 = Gesture("49", "slide_2_fingers_right", "1.0", "0.17", "0.29", "89.0")
l49 = Gesture("49", "stop_sign", "1.0", "0.5", "0.67", "90.0")
palm49 = Gesture("49", "swipe_down", "1.0", "0.01", "0.02", "87.0")
gestures_49 = [fist49, l49, palm49]

fist50 = Gesture("50", "slide_2_fingers_right", "1.0", "0.12", "0.22", "89.0")
l50 = Gesture("50", "stop_sign", "1.0", "0.32", "0.49", "90.0")
palm50 = Gesture("50", "swipe_down", "0.67", "0.02", "0.04", "87.0")
gestures_50 = [fist50, l50, palm50]

fist51 = Gesture("51", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l51 = Gesture("51", "stop_sign", "0.88", "0.84", "0.86", "90.0")
palm51 = Gesture("51", "swipe_down", "1.0", "0.03", "0.07", "87.0")
gestures_51 = [fist51, l51, palm51]

fist52 = Gesture("52", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l52 = Gesture("52", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm52 = Gesture("52", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_52 = [fist52, l52, palm52]

fist53 = Gesture("53", "slide_2_fingers_right", "1.0", "0.99", "0.99", "89.0")
l53 = Gesture("53", "stop_sign", "0.99", "1.0", "0.99", "90.0")
palm53 = Gesture("53", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_53 = [fist53, l53, palm53]

fist54 = Gesture("54", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l54 = Gesture("54", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm54 = Gesture("54", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_54 = [fist54, l54, palm54]

fist55 = Gesture("55", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l55 = Gesture("55", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm55 = Gesture("55", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_55 = [fist55, l55, palm55]

fist56 = Gesture("56", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
l56 = Gesture("56", "stop_sign", "0.24", "0.16", "0.19", "90.0")
palm56 = Gesture("56", "swipe_down", "0.0", "0.0", "0.0", "87.0")
gestures_56 = [fist56, l56, palm56]

fist57 = Gesture("57", "slide_2_fingers_right", "1.0", "0.26", "0.41", "89.0")
l57 = Gesture("57", "stop_sign", "1.0", "0.44", "0.62", "90.0")
palm57 = Gesture("57", "swipe_down", "1.0", "0.1", "0.19", "87.0")
gestures_57 = [fist57, l57, palm57]

fist58 = Gesture("58", "slide_2_fingers_right", "1.0", "0.25", "0.4", "89.0")
l58 = Gesture("58", "stop_sign", "0.93", "0.46", "0.61", "90.0")
palm58 = Gesture("58", "swipe_down", "1.0", "0.07", "0.13", "87.0")
gestures_58 = [fist58, l58, palm58]

fist59 = Gesture("59", "slide_2_fingers_right", "0.96", "0.53", "0.68", "89.0")
l59 = Gesture("59", "stop_sign", "0.95", "0.89", "0.92", "90.0")
palm59 = Gesture("59", "swipe_down", "1.0", "0.21", "0.34", "87.0")
gestures_59 = [fist59, l59, palm59]

fist60 = Gesture("60", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l60 = Gesture("60", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm60 = Gesture("60", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_60 = [fist60, l60, palm60]

fist61 = Gesture("61", "slide_2_fingers_right", "1.0", "0.99", "0.99", "89.0")
l61 = Gesture("61", "stop_sign", "0.99", "1.0", "0.99", "90.0")
palm61 = Gesture("61", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_61 = [fist61, l61, palm61]

fist62 = Gesture("62", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l62 = Gesture("62", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm62 = Gesture("62", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_62 = [fist62, l62, palm62]

fist63 = Gesture("63", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
l63 = Gesture("63", "stop_sign", "1.0", "1.0", "1.0", "90.0")
palm63 = Gesture("63", "swipe_down", "1.0", "1.0", "1.0", "87.0")
gestures_63 = [fist63, l63, palm63]

fist64 = Gesture("64", "pull_hand_in", "0.79", "0.34", "0.48", "90.0")
l64 = Gesture("64", "slide_2_fingers_right", "1.0", "0.04", "0.09", "89.0")
palm64 = Gesture("64", "slide_2_fingers_up", "0.44", "0.83", "0.57", "88.0")
gestures_64 = [fist64, l64, palm64]

fist65 = Gesture("65", "pull_hand_in", "0.69", "0.61", "0.65", "90.0")
l65 = Gesture("65", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
palm65 = Gesture("65", "slide_2_fingers_up", "0.62", "0.62", "0.62", "88.0")
gestures_65 = [fist65, l65, palm65]

fist66 = Gesture("66", "pull_hand_in", "0.43", "0.86", "0.57", "90.0")
l66 = Gesture("66", "slide_2_fingers_right", "0.91", "0.34", "0.49", "89.0")
palm66 = Gesture("66", "slide_2_fingers_up", "0.75", "0.43", "0.55", "88.0")
gestures_66 = [fist66, l66, palm66]

fist67 = Gesture("67", "pull_hand_in", "0.89", "0.93", "0.91", "90.0")
l67 = Gesture("67", "slide_2_fingers_right", "0.94", "1.0", "0.97", "89.0")
palm67 = Gesture("67", "slide_2_fingers_up", "0.93", "0.92", "0.93", "88.0")
gestures_67 = [fist67, l67, palm67]

fist68 = Gesture("68", "pull_hand_in", "0.99", "0.87", "0.92", "90.0")
l68 = Gesture("68", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm68 = Gesture("68", "slide_2_fingers_up", "0.94", "0.94", "0.94", "88.0")
gestures_68 = [fist68, l68, palm68]

fist69 = Gesture("69", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l69 = Gesture("69", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm69 = Gesture("69", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_69 = [fist69, l69, palm69]

fist70 = Gesture("70", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l70 = Gesture("70", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm70 = Gesture("70", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_70 = [fist70, l70, palm70]


fist71 = Gesture("71", "pull_hand_in", "0.25", "0.44", "0.32", "90.0")
l71 = Gesture("71", "slide_2_fingers_right", "0.22", "0.21", "0.21", "89.0")
palm71 = Gesture("71", "slide_2_fingers_up", "0.33", "0.22", "0.26", "88.0")
gestures_71 = [fist71, l71, palm71]

fist72 = Gesture("72", "pull_hand_in", "0.81", "0.47", "0.59", "90.0")
l72 = Gesture("72", "slide_2_fingers_right", "1.0", "0.13", "0.24", "89.0")
palm72 = Gesture("72", "slide_2_fingers_up", "0.49", "0.97", "0.65", "88.0")
gestures_72 = [fist72, l72, palm72]

fist73 = Gesture("73", "pull_hand_in", "0.97", "0.39", "0.56", "90.0")
l73 = Gesture("73", "slide_2_fingers_right", "1.0", "0.11", "0.2", "89.0")
palm73 = Gesture("73", "slide_2_fingers_up", "0.67", "0.66", "0.66", "88.0")
gestures_73 = [fist73, l73, palm73]

fist74 = Gesture("74", "pull_hand_in", "0.67", "0.83", "0.74", "90.0")
l74 = Gesture("74", "slide_2_fingers_right", "1.0", "0.38", "0.55", "89.0")
palm74 = Gesture("74", "slide_2_fingers_up", "0.77", "0.98", "0.86", "88.0")
gestures_74 = [fist74, l74, palm74]

fist75 = Gesture("75", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
l75 = Gesture("75", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
palm75 = Gesture("75", "slide_2_fingers_up", "0.98", "0.99", "0.98", "88.0")
gestures_75 = [fist75, l75, palm75]

fist76 = Gesture("76", "pull_hand_in", "0.99", "0.96", "0.97", "90.0")
l76 = Gesture("76", "slide_2_fingers_right", "0.99", "0.99", "0.99", "89.0")
palm76 = Gesture("76", "slide_2_fingers_up", "1.0", "0.94", "0.97", "88.0")
gestures_76 = [fist76, l76, palm76]

fist77 = Gesture("77", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l77 = Gesture("77", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm77 = Gesture("77", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_77 = [fist77, l77, palm77]

fist78 = Gesture("78", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l78 = Gesture("78", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm78 = Gesture("78", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_78 = [fist78, l78, palm78]

fist79 = Gesture("79", "pull_hand_in", "0.68", "0.44", "0.54", "90.0")
l79 = Gesture("79", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
palm79 = Gesture("79", "slide_2_fingers_up", "0.41", "0.8", "0.54", "88.0")
gestures_79 = [fist79, l79, palm79]

fist80 = Gesture("80", "pull_hand_in", "0.49", "0.19", "0.27", "90.0")
l80 = Gesture("80", "slide_2_fingers_right", "1.0", "0.01", "0.02", "89.0")
palm80 = Gesture("80", "slide_2_fingers_up", "0.93", "0.15", "0.25", "88.0")
gestures_80 = [fist80, l80, palm80]

fist81 = Gesture("81", "pull_hand_in", "0.42", "0.72", "0.53", "90.0")
l81 = Gesture("81", "slide_2_fingers_right", "1.0", "0.44", "0.61", "89.0")
palm81 = Gesture("81", "slide_2_fingers_up", "0.79", "0.22", "0.34", "88.0")
gestures_81 = [fist81, l81, palm81]


fist82 = Gesture("82", "pull_hand_in", "0.82", "0.97", "0.89", "90.0")
l82 = Gesture("82", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
palm82 = Gesture("82", "slide_2_fingers_up", "0.95", "0.95", "0.95", "88.0")
gestures_82 = [fist82, l82, palm82]

fist83 = Gesture("83", "pull_hand_in", "0.92", "0.81", "0.86", "90.0")
l83 = Gesture("83", "slide_2_fingers_right", "0.91", "1.0", "0.95", "89.0")
palm83 = Gesture("83", "slide_2_fingers_up", "0.99", "0.81", "0.89", "88.0")
gestures_83 = [fist83, l83, palm83]

fist84 = Gesture("84", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l84 = Gesture("84", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm84 = Gesture("84", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_84 = [fist84, l84, palm84]

fist85 = Gesture("85", "pull_hand_in", "0.99", "1.0", "0.99", "90.0")
l85 = Gesture("85", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm85 = Gesture("85", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_85 = [fist85, l85, palm85]

fist86 = Gesture("86", "pull_hand_in", "0.67", "0.46", "0.54", "90.0")
l86 = Gesture("86", "slide_2_fingers_right", "1.0", "0.03", "0.07", "89.0")
palm86 = Gesture("86", "slide_2_fingers_up", "0.48", "0.9", "0.62", "88.0")
gestures_86 = [fist86, l86, palm86]

fist87 = Gesture("87", "pull_hand_in", "0.79", "0.33", "0.47", "90.0")
l87 = Gesture("87", "slide_2_fingers_right", "1.0", "0.04", "0.09", "89.0")
palm87 = Gesture("87", "slide_2_fingers_up", "0.45", "0.67", "0.54", "88.0")
gestures_87 = [fist87, l87, palm87]

fist88 = Gesture("88", "pull_hand_in", "0.62", "0.81", "0.7", "90.0")
l88 = Gesture("88", "slide_2_fingers_right", "1.0", "0.37", "0.54", "89.0")
palm88 = Gesture("88", "slide_2_fingers_up", "0.65", "0.68", "0.67", "88.0")
gestures_88 = [fist88, l88, palm88]

fist89 = Gesture("89", "pull_hand_in", "0.98", "0.98", "0.98", "90.0")
l89 = Gesture("89", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
palm89 = Gesture("89", "slide_2_fingers_up", "0.99", "1.0", "0.99", "88.0")
gestures_89 = [fist89, l89, palm89]

fist90 = Gesture("90", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
l90 = Gesture("90", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
palm90 = Gesture("90", "slide_2_fingers_up", "0.99", "1.0", "0.99", "88.0")
gestures_90 = [fist90, l90, palm90]

fist91 = Gesture("91", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
l91 = Gesture("91", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm91 = Gesture("91", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_91 = [fist91, l91, palm91]

fist92 = Gesture("92", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
l92 = Gesture("92", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
palm92 = Gesture("92", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
gestures_92 = [fist92, l92, palm92]

fist93 = Gesture("93", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
l93 = Gesture("93", "slide_2_fingers_right", "0.99", "1.0", "1.0", "152.0")
palm93 = Gesture("93", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_93 = [fist93, l93, palm93]

fist94 = Gesture("94", "pull_hand_in", "0.99", "1.0", "1.0", "154.0")
l94 = Gesture("94", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
palm94 = Gesture("94", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_94 = [fist94, l94, palm94]

fist95 = Gesture("95", "pull_hand_in", "0.73", "0.7", "0.72", "154.0")
l95 = Gesture("95", "slide_2_fingers_right", "0.61", "0.91", "0.73", "152.0")
palm95 = Gesture("95", "slide_2_fingers_up", "0.69", "0.81", "0.74", "159.0")
gestures_95 = [fist95, l95, palm95]

fist96 = Gesture("96", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
l96 = Gesture("96", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
palm96 = Gesture("96", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_96 = [fist96, l96, palm96]

fist97 = Gesture("97", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
l97 = Gesture("97", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
palm97 = Gesture("97", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_97 = [fist97, l97, palm97]

fist98 = Gesture("98", "pull_hand_in", "0.99", "1.0", "1.0", "154.0")
l98 = Gesture("98", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
palm98 = Gesture("98", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_98 = [fist98, l98, palm98]

fist99 = Gesture("99", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
l99 = Gesture("99", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
palm99 = Gesture("99", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
gestures_99 = [fist99, l99, palm99]

fist100 = Gesture("100", "pull_hand_in", "0.62", "0.65", "0.63", "154.0")
l100 = Gesture("100", "slide_2_fingers_right", "0.62", "0.86", "0.72", "152.0")
palm100 = Gesture("100", "slide_2_fingers_up", "0.5", "0.53", "0.52", "159.0")
gestures_100 = [fist100, l100, palm100]

fist101 = Gesture("101", "pull_hand_in", "0.87", "0.77", "0.82", "154.0")
l101 = Gesture("101", "slide_2_fingers_right","0.75", "0.88", "0.81", "152.0")
ok101 = Gesture("101", "slide_2_fingers_up", "0.84", "0.75", "0.79", "159.0")
palm101 = Gesture("101", "stop_sign", "0.74", "0.83", "0.78", "155.0")
thumb_up101 = Gesture("101", "swipe_down", "0.83", "0.82", "0.82", "150.0")
gestures_101 = [fist101, l101, ok101, palm101, thumb_up101]

fist102 = Gesture("102", "pull_hand_in", "0.91", "0.82", "0.86", "154.0")
l102 = Gesture("102", "slide_2_fingers_right", "0.81", "0.96", "0.88", "152.0")
ok102 = Gesture("102", "slide_2_fingers_up", "0.87", "0.84", "0.86", "159.0")
palm102 = Gesture("102", "stop_sign", "0.76", "0.87", "0.81", "155.0")
thumb_up102 = Gesture("102", "swipe_down", "0.86", "0.87", "0.86", "150.0")
gestures_102 = [fist102, l102, ok102, palm102, thumb_up102]

fist103 = Gesture("103", "pull_hand_in", "1.0", "0.99", "1.0", "154.0")
l103 = Gesture("103", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
ok103 = Gesture("103", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
palm103 = Gesture("103", "stop_sign", "1.0", "0.99", "0.99", "155.0")
thumb_up103 = Gesture("103", "swipe_down", "1.0", "0.99", "1.0", "150.0")
gestures_103 = [fist103, l103, ok103, palm103, thumb_up103]

fist104 = Gesture("104", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
l104 = Gesture("104", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
ok104 = Gesture("104", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
palm104 = Gesture("104", "stop_sign", "1.0", "1.0", "1.0", "155.0")
thumb_up104 = Gesture("104", "swipe_down", "1.0", "0.99", "1.0", "150.0")
gestures_104 = [fist104, l104, ok104, palm104, thumb_up104]

fist105 = Gesture("105", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l105 = Gesture("105", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok105 = Gesture("105", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm105 = Gesture("105", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up105 = Gesture("105", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_105 = [fist105, l105, ok105, palm105, thumb_up105]

fist106 = Gesture("106", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l106 = Gesture("106", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok106 = Gesture("106", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm106 = Gesture("106", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up106 = Gesture("106", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_106 = [fist106, l106, ok106, palm106, thumb_up106]

fist107 = Gesture("107", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l107 = Gesture("107", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok107 = Gesture("107", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm107 = Gesture("107", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up107 = Gesture("107", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_107 = [fist107, l107, ok107, palm107, thumb_up107]

fist108 = Gesture("108", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l108 = Gesture("108", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok108 = Gesture("108", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm108 = Gesture("108", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up108 = Gesture("108", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_108 = [fist108, l108, ok108, palm108, thumb_up108]

fist109 = Gesture("109", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l109 = Gesture("109", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok109 = Gesture("109", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm109 = Gesture("109", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up109 = Gesture("109", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_109 = [fist109, l109, ok109, palm109, thumb_up109]

fist110 = Gesture("110", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l110 = Gesture("110", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok110 = Gesture("110", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm110 = Gesture("110", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up110 = Gesture("110", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_110 = [fist110, l110, ok110, palm110, thumb_up110]

fist111 = Gesture("111", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l111 = Gesture("51", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok111 = Gesture("51", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm111 = Gesture("51", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up111 = Gesture("51", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_111 = [fist111, l111, ok111, palm111, thumb_up111]

fist112 = Gesture("112", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l112 = Gesture("51", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok112 = Gesture("51", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm112 = Gesture("51", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up112 = Gesture("51", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_112 = [fist112, l112, ok112, palm112, thumb_up112]

fist113 = Gesture("113", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l113 = Gesture("113", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok113 = Gesture("113", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm113 = Gesture("113", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up113 = Gesture("113", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_113 = [fist113, l113, ok113, palm113, thumb_up113]

fist114 = Gesture("114", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l114 = Gesture("114", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok114 = Gesture("114", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm114 = Gesture("114", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up114 = Gesture("114", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_114 = [fist114, l114, ok114, palm114, thumb_up114]

fist115 = Gesture("115", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
l115 = Gesture("115", "stop_sign", "0.88", "0.84", "0.86", "90.0")
ok115 = Gesture("115", "swipe_down", "1.0", "0.03", "0.07", "87.0")
palm115 = Gesture("115", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up115 = Gesture("115", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_115 = [fist115, l115, ok115, palm115, thumb_up115]

# Adding the experiments metrics 

exp1_metrics = Experiment_Metrics("1", gestures_1)
exp2_metrics = Experiment_Metrics("2", gestures_2)
exp3_metrics = Experiment_Metrics("3", gestures_3)
exp4_metrics = Experiment_Metrics("4", gestures_4)
exp5_metrics = Experiment_Metrics("5", gestures_5)
exp6_metrics = Experiment_Metrics("6", gestures_6)
exp7_metrics = Experiment_Metrics("7", gestures_7)
exp8_metrics = Experiment_Metrics("8", gestures_8)
exp9_metrics = Experiment_Metrics("9", gestures_9)
exp10_metrics = Experiment_Metrics("10", gestures_10)
exp11_metrics = Experiment_Metrics("11", gestures_11)
exp12_metrics = Experiment_Metrics("12", gestures_12)
exp13_metrics = Experiment_Metrics("13", gestures_13)
exp14_metrics = Experiment_Metrics("14", gestures_14)
exp15_metrics = Experiment_Metrics("15", gestures_15)
exp16_metrics = Experiment_Metrics("16", gestures_16)
exp17_metrics = Experiment_Metrics("17", gestures_17)
exp18_metrics = Experiment_Metrics("18", gestures_18)
exp19_metrics = Experiment_Metrics("19", gestures_19)
exp20_metrics = Experiment_Metrics("20", gestures_20)
exp21_metrics = Experiment_Metrics("21", gestures_21)
exp22_metrics = Experiment_Metrics("22", gestures_22)
exp23_metrics = Experiment_Metrics("23", gestures_23)
exp24_metrics = Experiment_Metrics("24", gestures_24)
exp25_metrics = Experiment_Metrics("25", gestures_25)
exp26_metrics = Experiment_Metrics("26", gestures_26)
exp27_metrics = Experiment_Metrics("27", gestures_27)
exp28_metrics = Experiment_Metrics("28", gestures_28)
exp29_metrics = Experiment_Metrics("29", gestures_29)
exp30_metrics = Experiment_Metrics("30", gestures_30)
exp31_metrics = Experiment_Metrics("31", gestures_31)
exp32_metrics = Experiment_Metrics("32", gestures_32)
exp33_metrics = Experiment_Metrics("33", gestures_33)
exp34_metrics = Experiment_Metrics("34", gestures_34)
exp35_metrics = Experiment_Metrics("35", gestures_35)
exp36_metrics = Experiment_Metrics("36", gestures_36)
exp37_metrics = Experiment_Metrics("37", gestures_37)
exp38_metrics = Experiment_Metrics("38", gestures_38)
exp39_metrics = Experiment_Metrics("39", gestures_39)
exp40_metrics = Experiment_Metrics("40", gestures_40)
exp41_metrics = Experiment_Metrics("41", gestures_41)
exp42_metrics = Experiment_Metrics("42", gestures_42)
exp43_metrics = Experiment_Metrics("43", gestures_43)
exp44_metrics = Experiment_Metrics("44", gestures_44)
exp45_metrics = Experiment_Metrics("45", gestures_45)
exp46_metrics = Experiment_Metrics("46", gestures_46)
exp47_metrics = Experiment_Metrics("47", gestures_47)
exp48_metrics = Experiment_Metrics("48", gestures_48)
exp49_metrics = Experiment_Metrics("49", gestures_49)
exp50_metrics = Experiment_Metrics("50", gestures_50)
exp51_metrics = Experiment_Metrics("51", gestures_51)
exp52_metrics = Experiment_Metrics("52", gestures_52)
exp53_metrics = Experiment_Metrics("53", gestures_53)
exp54_metrics = Experiment_Metrics("54", gestures_54)
exp55_metrics = Experiment_Metrics("55", gestures_55)
exp56_metrics = Experiment_Metrics("56", gestures_56)
exp57_metrics = Experiment_Metrics("57", gestures_57)
exp58_metrics = Experiment_Metrics("58", gestures_58)
exp59_metrics = Experiment_Metrics("59", gestures_59)
exp60_metrics = Experiment_Metrics("60", gestures_60)
exp61_metrics = Experiment_Metrics("61", gestures_61)
exp62_metrics = Experiment_Metrics("62", gestures_62)
exp63_metrics = Experiment_Metrics("63", gestures_63)
exp64_metrics = Experiment_Metrics("64", gestures_64)
exp65_metrics = Experiment_Metrics("65", gestures_65)
exp66_metrics = Experiment_Metrics("66", gestures_66)
exp67_metrics = Experiment_Metrics("67", gestures_67)
exp68_metrics = Experiment_Metrics("68", gestures_68)
exp69_metrics = Experiment_Metrics("69", gestures_69)
exp70_metrics = Experiment_Metrics("70", gestures_70)
exp71_metrics = Experiment_Metrics("71", gestures_71)
exp72_metrics = Experiment_Metrics("72", gestures_72)
exp73_metrics = Experiment_Metrics("73", gestures_73)
exp74_metrics = Experiment_Metrics("74", gestures_74)
exp75_metrics = Experiment_Metrics("75", gestures_75)
exp76_metrics = Experiment_Metrics("76", gestures_76)
exp77_metrics = Experiment_Metrics("77", gestures_77)
exp78_metrics = Experiment_Metrics("78", gestures_78)
exp79_metrics = Experiment_Metrics("79", gestures_79)
exp80_metrics = Experiment_Metrics("80", gestures_80)
exp81_metrics = Experiment_Metrics("81", gestures_81)
exp82_metrics = Experiment_Metrics("82", gestures_82)
exp83_metrics = Experiment_Metrics("83", gestures_83)
exp84_metrics = Experiment_Metrics("84", gestures_84)
exp85_metrics = Experiment_Metrics("85", gestures_85)
exp86_metrics = Experiment_Metrics("86", gestures_86)
exp87_metrics = Experiment_Metrics("87", gestures_87)
exp88_metrics = Experiment_Metrics("88", gestures_88)
exp89_metrics = Experiment_Metrics("89", gestures_89)
exp90_metrics = Experiment_Metrics("90", gestures_90)
exp91_metrics = Experiment_Metrics("91", gestures_91)
exp92_metrics = Experiment_Metrics("92", gestures_92)
exp93_metrics = Experiment_Metrics("93", gestures_93)
exp94_metrics = Experiment_Metrics("94", gestures_94)
exp95_metrics = Experiment_Metrics("95", gestures_95)
exp96_metrics = Experiment_Metrics("96", gestures_96)
exp97_metrics = Experiment_Metrics("97", gestures_97)
exp98_metrics = Experiment_Metrics("98", gestures_98)
exp99_metrics = Experiment_Metrics("99", gestures_99)
exp100_metrics = Experiment_Metrics("100", gestures_100)
exp101_metrics = Experiment_Metrics("101", gestures_101)
exp102_metrics = Experiment_Metrics("102", gestures_102)
exp103_metrics = Experiment_Metrics("103", gestures_103)
exp104_metrics = Experiment_Metrics("104", gestures_104)


# Writing the experiments
exp_1.writeNewFile(filenameExp_path)
exp_2.append_row(filenameExp_path)
exp_3.append_row(filenameExp_path)
exp_4.append_row(filenameExp_path)
exp_5.append_row(filenameExp_path)
exp_6.append_row(filenameExp_path)
exp_7.append_row(filenameExp_path)
exp_8.append_row(filenameExp_path)
exp_9.append_row(filenameExp_path)
exp_10.append_row(filenameExp_path)
exp_11.append_row(filenameExp_path)
exp_12.append_row(filenameExp_path)
exp_13.append_row(filenameExp_path)
exp_14.append_row(filenameExp_path)
exp_15.append_row(filenameExp_path)
exp_16.append_row(filenameExp_path)
exp_17.append_row(filenameExp_path)
exp_18.append_row(filenameExp_path)
exp_19.append_row(filenameExp_path)
exp_20.append_row(filenameExp_path)
exp_21.append_row(filenameExp_path)
exp_22.append_row(filenameExp_path)
exp_23.append_row(filenameExp_path)
exp_24.append_row(filenameExp_path)
exp_25.append_row(filenameExp_path)
exp_26.append_row(filenameExp_path)
exp_27.append_row(filenameExp_path)
exp_28.append_row(filenameExp_path)
exp_29.append_row(filenameExp_path)
exp_30.append_row(filenameExp_path)
exp_31.append_row(filenameExp_path)
exp_32.append_row(filenameExp_path)
exp_33.append_row(filenameExp_path)
exp_34.append_row(filenameExp_path)
exp_35.append_row(filenameExp_path)
exp_36.append_row(filenameExp_path)
exp_37.append_row(filenameExp_path)
exp_38.append_row(filenameExp_path)
exp_39.append_row(filenameExp_path)
exp_40.append_row(filenameExp_path)
exp_41.append_row(filenameExp_path)
exp_42.append_row(filenameExp_path)
exp_43.append_row(filenameExp_path)
exp_44.append_row(filenameExp_path)
exp_45.append_row(filenameExp_path)
exp_46.append_row(filenameExp_path)
exp_47.append_row(filenameExp_path)
exp_48.append_row(filenameExp_path)
exp_49.append_row(filenameExp_path)
exp_50.append_row(filenameExp_path)
exp_51.append_row(filenameExp_path)
exp_52.append_row(filenameExp_path)
exp_53.append_row(filenameExp_path)
exp_54.append_row(filenameExp_path)
exp_55.append_row(filenameExp_path)
exp_56.append_row(filenameExp_path)
exp_57.append_row(filenameExp_path)
exp_58.append_row(filenameExp_path)
exp_59.append_row(filenameExp_path)
exp_60.append_row(filenameExp_path)
exp_61.append_row(filenameExp_path)
exp_62.append_row(filenameExp_path)
exp_63.append_row(filenameExp_path)
exp_64.append_row(filenameExp_path)
exp_65.append_row(filenameExp_path)
exp_66.append_row(filenameExp_path)
exp_67.append_row(filenameExp_path)
exp_68.append_row(filenameExp_path)
exp_69.append_row(filenameExp_path)
exp_70.append_row(filenameExp_path)
exp_71.append_row(filenameExp_path)
exp_72.append_row(filenameExp_path)
exp_73.append_row(filenameExp_path)
exp_74.append_row(filenameExp_path)
exp_75.append_row(filenameExp_path)
exp_76.append_row(filenameExp_path)
exp_77.append_row(filenameExp_path)
exp_78.append_row(filenameExp_path)
exp_79.append_row(filenameExp_path)
exp_80.append_row(filenameExp_path)
exp_81.append_row(filenameExp_path)
exp_82.append_row(filenameExp_path)
exp_83.append_row(filenameExp_path)
exp_84.append_row(filenameExp_path)
exp_85.append_row(filenameExp_path)
exp_86.append_row(filenameExp_path)
exp_87.append_row(filenameExp_path)
exp_88.append_row(filenameExp_path)
exp_89.append_row(filenameExp_path)
exp_90.append_row(filenameExp_path)
exp_91.append_row(filenameExp_path)
exp_92.append_row(filenameExp_path)
exp_93.append_row(filenameExp_path)
exp_94.append_row(filenameExp_path)
exp_95.append_row(filenameExp_path)
exp_96.append_row(filenameExp_path)
exp_97.append_row(filenameExp_path)
exp_98.append_row(filenameExp_path)
exp_99.append_row(filenameExp_path)
exp_100.append_row(filenameExp_path)
exp_101.append_row(filenameExp_path)
exp_102.append_row(filenameExp_path)
exp_103.append_row(filenameExp_path)
exp_104.append_row(filenameExp_path)

# Writing the experiments metrics
exp1_metrics.writeNewFile(filenameMetrics_path)
exp2_metrics.append_row(filenameMetrics_path)
exp3_metrics.append_row(filenameMetrics_path)
exp4_metrics.append_row(filenameMetrics_path)
exp5_metrics.append_row(filenameMetrics_path)
exp6_metrics.append_row(filenameMetrics_path)
exp7_metrics.append_row(filenameMetrics_path)
exp8_metrics.append_row(filenameMetrics_path)
exp9_metrics.append_row(filenameMetrics_path)
exp10_metrics.append_row(filenameMetrics_path)
exp11_metrics.append_row(filenameMetrics_path)
exp12_metrics.append_row(filenameMetrics_path)
exp13_metrics.append_row(filenameMetrics_path)
exp14_metrics.append_row(filenameMetrics_path)
exp15_metrics.append_row(filenameMetrics_path)
exp16_metrics.append_row(filenameMetrics_path)
exp17_metrics.append_row(filenameMetrics_path)
exp18_metrics.append_row(filenameMetrics_path)
exp19_metrics.append_row(filenameMetrics_path)
exp20_metrics.append_row(filenameMetrics_path)
exp21_metrics.append_row(filenameMetrics_path)
exp22_metrics.append_row(filenameMetrics_path)
exp23_metrics.append_row(filenameMetrics_path)
exp24_metrics.append_row(filenameMetrics_path)
exp25_metrics.append_row(filenameMetrics_path)
exp26_metrics.append_row(filenameMetrics_path)
exp27_metrics.append_row(filenameMetrics_path)
exp28_metrics.append_row(filenameMetrics_path)
exp29_metrics.append_row(filenameMetrics_path)
exp30_metrics.append_row(filenameMetrics_path)
exp31_metrics.append_row(filenameMetrics_path)
exp32_metrics.append_row(filenameMetrics_path)
exp33_metrics.append_row(filenameMetrics_path)
exp34_metrics.append_row(filenameMetrics_path)
exp35_metrics.append_row(filenameMetrics_path)
exp36_metrics.append_row(filenameMetrics_path)
exp37_metrics.append_row(filenameMetrics_path)
exp38_metrics.append_row(filenameMetrics_path)
exp39_metrics.append_row(filenameMetrics_path)
exp40_metrics.append_row(filenameMetrics_path)
exp41_metrics.append_row(filenameMetrics_path)
exp42_metrics.append_row(filenameMetrics_path)
exp43_metrics.append_row(filenameMetrics_path)
exp44_metrics.append_row(filenameMetrics_path)
exp45_metrics.append_row(filenameMetrics_path)
exp46_metrics.append_row(filenameMetrics_path)
exp47_metrics.append_row(filenameMetrics_path)
exp48_metrics.append_row(filenameMetrics_path)
exp49_metrics.append_row(filenameMetrics_path)
exp50_metrics.append_row(filenameMetrics_path)
exp51_metrics.append_row(filenameMetrics_path)
exp52_metrics.append_row(filenameMetrics_path)
exp53_metrics.append_row(filenameMetrics_path)
exp54_metrics.append_row(filenameMetrics_path)
exp55_metrics.append_row(filenameMetrics_path)
exp56_metrics.append_row(filenameMetrics_path)
exp57_metrics.append_row(filenameMetrics_path)
exp58_metrics.append_row(filenameMetrics_path)
exp59_metrics.append_row(filenameMetrics_path)
exp60_metrics.append_row(filenameMetrics_path)
exp61_metrics.append_row(filenameMetrics_path)
exp62_metrics.append_row(filenameMetrics_path)
exp63_metrics.append_row(filenameMetrics_path)
exp64_metrics.append_row(filenameMetrics_path)
exp65_metrics.append_row(filenameMetrics_path)
exp66_metrics.append_row(filenameMetrics_path)
exp67_metrics.append_row(filenameMetrics_path)
exp68_metrics.append_row(filenameMetrics_path)
exp69_metrics.append_row(filenameMetrics_path)
exp70_metrics.append_row(filenameMetrics_path)
exp71_metrics.append_row(filenameMetrics_path)
exp72_metrics.append_row(filenameMetrics_path)
exp73_metrics.append_row(filenameMetrics_path)
exp74_metrics.append_row(filenameMetrics_path)
exp75_metrics.append_row(filenameMetrics_path)
exp76_metrics.append_row(filenameMetrics_path)
exp77_metrics.append_row(filenameMetrics_path)
exp78_metrics.append_row(filenameMetrics_path)
exp79_metrics.append_row(filenameMetrics_path)
exp80_metrics.append_row(filenameMetrics_path)
exp81_metrics.append_row(filenameMetrics_path)
exp82_metrics.append_row(filenameMetrics_path)
exp83_metrics.append_row(filenameMetrics_path)
exp84_metrics.append_row(filenameMetrics_path)
exp85_metrics.append_row(filenameMetrics_path)
exp86_metrics.append_row(filenameMetrics_path)
exp87_metrics.append_row(filenameMetrics_path)
exp88_metrics.append_row(filenameMetrics_path)
exp89_metrics.append_row(filenameMetrics_path)
exp90_metrics.append_row(filenameMetrics_path)
exp91_metrics.append_row(filenameMetrics_path)
exp92_metrics.append_row(filenameMetrics_path)
exp93_metrics.append_row(filenameMetrics_path)
exp94_metrics.append_row(filenameMetrics_path)
exp95_metrics.append_row(filenameMetrics_path)
exp96_metrics.append_row(filenameMetrics_path)
exp97_metrics.append_row(filenameMetrics_path)
exp98_metrics.append_row(filenameMetrics_path)
exp99_metrics.append_row(filenameMetrics_path)
exp100_metrics.append_row(filenameMetrics_path)
exp101_metrics.append_row(filenameMetrics_path)
exp102_metrics.append_row(filenameMetrics_path)
exp103_metrics.append_row(filenameMetrics_path)
exp104_metrics.append_row(filenameMetrics_path)

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
        
