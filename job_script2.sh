#!/bin/bash
#SBATCH -p RM-shared
#SBATCH -t 6:00:00
#SBATCH --ntasks-per-node=30

#echo commands to stdout
#set -x

module load anaconda3/2024.10-1
module load fftw/3.3.8
module load gcc/13.2.1-p20240113   
module load openmpi/5.0.3-gcc13.2.1

conda activate 21cmFASTv4
cd /jet/home/breitman/EOSv4

python run_ICs_PFs.py
