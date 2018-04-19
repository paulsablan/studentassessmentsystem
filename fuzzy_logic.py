import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

class fis(object):
    def __init__(self):
        #STUDY HABIT
        # Create universe fucntion
        study_habit_SH_input = ctrl.Antecedent(np.arange(18, 54, 1), 'study_habit_SH_input')
        grade_SH = ctrl.Antecedent(np.arange(60, 100, 1), 'grade_SH')
        study_habit_SH_output = ctrl.Consequent(np.arange(1, 10, 1), 'study_habit_SH_output')
        # Membership function for study_habit_SH_input
        study_habit_SH_input['low'] = fuzz.trapmf(study_habit_SH_input.universe, [18, 18, 25, 30])
        study_habit_SH_input['med'] = fuzz.trapmf(study_habit_SH_input.universe, [25, 30, 45, 49])
        study_habit_SH_input['high'] = fuzz.trapmf(study_habit_SH_input.universe, [30, 46, 54, 54])
        # Membership function for grade_SH
        grade_SH['bad'] = fuzz.trapmf(grade_SH.universe, [60, 60, 70, 76])
        grade_SH['fair'] = fuzz.trapmf(grade_SH.universe, [75, 76, 80, 82])
        grade_SH['good'] = fuzz.trapmf(grade_SH.universe, [80, 82, 87, 95])
        grade_SH['best'] = fuzz.trapmf(grade_SH.universe, [90, 95, 100, 100])
        # Membership function for study_habit_SH_output
        study_habit_SH_output['low'] = fuzz.trapmf(study_habit_SH_output.universe, [1, 1, 3, 4])
        study_habit_SH_output['med'] = fuzz.trapmf(study_habit_SH_output.universe, [3, 4, 6, 7])
        study_habit_SH_output['severe'] = fuzz.trapmf(study_habit_SH_output.universe, [6, 8, 10, 10])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(study_habit_SH_input['low'] & grade_SH['bad'],  study_habit_SH_output['severe']))
        rules.append(ctrl.Rule(study_habit_SH_input['low'] & grade_SH['fair'],  study_habit_SH_output['severe']))
        rules.append(ctrl.Rule(study_habit_SH_input['low'] & grade_SH['good'],  study_habit_SH_output['med']))
        rules.append(ctrl.Rule(study_habit_SH_input['low'] & grade_SH['best'],  study_habit_SH_output['low']))
        rules.append(ctrl.Rule(study_habit_SH_input['med'] & grade_SH['bad'],  study_habit_SH_output['severe']))
        rules.append(ctrl.Rule(study_habit_SH_input['med'] & grade_SH['fair'],  study_habit_SH_output['med']))
        rules.append(ctrl.Rule(study_habit_SH_input['med'] & grade_SH['good'],  study_habit_SH_output['med']))
        rules.append(ctrl.Rule(study_habit_SH_input['med'] & grade_SH['best'],  study_habit_SH_output['low']))
        rules.append(ctrl.Rule(study_habit_SH_input['high'] & grade_SH['bad'],  study_habit_SH_output['severe']))
        rules.append(ctrl.Rule(study_habit_SH_input['high'] & grade_SH['fair'],  study_habit_SH_output['low']))
        rules.append(ctrl.Rule(study_habit_SH_input['high'] & grade_SH['good'],  study_habit_SH_output['low']))
        rules.append(ctrl.Rule(study_habit_SH_input['high'] & grade_SH['best'],  study_habit_SH_output['low']))
        # Control
        study_habit_ctrl = ctrl.ControlSystem(rules)
        self.rating_study_habit = ctrl.ControlSystemSimulation(study_habit_ctrl)

        # BROKEN FAMILY
        # Create universe fucntion
        broken_family_BF_input = ctrl.Antecedent(np.arange(0, 5 , 1), 'broken_family_BF_input')
        grade_BF = ctrl.Antecedent(np.arange(60, 100, 1), 'grade_BF')
        broken_family_BF_output = ctrl.Consequent(np.arange(1, 10, 1), 'broken_family_BF_output')
        # Membership function for broken_family_BF_input
        broken_family_BF_input['low'] = fuzz.trimf(broken_family_BF_input.universe, [0, 0, 2])
        broken_family_BF_input['med'] = fuzz.trapmf(broken_family_BF_input.universe, [1, 2, 3, 4])
        broken_family_BF_input['high'] = fuzz.trimf(broken_family_BF_input.universe, [3, 5, 5])
        # Membership function for grade_BF
        grade_BF['bad'] = fuzz.trapmf(grade_BF.universe, [60, 60, 70, 76])
        grade_BF['fair'] = fuzz.trapmf(grade_BF.universe, [75, 76, 80, 82])
        grade_BF['good'] = fuzz.trapmf(grade_BF.universe, [80, 82, 87, 95])
        grade_BF['best'] = fuzz.trapmf(grade_BF.universe, [90, 95, 100, 100])
        # Membership function for broken_family_BF_output
        broken_family_BF_output['low'] = fuzz.trapmf(broken_family_BF_output.universe, [1, 1, 3, 4])
        broken_family_BF_output['med'] = fuzz.trapmf(broken_family_BF_output.universe, [3, 4, 6, 7])
        broken_family_BF_output['severe'] = fuzz.trapmf(broken_family_BF_output.universe, [6, 8, 10, 10])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(broken_family_BF_input['low'] & grade_BF['bad'],  broken_family_BF_output['severe']))
        rules.append(ctrl.Rule(broken_family_BF_input['low'] & grade_BF['fair'],  broken_family_BF_output['med']))
        rules.append(ctrl.Rule(broken_family_BF_input['low'] & grade_BF['good'],  broken_family_BF_output['med']))
        rules.append(ctrl.Rule(broken_family_BF_input['low'] & grade_BF['best'],  broken_family_BF_output['low']))
        rules.append(ctrl.Rule(broken_family_BF_input['med'] & grade_BF['bad'],  broken_family_BF_output['severe']))
        rules.append(ctrl.Rule(broken_family_BF_input['med'] & grade_BF['fair'],  broken_family_BF_output['med']))
        rules.append(ctrl.Rule(broken_family_BF_input['med'] & grade_BF['good'],  broken_family_BF_output['low']))
        rules.append(ctrl.Rule(broken_family_BF_input['med'] & grade_BF['best'],  broken_family_BF_output['low']))
        rules.append(ctrl.Rule(broken_family_BF_input['high'] & grade_BF['bad'],  broken_family_BF_output['severe']))
        rules.append(ctrl.Rule(broken_family_BF_input['high'] & grade_BF['fair'],  broken_family_BF_output['low']))
        rules.append(ctrl.Rule(broken_family_BF_input['high'] & grade_BF['good'],  broken_family_BF_output['low']))
        rules.append(ctrl.Rule(broken_family_BF_input['high'] & grade_BF['best'],  broken_family_BF_output['low']))
        # Control
        broken_family = ctrl.ControlSystem(rules)
        self.rating_broken_family = ctrl.ControlSystemSimulation(broken_family)

        # FINANCIAL DIFFUCULTY
        # Create universe fucntion
        financial_diff_FH_input = ctrl.Antecedent(np.arange(1, 6, 1), 'financial_diff_FH_input')
        grade_FH = ctrl.Antecedent(np.arange(60, 100, 1), 'grade_FH')
        financial_diff_FH_output = ctrl.Consequent(np.arange(1, 10, 1), 'financial_diff_FH_output')
        # Membership function for financial_diff_FH_input
        financial_diff_FH_input['high'] = fuzz.trimf(financial_diff_FH_input.universe, [1, 1, 3])
        financial_diff_FH_input['med'] = fuzz.trapmf(financial_diff_FH_input.universe, [2, 3, 4, 5])
        financial_diff_FH_input['low'] = fuzz.trimf(financial_diff_FH_input.universe, [4, 6, 6])
        # Membership function for grade_FH
        grade_FH['bad'] = fuzz.trapmf(grade_FH.universe, [60, 60, 70, 76])
        grade_FH['fair'] = fuzz.trapmf(grade_FH.universe, [75, 76, 80, 82])
        grade_FH['good'] = fuzz.trapmf(grade_FH.universe, [80, 82, 87, 95])
        grade_FH['best'] = fuzz.trapmf(grade_FH.universe, [90, 95, 100, 100])
        # Membership function for financial_diff_FH_output
        financial_diff_FH_output['low'] = fuzz.trapmf(financial_diff_FH_output.universe, [1, 1, 3, 4])
        financial_diff_FH_output['med'] = fuzz.trapmf(financial_diff_FH_output.universe, [3, 4, 6, 7])
        financial_diff_FH_output['severe'] = fuzz.trapmf(financial_diff_FH_output.universe, [6, 8, 10, 10])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(financial_diff_FH_input['low'] & grade_FH['bad'],  financial_diff_FH_output['severe']))
        rules.append(ctrl.Rule(financial_diff_FH_input['low'] & grade_FH['fair'],  financial_diff_FH_output['med']))
        rules.append(ctrl.Rule(financial_diff_FH_input['low'] & grade_FH['good'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['low'] & grade_FH['best'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['med'] & grade_FH['bad'],  financial_diff_FH_output['severe']))
        rules.append(ctrl.Rule(financial_diff_FH_input['med'] & grade_FH['fair'],  financial_diff_FH_output['med']))
        rules.append(ctrl.Rule(financial_diff_FH_input['med'] & grade_FH['good'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['med'] & grade_FH['best'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['high'] & grade_FH['bad'],  financial_diff_FH_output['severe']))
        rules.append(ctrl.Rule(financial_diff_FH_input['high'] & grade_FH['fair'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['high'] & grade_FH['good'],  financial_diff_FH_output['low']))
        rules.append(ctrl.Rule(financial_diff_FH_input['high'] & grade_FH['best'],  financial_diff_FH_output['low']))

        # Control
        financial_diff = ctrl.ControlSystem(rules)
        self.rating_financial_diff = ctrl.ControlSystemSimulation(financial_diff)

    def financial_fuzzy(self, financial_diff_rating, grade):
        self.rating_financial_diff.input['financial_diff_FH_input'] = financial_diff_rating
        self.rating_financial_diff.input['grade_FH'] = grade
        # Crunch the numbers
        self.rating_financial_diff.compute()
        rate = self.rating_financial_diff.output['financial_diff_FH_output']
        if rate <= 3.9:
            label = 'mild'
        elif rate >= 3.9 and rate <= 6.9:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def broken_family(self, broken_family_rating, grade):
        self.rating_broken_family.input['broken_family_BF_input'] = broken_family_rating
        self.rating_broken_family.input['grade_BF'] = grade
        # Crunch the numbers
        self.rating_broken_family.compute()
        rate = self.rating_broken_family.output['broken_family_BF_output']
        if rate <= 3.9:
            label = 'mild'
        elif rate >= 3.9 and rate <= 6.9:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def study_habit(self, study_habit_rating, grade):
        self.rating_study_habit.input['study_habit_SH_input'] = study_habit_rating
        self.rating_study_habit.input['grade_SH'] = grade
        # Crunch the numbers
        self.rating_study_habit.compute()
        rate = self.rating_study_habit.output['study_habit_SH_output']
        if rate <= 3.9:
            label = 'mild'
        elif rate >= 3.9 and rate <= 6.9:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label
