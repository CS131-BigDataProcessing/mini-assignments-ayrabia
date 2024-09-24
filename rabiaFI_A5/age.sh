#!/bin/bash

ageinput=$1

if [ "$ageinput" -le 13 ]; then
    echo "You're a child"
elif [ "$ageinput" -gt 13 ] && [ "$ageinput" -le 20 ]; then
    echo "You're a teen"
elif [ "$ageinput" -gt 20 ] && [ "$ageinput" -le 65 ]; then
    echo "You're an adult"
else
    echo "You're elderly"
fi
