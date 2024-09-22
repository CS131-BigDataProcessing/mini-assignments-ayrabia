#!/bin/bash

#Defining the decimal places and using bc
floating=$(echo "scale=3; 4.5/2.7" | bc)

#Displaying the result
echo "Our floating variable is $floating"


