#!/bin/bash

echo 'running all core NF'

cd '/root/open5gs/'
./install/bin/open5gs-nrfd -d -c ../VM5GC/config_2smf2upf/nrf.yaml & sleep 5 & \
./install/bin/open5gs-amfd -d -c ../VM5GC/config_2smf2upf/amf_2slices.yaml & \
./install/bin/open5gs-smfd -d -c ../VM5GC/config_2smf2upf/smf1_sd1internet.yaml & \
./install/bin/open5gs-smfd -d -c ../VM5GC/config_2smf2upf/smf2_sd2ims.yaml & \
./install/bin/open5gs-ausfd -d -c ../VM5GC/config_2smf2upf/ausf.yaml & \
./install/bin/open5gs-udmd -d -c ../VM5GC/config_2smf2upf/udm.yaml & \
./install/bin/open5gs-udrd -d -c ../VM5GC/config_2smf2upf/udr.yaml & \
./install/bin/open5gs-pcfd -d -c ../VM5GC/config_2smf2upf/pcf.yaml & \
./install/bin/open5gs-nssfd -d -c ../VM5GC/config_2smf2upf/nssf.yaml & \
./install/bin/open5gs-bsfd -d -c ../VM5GC/config_2smf2upf/bsf.yaml & \

