#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
FILES=("spec_gobmk_001.champsimtrace.xz" "server_027.champsimtrace.xz" "server_026.champsimtrace.xz")
for f in ${FILES[@]};
do
    echo $f
    echo "[|____________]"    
    ./run_champsim.sh hashed_perceptron-tap_size1-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||___________]"  
    ./run_champsim.sh hashed_perceptron-tap_size2-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[|||__________]"      
    ./run_champsim.sh hashed_perceptron-tap_size3-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||||_________]"      
    ./run_champsim.sh hashed_perceptron-tap_size4-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[|||||________]"      
done
