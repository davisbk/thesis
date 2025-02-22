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

#include <cerrno>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cinttypes>
#include <cmath>
#include <cassert>
#include <getopt.h>
#include <sys/stat.h>
#include <list>
#include <zlib.h>

#include "aevol.h"
#include "IndivAnalysis.h"

using std::list;

using namespace aevol;

// =================================================================
//                     Command line option variables
// =================================================================
int32_t wanted_rank = -1;
int32_t wanted_index = -1;
static char* lineage_file_name = nullptr;
int32_t mutation_type = 0;
int32_t nb_mutants = -1;
static int32_t begin = 0; //< First generation to analyse
static int32_t end = -1; //< Last generation to analyse
static int32_t period = 1; //< Period of analysis
static bool verbose = false;
static bool full_output = false;

// =================================================================
//                         Function declarations
// =================================================================
void print_help(char* prog_path);
void interpret_cmd_line_options(int argc, char* argv[]);
int write_headers(FILE* output_file,bool full_output);

int main(int argc, char* argv[]) {
  interpret_cmd_line_options(argc, argv);

  // =======================
  //  Open the lineage file
  // =======================
  gzFile lineage_file = gzopen(lineage_file_name, "r");
  if (lineage_file == Z_NULL) {
    Utils::ExitWithUsrMsg(std::string("Could not read lineage file ") +
                          lineage_file_name + "\n");
  }

  int64_t t0 = 0;
  int64_t t_end = 0;
  int32_t final_indiv_index = 0;
  int32_t final_indiv_rank = 0;

  gzread(lineage_file, &t0, sizeof(t0));
  gzread(lineage_file, &t_end, sizeof(t_end));
  gzread(lineage_file, &final_indiv_index, sizeof(final_indiv_index));
  gzread(lineage_file, &final_indiv_rank, sizeof(final_indiv_rank));

  if (verbose) {
    printf("\n\n");
    printf(
        "===============================================================================\n");
    printf(" Mutagenesis analysis of the ancestors of indiv. %"
    PRId32
    " (rank %"
    PRId32
    ") from time %"
    PRId64
    " to %"
    PRId64
    "\n",
        final_indiv_index, final_indiv_rank, t0, t_end);
    printf(
        "================================================================================\n");
  }

  // =============================
  //  Open the experience manager
  // =============================
  ExpManager* exp_manager = new ExpManager();
  exp_manager->load(t0, true, false);

  // The current version doesn't allow for phenotypic variation nor for
  // different phenotypic targets among the grid
  if (not exp_manager->world()->phenotypic_target_shared()) {
    Utils::ExitWithUsrMsg("sorry, ancestor stats has not yet been implemented "
                              "for per grid-cell phenotypic target\n");
  }
  auto phenotypicTargetHandler =
      exp_manager->world()->phenotypic_target_handler();
  if (phenotypicTargetHandler->var_method() != NO_VAR) {
    Utils::ExitWithUsrMsg("sorry, ancestor stats has not yet been implemented "
                              "for variable phenotypic targets\n");
  }

  // =========================
  //  Open the output file(s)
  // =========================

char mutation_type_name[24];
  switch (mutation_type) {
    case SWITCH: {
      snprintf(mutation_type_name, 23, "point-mutation");
      break;
    }
    case S_INS: {
      snprintf(mutation_type_name, 23, "small-insertion");
      printf("mutation-type : small insertions\n");
      break;
    }
    case S_DEL: {
      snprintf(mutation_type_name, 23, "small-deletion");
      break;
    }
    case DUPL: {
      snprintf(mutation_type_name, 23, "duplication");
      break;
    }
    case DEL: {
      snprintf(mutation_type_name, 23, "large-deletion");
      break;
    }
    case TRANS: {
      snprintf(mutation_type_name, 23, "translocation");
      break;
    }
    case INV: {
      snprintf(mutation_type_name, 23, "inversion");
      break;
    }
    default: {
      fprintf(stderr, "Error, unexpected mutation type.\n");
      exit(EXIT_FAILURE);
    }
  }

   char output_file_name[256];
  snprintf(output_file_name, 255,
           "mutagenesis-n%d-%s.txt",nb_mutants,mutation_type_name);

  printf("%s\n",output_file_name);
  
  FILE* output_summary = fopen(output_file_name, "w");
  if (output_summary == nullptr) {
    Utils::ExitWithUsrMsg(std::string("Could not create ") + output_file_name);
  }

  printf("ouput file opened\n");
  write_headers(output_summary,full_output);

  std::shared_ptr <JumpingMT> prng = std::make_shared<JumpingMT>(9695);

  // ==============================
  //  Prepare the initial ancestor 
  // ==============================
  GridCell* grid_cell = new GridCell(lineage_file, exp_manager, nullptr);
  IndivAnalysis indiv(*(grid_cell->individual()));
  indiv.Evaluate();
  //  indiv->compute_statistical_data();
  //  indiv->compute_non_coding();



  if(begin == 0) {
    indiv.compute_experimental_mutagenesis(nb_mutants, mutation_type, prng, output_summary, verbose,full_output);
  }

   // ==========================================================================
  //  Replay the mutations to get the successive ancestors and analyze them
  // ==========================================================================
  ReplicationReport* rep = nullptr;

  int32_t index;

  aevol::AeTime::plusplus();
  while ((time() <= t_end) && (((time() < end) || (end == -1)))) {
    rep = new ReplicationReport(lineage_file, &indiv);
    index = rep->id(); // who we are building...
    indiv.Reevaluate();

    if (verbose) {
      printf("Ancestor at generation %"
      PRId64
      " has index %"
      PRId32
      "\n", time(), index);
    }


    // 2) Replay replication (create current individual's child)
    GeneticUnit& gen_unit = indiv.genetic_unit_nonconst(0);


    // For each genetic unit, replay the replication (undergo all mutations)
    // TODO <david.parsons@inria.fr> disabled for multiple GUs
    const auto& dnarep = rep->dna_replic_report();

    for (const auto& mut: dnarep.HT())
      gen_unit.dna()->undergo_this_mutation(*mut);
    for (const auto& mut: dnarep.rearrangements())
      {
      gen_unit.dna()->undergo_this_mutation(*mut);
          // 3) All the mutations have been replayed, we can now evaluate the new individual
    indiv.Reevaluate();

    // if we are between "begin" and "end" and at the correct period, compute robustness

    if ((time() >= begin) && ((time() < end) || (end == -1)) &&
        (((time() - begin) % period) == 0)) {
      indiv.compute_experimental_mutagenesis(nb_mutants, mutation_type, prng, output_summary,
					     verbose,full_output);
      }
      }
    for (const auto& mut: dnarep.mutations())
      {
      gen_unit.dna()->undergo_this_mutation(*mut);
          // 3) All the mutations have been replayed, we can now evaluate the new individual
    indiv.Reevaluate();

    // if we are between "begin" and "end" and at the correct period, compute robustness

    if ((time() >= begin) && ((time() < end) || (end == -1)) &&
        (((time() - begin) % period) == 0)) {
      indiv.compute_experimental_mutagenesis(nb_mutants, mutation_type, prng, output_summary,verbose,full_output);
    }
      }
    // 3) All the mutations have been replayed, we can now evaluate the new individual
    //GB indiv.Reevaluate();

    // if we are between "begin" and "end" and at the correct period, compute robustness

    //GB if ((time() >= begin) && ((time() < end) || (end == -1)) &&
    //GB    (((time() - begin) % period) == 0)) {
    //GB  indiv.compute_experimental_f_nu(nb_mutants, prng, output_summary, nullptr,
    //GB                                  verbose);
    //GB}
    delete rep;

    aevol::AeTime::plusplus();
  }

  gzclose(lineage_file);
  fclose(output_summary);
  delete exp_manager;
  return EXIT_SUCCESS;
}


void interpret_cmd_line_options(int argc, char* argv[]) {
  const char* short_options = "hVvfm:n:b:e:P:o:";
  static struct option long_options[] = {
        {"help",        no_argument,       nullptr, 'h'},
        {"version",     no_argument,       nullptr, 'V'},
        {"verbose",     no_argument,       nullptr, 'v'},
	{"full",        no_argument,       nullptr, 'f'},
	{"mutation-type", required_argument, nullptr, 'm'},
        {"nb-mutants",  required_argument, nullptr, 'n'},
        {"begin",       required_argument, nullptr, 'b'},
        {"end",         required_argument, nullptr, 'e'},
        {"period",      required_argument, nullptr, 'P'},
        {0, 0, 0, 0}
    };

  int option;
  while ((option = getopt_long(argc, argv, short_options, long_options,
                               nullptr)) != -1) {
    switch (option) {
      case 'h' :
        print_help(argv[0]);
        exit(EXIT_SUCCESS);
      case 'V' :
        Utils::PrintAevolVersion();
        exit(EXIT_SUCCESS);
      case 'v' :
        verbose = true;
        break;
    case 'f' :
      full_output = true;
      break;
      case 'b' :
        begin = atol(optarg);
        break;
      case 'e' :
        end = atol(optarg);
        break;
    case 'm':
        mutation_type = (MutationType) atol(optarg);
        if (mutation_type == SWITCH) {
        }
        else if ((mutation_type == S_INS) || (mutation_type == S_DEL) ||
                 (mutation_type == DUPL) || (mutation_type == DEL) ||
                 (mutation_type == TRANS) || (mutation_type == INV)) {
        }
        else {
          fprintf(stderr,
                  "%s: error: So far, mutagenesis is implemented only for "
                      "point mutations, small insertions, \n"
                      "           small deletions, duplications, deletions, "
                      "translocations or inversions.\n"
                      "           It is not available yet for lateral transfer.\n",
                  argv[0]);
          exit(EXIT_FAILURE);
        }
        break;
      case 'n' :
        nb_mutants = atol(optarg);
        break;
      case 'P' :
        period = atol(optarg);
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
  printf("%s: generate and analyse mutants for the provided lineage.\n",
         prog_name);
  printf("\n");
  printf("Usage : %s -h or --help\n", prog_name);
  printf("   or : %s -V or --version\n", prog_name);
  printf("   or : %s LINEAGE_FILE [-b TIMESTEP] [-e TIMESTEP] [-n NB_MUTANTS] [-P PERIOD] [-o output] [-v]\n",
         prog_name);
  printf("\nOptions\n");
  printf("  -h, --help\n\tprint this help, then exit\n");
  printf("  -V, --version\n\tprint version number, then exit\n");
  printf("  -b, --begin TIMESTEP\n");
  printf("\ttimestep at which to start the analysis\n");
  printf("  -e, --end TIMESTEP\n");
  printf("\ttimestep at which to stop the analysis\n");
  printf("  -n, --nb-mutants NB_MUTANTS\n");
  printf("\tnumber of mutants to be generated\n");
  printf("\t-m MUTATIONTYPE or --mutation-type MUTATIONTYPE : \n");
  printf(
      "\t                  Integer type of the mutation carried by each mutant: 0 for a point mutation, 1 for a \n");
  printf(
      "\t                  small insertion, 2 for small deletions, 3 for a duplication, 4 for a large deletion, \n");
  printf("\t                  5 for a translocation or 6 for an inversion. \n");
  printf("\n");
    printf("  -f, --full\n");
  printf("\tfull output (otherwize synthetic output will be produced). -f option must be used with care as it may produce very large output files\n");

  printf("  -P, --period\n");
  printf("\tperiod with which to perform the analysis\n");
  printf("  -v, --verbose\n\tbe verbose\n");
}


int write_headers(FILE* output_file,bool full_output) {
   // --------------------------------------
  //  Write headers in robustness files
  // --------------------------------------
  if (!full_output)
    {
  fprintf(output_file,"# ------------------------------------------------------------------\n");
  fprintf(output_file,"# Evolvability, Robustness and Antirobustness statistics for mutants\n");
  fprintf(output_file,"# ------------------------------------------------------------------\n");
  fprintf(output_file,"# \n");
  fprintf(output_file,"# 1. Generation \n");
  fprintf(output_file,"# 2. Fraction of positive mutants  (2*10 is Evolvability) \n");
  fprintf(output_file,"# 3. Fraction of neutral mutants (aka reproductive robustness) \n");
  fprintf(output_file,"# 4. Fraction of neutral mutants (aka mutational robustness) \n");
  fprintf(output_file,"# 5. Fraction of negative mutants \n");
  fprintf(output_file,"# 8. Cumul of delta-gaps of positive mutants\n");
  fprintf(output_file,"# 9. Cumul of delta-gaps of negative mutants\n");
  fprintf(output_file,"# 6. Delta-gap for the best mutants \n");
  fprintf(output_file,"# 7. Delta-gap for the worst mutants \n");
 fprintf(output_file,"# 10. Cumul of delta-fitness of positive mutants (2*10 is Evolvability)\n");
  fprintf(output_file,"# 11. Cumum of delta-fitness of negative mutants\n");
  fprintf(output_file,"# 12. Delta-fitness for the best mutants\n");
  fprintf(output_file,"# 13. Delta-fitness for the worst mutants\n\n\n");
    }
  else
    {
      fprintf(output_file,"# ------------------------------------------------------------------\n");
      fprintf(output_file,"# Evolvability, Robustness and Antirobustness statistics for mutants\n");
      fprintf(output_file,"# ------------------------------------------------------------------\n");
      fprintf(output_file,"# \n");
      fprintf(output_file,"# 1. Generation \n");
      fprintf(output_file,"# 2 to n+2. delta-fitness of each tested mutants \n\n\n");

    }
  return 0;
}
