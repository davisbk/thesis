// ****************************************************************************
//
//          Aevol - An in silico experimental evolution platform
//
// ****************************************************************************
//
// Copyright: See the AUTHORS file provided with the package or <www.aevol.fr>
// Web: http://www.aevol.fr/
// E-mail: See <http://www.aevol.fr/contact/>
// Original Authors : Guillaume Beslon, Carole Knibbe, David Parsons
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// ****************************************************************************

// The input file is produced by the lineage post-treatment, please refer to it
// for e.g. the file format/content

// ============================================================================
//                                   Includes
// ============================================================================
#include <cinttypes>
#include <getopt.h>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <zlib.h>
#include <err.h>
#include <cerrno>
#include <sys/stat.h>
#include <unistd.h>
#include <list>
#include <iostream>

#include "aevol.h"

using namespace aevol;

// Helper functions
void interpret_cmd_line_options(int argc, char* argv[]);
void print_help(char* prog_path);
FILE* open_environment_stat_file(const char* prefix, const char* postfix);
void write_environment_stats(int64_t t,
                             const PhenotypicTargetHandler* pth,
                             FILE* env_file);
FILE* open_terminators_stat_file(const char* prefix, const char* postfix);
void write_terminators_stats(int64_t t, Individual* indiv,
                             FILE* terminator_file);
FILE* open_zones_stat_file(const char* prefix, const char* postfix);
void write_zones_stats(int64_t t,
                       Individual* indiv,
                       const PhenotypicTargetHandler* phenotypicTargetHandler,
                       FILE* zone_file);
FILE* open_operons_stat_file(const char* prefix, const char* postfix);
void write_operons_stats(int64_t t, Individual* indiv, FILE* operon_file);

// Command-line option variables
static char* lineage_file_name = nullptr;
static bool verbose = false;
static bool full_check = false;
static bool trace_mutations = false;

int main(int argc, char* argv[]) {
  interpret_cmd_line_options(argc, argv);

  printf("\n"
         "WARNING : Parameter change during simulation is not managed in general.\n"
         "          Only changes in environmental target done with aevol_modify are handled.\n"
         "\n");

  // =======================
  //  Open the lineage file
  // =======================
  gzFile lineage_file = gzopen(lineage_file_name, "r");
  if (lineage_file == Z_NULL) {
    fprintf(stderr, "ERROR : Could not read the lineage file %s\n", lineage_file_name);
    exit(EXIT_FAILURE);
  }

  int64_t t0 = 0;
  int64_t t_end = 0;
  int32_t final_indiv_index = 0;
  int32_t final_indiv_rank  = 0;

  gzread(lineage_file, &t0, sizeof(t0));
  gzread(lineage_file, &t_end, sizeof(t_end));
  gzread(lineage_file, &final_indiv_index, sizeof(final_indiv_index));
  gzread(lineage_file, &final_indiv_rank,  sizeof(final_indiv_rank));

  if (verbose) {
    printf("\n\n""===============================================================================\n");
    printf(" Statistics of the ancestors of indiv. %" PRId32
           " (rank %" PRId32 ") from time %" PRId64 " to %" PRId64 "\n",
           final_indiv_index, final_indiv_rank, t0, t_end);
    printf("================================================================================\n");
  }



  // =============================
  //  Open the experiment manager
  // =============================
  ExpManager* exp_manager = new ExpManager();
  exp_manager->load(t0, true, false);

  // The current version doesn't allow for phenotypic variation nor for
  // different phenotypic targets among the grid
  if (not exp_manager->world()->phenotypic_target_shared())
    Utils::ExitWithUsrMsg("sorry, ancestor stats has not yet been implemented "
                              "for per grid-cell phenotypic target");
  auto phenotypicTargetHandler =
      exp_manager->world()->phenotypic_target_handler();
  if (not (phenotypicTargetHandler->var_method() == NO_VAR))
    Utils::ExitWithUsrMsg("sorry, ancestor stats has not yet been implemented "
                              "for variable phenotypic targets");

  int64_t backup_step = exp_manager->backup_step();


  // =========================
  //  Open the output file(s)
  // =========================
  // Create missing directories
  int status;
  status = mkdir("stats/ancestor_stats/", 0755);
  if ((status == -1) && (errno != EEXIST)) {
    err(EXIT_FAILURE, "stats/ancestor_stats/");
  }

  // Open main output files (uses the Stats utility class)
  auto prefix = "ancestor_stats/ancestor_stats";
  char postfix[255];
  snprintf(postfix, 255,
      "-b" TIMESTEP_FORMAT "-e" TIMESTEP_FORMAT "-i%" PRId32 "-r%" PRId32,
      t0, t_end, final_indiv_index, final_indiv_rank);
  bool best_indiv_only = true;
  bool addition_old_stats = false;
  bool delete_old_stats = true;
  Stats* mystats = new Stats(exp_manager, t0, best_indiv_only, prefix, postfix,
                             addition_old_stats, delete_old_stats);

  // Optional additional outputs
  FILE* env_output_file = open_environment_stat_file(prefix, postfix);
  FILE* term_output_file = open_terminators_stat_file(prefix, postfix);
  FILE* zones_output_file = NULL;

  // Next line patchy (specific for the constraints mentioned earlier, i.e.
  // works only for shared and unvarying phenotypic target)
  if (phenotypicTargetHandler->phenotypic_target().nb_segments() > 1) {
    zones_output_file = open_zones_stat_file(prefix, postfix);
  }
  FILE* operons_output_file = open_operons_stat_file(prefix, postfix);

  // Open optional output files
  FILE* fixed_mutations_file = nullptr;
  if (trace_mutations) {
    char fixed_mutations_file_name[255];
    snprintf(fixed_mutations_file_name, 60,
             "stats/fixedmut-b" TIMESTEP_FORMAT "-e" TIMESTEP_FORMAT "-i%"
                 PRId32 "-r%" PRId32 ".out",
             t0, t_end, final_indiv_index, final_indiv_rank);
    fixed_mutations_file = fopen(fixed_mutations_file_name, "w");
    if (fixed_mutations_file == nullptr) {
      Utils::ExitWithUsrMsg(std::string("Could not create the output file ") +
                            fixed_mutations_file_name);
    }

    // Write the header
    fprintf(fixed_mutations_file, "# #################################################################\n");
    fprintf(fixed_mutations_file, "#  Mutations in the lineage of the best indiv at generation %" PRId64 "\n", t_end);
    fprintf(fixed_mutations_file, "# #################################################################\n");
    fprintf(fixed_mutations_file, "#  1.  Generation       (mut. occurred when producing the indiv. of this generation)\n");
    fprintf(fixed_mutations_file, "#  2.  Genetic unit     (which underwent the mutation, 0 = chromosome) \n");
    fprintf(fixed_mutations_file, "#  3.  Mutation type    (0: switch, 1: smallins, 2: smalldel, 3:dupl, 4: del, 5:trans, 6:inv, 7:insert, 8:ins_HT, 9:repl_HT) \n");
    fprintf(fixed_mutations_file, "#  4.  pos_0            (position for the small events, begin_segment for the rearrangements, begin_segment of the inserted segment for ins_HT, begin_segment of replaced segment for repl_HT) \n");
    fprintf(fixed_mutations_file, "#  5.  pos_1            (-1 for the small events, end_segment for the rearrangements, end_segment of the inserted segment for ins_HT, begin_segment of donor segment for repl_HT) \n");
    fprintf(fixed_mutations_file, "#  6.  pos_2            (reinsertion point for duplic., cutting point in segment for transloc., insertion point in the receiver for ins_HT, end_segment of the replaced segment for repl_HT, -1 for other events)\n");
    fprintf(fixed_mutations_file, "#  7.  pos_3            (reinsertion point for transloc., breakpoint in the donor for ins_HT, end_segment of the donor segment for repl_HT, -1 for other events)\n");
    fprintf(fixed_mutations_file, "#  8.  invert           (transloc, was the segment inverted (0/1)?, sense of insertion for ins_HT (0=DIRECT, 1=INDIRECT), sense of the donor segment for repl_HT (0=DIRECT, 1=INDIRECT),-1 for other events)\n");
    fprintf(fixed_mutations_file, "#  9.  align_score      (score that was needed for the rearrangement to occur, score of the first alignment for ins_HT and repl_HT)\n");
    fprintf(fixed_mutations_file, "#  10. align_score2     (score for the reinsertion for transloc, score of the second alignment for ins_HT and repl_HT)\n");
    fprintf(fixed_mutations_file, "#  11. seg_len          (segment length for rearrangement, donor segment length for ins_HT and repl_HT)\n");
    fprintf(fixed_mutations_file, "#  12. repl_seg_len     (replaced segment length for repl_HT, -1 for the others)\n");
    fprintf(fixed_mutations_file, "#  13. GU_length        (before the event)\n");
    fprintf(fixed_mutations_file, "#  14. Impact of the mutation on the metabolic error (negative value = smaller gap after = beneficial mutation) \n");
    fprintf(fixed_mutations_file, "#  15. Number of coding RNAs possibly disrupted by the breakpoints \n");
    fprintf(fixed_mutations_file, "#  16. Number of coding RNAs completely included in the segment (donor segment in the case of a transfer) \n");
    fprintf(fixed_mutations_file, "#  17. Number of coding RNAs that were completely included in the replaced segment (meaningful only for repl_HT) \n");
    fprintf(fixed_mutations_file, "####################################################################################################################\n");
    fprintf(fixed_mutations_file, "#\n");
    fprintf(fixed_mutations_file, "# Header for R\n");
    fprintf(fixed_mutations_file, "gener gen_unit mut_type pos_0 pos_1 pos_2 pos_3 invert align_score align_score_2 seg_len repl_seg_len GU_len impact nbgenesatbreak nbgenesinseg nbgenesinreplseg\n");

  }

  // ==================================================
  //  Prepare the initial ancestor and write its stats
  // ==================================================
  GridCell* grid_cell = new GridCell(lineage_file, exp_manager, nullptr);
  auto* indiv = grid_cell->individual();
  indiv->Evaluate();
  indiv->compute_statistical_data();
  indiv->compute_non_coding();

  mystats->write_statistics_of_this_indiv(indiv, nullptr);

  // Additional outputs
  write_environment_stats(t0, phenotypicTargetHandler, env_output_file);
  write_terminators_stats(t0, indiv, term_output_file);
  if(phenotypicTargetHandler->phenotypic_target().nb_segments() > 1)
  {
    write_zones_stats(t0, indiv, phenotypicTargetHandler, zones_output_file);
  }
  write_operons_stats(t0, indiv, operons_output_file);

  if (verbose) {
    printf("Initial fitness     = %f\n", indiv->fitness());
    printf("Initial genome size = %" PRId32 "\n", indiv->total_genome_size());
  }

  // ==========================================================================
  //  Replay the mutations to get the successive ancestors and analyze them
  // ==========================================================================
  ReplicationReport* rep = nullptr;
  int32_t index;
  ExpManager* exp_manager_backup = nullptr;
  int32_t unitlen_before;
  double metabolic_error_before;
  double impact_on_metabolic_error;
  char mut_descr_string[255];

  bool check_now = false;

  aevol::AeTime::plusplus();
  while (time() <= t_end)
  {
    rep = new ReplicationReport(lineage_file, indiv);
    index = rep->id(); // who we are building...

    // Check now?
    check_now = time() == t_end ||
        (full_check && Utils::mod(time(), backup_step) == 0);

    if (verbose)
        printf("Rebuilding ancestor at generation %" PRId64
            " (index %" PRId32 ")...", time(), index);

    indiv->Reevaluate();

    // 2) Replay replication (create current individual's child)
    GeneticUnit& gen_unit = indiv->genetic_unit_nonconst(0);
    GeneticUnit* stored_gen_unit = nullptr;
    Individual* stored_indiv = nullptr;

    if (check_now)
    {
      exp_manager_backup = new ExpManager();
      exp_manager_backup->load(time(), true, false);
      stored_indiv = new Individual(
          *(Individual*) exp_manager_backup->indiv_by_id(index));
      stored_gen_unit = &(stored_indiv->genetic_unit_nonconst(0));
    }

    // For each genetic unit, replay the replication (undergo all mutations)
    // TODO <david.parsons@inria.fr> disabled for multiple GUs
    const auto& dnarep = rep->dna_replic_report();

    // TODO(dpa) The following 3 for loops should be factorized.
    // However, this is not as easy as it sounds :-D
    // see std::list::splice
    for (const auto& mut: dnarep.HT())
      gen_unit.dna()->undergo_this_mutation(*mut);

    for (const auto& mut: dnarep.rearrangements()) {
      if (trace_mutations) {
        // Store initial values before the mutation
        metabolic_error_before = indiv->dist_to_target_by_feature(METABOLISM);
        unitlen_before = gen_unit.dna()->length();
      }

      // Apply mutation
      gen_unit.dna()->undergo_this_mutation(*mut);

      if (trace_mutations) {
        indiv->Reevaluate();

        // Compute the metabolic impact of the mutation
        impact_on_metabolic_error =
            indiv->dist_to_target_by_feature(METABOLISM) -
            metabolic_error_before;

        mut->generic_description_string(mut_descr_string);
        fprintf(fixed_mutations_file,
                "%" PRId64 " %" PRId32 " %s %" PRId32 " %.15f \n",
                time(), 0, mut_descr_string, unitlen_before,
                impact_on_metabolic_error);
      }
    }

    for (const auto& mut: dnarep.mutations()) {
      if (trace_mutations) {
        // Store initial values before the mutation
        metabolic_error_before = indiv->dist_to_target_by_feature(METABOLISM);
        unitlen_before = gen_unit.dna()->length();
      }

      // Apply mutation
      gen_unit.dna()->undergo_this_mutation(*mut);

      if (trace_mutations) {
        indiv->Reevaluate();

        // Compute the metabolic impact of the mutation
        impact_on_metabolic_error =
            indiv->dist_to_target_by_feature(METABOLISM) -
            metabolic_error_before;

        mut->generic_description_string(mut_descr_string);
        fprintf(fixed_mutations_file,
                "%" PRId64 " %" PRId32 " %s %" PRId32 " %.15f \n",
                time(), 0, mut_descr_string, unitlen_before,
                impact_on_metabolic_error);
      }
    }

    if (check_now) {
      if (verbose) {
        printf("Checking the sequence of the unit...");
        fflush(NULL);
      }

      char * str1 = new char[gen_unit.dna()->length() + 1];
      memcpy(str1, gen_unit.dna()->data(), \
             gen_unit.dna()->length()*sizeof(char));
      str1[gen_unit.dna()->length()] = '\0';

      char * str2 = new char[(stored_gen_unit->dna())->length() + 1];
      memcpy(str2, (stored_gen_unit->dna())->data(),
             (stored_gen_unit->dna())->length()*sizeof(char));
      str2[(stored_gen_unit->dna())->length()] = '\0';

      if (strncmp(str1, str2, stored_gen_unit->dna()->length()) == 0) {
        if (verbose)
          printf(" OK\n");
      }
      else {
        if (verbose) printf(" ERROR !\n");
        fprintf(stderr, "Error: the rebuilt genetic unit is not the same as \n");
        fprintf(stderr, "the one saved at generation %" PRId64 "... ", time());
        fprintf(stderr, "Rebuilt unit : %" PRId32 " bp\n %s\n", (int32_t)strlen(str1), str1);
        fprintf(stderr, "Stored unit  : %" PRId32 " bp\n %s\n", (int32_t)strlen(str2), str2);

        delete [] str1;
        delete [] str2;
        gzclose(lineage_file);
        if (trace_mutations)
          gzclose(lineage_file);
        delete indiv;
        delete stored_indiv;
        delete exp_manager_backup;
        delete exp_manager;
        exit(EXIT_FAILURE);
      }

      delete [] str1;
      delete [] str2;
    }

    // 3) All the mutations have been replayed, we can now evaluate the new individual
    indiv->Reevaluate();
    indiv->compute_statistical_data();
    indiv->compute_non_coding();

    mystats->write_statistics_of_this_indiv(indiv, rep);

    // Additional outputs
    write_environment_stats(time(), phenotypicTargetHandler, env_output_file);
    write_terminators_stats(time(), indiv, term_output_file);
    if(phenotypicTargetHandler->phenotypic_target().nb_segments() > 1) {
      write_zones_stats(time(), indiv, phenotypicTargetHandler,
                        zones_output_file);
    }
    write_operons_stats(time(), indiv, operons_output_file);

    if (verbose) printf(" OK\n");

    delete rep;

    if (check_now) {
      delete stored_indiv;
      delete exp_manager_backup;
    }

    aevol::AeTime::plusplus();
  }

  gzclose(lineage_file);

  // Additional outputs
  fclose(env_output_file);
  fclose(term_output_file);
  if(phenotypicTargetHandler->phenotypic_target().nb_segments() > 1) {
    fclose(zones_output_file);
  }
  fclose(operons_output_file);

  delete exp_manager;
  delete mystats;
  delete indiv;

  return EXIT_SUCCESS;
}




FILE* open_environment_stat_file(const char* prefix, const char* postfix) {
  // Open file
  char* env_output_file_name = new char[120];
  sprintf(env_output_file_name, "stats/%s_envir%s.out", prefix, postfix);
  FILE* env_output_file = fopen(env_output_file_name, "w");
  delete env_output_file_name;

  // Write headers
  // TODO vld: was limited to "if environment->gaussians_provided"
  // are gaussians always available now?
  fprintf(env_output_file,
          "# Each line contains: Generation, and then, for each gaussian: M W H.\n");
  fprintf(env_output_file, "#\n");

  return env_output_file;
}


void write_environment_stats(int64_t t, const PhenotypicTargetHandler* pth,
                             FILE* env_output_file) {
  // Num gener
  fprintf(env_output_file, "%" PRId64, t);

  for (const Gaussian& g: pth->gaussians())
    fprintf(env_output_file,
            "     %.16f %.16f %.16f",
            g.mean(), g.width(), g.height());

  fprintf(env_output_file, "\n");
}



FILE* open_terminators_stat_file(const char* prefix, const char* postfix) {
  char* term_output_file_name = new char[120];
  sprintf(term_output_file_name, "stats/%s_nb_term%s.out", prefix, postfix);
  FILE* term_output_file = fopen(term_output_file_name, "w");
  delete [] term_output_file_name;

  // Write headers
  fprintf(term_output_file, "# Each line contains : \n");
  fprintf(term_output_file, "#   * Generation\n");
  fprintf(term_output_file, "#   * Genome size\n");
  fprintf(term_output_file, "#   * Terminator number\n");
  fprintf(term_output_file, "#\n");

  return term_output_file;
}

void write_terminators_stats(int64_t t,  Individual* indiv,
                             FILE* term_output_file) {
  fprintf(term_output_file, "%" PRId64 " %" PRId32 " %" PRId32 "\n",
            t,
            indiv->total_genome_size(),
            indiv->nb_terminators());
}



FILE* open_zones_stat_file(const char* prefix, const char* postfix) {
  // Open file
  char* zones_output_file_name = new char[120];
  sprintf(zones_output_file_name, "stats/%s_zones%s.out", prefix, postfix);
  FILE* zones_output_file = fopen(zones_output_file_name, "w");
  delete [] zones_output_file_name;

  // Write headers
  fprintf(zones_output_file, "# Each line contains : Generation, and then, for each zone:\n");
  fprintf(zones_output_file, "#   * Number of activation genes\n");
  fprintf(zones_output_file, "#   * Number of inhibition genes\n");
  fprintf(zones_output_file, "#   * Geometric area of the activation genes\n");
  fprintf(zones_output_file, "#   * Geometric area of the inhibition genes\n");
  fprintf(zones_output_file, "#   * Geometric area of the resulting phenotype\n");
  fprintf(zones_output_file, "#\n");

  return zones_output_file;
}

void write_zones_stats(int64_t t,
                       Individual* indiv,
                       const PhenotypicTargetHandler* phenotypicTargetHandler,
                       FILE* zones_output_file)
{
  assert(phenotypicTargetHandler->phenotypic_target().nb_segments() > 1);

  int16_t nb_segments = phenotypicTargetHandler->phenotypic_target().nb_segments();
  int16_t num_segment = 0;
  PhenotypicSegment** segments =
      phenotypicTargetHandler->phenotypic_target().segments();

  // Tables : index 0 for the 0 segment
  //                1 for the neutral segment
  int32_t nb_genes_activ[nb_segments];
  int32_t nb_genes_inhib[nb_segments];
  double  geom_area_activ[nb_segments];
  double  geom_area_inhib[nb_segments];
  double  geom_area_phen[nb_segments];

  for (num_segment = 0 ; num_segment < nb_segments ; num_segment++)
  {
    nb_genes_activ[num_segment]   = 0;
    nb_genes_inhib[num_segment]   = 0;
    geom_area_activ[num_segment]  = 0.0;
    geom_area_inhib[num_segment]  = 0.0;
    geom_area_phen[num_segment]   = 0.0;
  }


  AbstractFuzzy* activ = NULL;
  AbstractFuzzy* inhib = NULL;
  Phenotype* phen  = NULL;



  // Compute number of genes in each segment
  for (const auto& prot: indiv->protein_list()) {
    // Go to the corresponding segment
    num_segment = 0;
    while (prot->mean() > segments[num_segment]->stop)
    {
      num_segment++;
    }

    // Add a genes (activ or inhib)
    if (prot->is_functional())
    {
      if (prot->height() > 0)
      {
        nb_genes_activ[num_segment]++;
      }
      else if (prot->height() < 0)
      {
        nb_genes_inhib[num_segment]++;
      }

      // It the gene is exactly at the frontier between 2 zones, mark it in both
      if (prot->mean() == segments[num_segment]->stop && num_segment < nb_segments - 1)
      {
        if (prot->height() > 0)
        {
          nb_genes_activ[num_segment+1]++;
        }
        else if (prot->height() < 0)
        {
          nb_genes_inhib[num_segment+1]++;
        }
      }
    }
  }

  // Compute the geometric areas
  activ = indiv->phenotype_activ();
  inhib = indiv->phenotype_inhib();
  phen  = indiv->phenotype();

  for (num_segment = 0 ; num_segment < nb_segments ; num_segment++)
  {
    geom_area_activ[num_segment]  = activ->get_geometric_area(segments[num_segment]->start, segments[num_segment]->stop);
    geom_area_inhib[num_segment]  = inhib->get_geometric_area(segments[num_segment]->start, segments[num_segment]->stop);
    geom_area_phen[num_segment]   = phen->get_geometric_area(segments[num_segment]->start, segments[num_segment]->stop);
  }


  // Print stats to file
  fprintf(zones_output_file, "%" PRId64, t);

  for (num_segment = 0 ; num_segment < nb_segments ; num_segment++)
  {
    fprintf(zones_output_file, "     %" PRId32 " %" PRId32 " %lf %lf %lf",
              nb_genes_activ[num_segment],
              nb_genes_inhib[num_segment],
              geom_area_activ[num_segment],
              geom_area_inhib[num_segment],
              geom_area_phen[num_segment]);
  }

  fprintf(zones_output_file, "\n");
}



FILE* open_operons_stat_file(const char* prefix, const char* postfix) {
  char* operons_output_file_name = new char[120];
  sprintf(operons_output_file_name, "stats/%s_operons%s.out", prefix, postfix);
  FILE* operons_output_file = fopen(operons_output_file_name, "w");
  delete [] operons_output_file_name,

  // Write headers
  fprintf(operons_output_file, "# Each line contains : Generation, and then, for 20 RNA, the number of genes inside the RNA\n");
  return operons_output_file;
}

void write_operons_stats(int64_t t, Individual* indiv, FILE*  operons_output_file)
{
  int32_t nb_genes_per_rna[20];
  for (int i = 0 ; i < 20 ; i++)
  {
    nb_genes_per_rna[i] = 0;
  }

  for (const auto& rna: indiv->rna_list()) {
    if (rna->transcribed_proteins().size() >= 20)
    {
      printf("Found operon with 20 genes or more : %zu\n", rna->transcribed_proteins().size());
    }

    nb_genes_per_rna[rna->transcribed_proteins().size()]++;
  }

  fprintf(operons_output_file, "%" PRId64 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 " %" PRId32 "\n",
            t,
            nb_genes_per_rna[0],
            nb_genes_per_rna[1],
            nb_genes_per_rna[2],
            nb_genes_per_rna[3],
            nb_genes_per_rna[4],
            nb_genes_per_rna[5],
            nb_genes_per_rna[6],
            nb_genes_per_rna[7],
            nb_genes_per_rna[8],
            nb_genes_per_rna[9],
            nb_genes_per_rna[10],
            nb_genes_per_rna[11],
            nb_genes_per_rna[12],
            nb_genes_per_rna[13],
            nb_genes_per_rna[14],
            nb_genes_per_rna[15],
            nb_genes_per_rna[16],
            nb_genes_per_rna[17],
            nb_genes_per_rna[18],
            nb_genes_per_rna[19]);
}

void interpret_cmd_line_options(int argc, char* argv[]) {
  // =====================
  //  Parse command line
  // =====================
  const char * short_options = "hVF:vM";
  static struct option long_options[] = {
    {"help",                no_argument, NULL, 'h'},
    {"version",             no_argument, NULL, 'V'},
    {"full-check",          no_argument, NULL, 'F'},
    {"trace-mutations",     no_argument, NULL, 'M'},
    {"verbose",             no_argument, NULL, 'v'},
    {0, 0, 0, 0}
  };

  int option;
  while((option = getopt_long(argc, argv, short_options,
                              long_options, nullptr)) != -1) {
    switch(option) {
      case 'h':
        print_help(argv[0]);
        exit(EXIT_SUCCESS);
      case 'V':
        Utils::PrintAevolVersion();
        exit(EXIT_SUCCESS);
      case 'v':
        verbose = true;
        break;
      case 'F':
        full_check = true;
        break;
      case 'M':
        trace_mutations = true;
        break;
      default:
        // An error message is printed in getopt_long, we just need to exit
        exit(EXIT_FAILURE);
    }
  }

  // There should be only one remaining arg: the lineage file
  if (optind != argc - 1) {
    Utils::ExitWithUsrMsg("please specify a lineage file");
  }

  lineage_file_name = new char[strlen(argv[optind]) + 1];
  sprintf(lineage_file_name, "%s", argv[optind]);
}

void print_help(char* prog_path) {
  // Get the program file-name in prog_name (strip prog_path of the path)
  char* prog_name; // No new, it will point to somewhere inside prog_path
  if ((prog_name = strrchr(prog_path, '/'))) {
    prog_name++;
  }
  else {
    prog_name = prog_path;
  }

  printf("******************************************************************************\n");
  printf("*                                                                            *\n");
  printf("*                        aevol - Artificial Evolution                        *\n");
  printf("*                                                                            *\n");
  printf("* Aevol is a simulation platform that allows one to let populations of       *\n");
  printf("* digital organisms evolve in different conditions and study experimentally  *\n");
  printf("* the mechanisms responsible for the structuration of the genome and the     *\n");
  printf("* transcriptome.                                                             *\n");
  printf("*                                                                            *\n");
  printf("******************************************************************************\n");
  printf("\n");
  printf("%s: create an experiment with setup as specified in PARAM_FILE.\n",
  prog_name);
  printf("\n");
  printf("Usage : %s -h or --help\n", prog_name);
  printf("   or : %s -V or --version\n", prog_name);
  printf("   or : %s LINEAGE_FILE [-FMv]\n",
  prog_name);
  printf("\nOptions\n");
  printf("  -h, --help\n\tprint this help, then exit\n");
  printf("  -V, --version\n\tprint version number, then exit\n");
  printf("  -F, --full-check\n");
  printf("\tperform genome checks whenever possible\n");
  printf("  -M, --trace-mutations\n");
  printf("\toutputs the fixed mutations (in a separate file)\n");
  printf("  -v, --verbose\n\tbe verbose\n");
}
