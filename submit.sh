#!/bin/bash
#SBATCH --job-name=game_job
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH --account=ta016
#SBATCH --partition=standard
#SBATCH --qos=standardSBATCH

module load epcc-job-env
module load cray-python

python setup.py build
