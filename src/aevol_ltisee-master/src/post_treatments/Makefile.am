############################################
#           Set a few variables            #
############################################
AM_CPPFLAGS = $(AEVOLCPPFLAGS)
AM_CXXFLAGS = $(AEVOLCXXFLAGS)
AM_LDFLAGS = $(AEVOLLDFLAGS)

AM_CPPFLAGS += -I$(top_srcdir)/src/libaevol
AM_LDFLAGS  += -L$(top_srcdir)/src/libaevol

############################################
#         Set aevol library to use         #
############################################
LDADD = $(top_srcdir)/src/libaevol/libaevol.a $(top_srcdir)/src/libaevol/SFMT-src-1.4/libsfmt.a


############################################
# C99 exact-width integer specific support #
############################################
# __STDC_FORMAT_MACROS allows us to use exact-width integer format specifiers e.g. PRId32 (for printf etc)
# __STDC_CONSTANT_MACROS allows us to define exact-width integer macros with e.g. INT32_C( <value> )
# __STDC_LIMIT_MACROS allows us to use exact-width integer limit macros with e.g. INT32_MAX
AM_CPPFLAGS += -D__STDC_FORMAT_MACROS -D__STDC_CONSTANT_MACROS -D__STDC_LIMIT_MACROS


####################################
# Add hardening option to compiler #
####################################
# This replaces insecure unlimited length buffer function calls with
# length-limited ones (required for debian and not a bad idea anyway).
AM_CPPFLAGS += -D_FORTIFY_SOURCE=2


############################################
#           Set programs to build          #
############################################
bin_PROGRAMS = \
aevol_misc_ancestor_stats \
aevol_misc_ancestor_robustness \
aevol_misc_create_eps \
aevol_misc_extract \
aevol_misc_lineage \
aevol_misc_mutagenesis \
aevol_misc_robustness \
aevol_misc_ancestor_mutagenesis \
aevol_misc_coalescence \
aevol_misc_protein_map
# aevol_misc_gene_families
# aevol_misc_transform_plasmid

if WITH_X
  bin_PROGRAMS += aevol_misc_view
endif # X
# noinst_PROGRAMS = aevol_misc_template

CLEANFILES = $(bin_PROGRAMS)

aevol_misc_ancestor_stats_SOURCES = ancestor_stats.cpp
aevol_misc_ancestor_robustness_SOURCES = ancestor_robustness.cpp IndivAnalysis.cpp
aevol_misc_ancestor_robustness_SOURCES += IndivAnalysis.h # hack to get make dist to include IndivAnalysis.h
aevol_misc_create_eps_SOURCES = create_eps.cpp
aevol_misc_extract_SOURCES = extract.cpp
# aevol_misc_gene_families_SOURCES = gene_families.cpp
aevol_misc_lineage_SOURCES = lineage.cpp
aevol_misc_mutagenesis_SOURCES = mutagenesis.cpp
aevol_misc_ancestor_mutagenesis_SOURCES = ancestor_mutagenesis.cpp IndivAnalysis.cpp
aevol_misc_robustness_SOURCES = robustness.cpp IndivAnalysis.cpp
aevol_misc_robustness_SOURCES += IndivAnalysis.h # hack to get make dist to include IndivAnalysis.h
aevol_misc_coalescence_SOURCES = coalescence.cpp
# aevol_misc_template_SOURCES = template.cpp
# aevol_misc_transform_plasmid_SOURCES = transform_plasmid.cpp
aevol_misc_view_SOURCES = view.cpp
aevol_misc_protein_map_SOURCES = protein_map.cpp
