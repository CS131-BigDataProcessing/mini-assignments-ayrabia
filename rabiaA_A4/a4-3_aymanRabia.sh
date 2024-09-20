#!/bin/bash


#assign 5+1 to mathvar
mathvar1=$((1+5))

#calculate mathvar2 with mathvar1
mathvar2=$((mathvar1 * 20))

mathvar3=10

#calculate mathvar4
mathvar4=$((mathvar1*(mathvar2+mathvar3)))

echo "mathvar1: $mathvar1"
echo "mathvar2: $mathvar2"
echo "mathvar4: $mathvar4"




