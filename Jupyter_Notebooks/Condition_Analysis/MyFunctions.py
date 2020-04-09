import pandas as pd

def read_fitness(fileLoc):
    fitness_best_names = ['generation', 'pop_size', 'fitness', 'genome_size', 'metabolic_error','parents_metabolic_error', 'metabolic_fitness', 'secretion_error', 'parents_secretion_error', 'secretion_fitness', 'amt_compound_present']
    df_fitness = pd.read_csv(fileLoc, skiprows=18, delim_whitespace=True, header=0,dtype='float64', names=fitness_best_names)
    return df_fitness

def read_bp(fileLoc):
    bp_best_names = ['generation', 'num_bp_not_in_any_CDS', 'num_bp_not_in_any_functional_CDS', 'num_bp_not_in_any_non-functional_CDS', 'num_bp_not_included_in_any_RNA', 'num_bp_not_included_in_any_coding_RNA', 'num_bp_not_included_in_any_non-coding_RNA', 'num_of_non-essential_bp', 'num_of_non-essential_bp_including_non-functional_genes']
    df_bp = pd.read_csv(fileLoc, skiprows=17, delim_whitespace=True, header=0,dtype='float64', names=bp_best_names)
    return df_bp

def read_genes(fileLoc):
    genes_best_names = ['generation', 'num_coding_RNAs', 'num_non-coding_RNAs', 'avg_size_of_coding_RNAs', 'avg_size_of_non-coding_RNAs', 'num_functional_genes', 'num_non-functional_genes', 'avg_size_of_functional_genes', 'avg_size_of_non-functional_genes']
    df_genes = pd.read_csv(fileLoc, skiprows=14, delim_whitespace=True,header=0, dtype='float64', names=genes_best_names)
    return df_genes

def read_robustness(fileLoc):
    robustness_names = ['generation', 'frac_positive_offspring', 'frac_neutral_offspring', 'frac_neutral_mutants', 'frac_negative_offspring', 'cumul_delta-gap_positive_offspring', 'cumul_delta-gap_negative_offspring', 'delta-gap_best_offspring', 'delta-gap_worst_offspring', 'cumul_delta-fitness_positive_offspring', 'cumul_delta-fitness_negative_offspring', 'delta-fitness_best_offspring', 'delta-fitness_worst_offspring']
    df_robustness = pd.read_csv(fileLoc, na_values='-nan', skiprows= 19, delim_whitespace=True, header=0, dtype='float64', names=robustness_names)
    return df_robustness

def perc_diff(new_value, old_value):
    #if new_value.isnull().values.any():
    #    new_value.fillna(value=0, inplace=True)
    #elif old_value.isnull().values.any():
    #    old_value.fillna(value=0, inplace=True)
        
    df_perc_diff = (new_value - old_value)/ new_value
    return df_perc_diff