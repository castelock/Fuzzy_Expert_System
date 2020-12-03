import fuzzylite as fl

class TKS_fuzzylite:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="GestureRecognition_Rank",
        description="")

# Defining the Input Variables (Fuzzification)
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
                fl.Gaussian("HIGH",0.750,4),
                fl.Gaussian("MEDIUM",0.500,4),
                fl.Gaussian("LOW", 0.250,4) ]
                
            )
        ]

# Defining the Output Variables (Defuzzification)
    def creating_output(self):
        self.engine.output_variables = [
        fl.OutputVariable(
            name="Power",
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
    def create_fuzzy_rules(self):
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
                    fl.Rule.create("if Precision is HIGH then Power is HIGH", self.engine),
                    fl.Rule.create("if Precision is MEDIUM then Power is MEDIUM", self.engine),
                    fl.Rule.create("if Precision is LOW then Power is LOW", self.engine)
                ]
            )
        ]

# Creating the TKS Fuzzy System
tks = TKS_fuzzylite()
tks.creating_input()
tks.creating_output()
tks.create_fuzzy_rules()
tks.engine.input_variable("Precision").value = 0.2
tks.engine.process()
print("Output value:", tks.engine.output_variable("Power").value)
print("Output defuzzifier:", tks.engine.output_variable("Power").defuzzifier)
print("Output default value:", tks.engine.output_variable("Power").default_value)
print("Output fuzzy:", tks.engine.output_variable("Power").fuzzy)
tks.engine.output_variable("Power").defuzzify()
print("Output value:", tks.engine.output_variable("Power").value)
print("Output previous value:", tks.engine.output_variable("Power").previous_value)
print("Output fuzzy value:", tks.engine.output_variable("Power").fuzzy_value())
print("Output _value:", tks.engine.output_variable("Power")._value)
# print("Activation degree: ", tks.engine.output_variable("Power").fuzzy.activation_degree(tks.engine.output_variable("Power").term("HIGH")))
#result = tks.engine.output_variable("Power").fuzzy_value()
#print("Result: ", result)

print("Rules: ", tks.engine.rule_block("Rules").rules[0].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[1].weight.__str__())
print("Rules: ", tks.engine.rule_block("Rules").rules[2].weight.__str__())


list_rules = tks.engine.rule_block("Rules").rules

for rule in list_rules:
    print("Trigerred: ", rule.triggered.__str__())

threshold = 0.8
if tks.engine.output_variable("Power").fuzzy.activation_degree(tks.engine.output_variable("Power").term("HIGH")) >= threshold:
    print("Result is over threshold")
else:
    print("Result is under threshold")