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
exp_2 = Experiment("2", Keras, ResNet101, Adam, 0.001, 100, categorical_crossentropy,3)

exp_3 = Experiment(3, Keras, ResNet152, Adam, 0.001, 100, categorical_crossentropy, 3)
exp_4 = Experiment(4, Keras, ResNet50V2, Adam, 0.001, 100, categorical_crossentropy, 3)
# TO DO CONTINUE HERE
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
exp_52 = Experiment("52", "Keras", "VGG16", "Adam", "0.001", "0.1", "100", "mse", "5", gestures_5g, "10")
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
swipe_left18 = Gesture("18", "swipe_left", "0.94", "0.97", "0.95", "123.0")
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

stop_sign31 = Gesture("31", "stop_sign", "0.32", "0.51", "0.39", "90.0")
swipe_left31 = Gesture("31", "swipe_left", "0.26", "0.28", "0.27", "88.0")
thumb_up31 = Gesture("31", "thumb_up", "0.24", "0.06", "0.09", "86.0")
gestures_31 = [stop_sign31, swipe_left31, thumb_up31]

stop_sign32 = Gesture("32", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left32 = Gesture("32", "swipe_left", "0.33", "1.0", "0.5", "88.0")
thumb_up32 = Gesture("32", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_32 = [stop_sign32, swipe_left32, thumb_up32]

stop_sign33 = Gesture("33", "stop_sign", "0.34", "1.0", "0.51", "90.0")
swipe_left33 = Gesture("33", "swipe_left", "0.0", "0.0", "0.0", "88.0")
thumb_up33 = Gesture("33", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_33 = [stop_sign33, swipe_left33, thumb_up33]

stop_sign34 = Gesture("34", "stop_sign", "0.36", "0.39", "0.38", "90.0")
swipe_left34 = Gesture("34", "swipe_left", "1.0", "0.08", "0.15", "88.0")
thumb_up34 = Gesture("34", "thumb_up", "0.34", "0.63", "0.44", "86.0")
gestures_34 = [stop_sign34, swipe_left34, thumb_up34]

stop_sign35 = Gesture("35", "stop_sign", "0.2", "0.11", "0.14", "90.0")
swipe_left35 = Gesture("35", "swipe_left", "0.4", "0.11", "0.18", "88.0")
thumb_up35 = Gesture("35", "thumb_up", "0.29", "0.63", "0.39", "86.0")
gestures_35 = [stop_sign35, swipe_left35, thumb_up35]

stop_sign36 = Gesture("36", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left36 = Gesture("36", "swipe_left", "0.33", "1.0", "0.5", "88.0")
thumb_up36 = Gesture("36", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_36 = [stop_sign36, swipe_left36, thumb_up36]

stop_sign37 = Gesture("37", "stop_sign", "0.38", "0.03", "0.06", "90.0")
swipe_left37 = Gesture("37", "swipe_left", "1.0", "0.01", "0.02", "88.0")
thumb_up37 = Gesture("37", "thumb_up", "0.32", "0.94", "0.48", "86.0")
gestures_37 = [stop_sign37, swipe_left37, thumb_up37]

stop_sign38 = Gesture("38", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left38 = Gesture("38", "swipe_left", "0.4", "0.92", "0.56", "123.0")
thumb_up38 = Gesture("38", "thumb_up", "0.37", "0.08", "0.13", "86.0")
gestures_38 = [stop_sign38, swipe_left38, thumb_up38]

stop_sign39 = Gesture("39", "stop_sign", "0.33", "0.64", "0.43", "90.0")
swipe_left39 = Gesture("39", "swipe_left", "1.0", "0.07", "0.14", "123.0")
thumb_up39 = Gesture("39", "thumb_up", "0.29", "0.37", "0.32", "86.0")
gestures_39 = [stop_sign39, swipe_left39, thumb_up39]

stop_sign40 = Gesture("40", "stop_sign", "0.35", "0.99", "0.52", "90.0")
swipe_left40 = Gesture("40", "swipe_left", "1.0", "0.03", "0.07", "88.0")
thumb_up40 = Gesture("40", "thumb_up", "0.2", "0.02", "0.04", "86.0")
gestures_40 = [stop_sign40, swipe_left40, thumb_up40]

stop_sign41 = Gesture("41", "stop_sign", "0.38", "0.06", "0.1", "90.0")
swipe_left41 = Gesture("41", "swipe_left", "1.0", "0.11", "0.2", "88.0")
thumb_up41 = Gesture("41", "thumb_up", "0.34", "0.94", "0.5", "86.0")
gestures_41 = [stop_sign41, swipe_left41, thumb_up41]

stop_sign42 = Gesture("42", "stop_sign", "0.0", "0.0", "0.0", "90.0")
swipe_left42 = Gesture("42", "swipe_left", "0.18", "0.05", "0.07", "88.0")
thumb_up42 = Gesture("42", "thumb_up", "0.32", "0.87", "0.47", "86.0")
gestures_42 = [stop_sign42, swipe_left42, thumb_up42]

stop_sign43 = Gesture("43", "stop_sign", "0.34", "1.0", "0.51", "90.0")
swipe_left43 = Gesture("43", "swipe_left", "0.0", "0.0", "0.0", "88.0")
thumb_up43 = Gesture("43", "thumb_up", "0.0", "0.0", "0.0", "86.0")
gestures_43 = [stop_sign43, swipe_left43, thumb_up43]

stop_sign44 = Gesture("44", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left44 = Gesture("44", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up44 = Gesture("44", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_44 = [stop_sign44, swipe_left44, thumb_up44]

stop_sign45 = Gesture("45", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left45 = Gesture("45", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up45 = Gesture("45", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_45 = [stop_sign45, swipe_left45, thumb_up45]

stop_sign46 = Gesture("46", "stop_sign", "0.95", "0.6", "0.73", "90.0")
swipe_left46 = Gesture("46", "swipe_left", "0.7", "0.91", "0.79", "88.0")
thumb_up46 = Gesture("46", "thumb_up", "0.81", "0.87", "0.84", "86.0")
gestures_46 = [stop_sign46, swipe_left46, thumb_up46]

stop_sign47 = Gesture("47", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left47 = Gesture("47", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up47 = Gesture("47", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_47 = [stop_sign47, swipe_left47, thumb_up47]

stop_sign48 = Gesture("48", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_left48 = Gesture("48", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up48 = Gesture("48", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_48 = [stop_sign48, swipe_left48, thumb_up48]

slide_2_fingers_right49 = Gesture("49", "slide_2_fingers_right", "1.0", "0.17", "0.29", "89.0")
stop_sign49 = Gesture("49", "stop_sign", "1.0", "0.5", "0.67", "90.0")
swipe_down49 = Gesture("49", "swipe_down", "1.0", "0.01", "0.02", "87.0")
swipe_left49 = Gesture("49", "swipe_left", "0.85", "0.67", "0.75", "87.0")
thumb_up49 = Gesture("49", "thumb_up", "0.28", "1.0", "0.43", "86.0")
gestures_49 = [slide_2_fingers_right49, stop_sign49, swipe_down49, swipe_left49, thumb_up49]

slide_2_fingers_right50 = Gesture("50", "slide_2_fingers_right", "1.0", "0.12", "0.22", "89.0")
stop_sign50 = Gesture("50", "stop_sign", "1.0", "0.32", "0.49", "90.0")
swipe_down50 = Gesture("50", "swipe_down", "0.67", "0.02", "0.04", "87.0")
swipe_left50 = Gesture("50", "swipe_left", "0.69", "0.7", "0.7", "88.0")
thumb_up50 = Gesture("50", "thumb_up", "0.28", "1.0", "0.44", "86.0")
gestures_50 = [slide_2_fingers_right50, stop_sign50, swipe_down50, swipe_left50, thumb_up50]

slide_2_fingers_right51 = Gesture("51", "slide_2_fingers_right", "0.32", "0.87", "0.47", "86.0")
stop_sign51 = Gesture("51", "stop_sign", "0.88", "0.84", "0.86", "90.0")
swipe_down51 = Gesture("51", "swipe_down", "1.0", "0.03", "0.07", "87.0")
swipe_left51 = Gesture("51", "swipe_left", "0.75", "0.85", "0.8", "88.0")
thumb_up51 = Gesture("51", "thumb_up", "0.38", "1.0", "0.55", "86.0")
gestures_51 = [slide_2_fingers_right51, stop_sign51, swipe_down51, swipe_left51, thumb_up51]

slide_2_fingers_right52 = Gesture("52", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign52 = Gesture("52", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down52 = Gesture("52", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left52 = Gesture("52", "swipe_left", "1.0", "1.0", "1.0", "87.0")
thumb_up52 = Gesture("52", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_52 = [slide_2_fingers_right52, stop_sign52, swipe_down52, swipe_left52, thumb_up52]

slide_2_fingers_right53 = Gesture("53", "slide_2_fingers_right", "1.0", "0.99", "0.99", "89.0")
stop_sign53 = Gesture("53", "stop_sign", "0.99", "1.0", "0.99", "90.0")
swipe_down53 = Gesture("53", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left53 = Gesture("53", "swipe_left", "1.0", "0.99", "0.99", "88.0")
thumb_up53 = Gesture("53", "thumb_up", "0.99", "1.0", "0.99", "86.0")
gestures_53 = [slide_2_fingers_right53, stop_sign53, swipe_down53, swipe_left53, thumb_up53]

slide_2_fingers_right54 = Gesture("54", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign54 = Gesture("54", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down54 = Gesture("54", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left54 = Gesture("54", "swipe_left", "1.0", "1.0", "1.0", "87.0")
thumb_up54 = Gesture("54", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_54 = [slide_2_fingers_right54, stop_sign54, swipe_down54, swipe_left54, thumb_up54]

slide_2_fingers_right55 = Gesture("55", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign55 = Gesture("55", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down55 = Gesture("55", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left55 = Gesture("55", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up55 = Gesture("55", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_55 = [slide_2_fingers_right55, stop_sign55, swipe_down55, swipe_left55, thumb_up55]

slide_2_fingers_right56 = Gesture("56", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
stop_sign56 = Gesture("56", "stop_sign", "0.24", "0.16", "0.19", "90.0")
swipe_down56 = Gesture("56", "swipe_down", "0.0", "0.0", "0.0", "87.0")
swipe_left56 = Gesture("56", "swipe_left", "0.44", "0.29", "0.35", "87.0")
thumb_up56 = Gesture("56", "thumb_up", "0.23", "0.84", "0.36", "86.0")
gestures_56 = [slide_2_fingers_right56, stop_sign56, swipe_down56, swipe_left56, thumb_up56]

slide_2_fingers_right57 = Gesture("57", "slide_2_fingers_right", "1.0", "0.26", "0.41", "89.0")
stop_sign57 = Gesture("57", "stop_sign", "1.0", "0.44", "0.62", "90.0")
swipe_down57 = Gesture("57", "swipe_down", "1.0", "0.1", "0.19", "87.0")
swipe_left57 = Gesture("57", "swipe_left", "0.83", "0.69", "0.75", "87.0")
thumb_up57 = Gesture("57", "thumb_up", "0.29", "1.0", "0.45", "86.0")
gestures_57 = [slide_2_fingers_right57, stop_sign57, swipe_down57, swipe_left57, thumb_up57]

slide_2_fingers_right58 = Gesture("58", "slide_2_fingers_right", "1.0", "0.25", "0.4", "89.0")
stop_sign58 = Gesture("58", "stop_sign", "0.93", "0.46", "0.61", "90.0")
swipe_down58 = Gesture("58", "swipe_down", "1.0", "0.07", "0.13", "87.0")
swipe_left58 = Gesture("58", "swipe_left", "0.55", "0.99", "0.71", "88.0")
thumb_up58 = Gesture("58", "thumb_up", "0.4", "0.98", "0.57", "86.0")
gestures_58 = [slide_2_fingers_right58, stop_sign58, swipe_down58, swipe_left58, thumb_up58]

slide_2_fingers_right59 = Gesture("59", "slide_2_fingers_right", "0.96", "0.53", "0.68", "89.0")
stop_sign59 = Gesture("59", "stop_sign", "0.95", "0.89", "0.92", "90.0")
swipe_down59 = Gesture("59", "swipe_down", "1.0", "0.21", "0.34", "87.0")
swipe_left59 = Gesture("59", "swipe_left", "0.69", "0.84", "0.76", "87.0")
thumb_up59 = Gesture("59", "thumb_up", "0.47", "0.99", "0.63", "86.0")
gestures_59 = [slide_2_fingers_right59, stop_sign59, swipe_down59, swipe_left59, thumb_up59]

slide_2_fingers_right60 = Gesture("60", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign60 = Gesture("60", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down60 = Gesture("60", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left60 = Gesture("60", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up60 = Gesture("60", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_60 = [slide_2_fingers_right60, stop_sign60, swipe_down60, swipe_left60, thumb_up60]

slide_2_fingers_right61 = Gesture("61", "slide_2_fingers_right", "1.0", "0.99", "0.99", "89.0")
stop_sign61 = Gesture("61", "stop_sign", "0.99", "1.0", "0.99", "90.0")
swipe_down61 = Gesture("61", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left61 = Gesture("61", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up61 = Gesture("61", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_61 = [slide_2_fingers_right61, stop_sign61, swipe_down61, swipe_left61, thumb_up61]

slide_2_fingers_right62 = Gesture("62", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign62 = Gesture("62", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down62 = Gesture("62", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left62 = Gesture("62", "swipe_left", "1.0", "1.0", "1.0", "87.0")
thumb_up62 = Gesture("62", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_62 = [slide_2_fingers_right62, stop_sign62, swipe_down62, swipe_left62, thumb_up62]

slide_2_fingers_right63 = Gesture("63", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
stop_sign63 = Gesture("63", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down63 = Gesture("63", "swipe_down", "1.0", "1.0", "1.0", "87.0")
swipe_left63 = Gesture("63", "swipe_left", "1.0", "1.0", "1.0", "87.0")
thumb_up63 = Gesture("63", "thumb_up", "1.0", "1.0", "1.0", "86.0")
gestures_63 = [slide_2_fingers_right63, stop_sign63, swipe_down63, swipe_left63, thumb_up63]

pull_hand_in64 = Gesture("64", "pull_hand_in", "0.79", "0.34", "0.48", "90.0")
slide_2_fingers_right64 = Gesture("64", "slide_2_fingers_right", "1.0", "0.04", "0.09", "89.0")
slide_2_fingers_up64 = Gesture("64", "slide_2_fingers_up", "0.44", "0.83", "0.57", "88.0")
stop_sign64 = Gesture("64", "stop_sign", "0.87", "0.29", "0.43", "90.0")
swipe_down64 = Gesture("64", "swipe_down", "1.0", "0.09", "0.17", "86.0")
swipe_left64 = Gesture("64", "swipe_left", "0.91", "0.35", "0.51", "88.0")
thumb_up64 = Gesture("64", "thumb_up", "0.21", "1.0", "0.34", "86.0")
zoom_in_with_2_fingers64 = Gesture("64", "zoom_in_with_2_fingers", "1.0", "0.09", "0.16", "91.0")
gestures_64 = [pull_hand_in64, slide_2_fingers_right64, slide_2_fingers_up64, stop_sign64, swipe_down64, swipe_left64, thumb_up64, zoom_in_with_2_fingers64]

pull_hand_in65 = Gesture("65", "pull_hand_in", "0.69", "0.61", "0.65", "90.0")
slide_2_fingers_right65 = Gesture("65", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
slide_2_fingers_up65 = Gesture("65", "slide_2_fingers_up", "0.62", "0.62", "0.62", "88.0")
stop_sign65 = Gesture("65", "stop_sign", "0.74", "0.22", "0.34", "90.0")
swipe_down65 = Gesture("65", "swipe_down", "1.0", "0.06", "0.11", "86.0")
swipe_left65 = Gesture("65", "swipe_left", "0.55", "0.59", "0.57", "88.0")
thumb_up65 = Gesture("65", "thumb_up", "0.21", "0.97", "0.35", "86.0")
zoom_in_with_2_fingers65 = Gesture("65", "zoom_in_with_2_fingers", "1.0", "0.22", "0.36", "91.0")
gestures_65 = [pull_hand_in65, slide_2_fingers_right65, slide_2_fingers_up65, stop_sign65, swipe_down65, swipe_left65, thumb_up65, zoom_in_with_2_fingers65]

pull_hand_in66 = Gesture("66", "pull_hand_in", "0.43", "0.86", "0.57", "90.0")
slide_2_fingers_right66 = Gesture("66", "slide_2_fingers_right", "0.91", "0.34", "0.49", "89.0")
slide_2_fingers_up66 = Gesture("66", "slide_2_fingers_up", "0.75", "0.43", "0.55", "88.0")
stop_sign66 = Gesture("66", "stop_sign", "1.0", "0.44", "0.62", "90.0")
swipe_down66 = Gesture("66", "swipe_down", "1.0", "0.06", "0.11", "86.0")
swipe_left66 = Gesture("66", "swipe_left", "0.62", "0.77", "0.69", "88.0")
thumb_up66 = Gesture("66", "thumb_up", "0.35", "0.93", "0.51", "86.0")
zoom_in_with_2_fingers66 = Gesture("66", "zoom_in_with_2_fingers", "0.98", "0.63", "0.77", "91.0")
gestures_66 = [pull_hand_in66, slide_2_fingers_right66, slide_2_fingers_up66, stop_sign66, swipe_down66, swipe_left66, thumb_up66, zoom_in_with_2_fingers66]

pull_hand_in67 = Gesture("67", "pull_hand_in", "0.89", "0.93", "0.91", "90.0")
slide_2_fingers_right67 = Gesture("67", "slide_2_fingers_right", "0.94", "1.0", "0.97", "89.0")
slide_2_fingers_up67 = Gesture("67", "slide_2_fingers_up", "0.93", "0.92", "0.93", "88.0")
stop_sign67 = Gesture("67", "stop_sign", "0.89", "1.0", "0.94", "90.0")
swipe_down67 = Gesture("67", "swipe_down", "1.0", "0.85", "0.92", "86.0")
swipe_left67 = Gesture("67", "swipe_left", "0.98", "1.0", "0.99", "88.0")
thumb_up67 = Gesture("67", "thumb_up", "1.0", "0.88", "0.94", "86.0")
zoom_in_with_2_fingers67 = Gesture("67", "zoom_in_with_2_fingers", "0.99", "1.0", "0.99", "91.0")
gestures_67 = [pull_hand_in67, slide_2_fingers_right67, slide_2_fingers_up67, stop_sign67, swipe_down67, swipe_left67, thumb_up67, zoom_in_with_2_fingers67]

pull_hand_in68 = Gesture("68", "pull_hand_in", "0.99", "0.87", "0.92", "90.0")
slide_2_fingers_right68 = Gesture("68", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up68 = Gesture("68", "slide_2_fingers_up", "0.94", "0.94", "0.94", "88.0")
stop_sign68 = Gesture("68", "stop_sign", "0.85", "0.99", "0.91", "90.0")
swipe_down68 = Gesture("68", "swipe_down", "1.0", "0.99", "0.99", "86.0")
swipe_left68 = Gesture("68", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up68 = Gesture("68", "thumb_up", "1.0", "0.97", "0.98", "86.0")
zoom_in_with_2_fingers68 = Gesture("68", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_68 = [pull_hand_in68, slide_2_fingers_right68, slide_2_fingers_up68, stop_sign68, swipe_down68, swipe_left68, thumb_up68, zoom_in_with_2_fingers68]

pull_hand_in69 = Gesture("69", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right69 = Gesture("69", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up69 = Gesture("69", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign69 = Gesture("69", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down69 = Gesture("69", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left69 = Gesture("69", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up69 = Gesture("69", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers69 = Gesture("69", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_69 = [pull_hand_in69, slide_2_fingers_right69, slide_2_fingers_up69, stop_sign69, swipe_down69, swipe_left69, thumb_up69, zoom_in_with_2_fingers69]

pull_hand_in70 = Gesture("70", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right70 = Gesture("70", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up70 = Gesture("70", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign70 = Gesture("70", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down70 = Gesture("70", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left70 = Gesture("70", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up70 = Gesture("70", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers70 = Gesture("70", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_70 = [pull_hand_in70, slide_2_fingers_right70, slide_2_fingers_up70, stop_sign70, swipe_down70, swipe_left70, thumb_up70, zoom_in_with_2_fingers70]


pull_hand_in71 = Gesture("71", "pull_hand_in", "0.25", "0.44", "0.32", "90.0")
slide_2_fingers_right71 = Gesture("71", "slide_2_fingers_right", "0.22", "0.21", "0.21", "89.0")
slide_2_fingers_up71 = Gesture("71", "slide_2_fingers_up", "0.33", "0.22", "0.26", "88.0")
stop_sign71 = Gesture("71", "stop_sign", "0.33", "0.29", "0.31", "90.0")
swipe_down71 = Gesture("71", "swipe_down", "0.55", "0.13", "0.21", "86.0")
swipe_left71 = Gesture("71", "swipe_left", "0.22", "0.52", "0.31", "88.0")
thumb_up71 = Gesture("71", "thumb_up", "0.0", "0.0", "0.0", "86.0")
zoom_in_with_2_fingers71 = Gesture("71", "zoom_in_with_2_fingers", "0.4", "0.42", "0.41", "91.0")
gestures_71 = [pull_hand_in71, slide_2_fingers_right71, slide_2_fingers_up71, stop_sign71, swipe_down71, swipe_left71, thumb_up71, zoom_in_with_2_fingers71]

pull_hand_in72 = Gesture("72", "pull_hand_in", "0.81", "0.47", "0.59", "90.0")
slide_2_fingers_right72 = Gesture("72", "slide_2_fingers_right", "1.0", "0.13", "0.24", "89.0")
slide_2_fingers_up72 = Gesture("72", "slide_2_fingers_up", "0.49", "0.97", "0.65", "88.0")
stop_sign72 = Gesture("72", "stop_sign", "0.91", "0.68", "0.78", "90.0")
swipe_down72 = Gesture("72", "swipe_down", "1.0", "0.01", "0.02", "86.0")
swipe_left72 = Gesture("72", "swipe_left", "0.77", "0.69", "0.73", "88.0")
thumb_up72 = Gesture("72", "thumb_up", "0.27", "1.0", "0.43", "86.0")
zoom_in_with_2_fingers72 = Gesture("72", "zoom_in_with_2_fingers", "1.0", "0.12", "0.22", "91.0")
gestures_72 = [pull_hand_in72, slide_2_fingers_right72, slide_2_fingers_up72, stop_sign72, swipe_down72, swipe_left72, thumb_up72, zoom_in_with_2_fingers72]


pull_hand_in73 = Gesture("73", "pull_hand_in", "0.97", "0.39", "0.56", "90.0")
slide_2_fingers_right73 = Gesture("73", "slide_2_fingers_right", "1.0", "0.11", "0.2", "89.0")
slide_2_fingers_up73 = Gesture("73", "slide_2_fingers_up", "0.67", "0.66", "0.66", "88.0")
stop_sign73 = Gesture("73", "stop_sign", "0.91", "0.43", "0.59", "90.0")
swipe_down73 = Gesture("73", "swipe_down", "1.0", "0.02", "0.05", "86.0")
swipe_left73 = Gesture("73", "swipe_left", "0.67", "0.91", "0.77", "88.0")
thumb_up73 = Gesture("73", "thumb_up", "0.22", "1.0", "0.36", "86.0")
zoom_in_with_2_fingers73 = Gesture("73", "zoom_in_with_2_fingers", "1.0", "0.23", "0.38", "91.0")
gestures_73 = [pull_hand_in73, slide_2_fingers_right73, slide_2_fingers_up73, stop_sign73, swipe_down73, swipe_left73, thumb_up73, zoom_in_with_2_fingers73]

pull_hand_in74 = Gesture("74", "pull_hand_in", "0.67", "0.83", "0.74", "90.0")
slide_2_fingers_right74 = Gesture("74", "slide_2_fingers_right", "1.0", "0.38", "0.55", "89.0")
slide_2_fingers_up74 = Gesture("74", "slide_2_fingers_up", "0.77", "0.98", "0.86", "88.0")
stop_sign74 = Gesture("74", "stop_sign", "0.87", "0.74", "0.8", "90.0")
swipe_down74 = Gesture("74", "swipe_down", "1.0", "0.17", "0.3", "86.0")
swipe_left74 = Gesture("74", "swipe_left", "0.78", "0.84", "0.81", "88.0")
thumb_up74 = Gesture("74", "thumb_up", "0.41", "1.0", "0.59", "86.0")
zoom_in_with_2_fingers74 = Gesture("74", "zoom_in_with_2_fingers", "1.0", "0.6", "0.75", "91.0")
gestures_74 = [pull_hand_in74, slide_2_fingers_right74, slide_2_fingers_up74, stop_sign74, swipe_down74, swipe_left74, thumb_up74, zoom_in_with_2_fingers74]

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

pull_hand_in77 = Gesture("77", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right77 = Gesture("77", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up77 = Gesture("77", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign77 = Gesture("77", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down77 = Gesture("77", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left77 = Gesture("77", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up77 = Gesture("77", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers77 = Gesture("77", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_77 = [pull_hand_in77, slide_2_fingers_right77, slide_2_fingers_up77, stop_sign77, swipe_down77, swipe_left77, thumb_up77, zoom_in_with_2_fingers77]

pull_hand_in78 = Gesture("78", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right78 = Gesture("78", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up78 = Gesture("78", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign78 = Gesture("78", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down78 = Gesture("78", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left78 = Gesture("78", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up78 = Gesture("78", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers78 = Gesture("78", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
gestures_78 = [pull_hand_in78, slide_2_fingers_right78, slide_2_fingers_up78, stop_sign78, swipe_down78, swipe_left78, thumb_up78, zoom_in_with_2_fingers78]

pull_hand_in79 = Gesture("79", "pull_hand_in", "0.68", "0.44", "0.54", "90.0")
slide_2_fingers_right79 = Gesture("79", "slide_2_fingers_right", "0.0", "0.0", "0.0", "89.0")
slide_2_fingers_up79 = Gesture("79", "slide_2_fingers_up", "0.41", "0.8", "0.54", "88.0")
stop_sign79 = Gesture("79", "stop_sign", "0.77", "0.62", "0.69", "90.0")
swipe_down79 = Gesture("79", "swipe_down", "1.0", "0.12", "0.21", "86.0")
swipe_left79 = Gesture("79", "swipe_left", "0.69", "0.6", "0.64", "88.0")
thumb_up79 = Gesture("79", "thumb_up", "0.19", "0.85", "0.31", "86.0")
zoom_in_with_2_fingers79 = Gesture("79", "zoom_in_with_2_fingers", "1.0", "0.05", "0.1", "91.0")
zoom_in_with_full_hand79 = Gesture("79", "zoom_in_with_full_hand", "1.0", "0.06", "0.11", "87.0")
zoom_out_with_2_fingers79 = Gesture("79", "zoom_out_with_2_fingers", "0.58", "0.66", "0.62", "89.0")
gestures_79 = [pull_hand_in79, slide_2_fingers_right79, slide_2_fingers_up79, stop_sign79, swipe_down79, swipe_left79, thumb_up79, zoom_in_with_2_fingers79, zoom_in_with_full_hand79, zoom_out_with_2_fingers79]

pull_hand_in80 = Gesture("80", "pull_hand_in", "0.49", "0.19", "0.27", "90.0")
slide_2_fingers_right80 = Gesture("80", "slide_2_fingers_right", "1.0", "0.01", "0.02", "89.0")
slide_2_fingers_up80 = Gesture("80", "slide_2_fingers_up", "0.93", "0.15", "0.25", "88.0")
stop_sign80 = Gesture("80", "stop_sign", "0.61", "0.16", "0.25", "90.0")
swipe_down80 = Gesture("80", "swipe_down", "1.0", "0.09", "0.17", "86.0")
swipe_left80 = Gesture("80", "swipe_left", "0.61", "0.7", "0.66", "88.0")
thumb_up80 = Gesture("80", "thumb_up", "0.21", "0.94", "0.35", "86.0")
zoom_in_with_2_fingers80 = Gesture("80", "zoom_in_with_2_fingers", "1.0", "0.13", "0.23", "91.0")
zoom_in_with_full_hand80 = Gesture("80", "zoom_in_with_full_hand", "1.0", "0.09", "0.16", "90.0")
zoom_out_with_2_fingers80 = Gesture("80", "zoom_out_with_2_fingers", "0.25", "0.85", "0.39", "88.0")
gestures_80 = [pull_hand_in80, slide_2_fingers_right80, slide_2_fingers_up80, stop_sign80, swipe_down80, swipe_left80, thumb_up80, zoom_in_with_2_fingers80, zoom_in_with_full_hand80, zoom_out_with_2_fingers80]

pull_hand_in81 = Gesture("81", "pull_hand_in", "0.42", "0.72", "0.53", "90.0")
slide_2_fingers_right81 = Gesture("81", "slide_2_fingers_right", "1.0", "0.44", "0.61", "89.0")
slide_2_fingers_up81 = Gesture("81", "slide_2_fingers_up", "0.79", "0.22", "0.34", "88.0")
stop_sign81 = Gesture("81", "stop_sign", "0.75", "0.56", "0.64", "90.0")
swipe_down81 = Gesture("81", "swipe_down", "1.0", "0.07", "0.13", "86.0")
swipe_left81 = Gesture("81", "swipe_left", "0.37", "0.95", "0.53", "88.0")
thumb_up81 = Gesture("81", "thumb_up", "0.46", "0.72", "0.56", "86.0")
zoom_in_with_2_fingers81 = Gesture("81", "zoom_in_with_2_fingers", "1.0", "0.52", "0.68", "91.0")
zoom_in_with_full_hand81 = Gesture("81", "zoom_in_with_full_hand", "1.0", "0.18", "0.31", "87.0")
zoom_out_with_2_fingers81 = Gesture("81", "zoom_out_with_2_fingers", "0.45", "0.83", "0.58", "89.0")
gestures_81 = [pull_hand_in81, slide_2_fingers_right81, slide_2_fingers_up81, stop_sign81, swipe_down81, swipe_left81, thumb_up81, zoom_in_with_2_fingers81, zoom_in_with_full_hand81, zoom_out_with_2_fingers81]


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

pull_hand_in83 = Gesture("83", "pull_hand_in", "0.92", "0.81", "0.86", "90.0")
slide_2_fingers_right83 = Gesture("83", "slide_2_fingers_right", "0.91", "1.0", "0.95", "89.0")
slide_2_fingers_up83 = Gesture("83", "slide_2_fingers_up", "0.99", "0.81", "0.89", "88.0")
stop_sign83 = Gesture("83", "stop_sign", "0.73", "0.99", "0.84", "90.0")
swipe_down83 = Gesture("83", "swipe_down", "0.96", "0.78", "0.86", "86.0")
swipe_left83 = Gesture("83", "swipe_left", "0.98", "0.97", "0.97", "88.0")
thumb_up83 = Gesture("83", "thumb_up", "0.98", "0.94", "0.96", "86.0")
zoom_in_with_2_fingers83 = Gesture("83", "zoom_in_with_2_fingers", "0.98", "1.0", "0.99", "91.0")
zoom_in_with_full_hand83 = Gesture("83", "zoom_in_with_full_hand", "1.0", "0.84", "0.92", "90.0")
zoom_out_with_2_fingers83 = Gesture("83", "zoom_out_with_2_fingers", "0.78", "0.94", "0.86", "88.0")
gestures_83 = [pull_hand_in83, slide_2_fingers_right83, slide_2_fingers_up83, stop_sign83, swipe_down83, swipe_left83, thumb_up83, zoom_in_with_2_fingers83, zoom_in_with_full_hand83, zoom_out_with_2_fingers83]

pull_hand_in84 = Gesture("84", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right84 = Gesture("84", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up84 = Gesture("84", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign84 = Gesture("84", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down84 = Gesture("84", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left84 = Gesture("84", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up84 = Gesture("84", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers84 = Gesture("84", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand84 = Gesture("84", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "87.0")
zoom_out_with_2_fingers84 = Gesture("84", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "89.0")
gestures_84 = [pull_hand_in84, slide_2_fingers_right84, slide_2_fingers_up84, stop_sign84, swipe_down84, swipe_left84, thumb_up84, zoom_in_with_2_fingers84, zoom_in_with_full_hand84, zoom_out_with_2_fingers84]


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

pull_hand_in86 = Gesture("86", "pull_hand_in", "0.67", "0.46", "0.54", "90.0")
slide_2_fingers_right86 = Gesture("86", "slide_2_fingers_right", "1.0", "0.03", "0.07", "89.0")
slide_2_fingers_up86 = Gesture("86", "slide_2_fingers_up", "0.48", "0.9", "0.62", "88.0")
stop_sign86 = Gesture("86", "stop_sign", "0.9", "0.73", "0.81", "90.0")
swipe_down86 = Gesture("86", "swipe_down", "1.0", "0.12", "0.21", "86.0")
swipe_left86 = Gesture("86", "swipe_left", "0.71", "0.64", "0.67", "88.0")
thumb_up86 = Gesture("86", "thumb_up", "0.2", "0.94", "0.33", "86.0")
zoom_in_with_2_fingers86 = Gesture("86", "zoom_in_with_2_fingers", "1.0", "0.1", "0.18", "91.0")
zoom_in_with_full_hand86 = Gesture("86", "zoom_in_with_full_hand", "1.0", "0.01", "0.02", "87.0")
zoom_out_with_2_fingers86 = Gesture("86", "zoom_out_with_2_fingers", "0.73", "0.64", "0.68", "89.0")
gestures_86 = [pull_hand_in86, slide_2_fingers_right86, slide_2_fingers_up86, stop_sign86, swipe_down86, swipe_left86, thumb_up86, zoom_in_with_2_fingers86, zoom_in_with_full_hand86, zoom_out_with_2_fingers86]

pull_hand_in87 = Gesture("87", "pull_hand_in", "0.79", "0.33", "0.47", "90.0")
slide_2_fingers_right87 = Gesture("87", "slide_2_fingers_right", "1.0", "0.04", "0.09", "89.0")
slide_2_fingers_up87 = Gesture("87", "slide_2_fingers_up", "0.45", "0.67", "0.54", "88.0")
stop_sign87 = Gesture("87", "stop_sign", "0.84", "0.18", "0.29", "90.0")
swipe_down87 = Gesture("87", "swipe_down", "0.0", "0.0", "0.0", "86.0")
swipe_left87 = Gesture("87", "swipe_left", "0.84", "0.49", "0.62", "88.0")
thumb_up87 = Gesture("87", "thumb_up", "0.22", "0.95", "0.35", "86.0")
zoom_in_with_2_fingers87 = Gesture("87", "zoom_in_with_2_fingers", "0.97", "0.33", "0.49", "91.0")
zoom_in_with_full_hand87 = Gesture("87", "zoom_in_with_full_hand", "1.0", "0.04", "0.09", "90.0")
zoom_out_with_2_fingers87 = Gesture("87", "zoom_out_with_2_fingers", "0.34", "0.89", "0.5", "88.0")
gestures_87 = [pull_hand_in87, slide_2_fingers_right87, slide_2_fingers_up87, stop_sign87, swipe_down87, swipe_left87, thumb_up87, zoom_in_with_2_fingers87, zoom_in_with_full_hand87, zoom_out_with_2_fingers87]


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

pull_hand_in90 = Gesture("90", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
slide_2_fingers_right90 = Gesture("90", "slide_2_fingers_right", "0.99", "1.0", "0.99", "89.0")
slide_2_fingers_up90 = Gesture("90", "slide_2_fingers_up", "0.99", "1.0", "0.99", "88.0")
stop_sign90 = Gesture("90", "stop_sign", "0.98", "0.99", "0.98", "90.0")
swipe_down90 = Gesture("90", "swipe_down", "1.0", "0.99", "0.99", "86.0")
swipe_left90 = Gesture("90", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up90 = Gesture("90", "thumb_up", "1.0", "0.95", "0.98", "86.0")
zoom_in_with_2_fingers90 = Gesture("90", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand90 = Gesture("90", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "90.0")
zoom_out_with_2_fingers90 = Gesture("90", "zoom_out_with_2_fingers", "0.95", "0.98", "0.96", "88.0")
gestures_90 = [pull_hand_in90, slide_2_fingers_right90, slide_2_fingers_up90, stop_sign90, swipe_down90, swipe_left90, thumb_up90, zoom_in_with_2_fingers90, zoom_in_with_full_hand90, zoom_out_with_2_fingers90]

pull_hand_in91 = Gesture("91", "pull_hand_in", "1.0", "1.0", "1.0", "90.0")
slide_2_fingers_right91 = Gesture("91", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up91 = Gesture("91", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign91 = Gesture("91", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down91 = Gesture("91", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left91 = Gesture("91", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up91 = Gesture("91", "thumb_up", "1.0", "1.0", "1.0", "86.0")
zoom_in_with_2_fingers91 = Gesture("91", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand91 = Gesture("91", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "90.0")
zoom_out_with_2_fingers91 = Gesture("91", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "88.0")
gestures_91 = [pull_hand_in91, slide_2_fingers_right91, slide_2_fingers_up91, stop_sign91, swipe_down91, swipe_left91, thumb_up91, zoom_in_with_2_fingers91, zoom_in_with_full_hand91, zoom_out_with_2_fingers91]

pull_hand_in92 = Gesture("92", "pull_hand_in", "1.0", "0.99", "0.99", "90.0")
slide_2_fingers_right92 = Gesture("92", "slide_2_fingers_right", "1.0", "1.0", "1.0", "89.0")
slide_2_fingers_up92 = Gesture("92", "slide_2_fingers_up", "1.0", "1.0", "1.0", "88.0")
stop_sign92 = Gesture("92", "stop_sign", "1.0", "1.0", "1.0", "90.0")
swipe_down92 = Gesture("92", "swipe_down", "1.0", "1.0", "1.0", "86.0")
swipe_left92 = Gesture("92", "swipe_left", "1.0", "1.0", "1.0", "88.0")
thumb_up92 = Gesture("92", "thumb_up", "0.99", "1.0", "0.99", "86.0")
zoom_in_with_2_fingers92 = Gesture("92", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "91.0")
zoom_in_with_full_hand92 = Gesture("92", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "87.0")
zoom_out_with_2_fingers92 = Gesture("92", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "89.0")
gestures_92 = [pull_hand_in92, slide_2_fingers_right92, slide_2_fingers_up92, stop_sign92, swipe_down92, swipe_left92, thumb_up92, zoom_in_with_2_fingers92, zoom_in_with_full_hand92, zoom_out_with_2_fingers92]

pull_hand_in93 = Gesture("93", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
slide_2_fingers_right93 = Gesture("93", "slide_2_fingers_right", "0.99", "1.0", "1.0", "152.0")
slide_2_fingers_up93 = Gesture("93", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign93 = Gesture("93", "stop_sign", "1.0", "1.0", "1.0", "155.0")
swipe_down93 = Gesture("93", "swipe_down", "1.0", "1.0", "1.0", "150.0")
swipe_left93 = Gesture("93", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up93 = Gesture("93", "thumb_up", "0.99", "0.99", "0.99", "147.0")
zoom_in_with_2_fingers93 = Gesture("93", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand93 = Gesture("93", "zoom_in_with_full_hand", "0.99", "0.98", "0.99", "145.0")
zoom_out_with_2_fingers93 = Gesture("93", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_93 = [pull_hand_in93, slide_2_fingers_right93, slide_2_fingers_up93, stop_sign93, swipe_down93, swipe_left93, thumb_up93, zoom_in_with_2_fingers93, zoom_in_with_full_hand93, zoom_out_with_2_fingers93]

pull_hand_in94 = Gesture("94", "pull_hand_in", "0.99", "1.0", "1.0", "154.0")
slide_2_fingers_right94 = Gesture("94", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up94 = Gesture("94", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign94 = Gesture("94", "stop_sign", "1.0", "0.99", "1.0", "155.0")
swipe_down94 = Gesture("94", "swipe_down", "0.99", "1.0", "1.0", "150.0")
swipe_left94 = Gesture("94", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up94 = Gesture("94", "thumb_up", "1.0", "0.98", "0.99", "147.0")
zoom_in_with_2_fingers94 = Gesture("94", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand94 = Gesture("94", "zoom_in_with_full_hand", "0.98", "0.99", "0.99", "145.0")
zoom_out_with_2_fingers94 = Gesture("94", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_94 = [pull_hand_in94, slide_2_fingers_right94, slide_2_fingers_up94, stop_sign94, swipe_down94, swipe_left94, thumb_up94, zoom_in_with_2_fingers94, zoom_in_with_full_hand94, zoom_out_with_2_fingers94]

pull_hand_in95 = Gesture("95", "pull_hand_in", "0.73", "0.7", "0.72", "154.0")
slide_2_fingers_right95 = Gesture("95", "slide_2_fingers_right", "0.61", "0.91", "0.73", "152.0")
slide_2_fingers_up95 = Gesture("95", "slide_2_fingers_up", "0.69", "0.81", "0.74", "159.0")
stop_sign95 = Gesture("95", "stop_sign", "0.64", "0.8", "0.71", "155.0")
swipe_down95 = Gesture("95", "swipe_down", "0.75", "0.57", "0.65", "150.0")
swipe_left95 = Gesture("95", "swipe_left", "0.78", "0.72", "0.75", "150.0")
thumb_up95 = Gesture("95", "thumb_up", "0.88", "0.65", "0.75", "147.0")
zoom_in_with_2_fingers95 = Gesture("95", "zoom_in_with_2_fingers", "0.78", "0.85", "0.81", "152.0")
zoom_in_with_full_hand95 = Gesture("95", "zoom_in_with_full_hand", "0.83", "0.63", "0.72", "145.0")
zoom_out_with_2_fingers95 = Gesture("95", "zoom_out_with_2_fingers", "0.81", "0.66", "0.73", "145.0")
gestures_95 = [pull_hand_in95, slide_2_fingers_right95, slide_2_fingers_up95, stop_sign95, swipe_down95, swipe_left95, thumb_up95, zoom_in_with_2_fingers95, zoom_in_with_full_hand95, zoom_out_with_2_fingers95]

pull_hand_in96 = Gesture("96", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
slide_2_fingers_right96 = Gesture("96", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up96 = Gesture("96", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign96 = Gesture("96", "stop_sign", "1.0", "1.0", "1.0", "155.0")
swipe_down96 = Gesture("96", "swipe_down", "1.0", "0.99", "0.99", "150.0")
swipe_left96 = Gesture("96", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up96 = Gesture("96", "thumb_up", "0.99", "0.99", "0.99", "147.0")
zoom_in_with_2_fingers96 = Gesture("96", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand96 = Gesture("96", "zoom_in_with_full_hand", "0.98", "0.99", "0.99", "145.0")
zoom_out_with_2_fingers96 = Gesture("96", "zoom_out_with_2_fingers", "0.99", "1.0", "1.0", "145.0")
gestures_96 = [pull_hand_in96, slide_2_fingers_right96, slide_2_fingers_up96, stop_sign96, swipe_down96, swipe_left96, thumb_up96, zoom_in_with_2_fingers96, zoom_in_with_full_hand96, zoom_out_with_2_fingers96]


pull_hand_in97 = Gesture("97", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
slide_2_fingers_right97 = Gesture("97", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up97 = Gesture("97", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign97 = Gesture("97", "stop_sign", "1.0", "1.0", "1.0", "155.0")
swipe_down97 = Gesture("97", "swipe_down", "1.0", "1.0", "1.0", "150.0")
swipe_left97 = Gesture("97", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up97 = Gesture("97", "thumb_up", "0.96", "1.0", "0.98", "147.0")
zoom_in_with_2_fingers97 = Gesture("97", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand97 = Gesture("97", "zoom_in_with_full_hand", "1.0", "0.96", "0.98", "145.0")
zoom_out_with_2_fingers97 = Gesture("97", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_97 = [pull_hand_in97, slide_2_fingers_right97, slide_2_fingers_up97, stop_sign97, swipe_down97, swipe_left97, thumb_up97, zoom_in_with_2_fingers97, zoom_in_with_full_hand97, zoom_out_with_2_fingers97]

pull_hand_in98 = Gesture("98", "pull_hand_in", "0.99", "1.0", "1.0", "154.0")
slide_2_fingers_right98 = Gesture("98", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up98 = Gesture("98", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign98 = Gesture("98", "stop_sign", "1.0", "0.99", "1.0", "155.0")
swipe_down98 = Gesture("98", "swipe_down", "1.0", "1.0", "1.0", "150.0")
swipe_left98 = Gesture("98", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up98 = Gesture("98", "thumb_up", "0.97", "1.0", "0.99", "147.0")
zoom_in_with_2_fingers98 = Gesture("98", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand98 = Gesture("98", "zoom_in_with_full_hand", "1.0", "0.97", "0.99", "145.0")
zoom_out_with_2_fingers98 = Gesture("98", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_98 = [pull_hand_in98, slide_2_fingers_right98, slide_2_fingers_up98, stop_sign98, swipe_down98, swipe_left98, thumb_up98, zoom_in_with_2_fingers98, zoom_in_with_full_hand98, zoom_out_with_2_fingers98]

pull_hand_in99 = Gesture("99", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
slide_2_fingers_right99 = Gesture("99", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up99 = Gesture("99", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign99 = Gesture("99", "stop_sign", "1.0", "1.0", "1.0", "155.0")
swipe_down99 = Gesture("99", "swipe_down", "1.0", "1.0", "1.0", "150.0")
swipe_left99 = Gesture("99", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up99 = Gesture("99", "thumb_up", "1.0", "1.0", "1.0", "147.0")
zoom_in_with_2_fingers99 = Gesture("99", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand99 = Gesture("99", "zoom_in_with_full_hand", "1.0", "1.0", "0.99", "145.0")
zoom_out_with_2_fingers99 = Gesture("99", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_99 = [pull_hand_in99, slide_2_fingers_right99, slide_2_fingers_up99, stop_sign99, swipe_down99, swipe_left99, thumb_up99, zoom_in_with_2_fingers99, zoom_in_with_full_hand99, zoom_out_with_2_fingers99]

pull_hand_in100 = Gesture("100", "pull_hand_in", "0.62", "0.65", "0.63", "154.0")
slide_2_fingers_right100 = Gesture("100", "slide_2_fingers_right", "0.62", "0.86", "0.72", "152.0")
slide_2_fingers_up100 = Gesture("100", "slide_2_fingers_up", "0.5", "0.53", "0.52", "159.0")
stop_sign100 = Gesture("100", "stop_sign", "0.67", "0.65", "0.66", "155.0")
swipe_down100 = Gesture("100", "swipe_down", "0.7", "0.5", "0.58", "150.0")
swipe_left100 = Gesture("100", "swipe_left", "0.67", "0.41", "0.51", "150.0")
thumb_up100 = Gesture("100", "thumb_up", "0.73", "0.46", "0.56", "147.0")
zoom_in_with_2_fingers100 = Gesture("100", "zoom_in_with_2_fingers", "0.6", "0.9", "0.72", "152.0")
zoom_in_with_full_hand100 = Gesture("100", "zoom_in_with_full_hand", "0.59", "0.74", "0.66", "145.0")
zoom_out_with_2_fingers100 = Gesture("100", "zoom_out_with_2_fingers", "0.56", "0.45", "0.5", "145.0")
gestures_100 = [pull_hand_in100, slide_2_fingers_right100, slide_2_fingers_up100, stop_sign100, swipe_down100, swipe_left100, thumb_up100, zoom_in_with_2_fingers100, zoom_in_with_full_hand100, zoom_out_with_2_fingers100]

pull_hand_in101 = Gesture("101", "pull_hand_in", "0.87", "0.77", "0.82", "154.0")
slide_2_fingers_right101 = Gesture("101", "slide_2_fingers_right","0.75", "0.88", "0.81", "152.0")
slide_2_fingers_up101 = Gesture("101", "slide_2_fingers_up", "0.84", "0.75", "0.79", "159.0")
stop_sign101 = Gesture("101", "stop_sign", "0.74", "0.83", "0.78", "155.0")
swipe_down101 = Gesture("101", "swipe_down", "0.83", "0.82", "0.82", "150.0")
swipe_left101 = Gesture("101", "swipe_left", "0.82", "0.84", "0.83", "150.0")
thumb_up101 = Gesture("101", "thumb_up", "0.93", "0.69", "0.79", "147.0")
zoom_in_with_2_fingers101 = Gesture("101", "zoom_in_with_2_fingers", "0.84", "0.91", "0.87", "152.0")
zoom_in_with_full_hand101 = Gesture("101", "zoom_in_with_full_hand", "0.88", "0.85", "0.86", "145.0")
zoom_out_with_2_fingers101 = Gesture("101", "zoom_out_with_2_fingers", "0.79", "0.86", "0.82", "145.0")
gestures_101 = [pull_hand_in101, slide_2_fingers_right101, slide_2_fingers_up101, stop_sign101, swipe_down101, swipe_left101, thumb_up101, zoom_in_with_2_fingers101, zoom_in_with_full_hand101, zoom_out_with_2_fingers101]

pull_hand_in102 = Gesture("102", "pull_hand_in", "0.91", "0.82", "0.86", "154.0")
slide_2_fingers_right102 = Gesture("102", "slide_2_fingers_right", "0.81", "0.96", "0.88", "152.0")
slide_2_fingers_up102 = Gesture("102", "slide_2_fingers_up", "0.87", "0.84", "0.86", "159.0")
stop_sign102 = Gesture("102", "stop_sign", "0.76", "0.87", "0.81", "155.0")
swipe_down102 = Gesture("102", "swipe_down", "0.86", "0.87", "0.86", "150.0")
swipe_left102 = Gesture("102", "swipe_left", "0.88", "0.89", "0.88", "150.0")
thumb_up102 = Gesture("102", "thumb_up", "0.91", "0.76", "0.83", "147.0")
zoom_in_with_2_fingers102 = Gesture("102", "zoom_in_with_2_fingers", "0.83", "0.94", "0.88", "152.0")
zoom_in_with_full_hand102 = Gesture("102", "zoom_in_with_full_hand", "0.85", "0.81", "0.83", "145.0")
zoom_out_with_2_fingers102 = Gesture("102", "zoom_out_with_2_fingers", "0.97", "0.81", "0.88", "145.0")
gestures_102 = [pull_hand_in102, slide_2_fingers_right102, slide_2_fingers_up102, stop_sign102, swipe_down102, swipe_left102, thumb_up102, zoom_in_with_2_fingers102, zoom_in_with_full_hand102, zoom_out_with_2_fingers102]

pull_hand_in103 = Gesture("103", "pull_hand_in", "1.0", "0.99", "1.0", "154.0")
slide_2_fingers_right103 = Gesture("103", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up103 = Gesture("103", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign103 = Gesture("103", "stop_sign", "1.0", "0.99", "0.99", "155.0")
swipe_down103 = Gesture("103", "swipe_down", "1.0", "0.99", "1.0", "150.0")
swipe_left103 = Gesture("103", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up103 = Gesture("103", "thumb_up", "0.99", "1.0", "1.0", "147.0")
zoom_in_with_2_fingers103 = Gesture("103", "zoom_in_with_2_fingers", "0.99", "1.0", "0.99", "152.0")
zoom_in_with_full_hand103 = Gesture("103", "zoom_in_with_full_hand", "1.0", "1.0", "1.0", "145.0")
zoom_out_with_2_fingers103 = Gesture("103", "zoom_out_with_2_fingers", "0.99", "1.0", "1.0", "145.0")
gestures_103 = [pull_hand_in103, slide_2_fingers_right103, slide_2_fingers_up103, stop_sign103, swipe_down103, swipe_left103, thumb_up103, zoom_in_with_2_fingers103, zoom_in_with_full_hand103, zoom_out_with_2_fingers103]

pull_hand_in104 = Gesture("104", "pull_hand_in", "1.0", "1.0", "1.0", "154.0")
slide_2_fingers_right104 = Gesture("104", "slide_2_fingers_right", "1.0", "1.0", "1.0", "152.0")
slide_2_fingers_up104 = Gesture("104", "slide_2_fingers_up", "1.0", "1.0", "1.0", "159.0")
stop_sign104 = Gesture("104", "stop_sign", "1.0", "1.0", "1.0", "155.0")
swipe_down104 = Gesture("104", "swipe_down", "1.0", "0.99", "1.0", "150.0")
swipe_left104 = Gesture("104", "swipe_left", "1.0", "1.0", "1.0", "150.0")
thumb_up104 = Gesture("104", "thumb_up", "1.0", "0.97", "0.99", "147.0")
zoom_in_with_2_fingers104 = Gesture("104", "zoom_in_with_2_fingers", "1.0", "1.0", "1.0", "152.0")
zoom_in_with_full_hand104 = Gesture("104", "zoom_in_with_full_hand", "0.97", "1.0", "0.98", "145.0")
zoom_out_with_2_fingers104 = Gesture("104", "zoom_out_with_2_fingers", "1.0", "1.0", "1.0", "145.0")
gestures_104 = [pull_hand_in104, slide_2_fingers_right104, slide_2_fingers_up104, stop_sign104, swipe_down104, swipe_left104, thumb_up104, zoom_in_with_2_fingers104, zoom_in_with_full_hand104, zoom_out_with_2_fingers104]

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
        
