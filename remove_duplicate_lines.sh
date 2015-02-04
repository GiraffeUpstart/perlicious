# Remove duplicate lines in every .txt file in folder
#!/bin/bash

shopt -s nullglob
filearray=( *.txt )

for file in "${filearray[@]}"; do
    awk '!x[$0]++' "$file" > "$file".new
mv "$file".new "$file"
done
