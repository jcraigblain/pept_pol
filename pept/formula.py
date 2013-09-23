import re

class Formula:
	elements = {} #will load from config/elements.yaml during __init__.py
	
	def __init__(self, formula='C0'):
		self.formula = Formula.formula_as_dict(formula)
	
	def as_str(self):
		return Formula.formula_as_str(self.formula)
	
	def __str__(self):
		return Formula.formula_as_str(self.formula)
	
	def as_dict(self):
		return self.formula.copy()
	
	def mass(self):
		mass = 0
		for element in self.formula.keys():
			mass += Formula.elements[element]['mono'] * self.formula[element]
		return mass
	
	def add(self,formula):
		formula = Formula(formula).as_dict()
		for element in formula.keys():
			self.formula[element] += formula[element]
		return self
	
	def subtract(self,formula):
		formula = Formula(formula).as_dict()
		for element in formula.keys():
			self.formula[element] -= formula[element]
		return self
	
	def multiply(self,number):
		for element in self.formula.keys():
			self.formula[element] *= number
		return self
	
	@classmethod
	def formula_as_dict(cls, formula):
		if isinstance(formula, Formula):
			return formula.as_dict()
		elif isinstance(formula, dict):
			return formula
		elif isinstance(formula, str):
			return Formula.str_to_dict(formula)
	
	@classmethod
	def formula_as_str(cls, formula):
		if isinstance(formula, Formula):
			return formula.as_str()
		elif isinstance(formula, str):
			return formula
		elif isinstance(formula, dict):
			return Formula.dict_to_str(formula)
	
	@classmethod
	def str_to_dict(cls, formula_str):
		formula_dict = {}
		for element in Formula.elements.keys():
			formula_dict[element] = 0
		element_matches = re.findall(r'([A-Z][a-z]?)(-)?(\d*)\W*', formula_str)
		for element in element_matches:
			if element[2] == '':
				change = 1
			else:
				change = int(element[2])
			if element[1] == '-':
				formula_dict[element[0]] -= change
			else:
				formula_dict[element[0]] += change
		return formula_dict
	
	@classmethod
	def dict_to_str(cls, formula_dict):
		formula_str = ''
		for element in formula_dict.keys():
			count = formula_dict[element]
			if count == 1:
				formula_str += element
			elif count > 0:
				formula_str += element + str(count)
		return formula_str
			
		