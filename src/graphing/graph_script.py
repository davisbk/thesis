import pandas as pd



INPUT_ROOT_DIR = "C://Users//Brian Davis//Dropbox//Freiburg Masters Semesters//Thesis//Results//"
OUTPUT_ROOT_DIR = "C://Users//Brian Davis//Dropbox//Freiburg Masters Semesters//Thesis//Results//Graphics//"

# FITTEST INDIVIDUAL NON-CODING STATISTICS

# Read in the data from the five seeds
bp_best_names=['generation','nbp not in any CDS', 'nbp not in any functional CDS', 'nbp not in any non-functional CDS', 'nbp in any RNA', 'nbp not included in any coding RNA', 'nbp not included in any non-coding RNA', 'num non-essential bp', 'num non-essential bp including non-funct genes']
df_seed01_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed01//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)
df_seed02_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed02//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)
df_seed03_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed03//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)
df_seed04_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed04//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)
df_seed05_bp_best = pd.read_csv(INPUT_ROOT_DIR + "seed05//control//stats//stat_bp_best.out", skiprows=17, delim_whitespace=True, header=0, names=bp_best_names)

# Plot them all to the same figure
plot1_ax = df_seed01_bp_best.plot(x = 'generation', y = 'nbp not in any CDS', label='seed 1', figsize=(20,20))
df_seed02_bp_best.plot(x = 'generation', y = 'nbp not in any CDS', label='seed 2', ax=plot1_ax)
df_seed03_bp_best.plot(x = 'generation', y = 'nbp not in any CDS', label='seed 3', ax=plot1_ax)
df_seed04_bp_best.plot(x = 'generation', y = 'nbp not in any CDS', label='seed 4', ax=plot1_ax)
df_seed05_bp_best.plot(x = 'generation', y = 'nbp not in any CDS', label='seed 5', ax=plot1_ax)
plot1_ax.set_title("Control Condition - Num basepairs not in any CDS")
fig1 = plot1_ax.get_figure()
fig1.savefig(OUTPUT_ROOT_DIR + "control_nbp_not_in_any_CDS.png")



plot2_ax = df_seed01_bp_best.plot(x = 'generation', y = 'nbp not in any functional CDS', label='seed 1', figsize=(20,20))
df_seed02_bp_best.plot(x='generation', y='nbp not in any functional CDS', label='seed 2', ax=plot2_ax)
df_seed03_bp_best.plot(x='generation', y='nbp not in any functional CDS', label='seed 3', ax=plot2_ax)
df_seed04_bp_best.plot(x='generation', y='nbp not in any functional CDS', label='seed 4', ax=plot2_ax)
df_seed05_bp_best.plot(x='generation', y='nbp not in any functional CDS', label='seed 5', ax=plot2_ax)
plot2_ax.set_title("Control Condition - Num base pairs not in any functional CDS")
fig2 = plot2_ax.get_figure()
fig2.savefig(OUTPUT_ROOT_DIR + "control_nbp_not_in_any_functional_CDS.png")


plot3_ax = df_seed01_bp_best.plot(x = 'generation', y = 'nbp not in any non-functional CDS', label='seed 1', figsize=(20,20))
df_seed02_bp_best.plot(x = 'generation', y = 'nbp not in any non-functional CDS', label='seed 2', ax=plot3_ax)
df_seed03_bp_best.plot(x = 'generation', y = 'nbp not in any non-functional CDS', label='seed 3', ax=plot3_ax)
df_seed04_bp_best.plot(x = 'generation', y = 'nbp not in any non-functional CDS', label='seed 4', ax=plot3_ax)
df_seed05_bp_best.plot(x = 'generation', y = 'nbp not in any non-functional CDS', label='seed 5', ax=plot3_ax)
plot3_ax.set_title("Control Condition - Num base pairs not in any non-functional CDS")
fig3 = plot3_ax.get_figure()
fig3.savefig(OUTPUT_ROOT_DIR + "control_nbp_not_in_any_non-functional_CDS.png")


# TODO - FINISH stat_bp_best.out ???? 

# BEGIN PROCESSING stat_genes_glob.out

# Read in data from five seeds 
genes_glob_names=['generation', 'num coding RNAs', 'num non-coding RNAs', 'avg coding RNA size', 'avg non-coding RNA size', 'num functional genes', 'num non-functional genes', 'avg functional gene size', 'avg non-functional gene size']
df_seed01_stat_genes_glob_control = pd.read_csv(INPUT_ROOT_DIR + "seed01//control//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed02_stat_genes_glob_control = pd.read_csv(INPUT_ROOT_DIR + "seed02//control//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed03_stat_genes_glob_control = pd.read_csv(INPUT_ROOT_DIR + "seed03//control//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed04_stat_genes_glob_control = pd.read_csv(INPUT_ROOT_DIR + "seed04//control//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed05_stat_genes_glob_control = pd.read_csv(INPUT_ROOT_DIR + "seed05//control//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)

plot4_ax = df_seed01_stat_genes_glob_control.plot(x='generation', y='num coding RNAs', label='seed 1', figsize=(20,20))
df_seed02_stat_genes_glob_control.plot(x='generation', y='num coding RNAs', label='seed 2', ax=plot4_ax)
df_seed03_stat_genes_glob_control.plot(x='generation', y='num coding RNAs', label='seed 3', ax=plot4_ax)
df_seed04_stat_genes_glob_control.plot(x='generation', y='num coding RNAs', label='seed 4', ax=plot4_ax)
df_seed05_stat_genes_glob_control.plot(x='generation', y='num coding RNAs', label='seed 5', ax=plot4_ax)
plot4_ax.set_title("Control Condition - Number of coding RNAs")
fig4 = plot4_ax.get_figure()
fig4.savefig(OUTPUT_ROOT_DIR + "control_num_coding_RNAs.png")

# Create a boxplot of the number of functional genes across all conditions (control, m+, m-, n+, n-, sel+, sel-)
# First read in the same stats files for all other conditions
df_seed01_stat_genes_glob_mut_up = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_up//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed01_stat_genes_glob_mut_down = pd.read_csv(INPUT_ROOT_DIR + "seed01//mut_down//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed01_stat_genes_glob_pop_up = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_up//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed01_stat_genes_glob_pop_down = pd.read_csv(INPUT_ROOT_DIR + "seed01//pop_down//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed01_stat_genes_glob_selection_up = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_up//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)
df_seed01_stat_genes_glob_selection_down = pd.read_csv(INPUT_ROOT_DIR + "seed01//selection_down//stats//stat_genes_glob.out", skiprows=14, delim_whitespace=True, header=0, names=genes_glob_names)

# We need to have one DataFrame to give to .boxplot() so we will add an additional column with the experimental condition
# and then combine all of the DataFrames into one DataFrame.
df_seed01_stat_genes_glob_mut_up["condition"] = "mutation+"
df_seed01_stat_genes_glob_mut_down["condition"] = "mutation-"
df_seed01_stat_genes_glob_pop_up["condition"] = "population+"
df_seed01_stat_genes_glob_pop_down["condition"] = "population-"
df_seed01_stat_genes_glob_selection_up["condition"] = "selection+"
df_seed01_stat_genes_glob_selection_down["condition"] = "selection-"
df_seed01_stat_genes_glob_control["condition"] = "control"

allData = pd.DataFrame(pd.concat([df_seed01_stat_genes_glob_control, df_seed01_stat_genes_glob_mut_up, df_seed01_stat_genes_glob_mut_down, df_seed01_stat_genes_glob_pop_up, df_seed01_stat_genes_glob_pop_down, df_seed01_stat_genes_glob_selection_up, df_seed01_stat_genes_glob_selection_down]))


plot5_ax = allData.boxplot(column='num functional genes', by='condition', figsize=(20,20))
plot5_ax.set_title("Seed 1 - Number of functional genes across conditions.")
fig5 = plot5_ax.get_figure()
fig5.savefig(OUTPUT_ROOT_DIR + "seed01_num_functional_genes_all_conditions.png")




