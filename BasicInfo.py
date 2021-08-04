import obd
connection = obd.OBD()

speed_cmd = obd.commands.SPEED
rpm_cmd = obd.commands.RPM
fuel_level_cmd = obd.commands.FUEL_LEVEL
oil_temp_cmd = obd.commands.OIL_TEMP
load_cmd = obd.commands.ENGINE_LOAD

while True:
	speed = connection.query(speed_cmd).value
	rpm = connection.query(rpm_cmd).value
	fuel_level = connection.query(fuel_level_cmd).value
	oil_temp = connection.query(oil_temp_cmd).value
	load = connection.query(load_cmd).value
	print(f"Speed: {speed}KM/H, RPM: {rpm}, Engine Load: {load}%, Fuel Level: {fuel_level}%, Oil Temp: {oil_temp} C", end='\r')