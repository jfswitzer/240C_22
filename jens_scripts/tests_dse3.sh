#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
FILES=("spec_gobmk_002.champsimtrace.xz" "spec_gobmk_001.champsimtrace.xz" "server_027.champsimtrace.xz" "server_026.champsimtrace.xz")
for f in ${FILES[@]};
do
    echo $f
    ./run_champsim.sh gshare-pips_tag4-no-no-no-lru-1core 50 50 $f
    echo "[||||||||||||_]"      
    ./run_champsim.sh gshare-pips_tag2-no-no-no-lru-1core 50 50 $f
done
