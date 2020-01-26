import pandas as pd

def read_fitness(fileLoc):
    fitness_best_names = ['generation', 'pop_size', 'fitness', 'genome_size', 'metabolic_error','parents_metabolic_error', 'metabolic_fitness', 'secretion_error', 'parents_secretion_error', 'secretion_fitness', 'amt_compound_present']
    df_ = pd.read_csv(fileLoc, skiprows=17, delim_whitespace=True, header=0, names=fitness_best_names)
    return df_
    
def read_bp(fileLoc):
    bp_best_names = ['generation', 'num_bp_not_in_any_CDS', 'num_bp_not_in_any_functional_CDS', 'num_bp_not_in_any_non-functional_CDS', 'num_bp_not_included_in_any_RNA', 'num_bp_not_included_in_any_coding_RNA', 'num_bp_not_included_in_any_non-coding_RNA', 'num_of_non-essential_bp', 'num_of_non-essential_bp_including_non-functional_genes']
    df_ = pd.read_csv(fileLoc, skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)
    return df_