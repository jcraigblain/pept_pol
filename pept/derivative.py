from formula import Formula

class Derivative:
	derivatives = {} #will load from config/derivatives.yaml during __init__.py
	
	def __init__(self, code):
		self.code = code
		self.formula = Formula(Derivative.derivatives[code]['formula'])
	
	def form(self):
		return Formula(self.formula)
	
	def name(self):
		return Derivative.derivatives[self.code]['name']
		
	def code(self):
		return self.code
	
	def __str__(self):
		return self.code
	
	def mass(self):
		return self.formula.mass()
		