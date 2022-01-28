#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
#FILES=("600.perlbench_s-210B.champsimtrace.xz" "627.cam4_s-573B.champsimtrace.xz" "602.gcc_s-734B.champsimtrace.xz" "628.pop2_s-17B.champsimtrace.xz" "603.bwaves_s-3699B.champsimtrace.xz" "631.deepsjeng_s-928B.champsimtrace.xz" "605.mcf_s-665B.champsimtrace.xz" "638.imagick_s-10316B.champsimtrace.xz" "607.cactuBSSN_s-2421B.champsimtrace.xz" "641.leela_s-800B.champsimtrace.xz" "619.lbm_s-4268B.champsimtrace.xz" "644.nab_s-5853B.champsimtrace.xz" "620.omnetpp_s-874B.champsimtrace.xz" "648.exchange2_s-1699B.champsimtrace.xz" "621.wrf_s-575B.champsimtrace.xz" "649.fotonik3d_s-1176B.champsimtrace.xz" "623.xalancbmk_s-700B.champsimtrace.xz" "654.roms_s-842B.champsimtrace.xz" "625.x264_s-18B.champsimtrace.xz" "657.xz_s-3167B.champsimtrace.xz")
#for f in ${FILES[@]};
#tests for the tap
for f in *.xz
do
    echo $f
    ./run_champsim.sh hashed_perceptron-next_line-next_line-spp_dev-no-lru-1core 50 50 $f
    ./run_champsim.sh hashed_perceptron-tap-next_line-spp_dev-no-lru-1core 50 50 $f
    ./run_champsim.sh gshare-pips-no-no-no-lru-1core 50 50 $f 
done
