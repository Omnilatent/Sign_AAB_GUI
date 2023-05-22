#!/bin/zsh
cd "$(dirname "$0")"
zip -d Android.aab META-INF/\*
read -p "Press enter to continue"