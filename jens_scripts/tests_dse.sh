#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
FILES=("spec_gobmk_002.champsimtrace.xz" "spec_gobmk_001.champsimtrace.xz" "server_027.champsimtrace.xz" "server_026.champsimtrace.xz")
for f in ${FILES[@]};
do
    echo $f
    echo "[|____________]"    
    ./run_champsim.sh hashed_perceptron-tap_nd4-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||___________]"  
    ./run_champsim.sh hashed_perceptron-tap_nd8-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[|||__________]"      
    ./run_champsim.sh hashed_perceptron-tap_nd10-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||||_________]"      
    ./run_champsim.sh hashed_perceptron-tap_nd12-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[|||||________]"      
    ./run_champsim.sh hashed_perceptron-tap_hist8-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||||||_______]"      
    ./run_champsim.sh hashed_perceptron-tap_hist12-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[|||||||______]"      
    ./run_champsim.sh hashed_perceptron-tap_hist16-next_line-spp_dev-no-lru-1core 50 50 $f
    echo "[||||||||_____]"      
    ./run_champsim.sh gshare-pips_scout1-no-no-no-lru-1core 50 50 $f
    echo "[|||||||||____]"      
    ./run_champsim.sh gshare-pips_scout2-no-no-no-lru-1core 50 50 $f
    echo "[||||||||||___]"      
    ./run_champsim.sh gshare-pips_scout8-no-no-no-lru-1core 50 50 $f
    echo "[|||||||||||__]"      
    ./run_champsim.sh gshare-pips_tag8-no-no-no-lru-1core 50 50 $f
    echo "[||||||||||||_]"      
    ./run_champsim.sh gshare-pips_tag12-no-no-no-lru-1core 50 50 $f
    echo "[|||||||||||||]"      
    ./run_champsim.sh gshare-pips_tag24-no-no-no-lru-1core 50 50 $f      
done
