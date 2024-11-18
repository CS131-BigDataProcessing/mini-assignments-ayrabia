#!/bin/bash

# Remove trailing spaces and new lines
echo "Cleaning trailing spaces and new lines"
sed -i '' 's/[[:space:]]*$//' AB_NYC_2019.csv


# Replace missing values with 'NA'
echo "Replacing missing values with 'NA'"
awk -F',' 'BEGIN {OFS=","} {for(i=1;i<=NF;i++) if($i=="") $i="NA"; print}' AB_NYC_2019.csv > temp.csv && mv temp.csv AB_NYC_2019.csv

# Remove duplicate entries
echo "Removing duplicate entries"
sort -u AB_NYC_2019.csv -o AB_NYC_2019_cleaned.csv

# Cap the 'price' field at 1000
echo "Capping 'price' values at 1000"
awk -F',' 'BEGIN {OFS=","} {if($5 > 1000) $5=1000; print}' AB_NYC_2019_cleaned.csv > temp.csv && mv temp.csv AB_NYC_2019_cleaned.csv

# Final summary
echo "Preprocessing complete. Cleaned file: AB_NYC_2019_cleaned.csv"

