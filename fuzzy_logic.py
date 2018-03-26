import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

def financial_fuzzy(famsize, mjob, fjob):
    # Create universe fucntion
    mjob_f = ctrl.Antecedent(np.arange(1, 4, 1), 'mjob_f')
    fjob_f = ctrl.Antecedent(np.arange(1, 4, 1), 'fjob_f')
    famsize_f = ctrl.Antecedent(np.arange(0, 5, 1), 'famsize_f')
    financial_f = ctrl.Consequent(np.arange(0, 5, 1), 'financial_f')

    # Membership function for mjob
    mjob_f['low'] = fuzz.trimf(mjob_f.universe, [1, 1, 2])
    mjob_f['med'] = fuzz.trimf(mjob_f.universe, [1, 2, 3])
    mjob_f['high'] = fuzz.trimf(mjob_f.universe, [1, 4, 4])
    # Membership function for fjob
    fjob_f['low'] = fuzz.trimf(fjob_f.universe, [1, 1, 2])
    fjob_f['med'] = fuzz.trimf(fjob_f.universe, [1, 2, 3])
    fjob_f['high'] = fuzz.trimf(fjob_f.universe, [1, 4, 4])
    # Membership function for famsize
    famsize_f['few'] = fuzz.trimf(famsize_f.universe, [0, 1, 2])
    famsize_f['many'] = fuzz.trimf(famsize_f.universe, [1, 2, 3])
    # Membership function for financial
    financial_f['low'] = fuzz.trapmf(financial_f.universe, [0, 0, 1, 2])
    financial_f['med'] = fuzz.trapmf(financial_f.universe, [1, 2, 3, 4])
    financial_f['severe'] = fuzz.trapmf(financial_f.universe, [3, 4, 5, 5])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(mjob_f['low'] & fjob_f['low'] & famsize_f['many'], financial_f['severe']))
    rules.append(ctrl.Rule(mjob_f['low'] & fjob_f['med'] & famsize_f['many'], financial_f['severe']))
    rules.append(ctrl.Rule(mjob_f['med'] & fjob_f['low'] & famsize_f['many'], financial_f['severe']))
    rules.append(ctrl.Rule(mjob_f['low'] & fjob_f['med'] & famsize_f['few'], financial_f['med']))
    rules.append(ctrl.Rule(mjob_f['med'] & fjob_f['low'] & famsize_f['few'], financial_f['med']))
    rules.append(ctrl.Rule(mjob_f['low'] & fjob_f['low'] & famsize_f['few'], financial_f['med']))
    rules.append(ctrl.Rule(mjob_f['high'] & famsize_f['many'], financial_f['med']))
    rules.append(ctrl.Rule(fjob_f['high'] & famsize_f['many'], financial_f['med']))
    rules.append(ctrl.Rule(mjob_f['high'] & famsize_f['few'], financial_f['low']))
    rules.append(ctrl.Rule(fjob_f['high'] & famsize_f['few'], financial_f['low']))
    rules.append(ctrl.Rule(mjob_f['high'] & fjob_f['low'] & famsize_f['few'], financial_f['low']))
    rules.append(ctrl.Rule(mjob_f['low'] & fjob_f['high'] & famsize_f['few'], financial_f['low']))
    # Control
    financial_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(financial_ctrl)

    rating.input['mjob_f'] = mjob
    rating.input['fjob_f'] = fjob
    rating.input['famsize_f'] = famsize
    # Crunch the numbers
    rating.compute()
    rate = rating.output['financial_f']
    if rate <= 2.49:
        label = 'mild'
    elif rate >= 2.5 and rate <= 3.49:
        label = 'moderate'
    else:
        label = 'severe'
    return rate, label

def broken_family(pstatus, famsup):
    pstatus_f = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_f')
    famsup_f = ctrl.Antecedent(np.arange(1, 3, 1), 'famsup_f')
    broken_family_f = ctrl.Consequent(np.arange(1, 3, 1), 'broken_family_f')
    # Memberships
    pstatus_f['together'] = fuzz.trimf(pstatus_f.universe, [1, 1, 2])
    pstatus_f['apart'] = fuzz.trimf(pstatus_f.universe, [1, 2, 3])
    famsup_f['yes'] = fuzz.trimf(famsup_f.universe, [1, 1, 2])
    famsup_f['no'] = fuzz.trimf(famsup_f.universe, [1, 2, 3])
    broken_family_f['low'] = fuzz.trimf(broken_family_f.universe, [1, 1, 2])
    broken_family_f['high'] = fuzz.trapmf(broken_family_f.universe, [1, 2, 3, 3])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(pstatus_f['apart'] & famsup_f['no'] , broken_family_f['high']))
    rules.append(ctrl.Rule(pstatus_f['apart'] & famsup_f['yes'],  broken_family_f['low']))
    rules.append(ctrl.Rule(pstatus_f['together'] & famsup_f['no'] , broken_family_f['high']))
    rules.append(ctrl.Rule(pstatus_f['together'] & famsup_f['yes'],  broken_family_f['low']))
    # Control
    broken_family_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(broken_family_ctrl)

    rating.input['pstatus_f'] = pstatus
    rating.input['famsup_f'] = famsup
    # Crunch the numbers
    rating.compute()
    rate = rating.output['broken_family_f']
    if rate <= 1.49:
        label = 'mild'
    else:
        label = 'severe'
    return rate, label

def living_with_rel(pstatus, famsup):
    pstatus_f = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_f')
    famsup_f = ctrl.Antecedent(np.arange(1, 3, 1), 'famsup_f')
    living_with_rel_f = ctrl.Consequent(np.arange(1, 3, 1), 'living_with_rel_f')
    # Memberships
    pstatus_f['together'] = fuzz.trimf(pstatus_f.universe, [1, 1, 2])
    pstatus_f['apart'] = fuzz.trimf(pstatus_f.universe, [1, 2, 3])
    pstatus_f['together'] = fuzz.trimf(pstatus_f.universe, [1, 1, 2])
    pstatus_f['apart'] = fuzz.trimf(pstatus_f.universe, [1, 2, 3])
    famsup_f['yes'] = fuzz.trimf(famsup_f.universe, [1, 1, 2])
    famsup_f['no'] = fuzz.trimf(famsup_f.universe, [1, 2, 3])
    living_with_rel_f['low'] = fuzz.trimf(famsup_f.universe, [1, 1, 2])
    living_with_rel_f['high'] = fuzz.trapmf(living_with_rel_f.universe, [1, 2, 3, 3])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(pstatus_f['apart'] & famsup_f['no'] , living_with_rel_f['high']))
    rules.append(ctrl.Rule(pstatus_f['apart'] & famsup_f['yes'],  living_with_rel_f['low']))
    rules.append(ctrl.Rule(pstatus_f['together'] & famsup_f['no'] , living_with_rel_f['high']))
    rules.append(ctrl.Rule(pstatus_f['together'] & famsup_f['yes'],  living_with_rel_f['low']))
    # Control
    broken_family_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(broken_family_ctrl)
    rating.input['pstatus_f'] = pstatus
    rating.input['famsup_f'] = famsup
    # Crunch the numbers
    rating.compute()
    rate = rating.output['living_with_rel_f']
    if rate <= 1.49:
        label = 'mild'
    else:
        label = 'severe'
    return rate, label

def health_conditions(health, activities, absences):
    # Create universe fucntion
    health_f = ctrl.Antecedent(np.arange(1, 5, 1), 'health_f')
    activities_f = ctrl.Antecedent(np.arange(1, 3, 1), 'activities_f')
    absences_f = ctrl.Antecedent(np.arange(0, 100, 1), 'absences_f')
    health_conditions_f = ctrl.Consequent(np.arange(1, 5, 1), 'health_conditions_f')
    # Membership
    health_f['good'] = fuzz.trimf(health_f.universe, [3, 5, 5])
    health_f['neutral'] = fuzz.trimf(health_f.universe, [2, 3, 4])
    health_f['bad'] = fuzz.trimf(health_f.universe, [1, 1, 3])
    activities_f['yes'] = fuzz.trimf(activities_f.universe, [1, 1, 2])
    activities_f['no'] = fuzz.trimf(activities_f.universe, [1, 2, 3])
    absences_f['few'] = fuzz.trimf(absences_f.universe, [0, 0, 4])
    absences_f['moderate'] = fuzz.trimf(absences_f.universe, [2, 10, 15])
    absences_f['frequent'] = fuzz.trapmf(absences_f.universe, [10, 25, 100, 100])
    health_conditions_f['low'] = fuzz.trimf(health_conditions_f.universe, [1, 1, 3])
    health_conditions_f['med'] = fuzz.trimf(health_conditions_f.universe, [2, 3, 4])
    health_conditions_f['severe'] = fuzz.trimf(health_conditions_f.universe, [3, 5, 5])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(health_f['bad'] & (absences_f['moderate'] | absences_f['frequent']) & (activities_f['yes'] | activities_f['no']), health_conditions_f['severe']))
    rules.append(ctrl.Rule(health_f['bad'] & absences_f['few'] & (activities_f['yes'] | activities_f['no']), health_conditions_f['severe']))
    rules.append(ctrl.Rule(health_f['neutral'] & (absences_f['moderate'] | absences_f['frequent']) & activities_f['yes'], health_conditions_f['severe']))
    rules.append(ctrl.Rule(health_f['neutral'] & absences_f['few'], health_conditions_f['low']))
    rules.append(ctrl.Rule(health_f['neutral'] & absences_f['moderate'], health_conditions_f['med']))
    rules.append(ctrl.Rule(health_f['neutral'] & absences_f['frequent'], health_conditions_f['med']))
    rules.append(ctrl.Rule(health_f['good'] & (activities_f['yes'] | activities_f['no']) & (absences_f['moderate'] | absences_f['frequent']), health_conditions_f['low']))
    rules.append(ctrl.Rule(health_f['good'] & (activities_f['yes'] | activities_f['no']) & absences_f['few'], health_conditions_f['low']))
    # Control
    health_condition_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(health_condition_ctrl)
    rating.input['health_f'] = health
    rating.input['activities_f'] = activities
    rating.input['absences_f'] = absences
    # Crunch the 10umbers
    rating.compute()
    rate = rating.output['health_conditions_f']
    if rate <= 2.49:
        label = 'mild'
    elif rate >= 2.5 and rate <= 3.49:
        label = 'moderate'
    else:
        label = 'severe'
    return rate, label

def insufficient_learning_materials(internet, mjob, fjob):
    # Create universe fucntion
    internet_f = ctrl.Antecedent(np.arange(1, 3, 1), 'internet_f')
    mjob_f = ctrl.Antecedent(np.arange(1, 4, 1), 'mjob_f')
    fjob_f = ctrl.Antecedent(np.arange(1, 4, 1), 'fjob_f')
    learning_materials_f = ctrl.Consequent(np.arange(0, 5, 1), 'learning_materials_f')
    # Membership
    internet_f['yes'] = fuzz.trimf(internet_f.universe, [1, 1, 2])
    internet_f['no'] = fuzz.trimf(internet_f.universe, [1, 2, 3])
    mjob_f['low'] = fuzz.trimf(mjob_f.universe, [1, 1, 2])
    mjob_f['med'] = fuzz.trapmf(mjob_f.universe, [1, 2, 3, 4])
    mjob_f['high'] = fuzz.trapmf(mjob_f.universe, [1, 3, 4, 4])
    fjob_f['low'] = fuzz.trimf(fjob_f.universe, [1, 1, 2])
    fjob_f['med'] = fuzz.trapmf(fjob_f.universe, [1, 2, 3, 4])
    fjob_f['high'] = fuzz.trapmf(fjob_f.universe, [1, 3, 4, 4])
    learning_materials_f['low'] = fuzz.trapmf(learning_materials_f.universe, [0, 0, 1, 2])
    learning_materials_f['med'] = fuzz.trapmf(learning_materials_f.universe, [1, 2, 3, 4])
    learning_materials_f['severe'] = fuzz.trapmf(learning_materials_f.universe, [3, 5, 5, 5])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(internet_f['yes'] & (mjob_f['low'] | mjob_f['med'] | mjob_f['high']) & (fjob_f['low'] | fjob_f['med'] | fjob_f['high']), learning_materials_f['low']))
    rules.append(ctrl.Rule(internet_f['no'] & mjob_f['low'] & fjob_f['low'], learning_materials_f['severe']))
    rules.append(ctrl.Rule(internet_f['no'] & mjob_f['med'] & fjob_f['low'], learning_materials_f['severe']))
    rules.append(ctrl.Rule(internet_f['no'] & mjob_f['low'] & fjob_f['med'], learning_materials_f['severe']))
    rules.append(ctrl.Rule(internet_f['no'] & mjob_f['med'] & fjob_f['med'], learning_materials_f['med']))
    rules.append(ctrl.Rule(internet_f['no'] & (mjob_f['high'] | fjob_f['high']), learning_materials_f['med']))
    # Control
    learning_materials_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(learning_materials_ctrl)
    rating.input['internet_f'] = internet
    rating.input['mjob_f'] = mjob
    rating.input['fjob_f'] = fjob
    # Crunch the numbers
    rating.compute()
    rate = rating.output['learning_materials_f']
    if rate <= 2.49:
        label = 'mild'
    elif rate >= 2.5 and rate <= 3.49:
        label = 'moderate'
    else:
        label = 'severe'
    return rate, label

def parenting_issues(pstatus, medu, fedu):
    # Create universe fucntion
    pstatus_f = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_f')
    medu_f = ctrl.Antecedent(np.arange(0, 4, 1), 'medu_f')
    fedu_f = ctrl.Antecedent(np.arange(0, 4, 1), 'fedu_f')
    parenting_issues_f = ctrl.Consequent(np.arange(1, 4, 1), 'parenting_issues_f')
    # Membership
    medu_f['low'] = fuzz.trapmf(medu_f.universe, [0, 0, 1, 3])
    medu_f['med'] = fuzz.trimf(medu_f.universe, [1, 2, 4])
    medu_f['high'] = fuzz.trimf(medu_f.universe, [3, 4, 4])
    fedu_f['low'] = fuzz.trapmf(fedu_f.universe, [0, 0, 1, 3])
    fedu_f['med'] = fuzz.trimf(fedu_f.universe, [1, 2, 4])
    fedu_f['high'] = fuzz.trimf(fedu_f.universe, [3, 4, 4])
    pstatus_f['together'] = fuzz.trimf(pstatus_f.universe, [1, 1, 2])
    pstatus_f['apart'] = fuzz.trimf(pstatus_f.universe, [1, 2, 3])
    parenting_issues_f['low'] = fuzz.trimf(parenting_issues_f.universe, [1, 1, 2])
    parenting_issues_f['med'] = fuzz.trimf(parenting_issues_f.universe, [1, 2, 3])
    parenting_issues_f['severe'] = fuzz.trimf(parenting_issues_f.universe, [2, 3, 4])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['high'] & fedu_f['low'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['high'] & fedu_f['med'], parenting_issues_f['med']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['high'] & fedu_f['high'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['med'] & fedu_f['low'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['med'] & fedu_f['med'], parenting_issues_f['med']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['med'] & fedu_f['high'], parenting_issues_f['med']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['low'] & fedu_f['low'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['low'] & fedu_f['med'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['apart'] & medu_f['low'] & fedu_f['high'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['high'] & fedu_f['low'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['high'] & fedu_f['med'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['high'] & fedu_f['high'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['med'] & fedu_f['low'], parenting_issues_f['med']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['med'] & fedu_f['med'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['med'] & fedu_f['high'], parenting_issues_f['low']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['low'] & fedu_f['low'], parenting_issues_f['severe']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['low'] & fedu_f['med'], parenting_issues_f['med']))
    rules.append(ctrl.Rule( pstatus_f['together'] & medu_f['low'] & fedu_f['high'], parenting_issues_f['low']))
    # Control
    parenting_issues_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(parenting_issues_ctrl)
    rating.input['pstatus_f'] = pstatus
    rating.input['medu_f'] = medu
    rating.input['fedu_f'] = fedu
    # Crunch the numbers
    rating.compute()
    rate = rating.output['parenting_issues_f']
    if rate <= 1.49:
        label = 'mild'
    elif rate >= 1.5 and rate <= 2.49:
        label = 'moderate'
    else:
        label = 'severe'
    return rate, label

def study_habit(activities, absences, failures):
    # Create universe fucntion
    activities_f = ctrl.Antecedent(np.arange(1, 3, 1), 'activities_f')
    absences_f = ctrl.Antecedent(np.arange(0, 100, 1), 'absences_f')
    failures_f = ctrl.Antecedent(np.arange(0, 4, 1), 'failures_f')
    study_habits_f = ctrl.Consequent(np.arange(0, 5, 1), 'study_habits_f')
    # Membership
    absences_f['few'] = fuzz.trimf(absences_f.universe, [0, 0, 4])
    absences_f['moderate'] = fuzz.trimf(absences_f.universe, [2, 10, 15])
    absences_f['frequent'] = fuzz.trapmf(absences_f.universe, [10, 25, 100, 100])
    activities_f['yes'] = fuzz.trimf(activities_f.universe, [1, 1, 2])
    activities_f['no'] = fuzz.trimf(activities_f.universe, [1, 2, 3])
    failures_f['low'] = fuzz.trimf(failures_f.universe, [0, 0, 2])
    failures_f['high'] = fuzz.trapmf(failures_f.universe, [1, 2, 4, 4])
    study_habits_f['low'] = fuzz.trapmf(study_habits_f.universe, [0, 0, 1, 2])
    study_habits_f['med'] = fuzz.trapmf(study_habits_f.universe, [1, 2, 3, 4])
    study_habits_f['severe'] = fuzz.trapmf(study_habits_f.universe, [3, 5, 5, 5])
    # Fuzzy rules
    rules = []
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['frequent'] & failures_f['low'], study_habits_f['med']))
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['frequent'] & failures_f['high'], study_habits_f['severe']))
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['moderate'] & failures_f['low'], study_habits_f['med']))
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['moderate'] & failures_f['high'], study_habits_f['severe']))
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['few'] & failures_f['low'], study_habits_f['low']))
    rules.append(ctrl.Rule(activities_f['no'] & absences_f['few'] & failures_f['high'], study_habits_f['severe']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['frequent'] & failures_f['low'], study_habits_f['low']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['frequent'] & failures_f['high'], study_habits_f['severe']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['moderate'] & failures_f['low'], study_habits_f['low']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['moderate'] & failures_f['high'], study_habits_f['severe']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['few'] & failures_f['low'], study_habits_f['low']))
    rules.append(ctrl.Rule(activities_f['yes'] & absences_f['few'] & failures_f['high'], study_habits_f['severe']))
    # Control
    study_habits_ctrl = ctrl.ControlSystem(rules)
    rating = ctrl.ControlSystemSimulation(study_habits_ctrl)
    rating.input['activities_f'] = activities
    rating.input['failures_f'] = failures
    rating.input['absences_f'] = absences
    # Crunch the numbers
    rating.compute()
    rate = rating.output['study_habits_f']
    if rate <= 2.49:
        label = 'mild'
    elif rate >= 2.5 and rate <= 3.49:
        label = 'moderate'
    else:
        label = 'severe'
    return rate, label
