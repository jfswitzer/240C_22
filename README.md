# How to run

1. Download the IPC1 traces (I couldn't push them to GitHub because they're huge). Unzip and copy the xz files into this upper-level folder. I modifed their script to run traces from this folder because it made things marginally easier for my scripting.

2. All of the builds should already be saved to the bin. The scripts for running each of my tests are in this folder as well, and are named as follows:

- Reproducing results: ./tests_repro.sh
- Design space: ./tests_dse.sh
- Varying sizes/resources: ./tests_pip_size.sh, and ./tests_tap_size.sh
- For the latency comparison: ./tests_lat.sh

The only changes made to the winners' code was to modify parameters as noted in the write up.