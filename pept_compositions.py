from pept import *
import yaml

config = yaml.safe_load(open('config.yaml'))
min_len = config['min_len']
max_len = config['max_len']

residues = []
for res in config['residues']:
	residues.append(Residue(res))

derivatives = []
for der in config['derivatives']:
	derivatives.append(Derivative(der))

terminal_residues = []
if config['c_terminal_residues']:
	for res in config['c_terminal_residues']:
		terminal_residues.append(Residue(res))

if len(terminal_residues) > 0:
	min_len -= 1
	max_len -= 1

output = {}

for length in range(min_len,max_len+1):
	compositions = []
	carry_over = False
	bins = [0]*len(residues)
	while bins[-1] < length:
		bins[0] += 1
		for pos in range(len(residues)):
			if carry_over:
				bins[pos] += 1
			carry_over = False
			if bins[pos] > length:
				carry_over = True
				bins[pos] = 0
		res_count = 0
		for pos in range(len(residues)):
			res_count += bins[pos]
		if res_count == length:
			residue_dict_base = {}
			for pos in range(len(residues)):
				residue_dict_base[residues[pos]] = bins[pos]
			for der in derivatives:
				if len(terminal_residues) > 0:
					for res in terminal_residues:
						residue_dict = residue_dict_base.copy()
						residue_dict[res] = 1
						peptide = PeptComp(residue_dict,der)
				else:
					peptide = PeptComp(residue_dict_base,der)
				if peptide.mass() in output.keys():
					output[peptide.mass()]['Cpd'] += ' ' + str(peptide)
				else:
					output[peptide.mass()] = {'Cpd': str(peptide),
												'Formula': str(peptide.form()),
												'Pos': peptide.form().add('Pp').mass(),
												'Neg': peptide.form().subtract('Pp').mass()}

f = open(config['filename'],'w')
f.write('# Formula,RT,Mass,Cpd,Comments\r\n')
for mass, info in output.iteritems():
	f.write('%s,,%f,%s,%f,%f\r\n' % (info['Formula'],mass,info['Cpd'],info['Pos'],info['Neg']))
f.close()