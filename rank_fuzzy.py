import fuzzylite as fl
import GUI as gui_tk
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import statistics
import csv
import generating_input as input_exp

# TAKAGI-SUGENO-KANG


class TKS:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="GestureRecognition_Rank",
        description="")

# Defining the Input Variables (Fuzzification)
    def creating_input(self):
        x = np.arange(0,1,0.1)
        self.engine.input_variables = [
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
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if F1_score is LOW then Result is BAD", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
                ]
            )
        ]



# MANDANI

"""class Mandani:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="GestureRecognition_Rank",
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
]"""

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



#tks.engine.output_variable("Result").defuzzify()



# print("Activation degree: ", tks.engine.output_variable("Power").fuzzy.activation_degree(tks.engine.output_variable("Power").term("HIGH")))
#result = tks.engine.output_variable("Power").fuzzy_value()
#print("Result: ", result)

print("Rules: ", tks.engine.rule_block("Rules").rules[0].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[1].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[2].weight.__str__())

#print("Value output low:", tks.engine.output_variable("Result").terms.

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

# Initialize dictionary
list_perfect=[]
list_good=[]
list_mediocre=[]
list_low=[]
dic_result={"PERFECT": list_perfect, "GOOD": list_good, "MEDIOCRE": list_mediocre, "LOW": list_low}



print("PROCESS FINISHED")
