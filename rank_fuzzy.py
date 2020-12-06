import fuzzylite as fl
import GUI as gui_tk
import numpy as np

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
                fl.Gaussian("HIGH",x,4,0.8),
                fl.Gaussian("MEDIUM",x,4,0.5),
                fl.Gaussian("LOW", x,4,0.25) ]
                
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
                fl.Constant("LOW", 0.250),
                fl.Constant("MEDIUM", 0.500),
                fl.Constant("HIGH", 0.750)]
            )
        ]

# Creation of Fuzzy Rule Base
    def creating_fuzzy_rules(self):
        self.engine.rule_blocks = [
            fl.RuleBlock(
                name="Rules",
                description="",
                enabled=True,
                conjunction=None,
                disjunction=None,
                implication=None,
                activation=fl.Highest(),
                rules=[
                    fl.Rule.create("if Precision is HIGH then Result is HIGH", self.engine),
                    fl.Rule.create("if Precision is MEDIUM then Result is MEDIUM", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is LOW", self.engine)
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

# Creating the TKS Fuzzy System
tks = TKS()
tks.creating_input()
tks.creating_output()
tks.creating_fuzzy_rules()
tks.engine.input_variable("Precision").value = 0.1
tks.engine.process()
tks.engine.output_variable("Result").defuzzify()

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

for rule in list_rules:
    print("Trigerred: ", rule.triggered.__str__())

threshold = 0.8
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("HIGH")).__str__())
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("MEDIUM")).__str__())
print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("LOW")).__str__())

if tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("HIGH")) >= threshold:
    print("Result is over threshold")
else:
    print("Result is under threshold")