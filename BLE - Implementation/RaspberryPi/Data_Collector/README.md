| Supported Targets | RPi 4 | RPi 3b+ |
| ----------------- | ----- | -------- |

Raspberry Pi 4 Data Collector scripts
==============================================

These are the scripts that we have created for collecting and storing air quality values.

The Python scripts that starts with `read_Zone` are the ones that connects to the Range_Extender ESP's that are advertising the air quality values of the sensors. And the Bash scripts starting with `write_` are the ones that runs the Python scripts according the location of the zones. Every Python scripts according the location of the zones appends the air quality values to a .csv file.

To test this example, you can run the `write_TQ5_Zones_to_csv.sh`, which will run 2 more scripts `write_TQ5_Zone1_to_csv.sh` & `write_TQ5_Zone2_to_csv.sh` automatically, but the second script will sleep 20 seconds and then runs afterwards. They will append their air quality values to `TQ5.csv` every time the scripts runs by the scheduled crontab.
