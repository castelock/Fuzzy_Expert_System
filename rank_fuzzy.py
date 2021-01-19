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
def evaluate_predictions(list_perfect_pred, list_good_pred, list_mediocre_pred, list_low_pred, results_filename):
    list_perfect_true = {"23","24", "25", "26", "27", "28", "29", "44", "45", "47", "48", "52", "53", "54", "55", "60", "61", "62", "63", "68", "69", "70", "75", "76", "77", "78", "84", "85", "90", "91", "92", "93", "94", "96", "97", "98", "99", "103", "104"}
    list_good_true = {"3", "4", "17", "18", "19", "21", "22", "67", "82", "83", "89", "101", "102"}
    list_mediocre_true = {"1", "2", "5", "6", "11", "12", "13", "20", "46", "51", "59", "66", "74", "88", "95", "100"}
    list_low_true = {"7", "8", "9", "10", "14", "15", "16", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "49", "50", "56", "57", "58", "64", "65", "71", "72", "73", "79", "80", "81", "86", "87"}

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
    acc_rate_bad = 0


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

    # Calculating metric for perfect case
    tp_perfect = pred_pp
    tn_perfect = pred_gg+pred_gm+pred_gl+pred_mg+pred_mm+pred_ml+pred_lg+pred_lm+pred_ll
    fp_perfect = pred_pg+pred_pm+pred_pl
    fn_perfect = pred_gp+pred_mp+pred_lp
    
    try:
        acc_rate_perfect = (tp_perfect + tn_perfect) / (tp_perfect + tn_perfect + fp_perfect + fn_perfect)
    except(ZeroDivisionError):
        acc_rate_perfect = 0
    try:
        precision_perfect = tp_perfect/(tp_perfect+fn_perfect)
    except(ZeroDivisionError):
        precision_perfect = 0
    try:
        recall_perfect = tp_perfect/(tp_perfect+fn_perfect)
    except(ZeroDivisionError):
        recall_perfect = 0
    try:
        f1_score_perfect = 2*precision_perfect*recall_perfect/(precision_perfect+recall_perfect)
    except(ZeroDivisionError):
        f1_score_perfect = 0

    # Calculating metric for good case
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
    try:
        recall_good = tp_good/(tp_good+fn_good)
    except(ZeroDivisionError):
        recall_good = 0
    try:
        f1_score_good = 2*precision_good*recall_good/(precision_good+recall_good)
    except(ZeroDivisionError):
        f1_score_good = 0

    # Calculating metric for mediocre case
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
    try:
        recall_mediocre = tp_mediocre/(tp_mediocre+fn_mediocre)
    except(ZeroDivisionError):
        recall_mediocre = 0
    try:
        f1_score_mediocre = 2*precision_mediocre*recall_mediocre/(precision_mediocre+recall_mediocre)
    except(ZeroDivisionError):
        f1_score_mediocre = 0
    
    # Calculating metric for bad case
    tp_bad = pred_ll
    tn_bad = pred_pp+pred_pg+pred_pm+pred_gp+pred_gg+pred_gm+pred_mp+pred_mg+pred_mm
    fp_bad = pred_lp+pred_lg+pred_lm
    fn_bad = pred_pl+pred_gl+pred_ml

    try:
        acc_rate_bad = (tp_bad + tn_bad) / (tp_bad + tn_bad + fp_bad + fn_bad)
    except(ZeroDivisionError):
        acc_rate_bad = 0
    try:
        precision_bad = tp_bad/(tp_bad+fp_bad)
    except(ZeroDivisionError):
        precision_bad = 0
    try:
        recall_bad = tp_bad/(tp_bad+fn_bad)
    except(ZeroDivisionError):
        recall_bad = 0
    try:
        f1_score_bad = 2*precision_bad*recall_bad/(precision_bad+recall_bad)
    except(ZeroDivisionError):
        f1_score_bad = 0

    confusion_matrix = np.array([[pred_pp,pred_pg,pred_pm,pred_pl], [pred_gp,pred_gg,pred_gm,pred_gl], [pred_mp,pred_mg,pred_mm,pred_ml], [pred_lp,pred_lg,pred_lm,pred_ll]])

    class_names = ["Perfect", "Good", "Mediocre", "Bad"]

    fig, ax = plot_confusion_matrix(conf_mat=confusion_matrix,
                                colorbar=True,
                                show_absolute=True,
                                show_normed=False,
                                class_names=class_names)
    plt.show()

    with open(results_path+results_filename, 'w', newline='') as csvfile:
        fieldnames = ['Classes', 'Accuracy', 'Precision', 'Recall', 'F1_score']
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(fieldnames)
        row_perfect = ["Perfect", acc_rate_perfect, precision_perfect, recall_perfect, f1_score_perfect]
        row_good = ["Good", acc_rate_good, precision_good, recall_good, f1_score_good]
        row_mediocre = ["Mediocre", acc_rate_mediocre, precision_mediocre, recall_mediocre, f1_score_mediocre]
        row_bad = ["Bad", acc_rate_bad, precision_bad, recall_bad, f1_score_bad]
        writer.writerows([row_perfect, row_good, row_mediocre, row_bad])

    return acc_rate_perfect, acc_rate_good, acc_rate_mediocre, acc_rate_bad

def create_TKS(list_metrics, threshold):
    tks = TKS()
    tks.creating_input()
    tks.creating_output()
    tks.creating_fuzzy_rules()
    list_perfect = []
    list_good = []
    list_mediocre = []
    list_low = []
    # Writing the header of the file
    with open("metrics.csv", 'w', newline='') as csvfile:
        fieldnames = ['Id', 'Precision', 'Recall', 'F1_score']
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(fieldnames) 

    for metric in list_metrics:
        mean_precision, mean_recall, mean_f1score = metric.calculateMean()
        tks.engine.input_variable("Precision").value = mean_precision
        tks.engine.input_variable("Recall").value = mean_recall
        tks.engine.input_variable("F1_score").value = mean_f1score
        # TO DO
        print("Experiment metric info: ", metric.getId() +" "+ mean_precision.__str__()+" "+mean_recall.__str__()+" "+mean_f1score.__str__())
        # To write in a file
        with open("metrics.csv", 'a+', newline='') as csvfile:            
            writer = csv.writer(csvfile, delimiter=';')            
            # Writing the content
            row = [metric.getId(), mean_precision.__str__(), mean_recall.__str__(), mean_f1score.__str__()]
            writer.writerow(row)

        tks.engine.process()

        # TO DO
        """tks.engine.input_variable("Precision").value = 0.8
        tks.engine.process()
        list_rules = tks.engine.rule_block("Rules").rules
        for rule in list_rules:
            print("Trigerred: ", rule.triggered.__str__() + " " + rule.antecedent.text)"""
        ####################################################################################
        
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

    
    """list_rules = tks.engine.rule_block("Rules").rules

    for rule in list_rules:
        print("Trigerred: ", rule.triggered.__str__() + " " + rule.antecedent.text)"""
    
    print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("PERFECT")).__str__())
    print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("GOOD")).__str__())
    print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("MEDIOCRE")).__str__())
    print( "Activation degree: ", tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("BAD")).__str__())

    if tks.engine.output_variable("Result").fuzzy.activation_degree(tks.engine.output_variable("Result").term("PERFECT")) >= threshold:
        print("Result is over threshold")
    else:
        print("Result is under threshold")

    

    return list_perfect, list_good, list_mediocre, list_low

def create_Mamdani(list_metrics, threshold):
    mamdani = Mamdani()
    mamdani.creating_input()
    mamdani.creating_output()
    mamdani.creating_fuzzy_rules()
    list_perfect = []
    list_good = []
    list_mediocre = []
    list_low = []
    for metric in list_metrics:
        mean_precision, mean_recall, mean_f1score = metric.calculateMean()
        mamdani.engine.input_variable("Precision").value = mean_precision
        mamdani.engine.input_variable("Recall").value = mean_recall
        mamdani.engine.input_variable("F1_score").value = mean_f1score
        # TO DO
        print("Experiment metric info: ", metric.getId() +" "+ mean_precision.__str__()+" "+mean_recall.__str__()+" "+mean_f1score.__str__())
        mamdani.engine.process()
        if mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("PERFECT")) >= threshold:
            list_perfect.append(metric.getId())
        elif mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("GOOD")) >= threshold:
            list_good.append(metric.getId())
        elif mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("MEDIOCRE")) >= threshold:
            list_mediocre.append(metric.getId())
        elif mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("BAD")) >= threshold:
            list_low.append(metric.getId())
        else:
            print("ERROR: The output variable is wrong.")

    print("Rules: ", mamdani.engine.rule_block("Rules").rules[0].weight.__str__())
    print("Rules: ", mamdani.engine.rule_block("Rules").rules[1].weight.__str__())
    print("Rules: ", mamdani.engine.rule_block("Rules").rules[2].weight.__str__())

    list_terms = mamdani.engine.output_variable("Result").terms
    for term in list_terms:
        print("Terms name: ", term.name.__str__())
        print("Terms value: ", term.membership(0.2).__str__())

    list_rules = mamdani.engine.rule_block("Rules").rules

    for rule in list_rules:
        print("Trigerred: ", rule.triggered.__str__() + " " + rule.antecedent.text)
    
    print( "Activation degree: ", mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("PERFECT")).__str__())
    print( "Activation degree: ", mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("GOOD")).__str__())
    print( "Activation degree: ", mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("MEDIOCRE")).__str__())
    print( "Activation degree: ", mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("BAD")).__str__())

    if mamdani.engine.output_variable("Result").fuzzy.activation_degree(mamdani.engine.output_variable("Result").term("PERFECT")) >= threshold:
        print("Result is over threshold")
    else:
        print("Result is under threshold")

    return list_perfect, list_good, list_mediocre, list_low

def create_Tsukamoto(list_metrics, threshold):
    tsukamoto = Tsukamoto()
    tsukamoto.creating_input()
    tsukamoto.creating_output()
    tsukamoto.creating_fuzzy_rules()
    list_perfect = []
    list_good = []
    list_mediocre = []
    list_low = []
    for metric in list_metrics:
        mean_precision, mean_recall, mean_f1score = metric.calculateMean()
        tsukamoto.engine.input_variable("Precision").value = mean_precision
        tsukamoto.engine.input_variable("Recall").value = mean_recall
        tsukamoto.engine.input_variable("F1_score").value = mean_f1score
        # TO DO
        # print("Experiment metric info: ", metric.getId() +" "+ mean_precision.__str__()+" "+mean_recall.__str__()+" "+mean_f1score.__str__())
        tsukamoto.engine.process()
        if tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("PERFECT")) >= threshold:
            list_perfect.append(metric.getId())
        elif tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("GOOD")) >= threshold:
            list_good.append(metric.getId())
        elif tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("MEDIOCRE")) >= threshold:
            list_mediocre.append(metric.getId())
        elif tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("BAD")) >= threshold:
            list_low.append(metric.getId())
        else:
            print("ERROR: The output variable is wrong.")


    list_rules = tsukamoto.engine.rule_block("Rules").rules

    for rule in list_rules:
        print("Trigerred: ", rule.triggered.__str__() + " " + rule.antecedent.text)
    
    print( "Activation degree: ", tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("PERFECT")).__str__())
    print( "Activation degree: ", tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("GOOD")).__str__())
    print( "Activation degree: ", tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("MEDIOCRE")).__str__())
    print( "Activation degree: ", tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("BAD")).__str__())

    if tsukamoto.engine.output_variable("Result").fuzzy.activation_degree(tsukamoto.engine.output_variable("Result").term("PERFECT")) >= threshold:
        print("Result is over threshold")
    else:
        print("Result is under threshold")

    return list_perfect, list_good, list_mediocre, list_low

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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Cosine("VERY_HIGH",1.0,8),
                fl.Cosine("HIGH",0.9,8),
                fl.Cosine("MEDIUM",0.7,8),
                fl.Cosine("LOW",0.35,8)
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
                fl.Cosine("VERY_HIGH",1.0,8),
                fl.Cosine("HIGH",0.9,8),
                fl.Cosine("MEDIUM",0.7,8),
                fl.Cosine("LOW",0.35,8)
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
                fl.Cosine("VERY_HIGH",1.0,8),
                fl.Cosine("HIGH",0.9,8),
                fl.Cosine("MEDIUM",0.7,8),
                fl.Cosine("LOW",0.35,8)
                 ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Trapezoid("VERY_HIGH",0.9,1.0,1.0,1.2), # Trapezoid(vertexA, vertexB, vertexC, vertexD)
                fl.Trapezoid("HIGH",0.7,0.9,0.9,1.0),
                fl.Trapezoid("MEDIUM",0.35,0.7,0.7,0.9),
                fl.Trapezoid("LOW",0,0.35,0.35,0.7)
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
                fl.Trapezoid("VERY_HIGH",0.9,1.0,1.0,1.2), 
                fl.Trapezoid("HIGH",0.7,0.9,0.9,1.0),
                fl.Trapezoid("MEDIUM",0.35,0.7,0.7,0.9),
                fl.Trapezoid("LOW",0,0.35,0.35,0.7)
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
                fl.Trapezoid("VERY_HIGH",0.9,1.0,1.0,1.2), 
                fl.Trapezoid("HIGH",0.7,0.9,0.9,1.0),
                fl.Trapezoid("MEDIUM",0.35,0.7,0.7,0.9),
                fl.Trapezoid("LOW",0,0.35,0.35,0.7)
                ]
                            
            )
        ]

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
                ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Sigmoid("VERY_HIGH", 1.0, 0.5), # Sigmoid(inflection, slope)    
                fl.Sigmoid("HIGH", 0.9, 0.5),            
                fl.Sigmoid("MEDIUM", 0.7, 0.5), 
                fl.Sigmoid("LOW", 0.35, 0.5)
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
                fl.Sigmoid("VERY_HIGH", 1.0, 0.5), # Sigmoid(inflection, slope)    
                fl.Sigmoid("HIGH", 0.9, 0.5),            
                fl.Sigmoid("MEDIUM", 0.7, 0.5), 
                fl.Sigmoid("LOW", 0.35, 0.5)  
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
                fl.Sigmoid("VERY_HIGH", 1.0, 0.5), # Sigmoid(inflection, slope)    
                fl.Sigmoid("HIGH", 0.9, 0.5),            
                fl.Sigmoid("MEDIUM", 0.7, 0.5), 
                fl.Sigmoid("LOW", 0.35, 0.5)  
                ]                            
            )
        ] """

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55)   
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
                ]                            
            )
        ]"""                
    
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
                fl.Constant("GOOD", 0.8),
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
                activation=fl.General(),
                rules=[
                    fl.Rule.create("if Precision is VERY_HIGH and Recall is VERY_HIGH and F1_score is VERY_HIGH then Result is PERFECT", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),                    
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if F1_score is LOW then Result is BAD", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
                ]
            )
        ]
        # TO DO
        """self.engine.rule_blocks = [
            fl.RuleBlock(
                name="Rules",
                description="",
                enabled=True,
                conjunction=fl.Minimum(),
                disjunction=fl.Maximum(),
                implication=None,
                activation=fl.Highest(),
                rules=[
                    fl.Rule.create("if Precision is VERY_HIGH then Result is PERFECT", self.engine),
                    fl.Rule.create("if Precision is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM then Result is MEDIOCRE", self.engine),                     
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
                ]
            )
        ]"""



# MAMDANI

class Mamdani:

    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="Mamdani_Fuzzy_System",
        description="")

# Defining the Input Variables (Fuzzification)
    def creating_input(self):
        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Trapezoid("VERY_HIGH",0.95,1.0,1.0,1.2), # Trapezoid(vertexA, vertexB, vertexC, vertexD)
                fl.Trapezoid("HIGH",0.8,0.9,0.95,1.0),
                fl.Trapezoid("MEDIUM",0.5,0.6,0.68,0.8),
                fl.Trapezoid("LOW",0,0.25,0.35,0.5)
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
                fl.Trapezoid("VERY_HIGH",0.95,1.0,1.0,1.2), # Trapezoid(vertexA, vertexB, vertexC, vertexD)
                fl.Trapezoid("HIGH",0.8,0.9,0.95,1.0),
                fl.Trapezoid("MEDIUM",0.5,0.6,0.68,0.8),
                fl.Trapezoid("LOW",0,0.25,0.35,0.5)
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
                fl.Trapezoid("VERY_HIGH",0.95,1.0,1.0,1.2), # Trapezoid(vertexA, vertexB, vertexC, vertexD)
                fl.Trapezoid("HIGH",0.8,0.9,0.95,1.0),
                fl.Trapezoid("MEDIUM",0.5,0.6,0.68,0.8),
                fl.Trapezoid("LOW",0,0.25,0.35,0.5)
                ]
                            
            )
        ]

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
                ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55)   
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
                ]                            
            )
        ]"""

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
            aggregation=fl.Maximum(),
            defuzzifier=fl.Centroid(200),
            lock_previous=False,
            terms=[
            fl.Triangle("BAD", 0,0.35,0.7), 
            fl.Triangle("MEDIOCRE", 0.35,0.7,0.9),
            fl.Triangle("GOOD", 0.7,0.9,1.0), 
            fl.Triangle("PERFECT", 0.9,1.0,1.0)
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
            implication=fl.Minimum(),
            activation=fl.General(),
            rules=[
                fl.Rule.create("if Precision is VERY_HIGH and Recall is VERY_HIGH and F1_score is VERY_HIGH then Result is PERFECT", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),                    
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if F1_score is LOW then Result is BAD", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
            ]
            )
        ]

# TSUKAMOTO
class Tsukamoto:
    def __init__(self):
        # Declaring and Initializing the Fuzzy Engine
        self.engine = fl.Engine(
        name="Tsukamoto_Fuzzy_System",
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
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
                fl.Bell("VERY_HIGH", 1.0, 8, 4), # Bell(center, width,slope)    
                fl.Bell("HIGH", 0.9, 8, 4),            
                fl.Bell("MEDIUM", 0.7, 8, 4), 
                fl.Bell("LOW", 0.35, 8, 4) 
                ]
                            
            )
        ]

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
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
                fl.Gaussian("VERY_HIGH",1.0,0.5),
                fl.Gaussian("HIGH",0.9,0.5),
                fl.Gaussian("MEDIUM",0.7,0.5),
                fl.Gaussian("LOW",0.35,0.5)
                 ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
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
                fl.Triangle("VERY_HIGH",0.9,1.0,1.0), 
                fl.Triangle("HIGH",0.7,0.9,1.0),
                fl.Triangle("MEDIUM",0.35,0.7,0.9),
                fl.Triangle("LOW",0,0.35,0.7)
                ]
                            
            )
        ]"""

        """self.engine.input_variables = [
        fl.InputVariable(
            name="Precision",
            description="",
            enabled=True,
            minimum=0.000,
            maximum=1.000,
            lock_range=False,
            terms=[
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55)   
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
                fl.Ramp("VERY_HIGH", 0.95, 1.0), # Ramp (start, end)    
                fl.Ramp("HIGH", 0.8, 0.95),            
                fl.Ramp("MEDIUM", 0.55, 0.8), 
                fl.Ramp("LOW", 0.0, 0.55) 
                ]                            
            )
        ]"""
        
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
            aggregation=fl.Maximum(),
            defuzzifier=fl.Centroid(200),
            lock_previous=False,
            terms=[
            fl.Sigmoid("BAD", 0, 2), 
            fl.Sigmoid("MEDIOCRE", 0.5, 2), 
            fl.Sigmoid("GOOD", 0.7, 2),
            fl.Sigmoid("PERFECT", 1.0, 2)
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
            implication=fl.Minimum(),
            activation=fl.Highest(),
            rules=[
                fl.Rule.create("if Precision is VERY_HIGH and Recall is VERY_HIGH and F1_score is VERY_HIGH then Result is PERFECT", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is HIGH then Result is GOOD", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is HIGH then Result is GOOD", self.engine),                    
                    fl.Rule.create("if Precision is HIGH and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is HIGH and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is MEDIUM and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is HIGH and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if Precision is MEDIUM and Recall is LOW and F1_score is MEDIUM then Result is MEDIOCRE", self.engine),
                    fl.Rule.create("if F1_score is LOW then Result is BAD", self.engine),
                    fl.Rule.create("if Precision is LOW then Result is BAD", self.engine)
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
# Results folder path
results_path = "results/"
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

# Creating TKS Fuzzy System
# list_perfect, list_good, list_mediocre, list_low = create_TKS(list_metrics, threshold)
# results_filename = "results_metrics_tks.csv"

# Creating Mamdani Fuzzy System
list_perfect, list_good, list_mediocre, list_low = create_Mamdani(list_metrics,threshold)
results_filename = "results_metrics_mamdani.csv"

# Creating Tsukamoto Fuzzy System
# list_perfect, list_good, list_mediocre, list_low = create_Tsukamoto(list_metrics,threshold)
# results_filename = "results_metrics_tsukamoto.csv"

# GETTING RESULTS

# Create dictionary for the results
dic_result={"PERFECT": list_perfect, "GOOD": list_good, "MEDIOCRE": list_mediocre, "LOW": list_low}

# Evaluate the results
evaluate_predictions(dic_result["PERFECT"], dic_result["GOOD"], dic_result["MEDIOCRE"], dic_result["LOW"], results_filename)

print("PROCESS FINISHED")
