#!/bin/bash

echo '  
  #####                                    #                     
 #     # #    # ###### #####  #####  #   # #         ##   #####  
 #       #    # #      #    # #    #  # #  #        #  #  #    # 
 #       ###### #####  #    # #    #   #   #       #    # #####  
 #       #    # #      #####  #####    #   #       ###### #    # 
 #     # #    # #      #   #  #   #    #   #       #    # #    # 
  #####  #    # ###### #    # #    #   #   ####### #    # #####  
                                                                 '
echo -e 'Non-scientific computation engine'
echo -e 'Run your JavaScript code in CherryLab!'
echo -e 'Input you JavaScript code (end with "EOF")\n'

echo "" > /jerry.js

while read -t 30 input; do
    if [ "$input" = "EOF" ]; then
        break
    fi
    echo "$input" >> /jerry.js
done

/jerry /jerry.js
