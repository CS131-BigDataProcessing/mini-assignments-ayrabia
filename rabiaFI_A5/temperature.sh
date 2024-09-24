#!/bin/bash

temperature=$1

if [ "$temperature" -gt 55 ] && [ "$temperature" -lt 67 ]; then
	echo "cold."
elif [ "$temperature" -lt 85 ] && [ "$temperature" -gt 67 ]; then
	echo "nice."
elif [ "$temperature" -gt 85 ]; then
	echo "hot."
else
	echo "freezing."

fi
