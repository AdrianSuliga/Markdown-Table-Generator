|Message name|ID|Message Size (bytes)|Signal name|Unit|Endianness|Type|Size (bits)|Scaling|Offset|Min|Max|Value table|Comment|
|---|:---:|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
|MOTOR_POWER|0x00|6||||||||||||
||||MAIN_MOTOR|%|little endian (Intel)|signed|16|0.1|0|-100|100|||
||||PADDLE_MOTOR|%|little endian (Intel)|signed|16|0.1|0|-100|100|||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
|HYDROFOIL_ANGLES|0x01|4||||||||||||
||||LEFT_ANGLE||little endian (Intel)|signed|16|0.01|0|-10|10|||
||||RIGHT_ANGLE||little endian (Intel)|signed|16|0.01|0|-10|10|||
|STEERING_REQUEST|0x05|8||||||||||||
||||HYDROFOIL_CONTROL_MODE||little endian (Intel)|unsigned|8|1|0|0|2|AUTOMATIC/MANUAL_LINEAR_SPLINE_MIXER/MANUAL_ROLL_PID||
||||X_AXIS||little endian (Intel)|unsigned|16|1|0|0|4000|||
||||Y_AXIS||little endian (Intel)|unsigned|16|1|0|0|4000|||
||||COOLING_PUMP||little endian (Intel)|unsigned|8|1|0|0|2|OFF/ON/AUTO||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
|MOTOR_STATUS|0x33|8||||||||||||
||||MOTOR_TEMPERATURE_1|C|little endian (Intel)|unsigned|16|1|0|0|200|||
||||MOTOR_TEMPERATURE_2|C|little endian (Intel)|unsigned|16|1|0|0|200|||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
||||UNUSED2||little endian (Intel)|signed|16|1|0|0|1|||
|BMS_DATA|0x34|8||||||||||||
||||MAX_CELL_VOLTAGE|V|little endian (Intel)|unsigned|16|0.00001|0|0|5|||
||||MIN_CELL_VOLTAGE|V|little endian (Intel)|unsigned|16|0.00001|0|0|5|||
||||DISCHARGE_CURRENT|A|little endian (Intel)|unsigned|16|0.1|0|-20|500|||
||||CHARGE_CURRENT|A|little endian (Intel)|unsigned|16|0.1|0|0|100|||
|MAIN_BOX_TEMP|0x35|8||||||||||||
||||TEMP1|C|little endian (Intel)|unsigned|16|0.01|0|0|200|||
||||TEMP2|C|little endian (Intel)|unsigned|16|0.01|0|0|200|||
||||TEMP3|C|little endian (Intel)|unsigned|16|0.01|0|0|200|||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
|SUPP_BOARD_CURRENTS_1|0x36|8||||||||||||
||||ENGINE_PUMP_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
||||ESC_PUMP_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
||||MAIN_BILGE_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
||||MOTOR_BILGE_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
|SUPP_BOARD_CURRENTS_2|0x37|8||||||||||||
||||FAN_BOX_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
||||FAN_BATTERY_CURRENT|A|little endian (Intel)|unsigned|16|0.001|0|0|5|||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
||||UNUSED2||little endian (Intel)|signed|16|1|0|0|1|||
|SUPP_BOARD_TEMP|0x38|8||||||||||||
||||TEMP1|C|little endian (Intel)|unsigned|16|1|0|0|200|||
||||TEMP2|C|little endian (Intel)|unsigned|16|1|0|0|200|||
||||TEMP3|C|little endian (Intel)|unsigned|16|1|0|0|200|||
||||UNUSED1||little endian (Intel)|signed|16|1|0|0|1|||
|PV_VOLTAGE|0x39|5|||||||||||Message comment|
||||PV_SERIES_IDX||little endian (Intel)|unsigned|8|1|0|0|7|||
||||VOLTAGE|mV|little endian (Intel)|unsigned|32|1|0|0|60000|||
|PV_CURRENT|0x40|5||||||||||||
||||PV_SERIES_IDX||little endian (Intel)|unsigned|8|1|0|0|7|||
||||CURRENT|mA|little endian (Intel)|signed|32|1|0|-4000|6000||Signal comment|
|DMS_INDICATOR|0x41|8||||||||||||
||||DMS_INDICATOR||little endian (Intel)|unsigned|8|1|0|0|1|UNPLUGGED/PLUGGED||
||||UNUSED1||little endian (Intel)|signed|8|1|0|0|1|||
||||UNUSED2||little endian (Intel)|signed|16|1|0|0|1|||
||||UNUSED3||little endian (Intel)|signed|16|1|0|0|1|||
||||UNUSED4||little endian (Intel)|signed|16|1|0|0|1|||
