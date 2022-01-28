#!/bin/bash
FILES=("spec_gobmk_002.champsimtrace.xz" "spec_gobmk_001.champsimtrace.xz" "server_027.champsimtrace.xz" "server_026.champsimtrace.xz" "server_003.champsimtrace.xz" "server_023.champsimtrace.xz" "server_024.champsimtrace.xz" "server_028.champsimtrace.xz" "server_031.champsimtrace.xz" "server_032.champsimtrace.xz")
for f in ${FILES[@]};
do
    echo $f
    ./run_champsim.sh hashed_perceptron-next_line-next_line-spp_dev-no-lru-1core 50 50 $f
    ./run_champsim.sh hashed_perceptron-tap-next_line-spp_dev-no-lru-1core 50 50 $f
    ./run_champsim.sh gshare-pips-no-no-no-lru-1core 50 50 $f 
done
