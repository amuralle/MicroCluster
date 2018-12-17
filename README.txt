Ruhani Mumick & Alex Muralles

KCUTSOLVER.PY AND SUPPORTING SNIPPETS OF CODE

———————— INPUT FORMAT ———————

All files converted to a tabulated format from the NCBI GEO gene ontology database using the bioconductor package in R, sample R-script below: 

library(Biobase)
library(GEOquery)
gds6010 <- getGEO("GDS6010")
write.table(Table(gds6010), file = "gds6010.txt")

tabulated textfile in the following format: 

ID_REF IDENTIFIER GSM1626004 GSM1626005 GSM1626006 GSM1625995 GSM1625996 GSM1625997 GSM1626007 GSM1626008 GSM1626009 GSM1625998 GSM1625999 GSM1626000 GSM1626010 GSM1626011 GSM1626012 GSM1626001 GSM1626002 GSM1626003

Currently script only suitable for 18-sample databases, but can (and will) easily be fitted for more


———————— FILE OUTPUT TYPE ————————

randomizeSelection.py - Python code to select randomly from the tabulated file input, used for runtime analysis and data selection (no inputs, used in shell)

kCutSolver.py- Main Python Script, used to generate graph and run k-cut solver 

———————— USAGE ————————

CALLING: 
python kCutSolver.py [Processed Microarray Filename (see above for format)] [k] [function Option (1,2)] [Edge Threshold for graph creation] [Cost Threshold (for brute force only)]

[Processed Microarray Filename (see above for format)] - tabulated text file
[k]- # of clusters, int
[function Option (1,2)] - 1 = greedy algorithm, 2 = brute force algorithm 
[Edge Threshold for graph creation] - minimum weight required to form an edge on the graph, will be done in graph creation
[Cost Threshold (for brute force only)] - cost threshold for brute force algorithm, optional


OUTPUT: 
kCutSolverOutput.txt



