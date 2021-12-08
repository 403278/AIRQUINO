| Supported Targets | RPi 4 | RPi 3b+ |
| ----------------- | ----- | -------- |

Raspberry Pi 4 Data Collector scripts
==============================================

These are the scripts that we have created for collecting and storing air quality values.

The Python scripts that starts with `read_Zone` are the ones that connects to the Range_Extender ESP's that are advertising the air quality values of the sensors. And the Bash scripts starting with `write_` are the ones that runs the Python scripts according the location of the zones. Every Python scripts according the location of the zones appends the air quality values to a .csv file.

To test this example, you can run the [gatt_client_demo](../../ble/gatt_client), which can scan for and connect to this example automatically, and run [gatt_server_demo](../../ble/gatt_server), Waiting to be connected. They will start exchanging data once the GATT client has enabled the notification function of the GATT server.

Please check the [tutorial](../../ble/gatt_server/tutorial/Gatt_Server_Example_Walkthrough.md) for more information about the gatts part of this example.
Please check the [tutorial](../../ble/gatt_client/tutorial/Gatt_Client_Example_Walkthrough.md) for more information about the gattc part of this example.