from residue import Residue
from formula import Formula
from derivative import Derivative
from pept_comp import PeptComp

__all__ = ['Formula', 'Residue', 'Derivative', 'PeptComp']

import yaml

Residue.residues = yaml.safe_load(open('pept/config/residues.yaml'))
Formula.elements = yaml.safe_load(open('pept/config/elements.yaml'))
Derivative.derivatives = yaml.safe_load(open('pept/config/derivatives.yaml'))