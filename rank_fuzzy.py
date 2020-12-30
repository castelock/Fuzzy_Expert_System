import fuzzylite as fl
import GUI as gui_tk
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import statistics
import csv
import generating_input as input_exp
import sklearn.metrics
from mlxtend.plotting import plot_confusion_matrix

# METHODS
def evaluate_predictions(list_perfect_pred, list_good_pred, list_mediocre_pred, list_low_pred):
    list_perfect_true = {"24", "25", "26", "27", "28", "29", "44", "45", "47", "48", "52", "53", "54", "55", "60", "61", "62", "63", "69", "70", "75", "77", "78", "84", "85", "91", "92", "93", "94", "96", "98", "99", "103", "104"}
    list_good_true = {"3", "4", "17", "19", "21", "22", "23", "46", "67", "68", "76", "82", "83", "89", "90", "97", "101", "102"}
    list_mediocre_true = {"1", "2", "5", "6", "12", "13", "18", "20", "49", "51", "57", "58", "59", "64", "66", "72", "73", "74", "79", "80", "81", "86", "87", "88", "95", "100"}
    list_low_true = {"7", "8", "9", "10", "11", "14", "15", "16", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "50", "56", "65", "71"}

    # Right answers for each case
    pred_pp = 0
    pred_pg = 0
    pred_pm = 0
    pred_pl = 0

    pred_gg = 0
    pred_gp = 0
    pred_gm = 0
    pred_gl = 0

    pred_mm = 0
    pred_mp = 0
    pred_mg = 0
    pred_ml = 0

    pred_ll = 0
    pred_lp = 0
    pred_lg = 0
    pred_lm = 0

    # Accuracy rate 
    acc_rate_perfect = 0
    acc_rate_good = 0
    acc_rate_mediocre = 0
    acc_rate_low = 0


    # Counting the right answers for perfect cases
    for element in list_perfect_pred:
        if element in list_perfect_true:
            pred_pp+=1
        elif element in list_good_true:
            pred_pg+=1
        elif element in list_mediocre_true:
            pred_pm+=1
        elif element in list_low_true:
            pred_pl+=1

    # Counting the right answers for good cases
    for element in list_good_pred:
        if element in list_good_true:
            pred_gg+=1
        elif element in list_perfect_true:
            pred_gp+=1
        elif element in list_mediocre_true:
            pred_gm+=1
        elif element in list_low_true:
            pred_gl+=1
    
    # Counting the right answers for mediocrre cases
    for element in list_mediocre_pred:
        if element in list_mediocre_true:
            pred_mm+=1
        elif element in list_perfect_true:
            pred_mp+=1
        elif element in list_good_true:
            pred_mg+=1
        elif element in list_low_true:
            pred_ml+=1

    # Counting the right answers for low cases
    for element in list_low_pred:
        if element in list_low_true:
            pred_ll+=1
        elif element in list_perfect_true:
            pred_lp+=1
        elif element in list_good_true:
            pred_lg+=1
        elif element in list_mediocre_true:
            pred_lm+=1

    # Calculating the accurate rate for each case
    # acc = (TP + TN) / (TP + TN + FP + FN) 
    """acc_rate_perfect = right_perfect / len(list_perfect_true)
    acc_rate_good = right_good / len(list_good_true)
    acc_rate_mediocre = right_mediocre / len(list_mediocre_true)
    acc_rate_low = right_low / len(list_low_true)

    acc_rate = sklearn.metrics.accuracy_score(list_perfect_true, list_perfect_pred)"""

    tp_perfect = pred_pp
    tn_perfect = pred_gg+pred_gm+pred_gl+pred_mg+pred_mm+pred_ml+pred_lg+pred_lm+pred_ll
    fp_perfect = pred_pg+pred_pm+pred_pl
    fn_perfect = pred_gp+pred_mp+pred_lp

    try:
        acc_rate_perfect = (tp_perfect + tn_perfect) / (tp_perfect + tn_perfect + fp_perfect + fn_perfect)
    except(ZeroDivisionError):
        acc_rate_perfect = 0
    try:
        precision_perfect = tp_perfect/(tp_perfect+fp_perfect)
    except(ZeroDivisionError):
        precision_perfect = 0

    tp_good = pred_gg
    tn_good = pred_pp+pred_pm+pred_pl+pred_mp+pred_mm+pred_ml+pred_lp+pred_lm+pred_ll
    fp_good = pred_gp+pred_gm+pred_gl
    fn_good = pred_pg+pred_mg+pred_lg

    try:
        acc_rate_good = (tp_good + tn_good) / (tp_good + tn_good + fp_good + fn_good)
    except(ZeroDivisionError):
        acc_rate_good = 0
    
    try:
        precision_good = tp_good/(tp_good+fp_good)
    except(ZeroDivisionError):
        precision_good = 0

    tp_mediocre = pred_mm
    tn_mediocre = pred_pp+pred_pg+pred_pl+pred_gp+pred_gg+pred_gl+pred_lp+pred_lg+pred_ll
    fp_mediocre = pred_mp+pred_mg+pred_ml
    fn_mediocre = pred_pm+pred_gm+pred_gl

    try:
        acc_rate_mediocre = (tp_mediocre + tn_mediocre) / (tp_mediocre + tn_mediocre + fp_mediocre + fn_mediocre)
    except(ZeroDivisionError):
        acc_rate_mediocre = 0
    
    try:
        precision_mediocre = tp_mediocre/(tp_mediocre+fp_mediocre)
    except(ZeroDivisionError):
        precision_mediocre = 0
    

    tp_low = pred_ll
    tn_low = pred_pp+pred_pg+pred_pm+pred_gp+pred_gg+pred_gm+pred_mp+pred_mg+pred_mm
    fp_low = pred_lp+pred_lg+pred_lm
    fn_low = pred_pl+pred_gl+pred_ml

    try:
        acc_rate_low = (tp_low + tn_low) / (tp_low + tn_low + fp_low + fn_low)
    except(ZeroDivisionError):
        acc_rate_low = 0

    try:
        precision_low = tp_low/(tp_low+fp_low)
    except(ZeroDivisionError):
        precision_low = 0


    confusion_matrix = np.array([[pred_pp,pred_pg,pred_pm,pred_pl], [pred_gp,pred_gg,pred_gm,pred_gl], [pred_mp,pred_mg,pred_mm,pred_ml], [pred_lp,pred_lg,pred_lm,pred_ll]])

    class_names = ["Perfect", "Good", "Mediocre", "Low"]

    fig, ax = plot_confusion_matrix(conf_mat=confusion_matrix,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=False,
                                class_names=class_names)
    plt.show()

    return acc_rate_perfect, acc_rate_good, acc_rate_mediocre, acc_rate_low


# TAKAGI-SUGENO-KANG

class TKS:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="Takagi-Sugeno-Kang_Fuzzy_System",
        description="")

# Defining the Input Variables (Fuzzification)
    def creating_input(self):
        x = np.arange(0,1,0.1)
        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.6,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]                         
            ),
        fl.InputVariable(
            name="Recall",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.6,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]                          
            ),
        fl.InputVariable(
            name="F1_score",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.6,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]
                            
            )
        ]"""

        self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[ 
                fl.Triangle("HIGH",0.75,1.0,1.0),
                fl.Triangle("MEDIUM",0,0.5,0.75),
                fl.Triangle("LOW",0,0,0.5)
                ]                 
            ),
        fl.InputVariable(
            name="Recall",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[ 
                fl.Triangle("HIGH",0.75,1.0,1.0),
                fl.Triangle("MEDIUM",0,0.5,0.75),
                fl.Triangle("LOW",0,0,0.5)
                ]                            
            ),
        fl.InputVariable(
            name="F1_score",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[ 
                fl.Triangle("HIGH",0.75,1.0,1.0),
                fl.Triangle("MEDIUM",0,0.5,0.75),
                fl.Triangle("LOW",0,0,0.5)
                ]
                            
            )
        ]
        
        
        

# Defining the Output Variables (Defuzzification)
    def creating_output(self):
        self.engine.output_variables = [
        fl.OutputVariable(
            name="Result",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            aggregation=None,
            defuzzifier=fl.WeightedAverage("TakagiSugeno"),
            lock_previous=False,
            terms=[
                fl.Constant("PERFECT", 1),
                fl.Constant("GOOD", 0.9),
                fl.Constant("MEDIOCRE", 0.6),
                fl.Constant("BAD", 0.35),
                ]
            )
        ]

# Creation of Fuzzy Rule Base
    def creating_fuzzy_rules(self):
        self.engine.rule_blocks = [
            fl.RuleBlock(
                name="Rules",
                description="",
                enabled=True,
                conjunction=fl.Minimum(),
                disjunction=fl.Maximum(),
                implication=None,
                activation=fl.Highest(),
                rules=[
                    fl.Rule.create("if Precision is HIGH and Recall is HIGH and F1_score is HIGH then Result is PERFECT", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),                    
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if F1_score is LOW then Result is BAD", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
                ]
            )
        ]



# MAMDANI

class Mandani:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="Mamdani_Fuzzy_System",
        description="")

#Defining the Input Variables (Fuzzification)
    def creating_input(self):
        self.engine.input_variables = [
            fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
            fl.Triangle("DARK", 0.000, 0.250, 0.500), #Triangular Membership Function defining "Dark"
            fl.Triangle("MEDIUM", 0.250, 0.500, 0.750), #Triangular Membership Function defining "Medium"
            fl.Triangle("BRIGHT", 0.500, 0.750, 1.000) #Triangular Membership Function defining "Bright"
            ]
            )
        ]
#Defining the Output Variables (Defuzzification)
engine.output_variables = [
      fl.OutputVariable(
      name="Power",
      description="",
      enabled=True,
      minimum=0.000,
      maximum=1.000,
      lock_range=False,
      aggregation=fl.Maximum(),
      defuzzifier=fl.Centroid(200),
      lock_previous=False,
      terms=[
      fl.Triangle("LOW", 0.000, 0.250, 0.500), #Triangular Membership Function defining "LOW Light"
      fl.Triangle("MEDIUM", 0.250, 0.500, 0.750), #Triangular Membership Function defining "MEDIUM light"
      fl.Triangle("HIGH", 0.500, 0.750, 1.000) #Triangular Membership Function defining "HIGH Light"
      ]
      )
]
#Creation of Fuzzy Rule Base
engine.rule_blocks = [
      fl.RuleBlock(
      name="",
      description="",
      enabled=True,
      conjunction=None,
      disjunction=None,
      implication=fl.Minimum(),
      activation=fl.General(),
      rules=[
      fl.Rule.create("if Ambient is DARK then Power is HIGH", engine),
      fl.Rule.create("if Ambient is MEDIUM then Power is MEDIUM", engine),
      fl.Rule.create("if Ambient is BRIGHT then Power is LOW", engine)
      ]
      )
]

# TSUKAMOTO
#Defining the Input Variables (Fuzzification)
engine.input_variables = [
      fl.InputVariable(
      name="Ambient",
      description="",
      enabled=True,
      minimum=0.000,
      maximum=1.000,
      lock_range=False,
      terms=[
      fl.Bell("Dark", -10.000, 5.000, 3.000), #Generalized Bell Membership Function defining "Dark"
      fl.Bell("medium", 0.000, 5.000, 3.000), #Generalized Bell  Membership Function defining "Medium"
      fl.Bell("Bright", 10.000, 5.000, 3.000) #Generalized Bell  Membership Function defining "Bright"
      ]
      )
]
#Defining the Output Variables (Defuzzification)
engine.output_variables = [
      fl.OutputVariable(
      name="Power",
      description="",
      enabled=True,
      minimum=0.000,
      maximum=1.000,
      lock_range=False,
      aggregation=fl.Maximum(),
      defuzzifier=fl.Centroid(200),
      lock_previous=False,
      terms=[
      fl.Sigmoid("LOW", 0.500, -30.000), #Triangular Membership Function defining "LOW Light"
      fl.Sigmoid("MEDIUM", 0.130, 30.000), #Triangular Membership Function defining "MEDIUM light"
      fl.Sigmoid("HIGH", 0.830, 30.000), #Triangular Membership Function defining "HIGH Light"
      fl.Triangle("HIGH", 0.500, 0.750, 1.000)
      ]
      )
]

#Creation of Fuzzy Rule Base
engine.rule_blocks = [
      fl.RuleBlock(
      name="",
      description="",
      enabled=True,
      conjunction=None,
      disjunction=None,
      implication=None,
      activation=fl.General(),
      rules=[
      fl.Rule.create("if Ambient is DARK then Power is HIGH", engine),
      fl.Rule.create("if Ambient is MEDIUM then Power is MEDIUM", engine),
      fl.Rule.create("if Ambient is BRIGHT then Power is LOW", engine)
      ]
      )
]

# Building the GUI
"""window = gui_tk.Window("Fuzzy Expert System")
window.mainloop()"""

# PLOTS
"""mean = 0

standard_deviation = 1


x_values = np.arange(-5, 5, 0.1)

y_values = scipy.stats.norm(mean, standard_deviation)


plt.plot(x_values, y_values.pdf(x_values))
plt.show()"""

"""x = np.arange(0,1,0.1)
std_dev= statistics.stdev(x)
y = scipy.stats.norm(0.5, 0.5)
plt.plot(x,y.pdf(x))
plt.show()"""

# Input folder path
input_path = "input/"
# File to store the experiments characteristics
filename_exp = "experiments.csv"
filenameExp_path = input_path + filename_exp
# File to store the experiments metrics
filename_metrics = "experiments_metrics.csv"
filenameMetrics_path = input_path + filename_metrics
threshold = 0.9

# READING THE EXPERIMENTS
# Reading the experiments features
list_exp = {}
with open(filenameExp_path, newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    # Skipping the header line
    next(reader)   
    for row in reader:
        experiment = input_exp.Experiment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        # list_exp.append(experiment)
        list_exp[experiment.getId()]=experiment

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
            gesture = input_exp.Gesture(row[0], row[1], row[2], row[3], row[4], row[5])
            list_gestures.append(gesture)
            prev_id = row[0]
        else:
            if list_gestures is not None:
                # Creating a new metric
                metric = input_exp.Experiment_Metrics(prev_id, list_gestures)
                list_metrics.append(metric)
                # Adding the current gesture
                list_gestures = []
                gesture = input_exp.Gesture(row[0], row[1], row[2], row[3], row[4], row[5])
                list_gestures.append(gesture)
                prev_id = row[0]
            else:
                print("ERROR: The gestures list is empty")
    # Including the last metric
    metric = input_exp.Experiment_Metrics(prev_id, list_gestures)
    list_metrics.append(metric)

mean_precision, mean_recall, mean_f1score = list_metrics[0].calculateMean()  

print("Mean: ",list_metrics[0].getId()+" "+ mean_precision.__str__() +" "+mean_recall.__str__()+" "+mean_f1score.__str__())

# Creating the TKS Fuzzy System
tks = TKS()
tks.creating_input()
tks.creating_output()
tks.creating_fuzzy_rules()
list_perfect = []
list_good = []
list_mediocre = []
list_low = []
for metric in list_metrics:
    mean_precision, mean_recall, mean_f1score = metric.calculateMean()
    tks.engine.input_variable("Precision").value = mean_precision
    tks.engine.input_variable("Recall").value = mean_recall
    tks.engine.input_variable("F1_score").value = mean_f1score
    # TO DO
    print("Experiment metric info: ", metric.getId() +" "+ mean_precision.__str__()+" "+mean_recall.__str__()+" "+mean_f1score.__str__())
    tks.engine.process()
    if tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("PERFECT")) >= threshold:
        list_perfect.append(metric.getId())
    elif tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("GOOD")) >= threshold:
        list_good.append(metric.getId())
    elif tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("MEDIOCRE")) >= threshold:
        list_mediocre.append(metric.getId())
    elif tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("BAD")) >= threshold:
        list_low.append(metric.getId())
    else:
        print("ERROR: The output variable is wrong.")


# print("Activation degree: ", tks.engine.output_variable("Power").fuzzy.activation_degree(tks.engine.output_variable("Power").term("HIGH")))
#result = tks.engine.output_variable("Power").fuzzy_value()
#print("Result: ", result)

print("Rules: ", tks.engine.rule_block("Rules").rules[0].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[1].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[2].weight.__str__())

list_terms = tks.engine.output_variable("Result").terms
for term in list_terms:
    print("Terms name: ", term.name.__str__())
    print("Terms value: ", term.membership(0.2).__str__())

list_rules = tks.engine.rule_block("Rules").rules

#tks.engine.rule_block("Rules").

for rule in list_rules:
    print("Trigerred: ", rule.triggered.__str__() + " " + rule.antecedent.text)

threshold = 0.9
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("PERFECT")).__str__())
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("GOOD")).__str__())
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("MEDIOCRE")).__str__())
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("BAD")).__str__())

if tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("PERFECT")) >= threshold:
    print("Result is over threshold")
else:
    print("Result is under threshold")

# GETTING RESULTS

# Create dictionary for the results
dic_result={"PERFECT": list_perfect, "GOOD": list_good, "MEDIOCRE": list_mediocre, "LOW": list_low}

# Evaluate the results
evaluate_predictions(dic_result["PERFECT"], dic_result["GOOD"], dic_result["MEDIOCRE"], dic_result["LOW"])

print("PROCESS FINISHED")
