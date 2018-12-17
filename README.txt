Ruhani Mumick & Alex Muralles
02-512 Final project 

KCUTSOLVER.PY AND SUPPORTING SNIPPETS OF CODE

———————— FEATURED FILES ————————

finalProjectR.txt - R code using the bioconductor package to process Gene Ontology Data straight from the gene ontology database 

———————— FILE OUTPUT TYPE ————————

tabulated textile in the following format: 

ID_REF IDENTIFIER GSM1626004 GSM1626005 GSM1626006 GSM1625995 GSM1625996 GSM1625997 GSM1626007 GSM1626008 GSM1626009 GSM1625998 GSM1625999 GSM1626000 GSM1626010 GSM1626011 GSM1626012 GSM1626001 GSM1626002 GSM1626003

randomizeSelection.py - Python code to select randomly from the tabulated file input, used for runtime analysis and data selection (no inputs, used in shell)

kCutSolver.py- Main Python Script, used to generate graph and run k-cut solver 

———————— kCutSolver.py Documentation ————————

CALLING: 
python kCutSolver.py [Processed Microarray Filename (see above for format)] [k] [function Option (1,2)] [Edge Threshold for graph creation] [Cost Threshold (for brute force only)]

[Processed Microarray Filename (see above for format)] - tabulated text file
[k]- # of clusters, int
[function Option (1,2)] - 1 = greedy algorithm, 2 = brute force algorithm 
[Edge Threshold for graph creation] - minimum weight required to form an edge on the graph, will be done in graph creation
[Cost Threshold (for brute force only)] - cost threshold for brute force algorithm, optional


OUTPUT: 
kCutSolverOutput.txt



