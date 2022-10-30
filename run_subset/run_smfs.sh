#!/bin/bash

echo 'running NFs: SMF1, SMF2, NRF, AMF'
cd '/root/open5gs/'
./install/bin/open5gs-nrfd -d -c ../VM5GC/config_2smf2upf/nrf.yaml & sleep 5 & \
./install/bin/open5gs-amfd -d -c ../VM5GC/config_2smf2upf/amf_2slices.yaml & \
./install/bin/open5gs-smfd -d -c ../VM5GC/config_2smf2upf/smf1_sd1internet.yaml & \
./install/bin/open5gs-smfd -d -c ../VM5GC/config_2smf2upf/smf2_sd2ims.yaml 
