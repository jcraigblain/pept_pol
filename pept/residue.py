from formula import Formula

class Residue:
	resdiues = {} #will load from config/residues.yaml during __init__.py
	
	def __init__(self, code):
		self.residue = code
		formula = Formula(Residue.residues[code]['formula'])
		formula.add('C2H2NO')
		self.formula = formula
	
	def form(self):
		return Formula(self.formula)
	
	def __str__(self):
		return self.residue
	
	def name(self):
		return Residue.residues[self.residue]['name']
	
	def letter(self):
		return Residue.residues[self.residue]['code']
	
	def mass(self):
		return self.formula.mass()