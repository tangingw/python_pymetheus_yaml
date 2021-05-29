import yaml

from monitor_data import get_monitor_data


new_config = None

with open("new_config.yaml") as yaml_file:
    new_config = yaml.load(yaml_file.read())

monitoring_items = new_config["monitoring"]

for item in monitoring_items:

    print(
        get_monitor_data(
            "monitor.monitor_{0}".format(item["type"]),
            "Monitor{0}".format(item["category"][0].upper() + item["category"][1:]),
            "get_{0}".format(item["monitor"])
        )
    )