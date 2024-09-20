#!/bin/bash

echo "The date and time"
date

echo "Let's see who is logged into the system."
who 

user=-$(whoami)
home=$HOME

echo "For $user, the home directory $home"
