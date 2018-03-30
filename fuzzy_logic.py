import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

class fis(object):
    def __init__(self):
        #FINANCIAL
        # Create universe fucntion
        mjob_financial = ctrl.Antecedent(np.arange(1, 4, 1), 'mjob_financial')
        fjob_financial = ctrl.Antecedent(np.arange(1, 4, 1), 'fjob_financial')
        famsize_financial = ctrl.Antecedent(np.arange(0, 5, 1), 'famsize_financial')
        financial_financial = ctrl.Consequent(np.arange(0, 5, 1), 'financial_financial')

        # Membership function for mjob
        mjob_financial['low'] = fuzz.trimf(mjob_financial.universe, [1, 1, 2])
        mjob_financial['med'] = fuzz.trimf(mjob_financial.universe, [1, 2, 3])
        mjob_financial['high'] = fuzz.trimf(mjob_financial.universe, [1, 4, 4])
        # Membership function for fjob
        fjob_financial['low'] = fuzz.trimf(fjob_financial.universe, [1, 1, 2])
        fjob_financial['med'] = fuzz.trimf(fjob_financial.universe, [1, 2, 3])
        fjob_financial['high'] = fuzz.trimf(fjob_financial.universe, [1, 4, 4])
        # Membership function for famsize
        famsize_financial['few'] = fuzz.trimf(famsize_financial.universe, [0, 1, 2])
        famsize_financial['many'] = fuzz.trimf(famsize_financial.universe, [1, 2, 3])
        # Membership function for financial
        financial_financial['low'] = fuzz.trapmf(financial_financial.universe, [0, 0, 1, 2])
        financial_financial['med'] = fuzz.trapmf(financial_financial.universe, [1, 2, 3, 4])
        financial_financial['severe'] = fuzz.trapmf(financial_financial.universe, [3, 4, 5, 5])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(mjob_financial['low'] & fjob_financial['low'] & famsize_financial['many'], financial_financial['severe']))
        rules.append(ctrl.Rule(mjob_financial['low'] & fjob_financial['med'] & famsize_financial['many'], financial_financial['severe']))
        rules.append(ctrl.Rule(mjob_financial['med'] & fjob_financial['low'] & famsize_financial['many'], financial_financial['severe']))
        rules.append(ctrl.Rule(mjob_financial['low'] & fjob_financial['med'] & famsize_financial['few'], financial_financial['med']))
        rules.append(ctrl.Rule(mjob_financial['med'] & fjob_financial['low'] & famsize_financial['few'], financial_financial['med']))
        rules.append(ctrl.Rule(mjob_financial['low'] & fjob_financial['low'] & famsize_financial['few'], financial_financial['med']))
        rules.append(ctrl.Rule(mjob_financial['high'] & famsize_financial['many'], financial_financial['med']))
        rules.append(ctrl.Rule(fjob_financial['high'] & famsize_financial['many'], financial_financial['med']))
        rules.append(ctrl.Rule(mjob_financial['high'] & famsize_financial['few'], financial_financial['low']))
        rules.append(ctrl.Rule(fjob_financial['high'] & famsize_financial['few'], financial_financial['low']))
        rules.append(ctrl.Rule(mjob_financial['high'] & fjob_financial['low'] & famsize_financial['few'], financial_financial['low']))
        rules.append(ctrl.Rule(mjob_financial['low'] & fjob_financial['high'] & famsize_financial['few'], financial_financial['low']))
        # Control
        financial_ctrl = ctrl.ControlSystem(rules)
        self.rating_financial = ctrl.ControlSystemSimulation(financial_ctrl)

        # BROKEN FAMILY
        pstatus_broken_family = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_broken_family')
        famsup_broken_family = ctrl.Antecedent(np.arange(1, 3, 1), 'famsup_broken_family')
        broken_family = ctrl.Consequent(np.arange(1, 3, 1), 'broken_family')
        # Memberships
        pstatus_broken_family['together'] = fuzz.trimf(pstatus_broken_family.universe, [1, 1, 2])
        pstatus_broken_family['apart'] = fuzz.trimf(pstatus_broken_family.universe, [1, 2, 3])
        famsup_broken_family['yes'] = fuzz.trimf(famsup_broken_family.universe, [1, 1, 2])
        famsup_broken_family['no'] = fuzz.trimf(famsup_broken_family.universe, [1, 2, 3])
        broken_family['low'] = fuzz.trimf(broken_family.universe, [1, 1, 2])
        broken_family['high'] = fuzz.trapmf(broken_family.universe, [1, 2, 3, 3])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(pstatus_broken_family['apart'] & famsup_broken_family['no'] , broken_family['high']))
        rules.append(ctrl.Rule(pstatus_broken_family['apart'] & famsup_broken_family['yes'],  broken_family['low']))
        rules.append(ctrl.Rule(pstatus_broken_family['together'] & famsup_broken_family['no'] , broken_family['high']))
        rules.append(ctrl.Rule(pstatus_broken_family['together'] & famsup_broken_family['yes'],  broken_family['low']))
        # Control
        broken_family_ctrl = ctrl.ControlSystem(rules)
        self.rating_broken_family = ctrl.ControlSystemSimulation(broken_family_ctrl)

        # LIVING WITH RELATIVES
        pstatus_relatives = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_relatives')
        famsup_relatives = ctrl.Antecedent(np.arange(1, 3, 1), 'famsup_relatives')
        living_with_rel_relatives = ctrl.Consequent(np.arange(1, 3, 1), 'living_with_rel_relatives')
        # Memberships
        pstatus_relatives['together'] = fuzz.trimf(pstatus_relatives.universe, [1, 1, 2])
        pstatus_relatives['apart'] = fuzz.trimf(pstatus_relatives.universe, [1, 2, 3])
        pstatus_relatives['together'] = fuzz.trimf(pstatus_relatives.universe, [1, 1, 2])
        pstatus_relatives['apart'] = fuzz.trimf(pstatus_relatives.universe, [1, 2, 3])
        famsup_relatives['yes'] = fuzz.trimf(famsup_relatives.universe, [1, 1, 2])
        famsup_relatives['no'] = fuzz.trimf(famsup_relatives.universe, [1, 2, 3])
        living_with_rel_relatives['low'] = fuzz.trimf(famsup_relatives.universe, [1, 1, 2])
        living_with_rel_relatives['high'] = fuzz.trapmf(living_with_rel_relatives.universe, [1, 2, 3, 3])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(pstatus_relatives['apart'] & famsup_relatives['no'] , living_with_rel_relatives['high']))
        rules.append(ctrl.Rule(pstatus_relatives['apart'] & famsup_relatives['yes'],  living_with_rel_relatives['low']))
        rules.append(ctrl.Rule(pstatus_relatives['together'] & famsup_relatives['no'] , living_with_rel_relatives['high']))
        rules.append(ctrl.Rule(pstatus_relatives['together'] & famsup_relatives['yes'],  living_with_rel_relatives['low']))
        # Control
        relatives_ctrl = ctrl.ControlSystem(rules)
        self.rating_relatives = ctrl.ControlSystemSimulation(relatives_ctrl)

        # HEALTH CONDITION
        # Create universe fucntion
        health_health = ctrl.Antecedent(np.arange(1, 5, 1), 'health_health')
        activities_health = ctrl.Antecedent(np.arange(1, 3, 1), 'activities_health')
        absences_health = ctrl.Antecedent(np.arange(0, 100, 1), 'absences_health')
        health_conditions_health = ctrl.Consequent(np.arange(1, 5, 1), 'health_conditions_health')
        # Membership
        health_health['good'] = fuzz.trimf(health_health.universe, [3, 5, 5])
        health_health['neutral'] = fuzz.trimf(health_health.universe, [2, 3, 4])
        health_health['bad'] = fuzz.trimf(health_health.universe, [1, 1, 3])
        activities_health['yes'] = fuzz.trimf(activities_health.universe, [1, 1, 2])
        activities_health['no'] = fuzz.trimf(activities_health.universe, [1, 2, 3])
        absences_health['few'] = fuzz.trimf(absences_health.universe, [0, 0, 4])
        absences_health['moderate'] = fuzz.trimf(absences_health.universe, [2, 10, 15])
        absences_health['frequent'] = fuzz.trapmf(absences_health.universe, [10, 25, 100, 100])
        health_conditions_health['low'] = fuzz.trimf(health_conditions_health.universe, [1, 1, 3])
        health_conditions_health['med'] = fuzz.trimf(health_conditions_health.universe, [2, 3, 4])
        health_conditions_health['severe'] = fuzz.trimf(health_conditions_health.universe, [3, 5, 5])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(health_health['bad'] & (absences_health['moderate'] | absences_health['frequent']) & (activities_health['yes'] | activities_health['no']), health_conditions_health['severe']))
        rules.append(ctrl.Rule(health_health['bad'] & absences_health['few'] & (activities_health['yes'] | activities_health['no']), health_conditions_health['severe']))
        rules.append(ctrl.Rule(health_health['neutral'] & (absences_health['moderate'] | absences_health['frequent']) & activities_health['yes'], health_conditions_health['severe']))
        rules.append(ctrl.Rule(health_health['neutral'] & absences_health['few'], health_conditions_health['low']))
        rules.append(ctrl.Rule(health_health['neutral'] & absences_health['moderate'], health_conditions_health['med']))
        rules.append(ctrl.Rule(health_health['neutral'] & absences_health['frequent'], health_conditions_health['med']))
        rules.append(ctrl.Rule(health_health['good'] & (activities_health['yes'] | activities_health['no']) & (absences_health['moderate'] | absences_health['frequent']), health_conditions_health['low']))
        rules.append(ctrl.Rule(health_health['good'] & (activities_health['yes'] | activities_health['no']) & absences_health['few'], health_conditions_health['low']))
        # Control
        health_condition_ctrl = ctrl.ControlSystem(rules)
        self.rating_health = ctrl.ControlSystemSimulation(health_condition_ctrl)

        #LEARNING MATERIALS
        # Create universe fucntion
        internet_materials = ctrl.Antecedent(np.arange(1, 3, 1), 'internet_materials')
        mjob_materials = ctrl.Antecedent(np.arange(1, 4, 1), 'mjob_materials')
        fjob_materials = ctrl.Antecedent(np.arange(1, 4, 1), 'fjob_materials')
        learning_materials_materials = ctrl.Consequent(np.arange(0, 5, 1), 'learning_materials_materials')
        # Membership
        internet_materials['yes'] = fuzz.trimf(internet_materials.universe, [1, 1, 2])
        internet_materials['no'] = fuzz.trimf(internet_materials.universe, [1, 2, 3])
        mjob_materials['low'] = fuzz.trimf(mjob_materials.universe, [1, 1, 2])
        mjob_materials['med'] = fuzz.trapmf(mjob_materials.universe, [1, 2, 3, 4])
        mjob_materials['high'] = fuzz.trapmf(mjob_materials.universe, [1, 3, 4, 4])
        fjob_materials['low'] = fuzz.trimf(fjob_materials.universe, [1, 1, 2])
        fjob_materials['med'] = fuzz.trapmf(fjob_materials.universe, [1, 2, 3, 4])
        fjob_materials['high'] = fuzz.trapmf(fjob_materials.universe, [1, 3, 4, 4])
        learning_materials_materials['low'] = fuzz.trapmf(learning_materials_materials.universe, [0, 0, 1, 2])
        learning_materials_materials['med'] = fuzz.trapmf(learning_materials_materials.universe, [1, 2, 3, 4])
        learning_materials_materials['severe'] = fuzz.trapmf(learning_materials_materials.universe, [3, 5, 5, 5])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(internet_materials['yes'] & (mjob_materials['low'] | mjob_materials['med'] | mjob_materials['high']) & (fjob_materials['low'] | fjob_materials['med'] | fjob_materials['high']), learning_materials_materials['low']))
        rules.append(ctrl.Rule(internet_materials['no'] & mjob_materials['low'] & fjob_materials['low'], learning_materials_materials['severe']))
        rules.append(ctrl.Rule(internet_materials['no'] & mjob_materials['med'] & fjob_materials['low'], learning_materials_materials['severe']))
        rules.append(ctrl.Rule(internet_materials['no'] & mjob_materials['low'] & fjob_materials['med'], learning_materials_materials['severe']))
        rules.append(ctrl.Rule(internet_materials['no'] & mjob_materials['med'] & fjob_materials['med'], learning_materials_materials['med']))
        rules.append(ctrl.Rule(internet_materials['no'] & (mjob_materials['high'] | fjob_materials['high']), learning_materials_materials['med']))
        # Control
        learning_materials_ctrl = ctrl.ControlSystem(rules)
        self.rating_material = ctrl.ControlSystemSimulation(learning_materials_ctrl)

        # PARENTING ISSUES
        # Create universe fucntion
        pstatus_parent = ctrl.Antecedent(np.arange(1, 3, 1), 'pstatus_parent')
        medu_parent = ctrl.Antecedent(np.arange(0, 4, 1), 'medu_parent')
        fedu_parent = ctrl.Antecedent(np.arange(0, 4, 1), 'fedu_parent')
        parenting_issues_parent = ctrl.Consequent(np.arange(1, 4, 1), 'parenting_issues_parent')
        # Membership
        medu_parent['low'] = fuzz.trapmf(medu_parent.universe, [0, 0, 1, 3])
        medu_parent['med'] = fuzz.trimf(medu_parent.universe, [1, 2, 4])
        medu_parent['high'] = fuzz.trimf(medu_parent.universe, [3, 4, 4])
        fedu_parent['low'] = fuzz.trapmf(fedu_parent.universe, [0, 0, 1, 3])
        fedu_parent['med'] = fuzz.trimf(fedu_parent.universe, [1, 2, 4])
        fedu_parent['high'] = fuzz.trimf(fedu_parent.universe, [3, 4, 4])
        pstatus_parent['together'] = fuzz.trimf(pstatus_parent.universe, [1, 1, 2])
        pstatus_parent['apart'] = fuzz.trimf(pstatus_parent.universe, [1, 2, 3])
        parenting_issues_parent['low'] = fuzz.trimf(parenting_issues_parent.universe, [1, 1, 2])
        parenting_issues_parent['med'] = fuzz.trimf(parenting_issues_parent.universe, [1, 2, 3])
        parenting_issues_parent['severe'] = fuzz.trimf(parenting_issues_parent.universe, [2, 3, 4])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['high'] & fedu_parent['low'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['high'] & fedu_parent['med'], parenting_issues_parent['med']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['high'] & fedu_parent['high'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['med'] & fedu_parent['low'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['med'] & fedu_parent['med'], parenting_issues_parent['med']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['med'] & fedu_parent['high'], parenting_issues_parent['med']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['low'] & fedu_parent['low'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['low'] & fedu_parent['med'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['apart'] & medu_parent['low'] & fedu_parent['high'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['high'] & fedu_parent['low'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['high'] & fedu_parent['med'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['high'] & fedu_parent['high'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['med'] & fedu_parent['low'], parenting_issues_parent['med']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['med'] & fedu_parent['med'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['med'] & fedu_parent['high'], parenting_issues_parent['low']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['low'] & fedu_parent['low'], parenting_issues_parent['severe']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['low'] & fedu_parent['med'], parenting_issues_parent['med']))
        rules.append(ctrl.Rule( pstatus_parent['together'] & medu_parent['low'] & fedu_parent['high'], parenting_issues_parent['low']))
        # Control
        parenting_issues_ctrl = ctrl.ControlSystem(rules)
        self.rating_parent = ctrl.ControlSystemSimulation(parenting_issues_ctrl)

        # STUDY HABIT
        # Create universe fucntion
        activities_study = ctrl.Antecedent(np.arange(1, 3, 1), 'activities_study')
        absences_study = ctrl.Antecedent(np.arange(0, 100, 1), 'absences_study')
        failures_study = ctrl.Antecedent(np.arange(0, 4, 1), 'failures_study')
        study_habits_study = ctrl.Consequent(np.arange(0, 5, 1), 'study_habits_study')
        # Membership
        absences_study['few'] = fuzz.trimf(absences_study.universe, [0, 0, 4])
        absences_study['moderate'] = fuzz.trimf(absences_study.universe, [2, 10, 15])
        absences_study['frequent'] = fuzz.trapmf(absences_study.universe, [10, 25, 100, 100])
        activities_study['yes'] = fuzz.trimf(activities_study.universe, [1, 1, 2])
        activities_study['no'] = fuzz.trimf(activities_study.universe, [1, 2, 3])
        failures_study['low'] = fuzz.trimf(failures_study.universe, [0, 0, 2])
        failures_study['high'] = fuzz.trapmf(failures_study.universe, [1, 2, 4, 4])
        study_habits_study['low'] = fuzz.trapmf(study_habits_study.universe, [0, 0, 1, 2])
        study_habits_study['med'] = fuzz.trapmf(study_habits_study.universe, [1, 2, 3, 4])
        study_habits_study['severe'] = fuzz.trapmf(study_habits_study.universe, [3, 5, 5, 5])
        # Fuzzy rules
        rules = []
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['frequent'] & failures_study['low'], study_habits_study['med']))
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['frequent'] & failures_study['high'], study_habits_study['severe']))
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['moderate'] & failures_study['low'], study_habits_study['med']))
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['moderate'] & failures_study['high'], study_habits_study['severe']))
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['few'] & failures_study['low'], study_habits_study['low']))
        rules.append(ctrl.Rule(activities_study['no'] & absences_study['few'] & failures_study['high'], study_habits_study['severe']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['frequent'] & failures_study['low'], study_habits_study['low']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['frequent'] & failures_study['high'], study_habits_study['severe']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['moderate'] & failures_study['low'], study_habits_study['low']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['moderate'] & failures_study['high'], study_habits_study['severe']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['few'] & failures_study['low'], study_habits_study['low']))
        rules.append(ctrl.Rule(activities_study['yes'] & absences_study['few'] & failures_study['high'], study_habits_study['severe']))
        # Control
        study_habits_ctrl = ctrl.ControlSystem(rules)
        self.rating_study = ctrl.ControlSystemSimulation(study_habits_ctrl)

    def financial_fuzzy(self, famsize, mjob, fjob):
        self.rating_financial.input['mjob_financial'] = mjob
        self.rating_financial.input['fjob_financial'] = fjob
        self.rating_financial.input['famsize_financial'] = famsize
        # Crunch the numbers
        self.rating_financial.compute()
        rate = self.rating_financial.output['financial_financial']
        if rate <= 2.49:
            label = 'mild'
        elif rate >= 2.5 and rate <= 3.49:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def broken_family(self, pstatus, famsup):
        self.rating_broken_family.input['pstatus_broken_family'] = pstatus
        self.rating_broken_family.input['famsup_broken_family'] = famsup
        # Crunch the numbers
        self.rating_broken_family.compute()
        rate = self.rating_broken_family.output['broken_family']
        if rate <= 1.49:
            label = 'mild'
        else:
            label = 'severe'
        return rate, label

    def living_with_rel(self, pstatus, famsup):

        self.rating_relatives.input['pstatus_relatives'] = pstatus
        self.rating_relatives.input['famsup_relatives'] = famsup
        # Crunch the numbers
        self.rating_relatives.compute()
        rate = self.rating_relatives.output['living_with_rel_relatives']
        if rate <= 1.49:
            label = 'mild'
        else:
            label = 'severe'
        return rate, label

    def health_conditions(self, health, activities, absences):

        self.rating_health.input['health_health'] = health
        self.rating_health.input['activities_health'] = activities
        self.rating_health.input['absences_health'] = absences
        # Crunch the 10umbers
        self.rating_health.compute()
        rate = self.rating_health.output['health_conditions_health']
        if rate <= 2.49:
            label = 'mild'
        elif rate >= 2.5 and rate <= 3.49:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def insufficient_learning_materials(self, internet, mjob, fjob):

        self.rating_material.input['internet_materials'] = internet
        self.rating_material.input['mjob_materials'] = mjob
        self.rating_material.input['fjob_materials'] = fjob
        # Crunch the numbers
        self.rating_material.compute()
        rate = self.rating_material.output['learning_materials_materials']
        if rate <= 2.49:
            label = 'mild'
        elif rate >= 2.5 and rate <= 3.49:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def parenting_issues(self, pstatus, medu, fedu):

        self.rating_parent.input['pstatus_parent'] = pstatus
        self.rating_parent.input['medu_parent'] = medu
        self.rating_parent.input['fedu_parent'] = fedu
        # Crunch the numbers
        self.rating_parent.compute()
        rate = self.rating_parent.output['parenting_issues_parent']
        if rate <= 1.49:
            label = 'mild'
        elif rate >= 1.5 and rate <= 2.49:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label

    def study_habit(self, activities, absences, failures):
        self.rating_study.input['activities_study'] = activities
        self.rating_study.input['failures_study'] = failures
        self.rating_study.input['absences_study'] = absences
        # Crunch the numbers
        self.rating_study.compute()
        rate = self.rating_study.output['study_habits_study']
        if rate <= 2.49:
            label = 'mild'
        elif rate >= 2.5 and rate <= 3.49:
            label = 'moderate'
        else:
            label = 'severe'
        return rate, label
