#!/usr/bin/env bash
#UTF-8
file=$1
hash=$2
line=$(cat $file | grep $2)
hash_type=$(echo $line| awk -F ',' '{print $2}')
password=$(echo $line| awk -F ',' '{print $1}')
salt=$(echo $line| awk -F ',' '{print $4}')

printf "[-]The Hashing Algorithm is $hash_type\n[-]Salt is $salt\n[+]Password: $password\n"
