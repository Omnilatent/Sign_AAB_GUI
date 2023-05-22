#!/bin/zsh
cd "$(dirname "$0")"
7z d Android.aab META-INF
read -p "Press enter to continue"