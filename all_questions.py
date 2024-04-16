import pytest
from all_questions import *
import pickle
import math



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.028 # or 0.16

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002 # or 0.1

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    
    # w = 0.5*math.log((1-0.3)/0.3)
    answers['(c) Weight update'] = "0.5*math.log((1-p)/p)"

    # type: float
    # the answer should be correct to 3 significant digits
    
    # w_new = 1*math.exp(w)
    answers['(d) Weight influence'] = 1.5275 # or w_new 
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"
 
    # type: explain_string
    answers['Explain'] = "Though it is correct that the ensemble model combines the predictions of multiple predictors to improve the overall performance, but the key point is that each predictor should perform better than random guessing."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 'p'

    # type: eval_float
    answers['(a) C2-TPR'] = '2*p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2*p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'yes'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = 'C2 is a better classifier than C1 because both of them have same precision but C2 has a higher recall which means it is able to identify more positive cases.'  
    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = 'The precision-recall curve is more appropriate for imbalanced datasets as it focuses on the correctly predicted class and is not affected by the class imbalance.'
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2' 

    # type: explain_string
    answers['(i) Best classifier, explain'] = "both C1 and C2 have the same precision, but C2 has a higher recall, which makes it a better classifier."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'The precision-recall-F1-Measure is the appropriate metric pair because it better captures the trade-off between correctly identifying positive cases and avoiding misclassification of negative cases.'
    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'C2 has the highest F1-Measure, But the context of the problem and nature of data also play a role in choosing the best classifier eg. if minimizing False positive is crutial and some miss in identifying the true positive is acceptable then we might choose C3 '

    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '1/10' # or p*100/p*1000

    # type: eval_float
    answers['(a) recall for C0'] = 'p'

    # type: eval_float
    answers['(b) F-measure of C0'] = '0.2*p/(p+0.1)' # or 0.2

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no' # without context and p value, we can't say

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
                                'recall': 0.615,
                                'precision': 0.533,
                                'F-measure': 0.571,
                                'accuracy': 0.88}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'Accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'Beacuse of the class imbalance in the data, the F-measure is the best metric to use as it considers both precision and recall. Accuracy is the worst metric because it does not take into account the class imbalance and can be misleading.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'F1'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'In cancer diagnostics, missing a true case (high recall is crucial) can be life-threatening, and falsely diagnosing someone with cancer (requiring high precision to avoid) can lead to unnecessary and potentially harmful treatments. The F1-Score provides a balanced view of both these concerns, making it a particularly appropriate measure in this context.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'If the cost of false positives is very high, then we might choose TPR/FPR as the evaluation measure.'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
