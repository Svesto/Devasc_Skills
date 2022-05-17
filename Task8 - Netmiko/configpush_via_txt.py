from netmiko import ConnectHandler

Cisco_Switch = {
	'device_type': 'cisco_ios',
	'ip': '192.168.10.97',
	'username': 'admin',
	'password': 'cisco',
}

with open('config.txt') as f:
	lines = f.read().splitlines()
print(lines)

all_devices = [Cisco_Switch]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
  

cisco_Switch = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.10.97",
    username="admin",
    password="cisco"
    )
running=cisco_Switch.send_command("show run")


print(output)
print(running)