#!/bin/bash -l
#PBS -l select=1:ncpus=2:ngpus=0:mem=64gb:mpiprocs=16
#PBS -q q02hal
#PBS -m bea
#PBS -M daniela.breitman@sns.it
#PBS -N EOS25-PFs
conda activate 21cmFASTv4
module load gcc/9.3.0
cd /home/dbreitman/EOS25/EOS25
IDX=0
for j in $(seq 0 10);
    do
    printf "IDX is: $IDX \n"&
    python run_PFs.py  --z_idx $IDX &
    ((++IDX))
    done
wait
