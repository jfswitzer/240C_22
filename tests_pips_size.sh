#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
FILES=("spec_gobmk_002.champsimtrace.xz" "spec_gobmk_001.champsimtrace.xz" "server_027.champsimtrace.xz" "server_026.champsimtrace.xz")
for f in ${FILES[@]};
do
    echo $f
    echo "[||||||||_____]"      
    ./run_champsim.sh gshare-pips_size1-no-no-no-lru-1core 50 50 $f
    echo "[|||||||||____]"      
    ./run_champsim.sh gshare-pips_size2-no-no-no-lru-1core 50 50 $f
    echo "[||||||||||___]"      
    ./run_champsim.sh gshare-pips_size3-no-no-no-lru-1core 50 50 $f
    echo "[|||||||||||__]"      
    ./run_champsim.sh gshare-pips_size4-no-no-no-lru-1core 50 50 $f
    echo "[||||||||||||_]"      
done
