import csv
import statistics

class Experiment:

    def __init__(self, id, framework, model, optimizer, learning_rate, epochs, loss_function, num_gestures, gesture_names):

        self.id = id
        self.framework = framework
        self.model = model
        self.optimizer = optimizer
        self.learning_rate  = learning_rate
        #self.epsilon = epsilon
        self.epochs = epochs
        self.loss_function = loss_function
        self.num_gestures = num_gestures
        # This attribute is a list
        self.gesture_names = gesture_names
        #self.num_videos = num_videos

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
            fieldnames = ['Id', 'Framework', 'Model', 'Optimizer', 'Learning_rate', 'Epochs', 'Loss_function', 'Num_gestures', 'Gestures']
            writer = csv.writer(csvfile, delimiter=';')
            # Writing the header
            writer.writerow(fieldnames) 
            # Writing the content
            row = [self.getId(), self.getFramework(), self.getModel(), self.getOptimizer(), self.getLearning_rate(), self.getEpochs(), self.getLoss_function(), self.getNum_gestures(), self.getGesture_names()]
            writer.writerow(row)

    def append_row(self, filename):
        # Open file in append mode
        with open(filename,'a+', newline='') as csvfile:
            # Create a writer object from csv module
            writer = csv.writer(csvfile, delimiter=';')
            # Add contents of list as last row in the csv file
            row = [self.getId(), self.getFramework(), self.getModel(), self.getOptimizer(), self.getLearning_rate(), self.getEpochs(), self.getLoss_function(), self.getNum_gestures(), self.getGesture_names()]
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

exp_1 = Experiment("1", "Keras", "ResNet50", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_2 = Experiment("2", "Keras", "ResNet101", "Adam", "0.001", "100", "categorical_crossentropy","3", "['fist', 'l', 'palm']")
exp_3 = Experiment("3", "Keras", "ResNet152", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_4 = Experiment("4", "Keras", "ResNet50V2", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_5 = Experiment("5", "Keras", "ResNet101V2", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_6 = Experiment("6", "Keras", "ResNet152V2", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_7 = Experiment("7", "Keras", "VGG16", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_8 = Experiment("8", "Keras", "VGG19", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_9 = Experiment("9", "Keras", "InceptionV3", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_10 = Experiment("10", "Keras", "InceptionResnetV2", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_11 = Experiment("11", "Keras", "MobileNetV2", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_12 = Experiment("12", "Keras", "DenseNet121", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_13 = Experiment("13", "Keras", "DenseNet169", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_14 = Experiment("14", "Keras", "DenseNet201", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_15 = Experiment("15", "Keras", "NasNetLarge", "Adam", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_16 = Experiment("16", "Keras", "ResNet50", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_17 = Experiment("17", "Keras", "ResNet101", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_18 = Experiment("18", "Keras", "ResNet152", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_19 = Experiment("19", "Keras", "ResNet50V2", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_20 = Experiment("20", "Keras", "ResNet101V2", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_21 = Experiment("21", "Keras", "ResNet152V2", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_22 = Experiment("22", "Keras", "VGG16", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_23 = Experiment("23", "Keras", "VGG19", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_24 = Experiment("24", "Keras", "InceptionV3", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_25 = Experiment("25", "Keras", "InceptionResNetV2", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_26 = Experiment("26", "Keras", "MobileNetV2", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_27 = Experiment("27", "Keras", "DenseNet121", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_28 = Experiment("28", "Keras", "DenseNet169", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_29 = Experiment("29", "Keras", "DenseNet201", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_30 = Experiment("30", "Keras", "NasNetLarge", "SGD", "0.001", "100", "categorical_crossentropy", "3", "['fist', 'l', 'palm']")
exp_31 = Experiment("31", "Keras", "ResNet50", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_32 = Experiment("32", "Keras", "ResNet101", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_33 = Experiment("33", "Keras", "ResNet152", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_34 = Experiment("34", "Keras", "ResNet50V2", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_35 = Experiment("35", "Keras", "ResNet101V2", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_36 = Experiment("36", "Keras", "ResNet152V2", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_37 = Experiment("37", "Keras", "VGG16", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_38 = Experiment("38", "Keras", "VGG19", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_39 = Experiment("39", "Keras", "InceptionV3", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_40 = Experiment("40", "Keras", "InceptionResNetV2", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_41 = Experiment("41", "Keras", "MobileNetV2", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_42 = Experiment("42", "Keras", "DenseNet121", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_43 = Experiment("43", "Keras", "DenseNet169", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_44 = Experiment("44", "Keras", "DenseNet201", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_45 = Experiment("45", "Keras", "NasNetLarge", "Adam", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_46 = Experiment("46", "Keras", "ResNet50", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_47 = Experiment("47", "Keras", "ResNet101", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_48 = Experiment("48", "Keras", "ResNet152", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_49 = Experiment("49", "Keras", "ResNet50V2", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_50 = Experiment("50", "Keras", "ResNet101V2", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_51 = Experiment("51", "Keras", "ResNet152V2", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_52 = Experiment("52", "Keras", "VGG16", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_53 = Experiment("53", "Keras", "VGG19", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_54 = Experiment("54", "Keras", "InceptionV3", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_55 = Experiment("55", "Keras", "InceptionResNetV2", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_56 = Experiment("56", "Keras", "MobileNetV2", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_57 = Experiment("57", "Keras", "DenseNet121", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_58 = Experiment("58", "Keras", "DenseNet169", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_59 = Experiment("59", "Keras", "DenseNet201", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_60 = Experiment("60", "Keras", "NasNetLarge", "SGD", "0.001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_61 = Experiment("61", "Keras", "VGG16", "Adam", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_62 = Experiment("62", "Keras", "VGG19", "Adam", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_63 = Experiment("63", "Keras", "ResNet50V2", "Adam", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_64 = Experiment("64", "Keras", "InceptionV3", "Adam", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_65 = Experiment("65", "Keras", "DenseNet201", "Adam", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_66 = Experiment("66", "Keras", "VGG16", "Adam", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_67 = Experiment("67", "Keras", "VGG19", "Adam", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_68 = Experiment("68", "Keras", "ResNet50V2", "Adam", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_69 = Experiment("69", "Keras", "InceptionV3", "Adam", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_70 = Experiment("70", "Keras", "DenseNet201", "Adam", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_71 = Experiment("71", "Keras", "VGG16", "SGD", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_72 = Experiment("72", "Keras", "VGG19", "SGD", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_73 = Experiment("73", "Keras", "ResNet50V2", "SGD", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_74 = Experiment("74", "Keras", "InceptionV3", "SGD", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_75 = Experiment("75", "Keras", "DenseNet201", "SGD", "0.0001", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_76 = Experiment("76", "Keras", "VGG16", "SGD", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_77 = Experiment("77", "Keras", "VGG19", "SGD", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_78 = Experiment("78", "Keras", "ResNet50V2", "SGD", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_79 = Experiment("79", "Keras", "InceptionV3", "SGD", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_80 = Experiment("80", "Keras", "DenseNet201", "SGD", "0.01", "100", "mse", "3", "['fist', 'l', 'palm']")
exp_81 = Experiment("81", "Keras", "VGG16", "Adam", "0.001", "10", "mse", "3", "['fist', 'l', 'palm']")
exp_82 = Experiment("82", "Keras", "VGG19", "Adam", "0.001", "10", "mse", "3", "['fist', 'l', 'palm']")
exp_83 = Experiment("83", "Keras", "ResNet50V2", "Adam", "0.001", "10", "mse", "3", "['fist', 'l', 'palm']")
exp_84 = Experiment("84", "Keras", "InceptionV3", "Adam", "0.001", "10", "mse", "3", "['fist', 'l', 'palm']")
exp_85 = Experiment("85", "Keras", "DenseNet201", "Adam", "0.001", "10", "mse", "3", "['fist', 'l', 'palm']")
exp_86 = Experiment("86", "Keras", "VGG16", "Adam", "0.001", "30", "mse", "3", "['fist', 'l', 'palm']")
exp_87 = Experiment("87", "Keras", "VGG19", "Adam", "0.001", "30", "mse", "3", "['fist', 'l', 'palm']")
exp_88 = Experiment("88", "Keras", "ResNet50V2", "Adam", "0.001", "30", "mse", "3", "['fist', 'l', 'palm']")
exp_89 = Experiment("89", "Keras", "InceptionV3", "Adam", "0.001", "30", "mse", "3", "['fist', 'l', 'palm']")
exp_90 = Experiment("90", "Keras", "DenseNet201", "Adam", "0.001", "30", "mse", "3", "['fist', 'l', 'palm']")
exp_91 = Experiment("91", "Keras", "VGG16", "Adam", "0.001", "50", "mse", "3", "['fist', 'l', 'palm']")
exp_92 = Experiment("92", "Keras", "VGG19", "Adam", "0.001", "50", "mse", "3", "['fist', 'l', 'palm']")
exp_93 = Experiment("93", "Keras", "ResNet50V2", "Adam", "0.001", "50", "mse", "3", "['fist', 'l', 'palm']")
exp_94 = Experiment("94", "Keras", "InceptionV3", "Adam", "0.001", "50", "mse", "3", "['fist', 'l', 'palm']")
exp_95 = Experiment("95", "Keras", "DenseNet201", "Adam", "0.001", "50", "mse", "3", "['fist', 'l', 'palm']")
exp_96 = Experiment("96", "Keras", "VGG16", "Adam", "0.001", "70", "mse", "3", "['fist', 'l', 'palm']")
exp_97 = Experiment("97", "Keras", "VGG19", "Adam", "0.001", "70", "mse", "3", "['fist', 'l', 'palm']")
exp_98 = Experiment("98", "Keras", "ResNet50V2", "Adam", "0.001", "70", "mse", "3", "['fist', 'l', 'palm']")
exp_99 = Experiment("99", "Keras", "InceptionV3", "Adam", "0.001", "70", "mse", "3", "['fist', 'l', 'palm']")
exp_100 = Experiment("100", "Keras", "DenseNet201", "Adam", "0.001", "70", "mse", "3", "['fist', 'l', 'palm']")
exp_101 = Experiment("101", "Keras", "ResNet50", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_102 = Experiment("102", "Keras", "ResNet101", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_103 = Experiment("103", "Keras", "ResNet152", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_104 = Experiment("104", "Keras", "ResNet50V2", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_105 = Experiment("105", "Keras", "ResNet101V2", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_106 = Experiment("106", "Keras", "ResNet152V2", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_107 = Experiment("107", "Keras", "VGG16", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_108 = Experiment("108", "Keras", "VGG19", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_109 = Experiment("109", "Keras", "InceptionV3", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_110 = Experiment("110", "Keras", "InceptionResNetV2", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_111 = Experiment("111", "Keras", "MobileNetV2", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_112 = Experiment("112", "Keras", "DenseNet121", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_113 = Experiment("113", "Keras", "DenseNet169", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_114 = Experiment("114", "Keras", "DenseNet201", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")
exp_115 = Experiment("115", "Keras", "NasNetLarge", "Adam", "0.001", "100", "mse", "5", "['fist', 'l', 'palm', 'ok', 'thumb_up']")

# Adding the metrics gesture
fist1 = Gesture("1", "fist", "0.99", "1.0", "0.99", "76.0")
l1 = Gesture("1", "l", "1.0", "0.91", "0.95", "75.0")
palm1 = Gesture("1", "palm", "0.91", "0.99", "0.95", "75.0")
gestures_1 = [fist1, l1, palm1]

fist2 = Gesture("2", "fist", "1.0", "0.74", "0.85", "76.0")
l2 = Gesture("2", "l", "1.0", "0.8", "0.89", "75.0")
palm2 = Gesture("2", "palm", "0.68", "1.0", "0.81", "75.0")
gestures_2 = [fist2, l2, palm2]

fist3 = Gesture("3", "fist", "0.97", "1.0", "0.99", "76.0")
l3 = Gesture("3", "l", "1.0", "1.0", "1.0", "75.0")
palm3 = Gesture("3", "palm", "1.0", "0.97", "0.99", "75.0")
gestures_3 = [fist3, l3, palm3]

fist4 = Gesture("4", "fist", "0.0", "0.0", "0.0", "76.0")
l4 = Gesture("4", "l", "0.0", "0.0", "0.0", "75.0")
palm4 = Gesture("4", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_4 = [fist4, l4, palm4]

fist5 = Gesture("5", "fist", "0.0", "0.0", "0.0", "76.0")
l5 = Gesture("5", "l", "0.34", "0.35", "0.34", "75.0")
palm5 = Gesture("5", "palm", "0.35", "0.69", "0.46", "75.0")
gestures_5 = [fist5, l5, palm5]

fist6 = Gesture("6", "fist", "0.34", "1.0", "0.5", "76.0")
l6 = Gesture("6", "l", "0.0", "0.0", "0.0", "75.0")
palm6 = Gesture("6", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_6 = [fist6, l6, palm6]

fist7 = Gesture("7", "fist", "1.0", "1.0", "1.0", "76.0")
l7 = Gesture("7", "l", "1.0", "1.0", "1.0", "75.0")
palm7 = Gesture("7", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_7 = [fist7, l7, palm7]

fist8 = Gesture("8", "fist", "1.0", "1.0", "1.0", "76.0")
l8 = Gesture("8", "l", "1.0", "1.0", "1.0", "75.0")
palm8 = Gesture("8", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_8 = [fist8, l8, palm8]

fist9 = Gesture("9", "fist", "0.36", "0.36", "0.36", "76.0")
l9 = Gesture("9", "l", "0.0", "0.0", "0.0", "75.0")
palm9 = Gesture("9", "palm", "0.35", "0.71", "0.47", "75.0")
gestures_9 = [fist9, l9, palm9]

fist10 = Gesture("10", "fist", "0.0", "0.0", "0.0", "76.0")
l10 = Gesture("10", "l", "0.0", "0.0", "0.0", "75.0")
palm10 = Gesture("10", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_10 = [fist10, l10, palm10]

fist11 = Gesture("11", "fist", "0.0", "0.0", "0.0", "76.0")
l11 = Gesture("11", "l", "0.0", "0.0", "0.0", "75.0")
palm11 = Gesture("11", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_11 = [fist11, l11, palm11]

fist12 = Gesture("12", "fist", "0.0", "0.0", "0.0", "76.0")
l12 = Gesture("12", "l", "0.0", "0.0", "0.0", "75.0")
palm12 = Gesture("12", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_12 = [fist12, l12, palm12]

fist13 = Gesture("13", "fist", "0.0", "0.0", "0.0", "76.0")
l13 = Gesture("13", "l", "0.28", "0.52", "0.37", "75.0")
palm13 = Gesture("13", "palm", "0.29", "0.35", "0.32", "75.0")
gestures_13 = [fist13, l13, palm13]

fist14 = Gesture("14", "fist", "0.69", "0.57", "0.62", "76.0")
l14 = Gesture("14", "l", "0.27", "0.43", "0.33", "75.0")
palm14 = Gesture("14", "palm", "0.31", "0.19", "0.23", "75.0")
gestures_14 = [fist14, l14, palm14]

fist15 = Gesture("15", "fist", "0.34", "1.0", "0.5", "76.0")
l15 = Gesture("15", "l", "0.0", "0.0", "0.0", "75.0")
palm15 = Gesture("15", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_15 = [fist15, l15, palm15]

fist16 = Gesture("16", "fist", "0.97", "1.0", "0.99", "76.0")
l16 = Gesture("16", "l", "1.0", "0.97", "0.99", "75.0")
palm16 = Gesture("16", "palm", "0.97", "0.97", "0.97", "75.0")
gestures_16 = [fist16, l16, palm16]

fist17 = Gesture("17", "fist", "1.0", "0.64", "0.78", "76.0")
l17 = Gesture("17", "l", "1.0", "0.32", "0.48", "75.0")
palm17 = Gesture("17", "palm", "0.49", "1.0", "0.66", "75.0")
gestures_17 = [fist17, l17, palm17]

fist18 = Gesture("18", "fist", "0.97", "1.0", "0.99", "76.0")
l18 = Gesture("18", "l", "1.0", "1.0", "1.0", "75.0")
palm18 = Gesture("18", "palm", "1.0", "0.97", "0.99", "75.0")
gestures_18 = [fist18, l18, palm18]

fist19 = Gesture("19", "fist", "0.0", "0.0", "0.0", "76.0")
l19 = Gesture("19", "l", "0.0", "0.0", "0.0", "75.0")
palm19 = Gesture("19", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_19 = [fist19, l19, palm19]

fist20 = Gesture("20", "fist", "0.0", "0.0", "0.0", "76.0")
l20 = Gesture("20", "l", "0.0", "0.0", "0.0", "75.0")
palm20 = Gesture("20", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_20 = [fist20, l20, palm20]

fist21 = Gesture("21", "fist", "0.34", "1.0", "0.5", "76.0")
l21 = Gesture("21", "l", "0.0", "0.0", "0.0", "75.0")
palm21 = Gesture("21", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_21 = [fist21, l21, palm21]

fist22 = Gesture("22", "fist", "0.99", "1.0", "0.99", "76.0")
l22 = Gesture("22", "l", "1.0", "1.0", "1.0", "75.0")
palm22 = Gesture("22", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_22 = [fist22, l22, palm22]

fist23 = Gesture("23", "fist", "1.0", "1.0", "1.0", "76.0")
l23 = Gesture("23", "l", "1.0", "1.0", "1.0", "75.0")
palm23 = Gesture("23", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_23 = [fist23, l23, palm23]

fist24 = Gesture("24", "fist", "0.0", "0.0", "0.0", "76.0")
l24 = Gesture("24", "l", "0.0", "0.0", "0.0", "75.0")
palm24 = Gesture("24", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_24 = [fist24, l24, palm24]

fist25 = Gesture("25", "fist", "0.0", "0.0", "0.0", "76.0")
l25 = Gesture("25", "l", "0.0", "0.0", "0.0", "75.0")
palm25 = Gesture("25", "palm", "0.33", "0.99", "0.49", "75.0")
gestures_25 = [fist25, l25, palm25]

fist26 = Gesture("26", "fist", "0.0", "0.0", "0.0", "76.0")
l26 = Gesture("26", "l", "0.0", "0.0", "0.0", "75.0")
palm26 = Gesture("26", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_26 = [fist26, l26, palm26]

fist27 = Gesture("27", "fist", "0.0", "0.0", "0.0", "76.0")
l27 = Gesture("27", "l", "0.65", "0.35", "0.45", "75.0")
palm27 = Gesture("27", "palm", "0.33", "0.81", "0.47", "75.0")
gestures_27 = [fist27, l27, palm27]

fist28 = Gesture("28", "fist", "0.35", "1.0", "0.52", "76.0")
l28 = Gesture("28", "l", "1.0", "0.03", "0.05", "75.0")
palm28 = Gesture("28", "palm", "0.89", "0.11", "0.19", "75.0")
gestures_28 = [fist28, l28, palm28]

fist29 = Gesture("29", "fist", "0.0", "0.0", "0.0", "76.0")
l29 = Gesture("29", "l", "0.23", "0.04", "0.07", "75.0")
palm29 = Gesture("29", "palm", "0.31", "0.87", "0.45", "75.0")
gestures_29 = [fist29, l29, palm29]

fist30 = Gesture("30", "fist", "0.34", "1.0", "0.5", "76.0")
l30 = Gesture("30", "l", "0.0", "0.0", "0.0", "75.0")
palm30 = Gesture("30", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_30 = [fist30, l30, palm30]

fist31 = Gesture("31", "fist", "1.0", "1.0", "1.0", "76.0")
l31 = Gesture("31", "l", "1.0", "0.59", "0.74", "75.0")
palm31 = Gesture("31", "palm", "0.71", "1.0", "0.83", "75.0")
gestures_31 = [fist31, l31, palm31]

fist32 = Gesture("32", "fist", "0.97", "0.79", "0.87", "76.0")
l32 = Gesture("32", "l", "1.0", "0.8", "0.89", "75.0")
palm32 = Gesture("32", "palm", "0.7", "0.97", "0.82", "75.0")
gestures_32 = [fist32, l32, palm32]

fist33 = Gesture("33", "fist", "0.87", "1.0", "0.93", "76.0")
l33 = Gesture("33", "l", "1.0", "0.87", "0.93", "75.0")
palm33 = Gesture("33", "palm", "0.99", "0.97", "0.98", "75.0")
gestures_33 = [fist33, l33, palm33]

fist34 = Gesture("34", "fist", "0.0", "0.0", "0.0", "76.0")
l34 = Gesture("34", "l", "0.0", "0.0", "0.0", "75.0")
palm34 = Gesture("34", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_34 = [fist34, l34, palm34]

fist35 = Gesture("35", "fist", "0.0", "0.0", "0.0", "76.0")
l35 = Gesture("35", "l", "0.0", "0.0", "0.0", "75.0")
palm35 = Gesture("35", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_35 = [fist35, l35, palm35]

fist36 = Gesture("36", "fist", "0.0", "0.0", "0.0", "76.0")
l36 = Gesture("36", "l", "0.33", "1.0", "0.5", "75.0")
palm36 = Gesture("36", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_36 = [fist36, l36, palm36]

fist37 = Gesture("37", "fist", "0.99", "1.0", "0.99", "76.0")
l37 = Gesture("37", "l", "1.0", "1.0", "1.0", "75.0")
palm37 = Gesture("37", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_37 = [fist37, l37, palm37]

fist38 = Gesture("38", "fist", "1.0", "1.0", "1.0", "76.0")
l38 = Gesture("38", "l", "1.0", "1.0", "1.0", "75.0")
palm38 = Gesture("38", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_38 = [fist38, l38, palm38]

fist39 = Gesture("39", "fist", "0.0", "0.0", "0.0", "76.0")
l39 = Gesture("39", "l", "0.0", "0.0", "0.0", "75.0")
palm39 = Gesture("39", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_39 = [fist39, l39, palm39]

fist40 = Gesture("40", "fist", "0.0", "0.0", "0.0", "76.0")
l40 = Gesture("40", "l", "0.0", "0.0", "0.0", "75.0")
palm40 = Gesture("40", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_40 = [fist40, l40, palm40]

fist41 = Gesture("41", "fist", "0.0", "0.0", "0.0", "76.0")
l41 = Gesture("41", "l", "0.0", "0.0", "0.0", "75.0")
palm41 = Gesture("41", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_41 = [fist41, l41, palm41]

fist42 = Gesture("42", "fist", "0.0", "0.0", "0.0", "76.0")
l42 = Gesture("42", "l", "0.38", "0.35", "0.36", "75.0")
palm42 = Gesture("42", "palm", "0.38", "0.79", "0.51", "75.0")
gestures_42 = [fist42, l42, palm42]

fist43 = Gesture("43", "fist", "1.0", "0.32", "0.48", "76.0")
l43 = Gesture("43", "l", "0.0", "0.0", "0.0", "75.0")
palm43 = Gesture("43", "palm", "0.37", "1.0", "0.54", "75.0")
gestures_43 = [fist43, l43, palm43]

fist44 = Gesture("44", "fist", "0.0", "0.0", "0.0", "76.0")
l44 = Gesture("44", "l", "0.38", "0.56", "0.45", "75.0")
palm44 = Gesture("44", "palm", "0.2", "0.31", "0.24", "75.0")
gestures_44 = [fist44, l44, palm44]

fist45 = Gesture("45", "fist", "0.34", "1.0", "0.5", "76.0")
l45 = Gesture("45", "l", "0.0", "0.0", "0.0", "75.0")
palm45 = Gesture("45", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_45 = [fist45, l45, palm45]

fist46 = Gesture("46", "fist", "0.93", "1.0", "0.96", "76.0")
l46 = Gesture("46", "l", "1.0", "0.35", "0.51", "75.0")
palm46 = Gesture("46", "palm", "0.63", "0.99", "0.77", "75.0")
gestures_46 = [fist46, l46, palm46]

fist47 = Gesture("47", "fist", "0.96", "0.64", "0.77", "76.0")
l47 = Gesture("47", "l", "1.0", "0.72", "0.84", "75.0")
palm47 = Gesture("47", "palm", "0.6", "0.97", "0.74", "75.0")
gestures_47 = [fist47, l47, palm47]

fist48 = Gesture("48", "fist", "0.96", "1.0", "0.98", "76.0")
l48 = Gesture("48", "l", "1.0", "0.61", "0.76", "75.0")
palm48 = Gesture("48", "palm", "0.73", "0.99", "0.84", "75.0")
gestures_48 = [fist48, l48, palm48]

fist49 = Gesture("49", "fist", "0.0", "0.0", "0.0", "76.0")
l49 = Gesture("49", "l", "0.0", "0.0", "0.0", "75.0")
palm49 = Gesture("49", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_49 = [fist49, l49, palm49]

fist50 = Gesture("50", "fist", "0.0", "0.0", "0.0", "76.0")
l50 = Gesture("50", "l", "0.0", "0.0", "0.0", "75.0")
palm50 = Gesture("50", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_50 = [fist50, l50, palm50]

fist51 = Gesture("51", "fist", "0.34", "1.0", "0.5", "76.0")
l51 = Gesture("51", "l", "0.0", "0.0", "0.0", "75.0")
palm51 = Gesture("51", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_51 = [fist51, l51, palm51]

fist52 = Gesture("52", "fist", "0.93", "1.0", "0.96", "76.0")
l52 = Gesture("52", "l", "1.0", "1.0", "1.0", "75.0")
palm52 = Gesture("52", "palm", "1.0", "0.92", "0.96", "75.0")
gestures_52 = [fist52, l52, palm52]

fist53 = Gesture("53", "fist", "0.93", "1.0", "0.96", "76.0")
l53 = Gesture("53", "l", "1.0", "1.0", "1.0", "75.0")
palm53 = Gesture("53", "palm", "1.0", "0.92", "0.96", "75.0")
gestures_53 = [fist53, l53, palm53]

fist54 = Gesture("54", "fist", "0.0", "0.0", "0.0", "76.0")
l54 = Gesture("54", "l", "0.34", "1.0", "0.51", "75.0")
palm54 = Gesture("54", "palm", "1.0", "0.05", "0.1", "75.0")
gestures_54 = [fist54, l54, palm54]

fist55 = Gesture("55", "fist", "0.0", "0.0", "0.0", "76.0")
l55 = Gesture("55", "l", "0.0", "0.0", "0.0", "75.0")
palm55 = Gesture("55", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_55 = [fist55, l55, palm55]

fist56 = Gesture("56", "fist", "0.31", "0.68", "0.43", "76.0")
l56 = Gesture("56", "l", "0.0", "0.0", "0.0", "75.0")
palm56 = Gesture("56", "palm", "0.42", "0.33", "0.37", "75.0")
gestures_56 = [fist56, l56, palm56]

fist57 = Gesture("57", "fist", "0.0", "0.0", "0.0", "76.0")
l57 = Gesture("57", "l", "0.33", "1.0", "0.5", "75.0")
palm57 = Gesture("57", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_57 = [fist57, l57, palm57]

fist58 = Gesture("58", "fist", "0.46", "1.0", "0.63", "76.0")
l58 = Gesture("58", "l", "0.85", "0.69", "0.76", "75.0")
palm58 = Gesture("58", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_58 = [fist58, l58, palm58]

fist59 = Gesture("59", "fist", "0.0", "0.0", "0.0", "76.0")
l59 = Gesture("59", "l", "0.33", "1.0", "0.5", "75.0")
palm59 = Gesture("59", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_59 = [fist59, l59, palm59]

fist60 = Gesture("60", "fist", "0.5", "0.7", "0.58", "76.0")
l60 = Gesture("60", "l", "0.41", "0.65", "0.51", "75.0")
palm60 = Gesture("60", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_60 = [fist60, l60, palm60]

fist61 = Gesture("61", "fist", "0.96", "1.0", "0.98", "76.0")
l61 = Gesture("61", "l", "1.0", "1.0", "1.0", "75.0")
palm61 = Gesture("61", "palm", "1.0", "0.96", "0.98", "75.0")
gestures_61 = [fist61, l61, palm61]

fist62 = Gesture("62", "fist", "0.93", "1.0", "0.96", "76.0")
l62 = Gesture("62", "l", "1.0", "1.0", "1.0", "75.0")
palm62 = Gesture("62", "palm", "1.0", "0.92", "0.96", "75.0")
gestures_62 = [fist62, l62, palm62]

fist63 = Gesture("63", "fist", "0.37", "1.0", "0.54", "76.0")
l63 = Gesture("63", "l", "0.0", "0.0", "0.0", "75.0")
palm63 = Gesture("63", "palm", "1.0", "0.29", "0.45", "75.0")
gestures_63 = [fist63, l63, palm63]

fist64 = Gesture("64", "fist", "0.0", "0.0", "0.0", "76.0")
l64 = Gesture("64", "l", "0.33", "1.0", "0.5", "75.0")
palm64 = Gesture("64", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_64 = [fist64, l64, palm64]

fist65 = Gesture("65", "fist", "0.0", "0.0", "0.0", "76.0")
l65 = Gesture("65", "l", "0.33", "1.0", "0.5", "75.0")
palm65 = Gesture("65", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_65 = [fist65, l65, palm65]

fist66 = Gesture("66", "fist", "0.0", "0.0", "0.0", "76.0")
l66 = Gesture("66", "l", "0.0", "0.0", "0.0", "75.0")
palm66 = Gesture("66", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_66 = [fist66, l66, palm66]

fist67 = Gesture("67", "fist", "0.0", "0.0", "0.0", "76.0")
l67 = Gesture("67", "l", "0.33", "1.0", "0.5", "75.0")
palm67 = Gesture("67", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_67 = [fist67, l67, palm67]

fist68 = Gesture("68", "fist", "0.0", "0.0", "0.0", "76.0")
l68 = Gesture("68", "l", "0.0", "0.0", "0.0", "75.0")
palm68 = Gesture("68", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_68 = [fist68, l68, palm68]

fist69 = Gesture("69", "fist", "0.34", "0.7", "0.46", "76.0")
l69 = Gesture("69", "l", "0.0", "0.0", "0.0", "75.0")
palm69 = Gesture("69", "palm", "0.16", "0.15", "0.15", "75.0")
gestures_69 = [fist69, l69, palm69]

fist70 = Gesture("70", "fist", "0.0", "0.0", "0.0", "76.0")
l70 = Gesture("70", "l", "0.6", "0.84", "0.7", "75.0")
palm70 = Gesture("70", "palm", "0.35", "0.56", "0.43", "75.0")
gestures_70 = [fist70, l70, palm70]

fist71 = Gesture("71", "fist", "0.95", "1.0", "0.97", "76.0")
l71 = Gesture("71", "l", "0.97", "1.0", "0.99", "75.0")
palm71 = Gesture("71", "palm", "1.0", "0.92", "0.96", "75.0")
gestures_71 = [fist71, l71, palm71]

fist72 = Gesture("72", "fist", "0.94", "1.0", "0.97", "76.0")
l72 = Gesture("72", "l", "1.0", "1.0", "1.0", "75.0")
palm72 = Gesture("72", "palm", "1.0", "0.93", "0.97", "75.0")
gestures_72 = [fist72, l72, palm72]

fist73 = Gesture("73", "fist", "0.34", "1.0", "0.5", "76.0")
l73 = Gesture("73", "l", "0.0", "0.0", "0.0", "75.0")
palm73 = Gesture("73", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_73 = [fist73, l73, palm73]

fist74 = Gesture("74", "fist", "0.08", "0.09", "0.09", "76.0")
l74 = Gesture("74", "l", "0.0", "0.0", "0.0", "75.0")
palm74 = Gesture("74", "palm", "0.18", "0.35", "0.24", "75.0")
gestures_74 = [fist74, l74, palm74]

fist75 = Gesture("75", "fist", "0.34", "1.0", "0.5", "76.0")
l75 = Gesture("75", "l", "0.0", "0.0", "0.0", "75.0")
palm75 = Gesture("75", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_75 = [fist75, l75, palm75]

fist76 = Gesture("76", "fist", "1.0", "1.0", "1.0", "76.0")
l76 = Gesture("76", "l", "1.0", "1.0", "1.0", "75.0")
palm76 = Gesture("76", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_76 = [fist76, l76, palm76]

fist77 = Gesture("77", "fist", "1.0", "1.0", "1.0", "76.0")
l77 = Gesture("77", "l", "1.0", "1.0", "1.0", "75.0")
palm77 = Gesture("77", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_77 = [fist77, l77, palm77]

fist78 = Gesture("78", "fist", "0.0", "0.0", "0.0", "76.0")
l78 = Gesture("78", "l", "0.0", "0.0", "0.0", "75.0")
palm78 = Gesture("78", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_78 = [fist78, l78, palm78]

fist79 = Gesture("79", "fist", "0.36", "0.36", "0.36", "76.0")
l79 = Gesture("79", "l", "0.0", "0.0", "0.0", "75.0")
palm79 = Gesture("79", "palm", "0.36", "0.72", "0.48", "75.0")
gestures_79 = [fist79, l79, palm79]

fist80 = Gesture("80", "fist", "0.42", "0.64", "0.51", "76.0")
l80 = Gesture("80", "l", "0.03", "0.04", "0.04", "75.0")
palm80 = Gesture("80", "palm", "0.36", "0.07", "0.11", "75.0")
gestures_80 = [fist80, l80, palm80]

fist81 = Gesture("81", "fist", "0.94", "1.0", "0.97", "76.0")
l81 = Gesture("81", "l", "0.84", "1.0", "0.91", "75.0")
palm81 = Gesture("81", "palm", "1.0", "0.75", "0.85", "75.0")
gestures_81 = [fist81, l81, palm81]

fist82 = Gesture("82", "fist", "0.94", "1.0", "0.97", "76.0")
l82 = Gesture("82", "l", "1.0", "1.0", "1.0", "75.0")
palm82 = Gesture("82", "palm", "1.0", "0.93", "0.97", "75.0")
gestures_82 = [fist82, l82, palm82]

fist83 = Gesture("83", "fist", "0.0", "0.0", "0.0", "76.0")
l83 = Gesture("83", "l", "0.0", "0.0", "0.0", "75.0")
palm83 = Gesture("83", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_83 = [fist83, l83, palm83]

fist84 = Gesture("84", "fist", "0.0", "0.0", "0.0", "76.0")
l84 = Gesture("84", "l", "0.0", "0.0", "0.0", "75.0")
palm84 = Gesture("84", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_84 = [fist84, l84, palm84]

fist85 = Gesture("85", "fist", "0.0", "0.0", "0.0", "76.0")
l85 = Gesture("85", "l", "0.42", "0.73", "0.53", "75.0")
palm85 = Gesture("85", "palm", "0.31", "0.39", "0.34", "75.0")
gestures_85 = [fist85, l85, palm85]

fist86 = Gesture("86", "fist", "0.99", "1.0", "0.99", "76.0")
l86 = Gesture("86", "l", "1.0", "1.0", "1.0", "75.0")
palm86 = Gesture("86", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_86 = [fist86, l86, palm86]

fist87 = Gesture("87", "fist", "0.99", "1.0", "0.99", "76.0")
l87 = Gesture("87", "l", "1.0", "1.0", "1.0", "75.0")
palm87 = Gesture("87", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_87 = [fist87, l87, palm87]

fist88 = Gesture("88", "fist", "0.0", "0.0", "0.0", "76.0")
l88 = Gesture("88", "l", "0.0", "0.0", "0.0", "75.0")
palm88 = Gesture("88", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_88 = [fist88, l88, palm88]

fist89 = Gesture("89", "fist", "0.34", "1.0", "0.5", "76.0")
l89 = Gesture("89", "l", "0.0", "0.0", "0.0", "75.0")
palm89 = Gesture("89", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_89 = [fist89, l89, palm89]

fist90 = Gesture("90", "fist", "0.0", "0.0", "0.0", "76.0")
l90 = Gesture("90", "l", "0.33", "1.0", "0.5", "75.0")
palm90 = Gesture("90", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_90 = [fist90, l90, palm90]

fist91 = Gesture("91", "fist", "0.99", "1.0", "0.99", "76.0")
l91 = Gesture("91", "l", "1.0", "1.0", "1.0", "75.0")
palm91 = Gesture("91", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_91 = [fist91, l91, palm91]

fist92 = Gesture("92", "fist", "0.99", "1.0", "0.99", "76.0")
l92 = Gesture("92", "l", "1.0", "1.0", "1.0", "75.0")
palm92 = Gesture("92", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_92 = [fist92, l92, palm92]

fist93 = Gesture("93", "fist", "0.0", "0.0", "0.0", "76.0")
l93 = Gesture("93", "l", "0.0", "0.0", "0.0", "75.0")
palm93 = Gesture("93", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_93 = [fist93, l93, palm93]

fist94 = Gesture("94", "fist", "0.0", "0.0", "0.0", "76.0")
l94 = Gesture("94", "l", "0.0", "0.0", "0.0", "75.0")
palm94 = Gesture("94", "palm", "0.33", "1.0", "0.5", "75.0")
gestures_94 = [fist94, l94, palm94]

fist95 = Gesture("95", "fist", "0.0", "0.0", "0.0", "76.0")
l95 = Gesture("95", "l", "0.89", "0.21", "0.34", "75.0")
palm95 = Gesture("95", "palm", "0.35", "0.97", "0.52", "75.0")
gestures_95 = [fist95, l95, palm95]

fist96 = Gesture("96", "fist", "0.99", "1.0", "0.99", "76.0")
l96 = Gesture("96", "l", "1.0", "1.0", "1.0", "75.0")
palm96 = Gesture("96", "palm", "1.0", "0.99", "0.99", "75.0")
gestures_96 = [fist96, l96, palm96]

fist97 = Gesture("97", "fist", "1.0", "1.0", "1.0", "76.0")
l97 = Gesture("97", "l", "1.0", "1.0", "1.0", "75.0")
palm97 = Gesture("97", "palm", "1.0", "1.0", "1.0", "75.0")
gestures_97 = [fist97, l97, palm97]

fist98 = Gesture("98", "fist", "0.0", "0.0", "0.0", "76.0")
l98 = Gesture("98", "l", "0.0", "0.0", "0.0", "75.0")
palm98 = Gesture("98", "palm", "0.33", "1.0", "0.5", "75.0" )
gestures_98 = [fist98, l98, palm98]

fist99 = Gesture("99", "fist", "0.46", "0.59", "0.52", "76.0")
l99 = Gesture("99", "l", "0.0", "0.0", "0.0", "75.0")
palm99 = Gesture("99", "palm", "0.38", "0.64", "0.47", "75.0")
gestures_99 = [fist99, l99, palm99]

fist100 = Gesture("100", "fist", "0.69", "0.64", "0.67", "76.0")
l100 = Gesture("100", "l", "0.36", "0.75", "0.49", "75.0")
palm100 = Gesture("100", "palm", "0.0", "0.0", "0.0", "75.0")
gestures_100 = [fist100, l100, palm100]

fist101 = Gesture("101", "fist", "0.89", "0.93", "0.91", "75.0")
l101 = Gesture("101", "l", "1.0", "0.64", "0.78", "75.0")
ok101 = Gesture("101", "ok", "1.0", "0.32", "0.48", "75.0")
palm101 = Gesture("101", "palm", "0.42", "1.0", "0.59", "75.0")
thumb_up101 = Gesture("101", "thumb_up", "1.0", "0.6", "0.75", "75.0")
gestures_101 = [fist101, l101, ok101, palm101, thumb_up101]

fist102 = Gesture("102", "fist", "1.0", "0.81", "0.9", "75.0")
l102 = Gesture("102", "l", "1.0", "0.4", "0.57", "75.0")
ok102 = Gesture("102", "ok", "0.3", "0.11", "0.16", "75.0")
palm102 = Gesture("102", "palm", "0.33", "1.0", "0.49", "75.0")
thumb_up102 = Gesture("102", "thumb_up", "1.0", "0.37", "0.54", "75.0")
gestures_102 = [fist102, l102, ok102, palm102, thumb_up102]

fist103 = Gesture("103", "fist", "0.95", "1.0", "0.97", "75.0")
l103 = Gesture("103", "l", "0.94", "1.0", "0.97", "75.0")
ok103 = Gesture("103", "ok", "1.0", "0.56", "0.72", "75.0")
palm103 = Gesture("103", "palm", "0.65", "1.0", "0.79", "75.0")
thumb_up103 = Gesture("103", "thumb_up", "1.0", "0.79", "0.88", "75.0")
gestures_103 = [fist103, l103, ok103, palm103, thumb_up103]

fist104 = Gesture("104", "fist", "0.17", "0.4", "0.24", "75.0")
l104 = Gesture("104", "l", "0.0", "0.0", "0.0", "75.0")
ok104 = Gesture("104", "ok", "0.0", "0.0", "0.0", "75.0")
palm104 = Gesture("104", "palm", "0.15", "0.4", "0.22", "75.0")
thumb_up104 = Gesture("104", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_104 = [fist104, l104, ok104, palm104, thumb_up104]

fist105 = Gesture("105", "fist", "0.0", "0.0", "0.0", "75.0")
l105 = Gesture("105", "l", "0.0", "0.0", "0.0", "75.0")
ok105 = Gesture("105", "ok", "0.0", "0.0", "0.0", "75.0")
palm105 = Gesture("105", "palm", "0.0", "0.0", "0.0", "75.0")
thumb_up105 = Gesture("105", "thumb_up", "0.2", "1.0", "0.33", "75.0")
gestures_105 = [fist105, l105, ok105, palm105, thumb_up105]

fist106 = Gesture("106", "fist", "0.2", "1.0", "0.33", "75.0")
l106 = Gesture("106", "l", "0.0", "0.0", "0.0", "75.0")
ok106 = Gesture("106", "ok", "0.0", "0.0", "0.0", "75.0")
palm106 = Gesture("106", "palm", "0.0", "0.0", "0.0", "75.0")
thumb_up106 = Gesture("106", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_106 = [fist106, l106, ok106, palm106, thumb_up106]

fist107 = Gesture("107", "fist", "1.0", "1.0", "1.0", "75.0")
l107 = Gesture("107", "l", "1.0", "1.0", "1.0", "75.0")
ok107 = Gesture("107", "ok", "1.0", "1.0", "1.0", "75.0")
palm107 = Gesture("107", "palm", "1.0", "1.0", "1.0", "75.0")
thumb_up107 = Gesture("107", "thumb_up", "1.0", "1.0", "1.0", "75.0")
gestures_107 = [fist107, l107, ok107, palm107, thumb_up107]

fist108 = Gesture("108", "fist", "1.0", "1.0", "1.0", "75.0")
l108 = Gesture("108", "l", "1.0", "1.0", "1.0", "75.0")
ok108 = Gesture("108", "ok", "1.0", "0.97", "0.99", "75.0")
palm108 = Gesture("108", "palm", "0.97", "1.0", "0.99", "75.0")
thumb_up108 = Gesture("108", "thumb_up", "1.0", "1.0", "1.0", "75.0")
gestures_108 = [fist108, l108, ok108, palm108, thumb_up108]

fist109 = Gesture("109", "fist", "0.0", "0.0", "0.0", "75.0")
l109 = Gesture("109", "l", "0.0", "0.0", "0.0", "75.0")
ok109 = Gesture("109", "ok", "0.0", "0.0", "0.0", "75.0")
palm109 = Gesture("109", "palm", "0.2", "1.0", "0.33", "75.0")
thumb_up109 = Gesture("109", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_109 = [fist109, l109, ok109, palm109, thumb_up109]

fist110 = Gesture("110", "fist", "0.0", "0.0", "0.0", "75.0")
l110 = Gesture("110", "l", "0.0", "0.0", "0.0", "75.0")
ok110 = Gesture("110", "ok", "0.0", "0.0", "0.0", "75.0")
palm110 = Gesture("110", "palm", "0.2", "1.0", "0.33", "75.0")
thumb_up110 = Gesture("110", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_110 = [fist110, l110, ok110, palm110, thumb_up110]

fist111 = Gesture("111", "fist", "1.0", "0.03", "0.05", "75.0")
l111 = Gesture("111", "l", "0.0", "0.0", "0.0", "75.0")
ok111 = Gesture("111", "ok", "0.26", "0.84", "0.4", "75.0")
palm111 = Gesture("111", "palm", "0.3", "0.52", "0.38", "75.0")
thumb_up111 = Gesture("111", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_111 = [fist111, l111, ok111, palm111, thumb_up111]

fist112 = Gesture("112", "fist", "0.0", "0.0", "0.0", "75.0")
l112 = Gesture("112", "l", "0.11", "0.01", "0.02", "75.0")
ok112 = Gesture("112", "ok", "0.09", "0.05", "0.07", "75.0")
palm112 = Gesture("112", "palm", "0.15", "0.63", "0.24", "75.0")
thumb_up112 = Gesture("112", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_112 = [fist112, l112, ok112, palm112, thumb_up112]

fist113 = Gesture("113", "fist", "0.3", "0.36", "0.33", "75.0")
l113 = Gesture("113", "l", "0.0", "0.0", "0.0", "75.0")
ok113 = Gesture("113", "ok", "0.16", "0.61", "0.25", "75.0")
palm113 = Gesture("113", "palm", "0.0", "0.0", "0.0", "75.0")
thumb_up113 = Gesture("113", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_113 = [fist113, l113, ok113, palm113, thumb_up113]

fist114 = Gesture("114", "fist", "0.31", "0.69", "0.43", "75.0")
l114 = Gesture("114", "l", "0.26", "0.72", "0.38", "75.0")
ok114 = Gesture("114", "ok", "0.0", "0.0", "0.0", "75.0")
palm114 = Gesture("114", "palm", "0.0", "0.0", "0.0", "75.0")
thumb_up114 = Gesture("114", "thumb_up", "0.0", "0.0", "0.0", "75.0")
gestures_114 = [fist114, l114, ok114, palm114, thumb_up114]

fist115 = Gesture("115", "fist", "0.0", "0.0", "0.0", "75.0")
l115 = Gesture("115", "l", "0.2", "1.0", "0.33", "75.0")
ok115 = Gesture("115", "ok", "0.0", "0.0", "0.0", "75.0")
palm115 = Gesture("115", "palm", "0.0", "0.0", "0.0", "75.0")
thumb_up115 = Gesture("115", "thumb_up", "0.0", "0.0", "0.0", "75.0")
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
exp105_metrics = Experiment_Metrics("104", gestures_105)
exp106_metrics = Experiment_Metrics("104", gestures_106)
exp107_metrics = Experiment_Metrics("104", gestures_107)
exp108_metrics = Experiment_Metrics("104", gestures_108)
exp109_metrics = Experiment_Metrics("104", gestures_109)
exp110_metrics = Experiment_Metrics("104", gestures_110)
exp111_metrics = Experiment_Metrics("104", gestures_111)
exp112_metrics = Experiment_Metrics("104", gestures_112)
exp113_metrics = Experiment_Metrics("104", gestures_113)
exp114_metrics = Experiment_Metrics("104", gestures_114)
exp115_metrics = Experiment_Metrics("104", gestures_115)


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
exp_105.append_row(filenameExp_path)
exp_106.append_row(filenameExp_path)
exp_107.append_row(filenameExp_path)
exp_108.append_row(filenameExp_path)
exp_109.append_row(filenameExp_path)
exp_110.append_row(filenameExp_path)
exp_111.append_row(filenameExp_path)
exp_112.append_row(filenameExp_path)
exp_113.append_row(filenameExp_path)
exp_114.append_row(filenameExp_path)
exp_115.append_row(filenameExp_path)

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
exp105_metrics.append_row(filenameMetrics_path)
exp106_metrics.append_row(filenameMetrics_path)
exp107_metrics.append_row(filenameMetrics_path)
exp108_metrics.append_row(filenameMetrics_path)
exp109_metrics.append_row(filenameMetrics_path)
exp110_metrics.append_row(filenameMetrics_path)
exp111_metrics.append_row(filenameMetrics_path)
exp112_metrics.append_row(filenameMetrics_path)
exp113_metrics.append_row(filenameMetrics_path)
exp114_metrics.append_row(filenameMetrics_path)
exp115_metrics.append_row(filenameMetrics_path)

# READING THE FILES

# Reading the experiments features
list_exp = []
with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)   
    for row in reader:
        experiment = Experiment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
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
        
