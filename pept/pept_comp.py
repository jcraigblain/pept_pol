from residue import Residue
from derivative import Derivative
from formula import Formula

class PeptComp:
	
	def __init__(self, residue_dict, derivative):
		self.residue_dict = residue_dict
		self.derivative = derivative
		formula = Formula(derivative.form())
		for residue, count in residue_dict.iteritems():
			formula.add(residue.form().multiply(count))
		self.formula = formula
	
	def form(self):
		return Formula(self.formula)
	
	def form_str(self):
		return self.formula.as_str()
	
	def mass(self):
		return self.formula.mass()
	
	def __str__(self):
		name = str(self.derivative) + '-'
		for residue, count in self.residue_dict.iteritems():
			if count > 0:
				name += residue.letter() + str(count)
		return name