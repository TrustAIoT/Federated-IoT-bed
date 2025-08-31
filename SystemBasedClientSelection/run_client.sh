#!/usr/bin/env bash
RANK=$1
python3 main_fedml_system_selection.py --cf config/fedml_config.yaml --run_id heart_disease --rank $RANK --role client
