curl --silent $1 | grep http | cut -d "\"" -f 2 
