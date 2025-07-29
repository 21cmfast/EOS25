#!/bin/bash
#SBATCH -p RM-512
#SBATCH -t 12:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=128

#echo commands to stdout
#set -x

module load anaconda3/2024.10-1
module load fftw/3.3.8
module load gcc/13.2.1-p20240113   
module load openmpi/5.0.3-gcc13.2.1

conda activate 21cmFASTv4
cd /jet/home/breitman/EOSv4
IDX="$1"

printf "IDX is: $IDX \n"&
python run_ten_PFs.py  --z_idx_start $IDX
wait
