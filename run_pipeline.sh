dvc exp run -f
#-f forces to rerun all the stages of the pipeline, even if no changes were found
# the differente between dvc exp run and dvc repro is that exp run will save the results
# as an experiment (and has experiment related features
# https://dvc.org/doc/user-guide/experiment-management/running-experiments)
