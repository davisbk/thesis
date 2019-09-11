# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:36:51 2019

@author: Brian Davis
"""

import pandas as pd
import matplotlib.pyplot as plt

INPUT_ROOT_DIR = "C://Users//Brian Davis//Dropbox//Freiburg Masters Semesters//Thesis//Results//"
OUTPUT_ROOT_DIR = INPUT_ROOT_DIR + "Graphics//"

############ READ IN THE DATA ############
print("Reading in data...")
############ READ IN THE DATA FROM stat_bp_best.out FOR THE DIFFERENT CONDITIONS ############
print("from \"stat_bp_best.out\" for all conditions...")
# control condition
bp_best_names = ['generation', 'num_bp_not_in_any_CDS', 'num_bp_not_in_any_functional_CDS', 'num_bp_not_in_any_non-functional_CDS', 'num_bp_not_included_in_any_RNA', 'num_bp_not_included_in_any_coding_RNA', 'num_bp_not_included_in_any_non-coding_RNA', 'num_of_non-essential_bp', 'num_of_non-essential_bp_including_non-functional_genes']
df_seed01_control_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_control_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_control_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_control_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_control_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# population up condition
df_seed01_population_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_population_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_population_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_population_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_population_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# population down condition
df_seed01_population_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_population_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_population_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_population_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_population_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# selection up condition
df_seed01_selection_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_selection_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_selection_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_selection_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_selection_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# selection down condition
df_seed01_selection_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_selection_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_selection_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_selection_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_selection_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# mutation up condition
df_seed01_mutation_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_mutation_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_mutation_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_mutation_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_mutation_up_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_up//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

# mutation down condition
df_seed01_mutation_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed02_mutation_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed03_mutation_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed04_mutation_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)
df_seed05_mutation_down_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_down//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0,names=bp_best_names)

print("done.")


############ READ IN THE DATA FROM stat_fitness_best.out FOR THE DIFFERENT CONDITIONS ############
print("from \"stat_fitness_best.out\" for all conditions...")
# control condition
fitness_best_names = ['generation', 'pop_size', 'fitness', 'genome_size', 'metabolic_error','parents_metabolic_error', 'metabolic_fitness', 'secretion_error', 'parents_secretion_error', 'secretion_fitness', 'amt_compound_present']
df_seed01_control_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//control//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_control_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//control//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_control_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//control//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_control_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//control//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_control_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//control//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)


# population up condition
df_seed01_pop_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_pop_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_pop_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_pop_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_pop_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)

# population down condition
df_seed01_pop_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_pop_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_pop_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_pop_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_pop_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)

# selection up condition
df_seed01_selection_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_selection_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_selection_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_selection_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_selection_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)

# selection down condition
df_seed01_selection_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_selection_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_selection_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_selection_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_selection_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)

# mutation up condition
df_seed01_mutation_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_mutation_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_mutation_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_mutation_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_mutation_up_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_up//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
  
# mutation down condition
df_seed01_mutation_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed02_mutation_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed03_mutation_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed04_mutation_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)
df_seed05_mutation_down_fitness_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_down//stats//stat_fitness_best.out", skiprows=18, delim_whitespace=True, header=0,names=fitness_best_names)

print("done.")

############ READ IN THE DATA FROM stat_genes_best.out FOR THE DIFFERENT CONDITIONS ############
print("from \"stat_genes_best.out\" for all conditions...")

# Control condition
genes_best_names = ['generation', 'num_coding_RNAs', 'num_non-coding_RNAs', 'avg_size_of_coding_RNAs', 'avg_size_of_non-coding_RNAs', 'num_functional_genes', 'num_non-functional_genes', 'avg_size_of_functional_genes', 'avg_size_of_non-functional_genes']
df_seed01_control_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//control//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_control_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//control//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_control_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//control//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_control_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//control//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_control_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//control//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# population up condition
df_seed01_pop_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_pop_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_pop_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_pop_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_pop_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# population down condition
df_seed01_pop_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_pop_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//pop_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_pop_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//pop_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_pop_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//pop_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_pop_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//pop_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# selection up condition
df_seed01_selection_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_selection_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_selection_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_selection_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_selection_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# selection down condition
df_seed01_selection_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_selection_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//selection_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_selection_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//selection_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_selection_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//selection_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_selection_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//selection_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# mutation up condition
df_seed01_mutation_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_mutation_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_mutation_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_mutation_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_mutation_up_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_up//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)

# mutation down condition
df_seed01_mutation_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed02_mutation_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//mut_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed03_mutation_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//mut_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed04_mutation_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//mut_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)
df_seed05_mutation_down_genes_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//mut_down//stats//stat_genes_best.out", skiprows=14, delim_whitespace=True, header=0, names=genes_best_names)



########### GRAPHING ###########
print("Graphing results...")

#### METABOLIC ERROR ####
print("metabolic error")
## CONTROL CONDITION ##

# Plot all five seeds to one plot
ax_control_metabolic_error_best = df_seed01_control_fitness_best.plot(x='generation', y='metabolic_error',label='seed 1', figsize=(30, 20))
df_seed02_control_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_control_metabolic_error_best)
df_seed03_control_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_control_metabolic_error_best)
df_seed04_control_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_control_metabolic_error_best)
df_seed05_control_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_control_metabolic_error_best)

# Label the figure
ax_control_metabolic_error_best.set_title("Metabolic Error - Control Condition", fontsize=32)
ax_control_metabolic_error_best.set_xlabel("Generation", fontsize=20)
ax_control_metabolic_error_best.set_ylabel("Error", fontsize=20)

# Save the figure
fig_control_metabolic_error = ax_control_metabolic_error_best.get_figure()
fig_control_metabolic_error.savefig(OUTPUT_ROOT_DIR + "metabolic_error_control.png")
plt.close(fig_control_metabolic_error)

### REMAINING CONDITIONS ###

# Create a shared figure for the remaining conditions
fig_metabolic_error_best, ax_metabolic_error_best = plt.subplots(nrows=2, ncols=3, figsize=(30, 20), sharex=True, sharey=True) # to have them share an x axis, pass sharex=True to plt.subplots()
fig_metabolic_error_best.suptitle("Metabolic Error", fontsize=48) # Title of graph
fig_metabolic_error_best.text(0.5, 0.04, 'Generation', ha='center', fontsize=32) # Common x label
fig_metabolic_error_best.text(0.04, 0.5, 'Error', va='center', rotation='vertical', fontsize=32) # Common y label

## POPULATION UP ##

# Plot all five seeds to one subplot
df_seed01_pop_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[0,0]) # upper left
df_seed02_pop_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[0,0])
df_seed03_pop_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[0,0])
df_seed04_pop_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[0,0])
df_seed05_pop_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[0,0])

ax_metabolic_error_best[0,0].set_title('population up', fontsize=20)


## POPULATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_pop_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[1,0]) # lower left
df_seed02_pop_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[1,0])
df_seed03_pop_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[1,0])
df_seed04_pop_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[1,0])
df_seed05_pop_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[1,0])

ax_metabolic_error_best[1,0].set_title('population down', fontsize=20)

## SELECTION UP ##

# Plot all five seeds to one subplot
df_seed01_selection_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[0,1]) # top center
df_seed02_selection_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[0,1])
df_seed03_selection_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[0,1])
df_seed04_selection_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[0,1])
df_seed05_selection_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[0,1])

ax_metabolic_error_best[0,1].set_title('selection up', fontsize=20)

## SELECTION DOWN ##

# Plot all five seeds to one subplot
df_seed01_selection_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[1,1]) # bottom center
df_seed02_selection_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[1,1])
df_seed03_selection_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[1,1])
df_seed04_selection_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[1,1])
df_seed05_selection_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[1,1])

ax_metabolic_error_best[1,1].set_title('selection down', fontsize=20)

## MUTATION UP ##

# Plot all five seeds to one subplot
df_seed01_mutation_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[0,2]) # top right
df_seed02_mutation_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[0,2])
df_seed03_mutation_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[0,2])
df_seed04_mutation_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[0,2])
df_seed05_mutation_up_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[0,2])

ax_metabolic_error_best[0,2].set_title('mutation up', fontsize=20)


## MUTATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_mutation_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 1', ax=ax_metabolic_error_best[1,2]) # bottom right
df_seed02_mutation_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 2', ax=ax_metabolic_error_best[1,2])
df_seed03_mutation_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 3', ax=ax_metabolic_error_best[1,2])
df_seed04_mutation_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 4', ax=ax_metabolic_error_best[1,2])
df_seed05_mutation_down_fitness_best.plot(x='generation', y='metabolic_error', label='seed 5', ax=ax_metabolic_error_best[1,2])

ax_metabolic_error_best[1,2].set_title('mutation down', fontsize=20)

# Save the final figure
fig_metabolic_error_best.savefig(OUTPUT_ROOT_DIR + "metabolic_error_conditions.png")

plt.close(fig_metabolic_error_best)




#### GENOME SIZE ####
print("genome size")
## CONTROL CONDITION ##

# For the control condition, plot all five seeds to one plot
fig_control_genome_size_best = plt.figure(figsize=(30,20))
ax_control_genome_size_best = fig_control_genome_size_best.add_subplot(111)
ax_control_genome_size_best.set_title("Genome Size - Control Condition", fontsize=32)
ax_control_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_control_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

df_seed01_control_fitness_best.plot(x='generation', y='genome_size',label='seed 1', ax=ax_control_genome_size_best)
df_seed02_control_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_control_genome_size_best)
df_seed03_control_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_control_genome_size_best)
df_seed04_control_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_control_genome_size_best)
df_seed05_control_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_control_genome_size_best)

# Save the figure
fig_control_genome_size_best.savefig(OUTPUT_ROOT_DIR + "genome_size_control.png")
plt.close(fig_control_genome_size_best)

plt.close(fig_control_genome_size_best)

### GENOME SIZE - CONDITIONS ### 

# Create new figure with subplots for the other conditions 
fig_genome_size_best, ax_genome_size_best = plt.subplots(nrows=2, ncols=3, figsize=(30, 20), sharex=True, sharey=True) # to have them share an x axis, pass sharex=True to plt.subplots()
fig_genome_size_best.suptitle("Genome Size", fontsize=48) # Title of graph
fig_genome_size_best.text(0.5, 0.04, 'Generation', ha='center', fontsize=32) # Common x label
fig_genome_size_best.text(0.04, 0.5, 'Num Base Pairs', va='center', rotation='vertical', fontsize=32) # Common y label

## POPULATION UP ##

# Plot all five seeds to one subplot
df_seed01_pop_up_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[0,0]) # upper left
df_seed02_pop_up_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[0,0])
df_seed03_pop_up_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[0,0])
df_seed04_pop_up_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[0,0])
df_seed05_pop_up_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[0,0])

ax_genome_size_best[0,0].set_title('population up', fontsize=20)



## POPULATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_pop_down_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[1,0]) # bottom left
df_seed02_pop_down_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[1,0])
df_seed03_pop_down_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[1,0])
df_seed04_pop_down_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[1,0])
df_seed05_pop_down_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[1,0])

ax_genome_size_best[1,0].set_title('population down', fontsize=20)

## SELECTION UP ##

# Plot all five seeds to one subplot
df_seed01_selection_up_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[0,1]) # top center
df_seed02_selection_up_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[0,1])
df_seed03_selection_up_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[0,1])
df_seed04_selection_up_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[0,1])
df_seed05_selection_up_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[0,1])

ax_genome_size_best[0,1].set_title('selection up', fontsize=20)

## SELECTION DOWN ##

# Plot all five seeds to one subplot
df_seed01_selection_down_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[1,1]) # bottom center
df_seed02_selection_down_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[1,1])
df_seed03_selection_down_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[1,1])
df_seed04_selection_down_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[1,1])
df_seed05_selection_down_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[1,1])

ax_genome_size_best[1,1].set_title('selection down', fontsize=20)

## MUTATION UP ##

# Plot all five seeds to one subplot
df_seed01_mutation_up_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[0,2]) # top right
df_seed02_mutation_up_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[0,2])
df_seed03_mutation_up_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[0,2])
df_seed04_mutation_up_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[0,2])
df_seed05_mutation_up_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[0,2])

ax_genome_size_best[0,2].set_title('mutation up', fontsize=20)


## MUTATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_mutation_down_fitness_best.plot(x='generation', y='genome_size', label='seed 1', ax=ax_genome_size_best[1,2]) # bottom right
df_seed02_mutation_down_fitness_best.plot(x='generation', y='genome_size', label='seed 2', ax=ax_genome_size_best[1,2])
df_seed03_mutation_down_fitness_best.plot(x='generation', y='genome_size', label='seed 3', ax=ax_genome_size_best[1,2])
df_seed04_mutation_down_fitness_best.plot(x='generation', y='genome_size', label='seed 4', ax=ax_genome_size_best[1,2])
df_seed05_mutation_down_fitness_best.plot(x='generation', y='genome_size', label='seed 5', ax=ax_genome_size_best[1,2])

ax_genome_size_best[1,2].set_title('mutation down', fontsize=20)

# Save the final figure and close it
fig_genome_size_best.savefig(OUTPUT_ROOT_DIR + "genome_size_conditions.png")
plt.close(fig_genome_size_best)

#### NUMBER OF CODING SEQUENCES ####
print("number of coding sequences (CDSs)")
# For the control condition, plot all five seeds to one plot
fig_control_num_CDS_best = plt.figure(figsize=(30,20))
ax_control_num_CDS_best = fig_control_num_CDS_best.add_subplot(111)
ax_control_num_CDS_best.set_title("Number of Coding Sequences - Control Condition", fontsize=32)
ax_control_num_CDS_best.set_xlabel("Generation", fontsize=20)
ax_control_num_CDS_best.set_ylabel("Num of CDSs", fontsize=20)

# The number of coding sequences is the number of functional genes plus the number
# of non-functional genes. This data is in stat_genes_best.out.

# Create a new DataFrame with the generation data
df_seed01_control_num_CDS = pd.DataFrame(df_seed01_control_genes_best['generation'])
df_seed02_control_num_CDS = pd.DataFrame(df_seed02_control_genes_best['generation'])
df_seed03_control_num_CDS = pd.DataFrame(df_seed03_control_genes_best['generation'])
df_seed04_control_num_CDS = pd.DataFrame(df_seed04_control_genes_best['generation'])
df_seed05_control_num_CDS = pd.DataFrame(df_seed05_control_genes_best['generation'])

# Append a new column with the necessarily calculation (num functional + num non-functional genes)
df_seed01_control_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_control_genes_best['num_functional_genes'] + df_seed01_control_genes_best['num_non-functional_genes'])
df_seed02_control_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_control_genes_best['num_functional_genes'] + df_seed02_control_genes_best['num_non-functional_genes'])
df_seed03_control_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_control_genes_best['num_functional_genes'] + df_seed03_control_genes_best['num_non-functional_genes'])
df_seed04_control_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_control_genes_best['num_functional_genes'] + df_seed04_control_genes_best['num_non-functional_genes'])
df_seed05_control_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_control_genes_best['num_functional_genes'] + df_seed05_control_genes_best['num_non-functional_genes'])

# Now plot the results to one plot
df_seed01_control_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_control_num_CDS_best)
df_seed02_control_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_control_num_CDS_best)
df_seed03_control_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_control_num_CDS_best)
df_seed04_control_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_control_num_CDS_best)
df_seed05_control_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_control_num_CDS_best)

# Save and close the figure
fig_control_num_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_CDS_control.png")
plt.close(fig_control_num_CDS_best)

### NUMBER OF CODING SEQUENCES - CONDITIONS ###

# Create new figure with subplots for the other conditions 
fig_num_CDS_best, ax_num_CDS_best = plt.subplots(nrows=2, ncols=3, figsize=(30, 20), sharex=True, sharey=True) # to have them share an x axis, pass sharex=True to plt.subplots()
fig_num_CDS_best.suptitle("Number of Coding Sequences", fontsize=48) # Title of graph
fig_num_CDS_best.text(0.5, 0.04, 'Generation', ha='center', fontsize=32) # Common x label
fig_num_CDS_best.text(0.04, 0.5, 'Num CDS', va='center', rotation='vertical', fontsize=32) # Common y label

## POPULATION UP ##

# Create new DataFrames with the generation numbers
df_seed01_population_up_num_CDS = pd.DataFrame(df_seed01_pop_up_genes_best['generation'])
df_seed02_population_up_num_CDS = pd.DataFrame(df_seed02_pop_up_genes_best['generation'])
df_seed03_population_up_num_CDS = pd.DataFrame(df_seed03_pop_up_genes_best['generation'])
df_seed04_population_up_num_CDS = pd.DataFrame(df_seed04_pop_up_genes_best['generation'])
df_seed05_population_up_num_CDS = pd.DataFrame(df_seed05_pop_up_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_population_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_pop_up_genes_best['num_functional_genes'] + df_seed01_pop_up_genes_best['num_non-functional_genes'])
df_seed02_population_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_pop_up_genes_best['num_functional_genes'] + df_seed02_pop_up_genes_best['num_non-functional_genes'])
df_seed03_population_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_pop_up_genes_best['num_functional_genes'] + df_seed03_pop_up_genes_best['num_non-functional_genes'])
df_seed04_population_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_pop_up_genes_best['num_functional_genes'] + df_seed04_pop_up_genes_best['num_non-functional_genes'])
df_seed05_population_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_pop_up_genes_best['num_functional_genes'] + df_seed05_pop_up_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_population_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[0,0]) # top left
df_seed02_population_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[0,0])
df_seed03_population_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[0,0])
df_seed04_population_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[0,0])
df_seed05_population_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[0,0])

ax_num_CDS_best[0,0].set_title("population up", fontsize=20)

## POPULATION DOWN ##

# Create new DataFrames with the generation numbers
df_seed01_population_down_num_CDS = pd.DataFrame(df_seed01_pop_down_genes_best['generation'])
df_seed02_population_down_num_CDS = pd.DataFrame(df_seed02_pop_down_genes_best['generation'])
df_seed03_population_down_num_CDS = pd.DataFrame(df_seed03_pop_down_genes_best['generation'])
df_seed04_population_down_num_CDS = pd.DataFrame(df_seed04_pop_down_genes_best['generation'])
df_seed05_population_down_num_CDS = pd.DataFrame(df_seed05_pop_down_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_population_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_pop_down_genes_best['num_functional_genes'] + df_seed01_pop_down_genes_best['num_non-functional_genes'])
df_seed02_population_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_pop_down_genes_best['num_functional_genes'] + df_seed02_pop_down_genes_best['num_non-functional_genes'])
df_seed03_population_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_pop_down_genes_best['num_functional_genes'] + df_seed03_pop_down_genes_best['num_non-functional_genes'])
df_seed04_population_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_pop_down_genes_best['num_functional_genes'] + df_seed04_pop_down_genes_best['num_non-functional_genes'])
df_seed05_population_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_pop_down_genes_best['num_functional_genes'] + df_seed05_pop_down_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_population_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[1,0]) # bottom left
df_seed02_population_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[1,0])
df_seed03_population_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[1,0])
df_seed04_population_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[1,0])
df_seed05_population_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[1,0])

ax_num_CDS_best[1,0].set_title("population down", fontsize=20)

## SELECTION UP ##

# Create new DataFrames with the generation numbers
df_seed01_selection_up_num_CDS = pd.DataFrame(df_seed01_selection_up_genes_best['generation'])
df_seed02_selection_up_num_CDS = pd.DataFrame(df_seed02_selection_up_genes_best['generation'])
df_seed03_selection_up_num_CDS = pd.DataFrame(df_seed03_selection_up_genes_best['generation'])
df_seed04_selection_up_num_CDS = pd.DataFrame(df_seed04_selection_up_genes_best['generation'])
df_seed05_selection_up_num_CDS = pd.DataFrame(df_seed05_selection_up_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_selection_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_selection_up_genes_best['num_functional_genes'] + df_seed01_selection_up_genes_best['num_non-functional_genes'])
df_seed02_selection_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_selection_up_genes_best['num_functional_genes'] + df_seed02_selection_up_genes_best['num_non-functional_genes'])
df_seed03_selection_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_selection_up_genes_best['num_functional_genes'] + df_seed03_selection_up_genes_best['num_non-functional_genes'])
df_seed04_selection_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_selection_up_genes_best['num_functional_genes'] + df_seed04_selection_up_genes_best['num_non-functional_genes'])
df_seed05_selection_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_selection_up_genes_best['num_functional_genes'] + df_seed05_selection_up_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_selection_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[0,1]) # top middle
df_seed02_selection_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[0,1])
df_seed03_selection_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[0,1])
df_seed04_selection_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[0,1])
df_seed05_selection_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[0,1])

ax_num_CDS_best[0,1].set_title("selection up", fontsize=20)

## SELECTION DOWN ##

# Create new DataFrames with the generation numbers
df_seed01_selection_down_num_CDS = pd.DataFrame(df_seed01_selection_down_genes_best['generation'])
df_seed02_selection_down_num_CDS = pd.DataFrame(df_seed02_selection_down_genes_best['generation'])
df_seed03_selection_down_num_CDS = pd.DataFrame(df_seed03_selection_down_genes_best['generation'])
df_seed04_selection_down_num_CDS = pd.DataFrame(df_seed04_selection_down_genes_best['generation'])
df_seed05_selection_down_num_CDS = pd.DataFrame(df_seed05_selection_down_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_selection_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_selection_down_genes_best['num_functional_genes'] + df_seed01_selection_down_genes_best['num_non-functional_genes'])
df_seed02_selection_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_selection_down_genes_best['num_functional_genes'] + df_seed02_selection_down_genes_best['num_non-functional_genes'])
df_seed03_selection_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_selection_down_genes_best['num_functional_genes'] + df_seed03_selection_down_genes_best['num_non-functional_genes'])
df_seed04_selection_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_selection_down_genes_best['num_functional_genes'] + df_seed04_selection_down_genes_best['num_non-functional_genes'])
df_seed05_selection_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_selection_down_genes_best['num_functional_genes'] + df_seed05_selection_down_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_selection_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[1,1]) # bottom middle
df_seed02_selection_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[1,1])
df_seed03_selection_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[1,1])
df_seed04_selection_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[1,1])
df_seed05_selection_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[1,1])

ax_num_CDS_best[1,1].set_title("selection down", fontsize=20)

## MUTATION UP ##

# Create new DataFrames with the generation numbers
df_seed01_mutation_up_num_CDS = pd.DataFrame(df_seed01_mutation_up_genes_best['generation'])
df_seed02_mutation_up_num_CDS = pd.DataFrame(df_seed02_mutation_up_genes_best['generation'])
df_seed03_mutation_up_num_CDS = pd.DataFrame(df_seed03_mutation_up_genes_best['generation'])
df_seed04_mutation_up_num_CDS = pd.DataFrame(df_seed04_mutation_up_genes_best['generation'])
df_seed05_mutation_up_num_CDS = pd.DataFrame(df_seed05_mutation_up_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_mutation_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_mutation_up_genes_best['num_functional_genes'] + df_seed01_mutation_up_genes_best['num_non-functional_genes'])
df_seed02_mutation_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_mutation_up_genes_best['num_functional_genes'] + df_seed02_mutation_up_genes_best['num_non-functional_genes'])
df_seed03_mutation_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_mutation_up_genes_best['num_functional_genes'] + df_seed03_mutation_up_genes_best['num_non-functional_genes'])
df_seed04_mutation_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_mutation_up_genes_best['num_functional_genes'] + df_seed04_mutation_up_genes_best['num_non-functional_genes'])
df_seed05_mutation_up_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_mutation_up_genes_best['num_functional_genes'] + df_seed05_mutation_up_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_mutation_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[0,2]) # top right
df_seed02_mutation_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[0,2])
df_seed03_mutation_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[0,2])
df_seed04_mutation_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[0,2])
df_seed05_mutation_up_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[0,2])

ax_num_CDS_best[0,2].set_title("mutation up", fontsize=20)

## MUTATION DOWN ##
# Create new DataFrames with the generation numbers
df_seed01_mutation_down_num_CDS = pd.DataFrame(df_seed01_mutation_down_genes_best['generation'])
df_seed02_mutation_down_num_CDS = pd.DataFrame(df_seed02_mutation_down_genes_best['generation'])
df_seed03_mutation_down_num_CDS = pd.DataFrame(df_seed03_mutation_down_genes_best['generation'])
df_seed04_mutation_down_num_CDS = pd.DataFrame(df_seed04_mutation_down_genes_best['generation'])
df_seed05_mutation_down_num_CDS = pd.DataFrame(df_seed05_mutation_down_genes_best['generation'])

# Now append the relevant calculation (num functional genes + num non-functional genes)
df_seed01_mutation_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed01_mutation_down_genes_best['num_functional_genes'] + df_seed01_mutation_down_genes_best['num_non-functional_genes'])
df_seed02_mutation_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed02_mutation_down_genes_best['num_functional_genes'] + df_seed02_mutation_down_genes_best['num_non-functional_genes'])
df_seed03_mutation_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed03_mutation_down_genes_best['num_functional_genes'] + df_seed03_mutation_down_genes_best['num_non-functional_genes'])
df_seed04_mutation_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed04_mutation_down_genes_best['num_functional_genes'] + df_seed04_mutation_down_genes_best['num_non-functional_genes'])
df_seed05_mutation_down_num_CDS['num_CDS'] = pd.DataFrame(df_seed05_mutation_down_genes_best['num_functional_genes'] + df_seed05_mutation_down_genes_best['num_non-functional_genes'])

# Now plot all five seeds to one subplot
df_seed01_mutation_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 1', ax=ax_num_CDS_best[1,2]) # bottom right
df_seed02_mutation_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 2', ax=ax_num_CDS_best[1,2])
df_seed03_mutation_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 3', ax=ax_num_CDS_best[1,2])
df_seed04_mutation_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 4', ax=ax_num_CDS_best[1,2])
df_seed05_mutation_down_num_CDS.plot(x='generation', y='num_CDS', label='seed 5', ax=ax_num_CDS_best[1,2])

ax_num_CDS_best[1,2].set_title("mutation down", fontsize=20)

# Save and close the figure
fig_num_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_CDS_conditions.png")
plt.close(fig_num_CDS_best)

#### NUMBER OF BASE PAIRS IN CDS ####
print("number of base pairs in a CDS")

## CONTROL CONDITION ##

# For the control condition, plot all five seeds to one plot
fig_control_num_bp_in_a_CDS_best = plt.figure(figsize=(30,20))
ax_control_num_bp_in_a_CDS_best = fig_control_num_bp_in_a_CDS_best.add_subplot(111)
ax_control_num_bp_in_a_CDS_best.set_title("Number of Base Pairs in a CDS - Control Condition", fontsize=32)
ax_control_num_bp_in_a_CDS_best.set_xlabel("Generation", fontsize=20)
ax_control_num_bp_in_a_CDS_best.set_ylabel("Num Base Pairs", fontsize=20)

# We need to  calculate the number of base pairs which are in the CDS. We know
# the total number of base pairs and the number NOT in a CDS, so we can subtract
# the latter from the former to find our goal

# Do this for all five seeds, but first get the generation numbers
df_seed01_control_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_control_fitness_best['generation'])
df_seed02_control_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_control_fitness_best['generation'])
df_seed03_control_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_control_fitness_best['generation'])
df_seed04_control_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_control_fitness_best['generation'])
df_seed05_control_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_control_fitness_best['generation'])

df_seed01_control_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_control_fitness_best['genome_size'] - df_seed01_control_bp_best['num_bp_not_in_any_CDS'])
df_seed02_control_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_control_fitness_best['genome_size'] - df_seed02_control_bp_best['num_bp_not_in_any_CDS'])
df_seed03_control_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_control_fitness_best['genome_size'] - df_seed03_control_bp_best['num_bp_not_in_any_CDS'])
df_seed04_control_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_control_fitness_best['genome_size'] - df_seed04_control_bp_best['num_bp_not_in_any_CDS'])
df_seed05_control_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_control_fitness_best['genome_size'] - df_seed05_control_bp_best['num_bp_not_in_any_CDS'])

# Now plot the results for all five seeds
df_seed01_control_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS',label='seed 1', ax=ax_control_num_bp_in_a_CDS_best)
df_seed02_control_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_control_num_bp_in_a_CDS_best)
df_seed03_control_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_control_num_bp_in_a_CDS_best)
df_seed04_control_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_control_num_bp_in_a_CDS_best)
df_seed05_control_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_control_num_bp_in_a_CDS_best)

# Save and close the figure
fig_control_num_bp_in_a_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_bp_in_a_CDS_control.png")
plt.close(fig_control_num_bp_in_a_CDS_best)

### NUMBER OF BASE PAIRS IN A CDS - CONDITIONS ### 

# Create new figure with subplots for the other conditions 
fig_num_bp_in_a_CDS_best, ax_num_bp_in_a_CDS_best = plt.subplots(nrows=2, ncols=3, figsize=(30, 20), sharex=True, sharey=True) # to have them share an x axis, pass sharex=True to plt.subplots()
fig_num_bp_in_a_CDS_best.suptitle("Number of Base Pairs in a CDS", fontsize=48) # Title of graph
fig_num_bp_in_a_CDS_best.text(0.5, 0.04, 'Generation', ha='center', fontsize=32) # Common x label
fig_num_bp_in_a_CDS_best.text(0.04, 0.5, 'Num Base Pairs', va='center', rotation='vertical', fontsize=32) # Common y label

## POPULATION UP ##

# Create new DataFrames with the 'generation' numbers
df_seed01_population_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_population_up_bp_best['generation'])
df_seed02_population_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_population_up_bp_best['generation'])
df_seed03_population_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_population_up_bp_best['generation'])
df_seed04_population_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_population_up_bp_best['generation'])
df_seed05_population_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_population_up_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_population_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_pop_up_fitness_best['genome_size'] - df_seed01_population_up_bp_best['num_bp_not_in_any_CDS'])
df_seed02_population_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_pop_up_fitness_best['genome_size'] - df_seed02_population_up_bp_best['num_bp_not_in_any_CDS'])
df_seed03_population_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_pop_up_fitness_best['genome_size'] - df_seed03_population_up_bp_best['num_bp_not_in_any_CDS'])
df_seed04_population_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_pop_up_fitness_best['genome_size'] - df_seed04_population_up_bp_best['num_bp_not_in_any_CDS'])
df_seed05_population_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_pop_up_fitness_best['genome_size'] - df_seed05_population_up_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
# TODO - Determine if there was an error in seed03
df_seed01_population_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[0,0]) # top left
df_seed02_population_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[0,0])
#df_seed03_population_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[0,0])
df_seed04_population_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[0,0])
df_seed05_population_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[0,0])

ax_num_bp_in_a_CDS_best[0,0].set_title("population up", fontsize=20)

## POPULATION DOWN ##

# Create new DataFrames with the 'generation' numbers
df_seed01_population_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_population_down_bp_best['generation'])
df_seed02_population_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_population_down_bp_best['generation'])
df_seed03_population_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_population_down_bp_best['generation'])
df_seed04_population_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_population_down_bp_best['generation'])
df_seed05_population_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_population_down_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_population_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_pop_down_fitness_best['genome_size'] - df_seed01_population_down_bp_best['num_bp_not_in_any_CDS'])
df_seed02_population_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_pop_down_fitness_best['genome_size'] - df_seed02_population_down_bp_best['num_bp_not_in_any_CDS'])
df_seed03_population_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_pop_down_fitness_best['genome_size'] - df_seed03_population_down_bp_best['num_bp_not_in_any_CDS'])
df_seed04_population_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_pop_down_fitness_best['genome_size'] - df_seed04_population_down_bp_best['num_bp_not_in_any_CDS'])
df_seed05_population_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_pop_down_fitness_best['genome_size'] - df_seed05_population_down_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
df_seed01_population_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[1,0]) # bottom left
df_seed02_population_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[1,0])
df_seed03_population_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[1,0])
df_seed04_population_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[1,0])
df_seed05_population_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[1,0])

ax_num_bp_in_a_CDS_best[1,0].set_title("population down", fontsize=20)

## SELECTION UP ##

# Create new DataFrames with the 'generation' numbers
df_seed01_selection_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_selection_up_bp_best['generation'])
df_seed02_selection_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_selection_up_bp_best['generation'])
df_seed03_selection_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_selection_up_bp_best['generation'])
df_seed04_selection_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_selection_up_bp_best['generation'])
df_seed05_selection_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_selection_up_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_selection_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_selection_up_fitness_best['genome_size'] - df_seed01_selection_up_bp_best['num_bp_not_in_any_CDS'])
df_seed02_selection_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_selection_up_fitness_best['genome_size'] - df_seed02_selection_up_bp_best['num_bp_not_in_any_CDS'])
df_seed03_selection_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_selection_up_fitness_best['genome_size'] - df_seed03_selection_up_bp_best['num_bp_not_in_any_CDS'])
df_seed04_selection_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_selection_up_fitness_best['genome_size'] - df_seed04_selection_up_bp_best['num_bp_not_in_any_CDS'])
df_seed05_selection_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_selection_up_fitness_best['genome_size'] - df_seed05_selection_up_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
df_seed01_selection_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[0,1]) # top center
df_seed02_selection_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[0,1])
df_seed03_selection_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[0,1])
df_seed04_selection_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[0,1])
df_seed05_selection_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[0,1])

ax_num_bp_in_a_CDS_best[0,1].set_title("selection up", fontsize=20)

## SELECTION DOWN ##

# Create new DataFrames with the 'generation' numbers
df_seed01_selection_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_selection_down_bp_best['generation'])
df_seed02_selection_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_selection_down_bp_best['generation'])
df_seed03_selection_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_selection_down_bp_best['generation'])
df_seed04_selection_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_selection_down_bp_best['generation'])
df_seed05_selection_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_selection_down_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_selection_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_selection_down_fitness_best['genome_size'] - df_seed01_selection_down_bp_best['num_bp_not_in_any_CDS'])
df_seed02_selection_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_selection_down_fitness_best['genome_size'] - df_seed02_selection_down_bp_best['num_bp_not_in_any_CDS'])
df_seed03_selection_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_selection_down_fitness_best['genome_size'] - df_seed03_selection_down_bp_best['num_bp_not_in_any_CDS'])
df_seed04_selection_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_selection_down_fitness_best['genome_size'] - df_seed04_selection_down_bp_best['num_bp_not_in_any_CDS'])
df_seed05_selection_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_selection_down_fitness_best['genome_size'] - df_seed05_selection_down_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
df_seed01_selection_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[1,1]) # bottom center
df_seed02_selection_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[1,1])
df_seed03_selection_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[1,1])
df_seed04_selection_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[1,1])
df_seed05_selection_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[1,1])

ax_num_bp_in_a_CDS_best[1,1].set_title("selection down", fontsize=20)

## MUTATION UP ##

# Create new DataFrames with the 'generation' numbers
df_seed01_mut_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_mutation_up_bp_best['generation'])
df_seed02_mut_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_mutation_up_bp_best['generation'])
df_seed03_mut_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_mutation_up_bp_best['generation'])
df_seed04_mut_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_mutation_up_bp_best['generation'])
df_seed05_mut_up_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_mutation_up_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_mut_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_mutation_up_fitness_best['genome_size'] - df_seed01_mutation_up_bp_best['num_bp_not_in_any_CDS'])
df_seed02_mut_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_mutation_up_fitness_best['genome_size'] - df_seed02_mutation_up_bp_best['num_bp_not_in_any_CDS'])
df_seed03_mut_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_mutation_up_fitness_best['genome_size'] - df_seed03_mutation_up_bp_best['num_bp_not_in_any_CDS'])
df_seed04_mut_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_mutation_up_fitness_best['genome_size'] - df_seed04_mutation_up_bp_best['num_bp_not_in_any_CDS'])
df_seed05_mut_up_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_mutation_up_fitness_best['genome_size'] - df_seed05_mutation_up_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
df_seed01_mut_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[0,2]) # top right
df_seed02_mut_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[0,2])
df_seed03_mut_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[0,2])
df_seed04_mut_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[0,2])
df_seed05_mut_up_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[0,2])

ax_num_bp_in_a_CDS_best[0,2].set_title("mutation up", fontsize=20)

## MUTATION DOWN ##

# Create new DataFrames with the 'generation' numbers
df_seed01_mut_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed01_mutation_down_bp_best['generation'])
df_seed02_mut_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed02_mutation_down_bp_best['generation'])
df_seed03_mut_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed03_mutation_down_bp_best['generation'])
df_seed04_mut_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed04_mutation_down_bp_best['generation'])
df_seed05_mut_down_num_bp_in_a_CDS_best = pd.DataFrame(df_seed05_mutation_down_bp_best['generation'])

# Append the number of base pairs in a CDS (total bps minus bps not in any CDS)
df_seed01_mut_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed01_mutation_down_fitness_best['genome_size'] - df_seed01_mutation_down_bp_best['num_bp_not_in_any_CDS'])
df_seed02_mut_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed02_mutation_down_fitness_best['genome_size'] - df_seed02_mutation_down_bp_best['num_bp_not_in_any_CDS'])
df_seed03_mut_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed03_mutation_down_fitness_best['genome_size'] - df_seed03_mutation_down_bp_best['num_bp_not_in_any_CDS'])
df_seed04_mut_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed04_mutation_down_fitness_best['genome_size'] - df_seed04_mutation_down_bp_best['num_bp_not_in_any_CDS'])
df_seed05_mut_down_num_bp_in_a_CDS_best['num_bp_in_a_CDS'] = pd.DataFrame(df_seed05_mutation_down_fitness_best['genome_size'] - df_seed05_mutation_down_bp_best['num_bp_not_in_any_CDS'])

# Plot the result for all five seeds
df_seed01_mut_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 1', ax=ax_num_bp_in_a_CDS_best[1,2]) # bottom right
df_seed02_mut_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 2', ax=ax_num_bp_in_a_CDS_best[1,2])
df_seed03_mut_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 3', ax=ax_num_bp_in_a_CDS_best[1,2])
df_seed04_mut_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 4', ax=ax_num_bp_in_a_CDS_best[1,2])
df_seed05_mut_down_num_bp_in_a_CDS_best.plot(x='generation', y='num_bp_in_a_CDS', label='seed 5', ax=ax_num_bp_in_a_CDS_best[1,2])

ax_num_bp_in_a_CDS_best[1,2].set_title("mutation down", fontsize=20)

# Save and close the figure
fig_num_bp_in_a_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_bp_in_a_CDS_conditions.png")
plt.close(fig_num_bp_in_a_CDS_best)

#### NUMBER OF BASE PAIRS OUTSIDE OF CDS ####
print("number of base pairs not in any CDS")

# For the control condition, plot all five seeds to one plot
fig_control_num_bp_outside_CDS_best = plt.figure(figsize=(30,20))
ax_control_num_bp_outside_CDS_best = fig_control_num_bp_outside_CDS_best.add_subplot(111)
ax_control_num_bp_outside_CDS_best.set_title("Number of Base Pairs Outside of a CDS - Control Condition", fontsize=32)
ax_control_num_bp_outside_CDS_best.set_xlabel("Generation", fontsize=20)
ax_control_num_bp_outside_CDS_best.set_ylabel("Num Base Pairs", fontsize=20)

df_seed01_control_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS',label='seed 1', ax=ax_control_num_bp_outside_CDS_best)
df_seed02_control_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_control_num_bp_outside_CDS_best)
df_seed03_control_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_control_num_bp_outside_CDS_best)
df_seed04_control_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_control_num_bp_outside_CDS_best)
df_seed05_control_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_control_num_bp_outside_CDS_best)

# Save and close the figure
fig_control_num_bp_outside_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_bp_not_in_any_CDS_control.png")
plt.close(fig_control_num_bp_outside_CDS_best)

### NUMBER OF BASE PAIRS OUTSIDE OF CDS - CONDITIONS ###

# Create new figure with subplots for the other conditions 
fig_num_bp_outside_CDS_best, ax_num_bp_outside_CDS_best = plt.subplots(nrows=2, ncols=3, figsize=(30, 20), sharex=True, sharey=True) # to have them share an x axis, pass sharex=True to plt.subplots()
fig_num_bp_outside_CDS_best.suptitle("Number of Base Pairs Outside of Any CDS", fontsize=48) # Title of graph
fig_num_bp_outside_CDS_best.text(0.5, 0.04, 'Generation', ha='center', fontsize=32) # Common x label
fig_num_bp_outside_CDS_best.text(0.04, 0.5, 'Num Base Pairs', va='center', rotation='vertical', fontsize=32) # Common y label

## POPULATION UP ##

# Plot all five seeds to one subplot
df_seed01_population_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[0,0]) # top left
df_seed02_population_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[0,0])
df_seed03_population_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[0,0])
df_seed04_population_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[0,0])
df_seed05_population_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[0,0])

ax_num_bp_outside_CDS_best[0,0].set_title('population up', fontsize=20)
## POPULATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_population_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[1,0]) # bottom left
df_seed02_population_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[1,0])
df_seed03_population_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[1,0])
df_seed04_population_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[1,0])
df_seed05_population_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[1,0])

ax_num_bp_outside_CDS_best[1,0].set_title('population down', fontsize=20)

## SELECTION UP ##

# Plot all five seeds to one subplot
df_seed01_selection_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[0,1]) # top center
df_seed02_selection_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[0,1])
df_seed03_selection_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[0,1])
df_seed04_selection_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[0,1])
df_seed05_selection_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[0,1])

ax_num_bp_outside_CDS_best[0,1].set_title('selection up', fontsize=20)

## SELECTION DOWN ##

# Plot all five seeds to one subplot
df_seed01_selection_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[1,1]) # bottom center
df_seed02_selection_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[1,1])
df_seed03_selection_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[1,1])
df_seed04_selection_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[1,1])
df_seed05_selection_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[1,1])

ax_num_bp_outside_CDS_best[1,1].set_title('selection down', fontsize=20)

## MUTATION UP ##

# Plot all five seeds to one subplot
df_seed01_mutation_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[0,2]) # top right
df_seed02_mutation_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[0,2])
df_seed03_mutation_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[0,2])
df_seed04_mutation_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[0,2])
df_seed05_mutation_up_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[0,2])

ax_num_bp_outside_CDS_best[0,2].set_title('mutation up', fontsize=20)

## MUTATION DOWN ##

# Plot all five seeds to one subplot
df_seed01_mutation_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 1', ax=ax_num_bp_outside_CDS_best[1,2]) # bottom right
df_seed02_mutation_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 2', ax=ax_num_bp_outside_CDS_best[1,2])
df_seed03_mutation_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 3', ax=ax_num_bp_outside_CDS_best[1,2])
df_seed04_mutation_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 4', ax=ax_num_bp_outside_CDS_best[1,2])
df_seed05_mutation_down_bp_best.plot(x='generation', y='num_bp_not_in_any_CDS', label='seed 5', ax=ax_num_bp_outside_CDS_best[1,2])

ax_num_bp_outside_CDS_best[1,2].set_title('mutation down', fontsize=20)



# Save and close the figure
fig_num_bp_outside_CDS_best.savefig(OUTPUT_ROOT_DIR + "num_bp_not_in_any_CDS_conditions.png")
plt.close(fig_num_bp_outside_CDS_best)
print("Graphing complete.")


