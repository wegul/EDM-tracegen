#!/bin/bash

dir="2:1"

echo "python data_cleaning.py ${dir}/all-to-all-144-aditya/"
python data_cleaning.py ${dir}/all-to-all-144-aditya/
echo "python slowdown.py ${dir}/all-to-all-144-aditya/"
python slowdown.py ${dir}/all-to-all-144-aditya/
echo "python utilization.py ${dir}/all-to-all-144-aditya"
python utilization.py ${dir}/all-to-all-144-aditya

echo "python data_cleaning.py ${dir}/all-to-all-144-dctcp/"
python data_cleaning.py ${dir}/all-to-all-144-dctcp/
echo "python slowdown.py ${dir}/all-to-all-144-dctcp/"
python slowdown.py ${dir}/all-to-all-144-dctcp/
echo "python utilization.py ${dir}/all-to-all-144-dctcp"
python utilization.py ${dir}/all-to-all-144-dctcp

echo "python data_cleaning.py ${dir}/all-to-all-144-datamining/"
python data_cleaning.py ${dir}/all-to-all-144-datamining/
echo "python slowdown.py ${dir}/all-to-all-144-datamining/"
python slowdown.py ${dir}/all-to-all-144-datamining/
echo "python utilization.py ${dir}/all-to-all-144-datamining"
python utilization.py ${dir}/all-to-all-144-datamining

#echo "python data_cleaning.py permutation-144-aditya/"
#python data_cleaning.py permutation-144-aditya/
#echo "python slowdown.py permutation-144-aditya/"
#python slowdown.py permutation-144-aditya/
#echo "python utilization.py permutation-144-aditya"
#python utilization.py permutation-144-aditya
#
#echo "python data_cleaning.py permutation-144-dctcp/"
#python data_cleaning.py permutation-144-dctcp/
#echo "python slowdown.py permutation-144-dctcp/"
#python slowdown.py permutation-144-dctcp/
#echo "python utilization.py permutation-144-dctcp"
#python utilization.py permutation-144-dctcp
#
#echo "python data_cleaning.py permutation-144-datamining/"
#python data_cleaning.py permutation-144-datamining/
#echo "python slowdown.py permutation-144-datamining/"
#python slowdown.py permutation-144-datamining/
#echo "python utilization.py permutation-144-datamining"
#python utilization.py permutation-144-datamining
