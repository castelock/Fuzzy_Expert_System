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
                name="",
                description="",
                enabled=True,
                conjunction=None,
                disjunction=None,
                implication=None,
                activation=fl.General(),
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
tks.engine.input_variable("Precision").value = 0.5
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
print("Output rule blocks:", tks.engine.rule_blocks.count()
# print("Activation degree: ", tks.engine.output_variable("Power").fuzzy.activation_degree(tks.engine.output_variable("Power").term("HIGH")))


"""class FuzzySet():
    
    def __init__(self):

    def create_triangular(cls, name, domain_min, domain_max, res, a, b, c):
        t1fs = cls(name, domain_min, domain_max, res)

        a = t1fs._adjust_domain_val(a)
        b = t1fs._adjust_domain_val(b)
        c = t1fs._adjust_domain_val(c)

        t1fs._dom = np.round(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0), t1fs._precision)

    def _adjust_domain_val(self, x_val):
        return self._domain[np.abs(self._domain-x_val).argmin()]

    def create_triangular(cls, name, domain_min, domain_max, res, a, b, c):
        t1fs = cls(name, domain_min, domain_max, res)

        a = t1fs._adjust_domain_val(a)
        b = t1fs._adjust_domain_val(b)
        c = t1fs._adjust_domain_val(c)

        t1fs._dom = np.round(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0), t1fs._precision)

    def union(self, f_set):

		result = FuzzySet(f'({self._name}) union ({f_set._name})', self._domain_min, self._domain_max, self._res)
		result._dom = np.maximum(self._dom, f_set._dom)

		return result

    def cog_defuzzify(self):

        num = np.sum(np.multiply(self._dom, self._domain))
        den = np.sum(self._dom)

        return num/den

class FuzzyVariable():
    def __init__(self, name):
        # Attribute name
        self.name = name

class FuzzyInputVariable(FuzzyVariable):
    def __init__(self):
        print('Init method')

    def fuzzify(self, val):

        # get dom for each set and store it - 
        # it will be required for each rule
        for set_name, f_set in self._sets.items():
            f_set.last_dom_value = f_set[val]

class FuzzyOutputVariable(FuzzyVariable):

    def __init__(self, name, min_val, max_val, res):
        super().__init__(name, min_val, max_val, res)
        self._output_distribution = FuzzySet(name, min_val, max_val, res)

    def add_rule_contribution(self, rule_consequence):
        self._output_distribution = self._output_distribution.union(rule_consequence)

    def get_crisp_output(self):
        return self._output_distribution.cog_defuzzify()

class FuzzyClause():
    def __init__(self, fuzzy_variable, fuzzy_set):
        # Attribute Fuzzy Variable
        self.fuzzy_variable = fuzzy_variable
        # Attribute Fuzzy Set
        self.fuzzy_set = fuzzy_set
    
    def evaluate_antecedent(self):
	return self._set.last_dom_value

    def evaluate_consequent(self, activation):
        self._variable.add_rule_contribution(self._set.min_scalar(activation))


class FuzzyRule():
    def __init__(self, FuzzyClause antecedent_clauses, FuzzyClause consequent_clauses):
        # Antecedents and consequents lists
        self.antecedent_clauses = antecedent_clauses
        self.consequent_clauses = consequent_clauses

    def evaluate(self):
        # rule activation initialize to 1 as min operator will be performed
        rule_activation = 1
        # execute all antecedent clauses, keeping the minimum of the returned doms to determine the activation
        for ante_clause in self._antecedent:
            rule_activation = min(ante_clause.evaluate_antecedent(), rule_activation)

        # execute consequent clauses, each output variable will update its output_distribution set
        for consequent_clause in self._consequent:
            consequent_clause.evaluate_consequent(rule_activation)

class FuzzySystem():
    def __init__(self):

    def add_rule(self, antecedent_clauses, consequent_clauses):
		'''
		adds a new rule to the system.
		TODO: add checks
		Arguments:
		-----------
		antecedent_clauses -- dict, having the form {variable_name:set_name, ...}
		consequent_clauses -- dict, having the form {variable_name:set_name, ...}
		'''
		# create a new rule
		# new_rule = FuzzyRule(antecedent_clauses, consequent_clauses)
		new_rule = FuzzyRule()

		for var_name, set_name in antecedent_clauses.items():
			# get variable by name
			var = self.get_input_variable(var_name)
			# get set by name
			f_set = var.get_set(set_name)
			# add clause
			new_rule.add_antecedent_clause(var, f_set)

		for var_name, set_name in consequent_clauses.items():
			var = self.get_output_variable(var_name)
			f_set = var.get_set(set_name)
			new_rule.add_consequent_clause(var, f_set)

		# add the new rule
		self._rules.append(new_rule)

    def launch_inference(self):
        # clear the fuzzy consequences as we are evaluating a new set of inputs.
        # can be optimized by comparing if the inputs have changes from the previous
        # iteration.
        self._clear_output_distributions()

        # Fuzzify the inputs. The degree of membership will be stored in
        # each set
        for input_name, input_value in input_values.items():
            self._input_variables[input_name].fuzzify(input_value)

        # evaluate rules
        for rule in self._rules:
            rule.evaluate()

        # finally, defuzzify all output distributions to get the crisp outputs
        output = {}
        for output_var_name, output_var in self._output_variables.items():
            output[output_var_name] = output_var.get_crisp_output()

        return output"""
