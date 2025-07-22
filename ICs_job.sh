#!/bin/bash
#SBATCH -p EM
#SBATCH -t 12:00:00
#SBATCH --ntasks-per-node=48

#echo commands to stdout
#set -x

module load anaconda3/2024.10-1
module load fftw/3.3.8
module load gcc/13.2.1-p20240113   
module load openmpi/5.0.3-gcc13.2.1

conda activate 21cmFASTv4
cd /jet/home/breitman/EOSv4

21cmfast run ics --param-file EOS25.toml --seed 1234 --cachedir "/ocean/projects/phy210034p/breitman/EOS25/EOS25_L2100_HIIDIM1400_DIM4200"
