# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:11:15 2019

@author: Brian Davis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INPUT_ROOT_DIR = "C://Users//Brian Davis//Dropbox//Freiburg Masters Semesters//Thesis//Results//"
OUTPUT_ROOT_DIR = INPUT_ROOT_DIR + "Graphics//"
GEN_GRAPH_SCALE = 1000

############ READ IN THE DATA ############
print("Reading in data...")

############# READ IN THE DATA FROM stat_fitness_best.out FOR THE DIFFERENT CONDITIONS ############
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


########### PUTTING DATA INTO DICTIONARIES FOR EASY ITERATION ########### 
print("Creating data dictionaries...")
seed01_fitness_dict = {
        "control": df_seed01_control_fitness_best,
        "mutation_up": df_seed01_mutation_up_fitness_best,
        "mutation_down": df_seed01_mutation_down_fitness_best,
        "selection_up": df_seed01_selection_up_fitness_best,
        "selection_down": df_seed01_selection_down_fitness_best,
        "population_up": df_seed01_pop_up_fitness_best,
        "population_down": df_seed01_pop_down_fitness_best
        }

seed02_fitness_dict = {
        "control": df_seed02_control_fitness_best,
        "mutation_up": df_seed02_mutation_up_fitness_best,
        "mutation_down": df_seed02_mutation_down_fitness_best,
        "selection_up": df_seed02_selection_up_fitness_best,
        "selection_down": df_seed02_selection_down_fitness_best,
        "population_up": df_seed02_pop_up_fitness_best,
        "population_down": df_seed02_pop_down_fitness_best
        }

seed03_fitness_dict = {
        "control": df_seed03_control_fitness_best,
        "mutation_up": df_seed03_mutation_up_fitness_best,
        "mutation_down": df_seed03_mutation_down_fitness_best,
        "selection_up": df_seed03_selection_up_fitness_best,
        "selection_down": df_seed03_selection_down_fitness_best,
        "population_up": df_seed03_pop_up_fitness_best,
        "population_down": df_seed03_pop_down_fitness_best
        }

seed04_fitness_dict = {
        "control": df_seed04_control_fitness_best,
        "mutation_up": df_seed04_mutation_up_fitness_best,
        "mutation_down": df_seed04_mutation_down_fitness_best,
        "selection_up": df_seed04_selection_up_fitness_best,
        "selection_down": df_seed04_selection_down_fitness_best,
        "population_up": df_seed04_pop_up_fitness_best,
        "population_down": df_seed04_pop_down_fitness_best
        }

seed05_fitness_dict = {
        "control": df_seed05_control_fitness_best,
        "mutation_up": df_seed05_mutation_up_fitness_best,
        "mutation_down": df_seed05_mutation_down_fitness_best,
        "selection_up": df_seed05_selection_up_fitness_best,
        "selection_down": df_seed05_selection_down_fitness_best,
        "population_up": df_seed05_pop_up_fitness_best,
        "population_down": df_seed05_pop_down_fitness_best
        }

print("done.")

########### GRAPHING ###########
print("Graphing results...")

# For each seed, create a figure
fig_seed01_genome_size_best = plt.figure(figsize=(30,20))
ax_seed01_genome_size_best = fig_seed01_genome_size_best.add_subplot(111)
ax_seed01_genome_size_best.set_title("Genome Size - Seed 1", fontsize=32)
ax_seed01_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_seed01_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

# A dictionary to store the results of the averages
seed01_result_dict = {}

for df in seed01_fitness_dict:
    # Smooth the graph a bit by taking the average of GEN_GRAPH_SCALE generations
    df_tmp = pd.DataFrame(seed01_fitness_dict[df]['genome_size'].groupby(np.arange(len(seed01_fitness_dict[df]))//GEN_GRAPH_SCALE).mean())
    df_tmp['generation'] = GEN_GRAPH_SCALE + df_tmp.index*GEN_GRAPH_SCALE # fix the indexes for plotting
    seed01_result_dict[df] = df_tmp
    
for df in seed01_result_dict:
    seed01_result_dict[df].plot(x='generation', y='genome_size', label=df, ax=ax_seed01_genome_size_best)
    
       
# Save and close the figure
fig_seed01_genome_size_best.savefig(OUTPUT_ROOT_DIR + "seed01_genome_size.png")
plt.close(fig_seed01_genome_size_best)


##### SEED 02 #####

# For each seed, create a figure
fig_seed02_genome_size_best = plt.figure(figsize=(30,20))
ax_seed02_genome_size_best = fig_seed02_genome_size_best.add_subplot(111)
ax_seed02_genome_size_best.set_title("Genome Size - Seed 2", fontsize=32)
ax_seed02_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_seed02_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

# A dictionary to store the results of the averages
seed02_result_dict = {}

for df in seed02_fitness_dict:
    # Smooth the graph a bit by taking the average of GEN_GRAPH_SCALE generations
    df_tmp = pd.DataFrame(seed02_fitness_dict[df]['genome_size'].groupby(np.arange(len(seed02_fitness_dict[df]))//GEN_GRAPH_SCALE).mean())
    df_tmp['generation'] = GEN_GRAPH_SCALE + df_tmp.index*GEN_GRAPH_SCALE # fix the indexes for plotting
    seed02_result_dict[df] = df_tmp
    
for df in seed02_result_dict:
    seed02_result_dict[df].plot(x='generation', y='genome_size', label=df, ax=ax_seed02_genome_size_best)
    
       
# Save and close the figure
fig_seed02_genome_size_best.savefig(OUTPUT_ROOT_DIR + "seed02_genome_size.png")
plt.close(fig_seed02_genome_size_best)

##### SEED 03 #####

# For each seed, create a figure
fig_seed03_genome_size_best = plt.figure(figsize=(30,20))
ax_seed03_genome_size_best = fig_seed03_genome_size_best.add_subplot(111)
ax_seed03_genome_size_best.set_title("Genome Size - Seed 3", fontsize=32)
ax_seed03_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_seed03_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

# A dictionary to store the results of the averages
seed03_result_dict = {}

for df in seed03_fitness_dict:
    # Smooth the graph a bit by taking the average of GEN_GRAPH_SCALE generations
    df_tmp = pd.DataFrame(seed03_fitness_dict[df]['genome_size'].groupby(np.arange(len(seed03_fitness_dict[df]))//GEN_GRAPH_SCALE).mean())
    df_tmp['generation'] = GEN_GRAPH_SCALE + df_tmp.index*GEN_GRAPH_SCALE # fix the indexes for plotting
    seed03_result_dict[df] = df_tmp
    
for df in seed03_result_dict:
    seed03_result_dict[df].plot(x='generation', y='genome_size', label=df, ax=ax_seed03_genome_size_best)
    
       
# Save and close the figure
fig_seed03_genome_size_best.savefig(OUTPUT_ROOT_DIR + "seed03_genome_size.png")
plt.close(fig_seed03_genome_size_best)

##### SEED 04 #####

# For each seed, create a figure
fig_seed04_genome_size_best = plt.figure(figsize=(30,20))
ax_seed04_genome_size_best = fig_seed04_genome_size_best.add_subplot(111)
ax_seed04_genome_size_best.set_title("Genome Size - Seed 4", fontsize=32)
ax_seed04_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_seed04_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

# A dictionary to store the results of the averages
seed04_result_dict = {}

for df in seed04_fitness_dict:
    # Smooth the graph a bit by taking the average of GEN_GRAPH_SCALE generations
    df_tmp = pd.DataFrame(seed04_fitness_dict[df]['genome_size'].groupby(np.arange(len(seed04_fitness_dict[df]))//GEN_GRAPH_SCALE).mean())
    df_tmp['generation'] = GEN_GRAPH_SCALE + df_tmp.index*GEN_GRAPH_SCALE # fix the indexes for plotting
    seed04_result_dict[df] = df_tmp
    
for df in seed04_result_dict:
    seed04_result_dict[df].plot(x='generation', y='genome_size', label=df, ax=ax_seed04_genome_size_best)
    
       
# Save and close the figure
fig_seed04_genome_size_best.savefig(OUTPUT_ROOT_DIR + "seed04_genome_size.png")
plt.close(fig_seed04_genome_size_best)

##### SEED 05 #####

# For each seed, create a figure
fig_seed05_genome_size_best = plt.figure(figsize=(30,20))
ax_seed05_genome_size_best = fig_seed05_genome_size_best.add_subplot(111)
ax_seed05_genome_size_best.set_title("Genome Size - Seed 5", fontsize=32)
ax_seed05_genome_size_best.set_xlabel("Generation", fontsize=20)
ax_seed05_genome_size_best.set_ylabel("Num Base Pairs", fontsize=20)

# A dictionary to store the results of the averages
seed05_result_dict = {}

for df in seed05_fitness_dict:
    # Smooth the graph a bit by taking the average of GEN_GRAPH_SCALE generations
    df_tmp = pd.DataFrame(seed05_fitness_dict[df]['genome_size'].groupby(np.arange(len(seed05_fitness_dict[df]))//GEN_GRAPH_SCALE).mean())
    df_tmp['generation'] = GEN_GRAPH_SCALE + df_tmp.index*GEN_GRAPH_SCALE # fix the indexes for plotting
    seed05_result_dict[df] = df_tmp
    
for df in seed05_result_dict:
    seed05_result_dict[df].plot(x='generation', y='genome_size', label=df, ax=ax_seed05_genome_size_best)
    
       
# Save and close the figure
fig_seed05_genome_size_best.savefig(OUTPUT_ROOT_DIR + "seed05_genome_size.png")
plt.close(fig_seed05_genome_size_best)

print("Graphing complete!")