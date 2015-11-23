#!/usr/bin/python

#This file setup a cluster job then adds it to the MSU queue
#Copyright 2014 Justin R. Klesmith

#First we need to define our residues
#Then we need to create directories for the residues
#Following that we have to write our job submission files, and mutation files
#Then we will submit our jobs to the main cluster

from subprocess import call

Locations = [32,33,34,35,37,62,63,66,67,68,70,73,75,77,78,79,80,81,82,83,84,85,86,87,115,116,118,119,122,123,125,127]
AA_Table = 'ACDEFGHIKLMNPQRSTVWY'

def Sub_Template(Residue, Mutation):
    qsub = """#!/bin/bash -login
    
### define resources needed:
### walltime - how long you expect the job to run
#PBS -l walltime=4:00:00
     
### nodes:ppn - how many nodes & cores per node (ppn) that you require
#PBS -l nodes=1:ppn=1
 
### mem: amount of memory that the job will need
#PBS -l mem=4gb

### you can give your job a name for easier identification
#PBS -N RosettaDDG"""+Residue+Mutation+"""
 
### change to the working directory where your code is located
cd /mnt/home/user/"""+Residue+Mutation+"""/
 
### call your executable
/mnt/home/user/ddg_monomer.linuxgccrelease -in:file:s /mnt/home/user/file.pdb -resfile /mnt/home/user/"""+Residue+Mutation+"""/mutations.res -ddg:weight_file soft_rep_design -ddg:minimization_scorefunction talaris2013 -database /mnt/home/user/rosetta/main/database -fa_max_dis 9.0 -ddg::iterations 50 -ddg::dump_pdbs false -ignore_unrecognized_res -ddg::local_opt_only false -ddg::min_cst true -constraints::cst_file /mnt/home/user/input.cst -ddg::suppress_checkpointing true -in::file::fullatom -ddg::mean false -ddg::min true -ddg::sc_min_only false -ddg::ramp_repulsive true -unmute core.optimization.LineMinimizer -ddg::output_silent true  -override_rsd_type_limit
"""    
    return qsub

def Resfile_Template(Residue, Mutation):
    mut_res = """NATAA
start

"""+str(Residue)+""" A PIKAA """+Mutation+"""
"""
    return mut_res

#The major program loop
for i in enumerate(Locations):

    Residue = str(i[1])

    for j in enumerate(AA_Table):
        
        #Define which mutation
        Mutation = str(j[1])
        
        #Create the directories
        call(["mkdir", Residue+Mutation])
    
        #Write the Sub file
        file = open("./"+Residue+Mutation+"/"+Residue+Mutation+".sub", "w")
        file.write(Sub_Template(Residue, Mutation))
        file.close()
    
        #Write the Resfile
        file = open("./"+Residue+Mutation+"/mutations.res", "w")
        file.write(Resfile_Template(i[1], j[1]))
        file.close()
    
        #Submit to the queue
        call(["qsub", "/mnt/home/user/"+Residue+Mutation+"/"+Residue+Mutation+".sub"])