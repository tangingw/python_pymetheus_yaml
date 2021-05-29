import yaml
import pytest
from yaml import loader
from monitor_data import get_monitor_data


@pytest.fixture
def load_yaml_config():
    new_config = None

    with open("new_config.yaml", "r") as yaml_file:
        new_config = yaml.load(yaml_file.read(), Loader=yaml.CLoader)

    return new_config


def test_yaml_cpu(load_yaml_config):

    new_config = load_yaml_config["monitoring"]
    monitor_data = get_monitor_data(
        "monitor.monitor_{0}".format(new_config[0]["type"]),
        "Monitor{0}".format(new_config[0]["category"][0].upper() + new_config[0]["category"][1:]),
        "get_{0}".format(new_config[0]["monitor"])
    )
    assert isinstance(monitor_data, dict)
    assert set(["cpu_percent_overall", "cpu_percent_per_cpu"]) == set(monitor_data.keys())


def test_yaml_memory(load_yaml_config):
    new_config = load_yaml_config["monitoring"]
    monitor_data = get_monitor_data(
        "monitor.monitor_{0}".format(new_config[1]["type"]),
        "Monitor{0}".format(new_config[1]["category"][0].upper() + new_config[1]["category"][1:]),
        "get_{0}".format(new_config[1]["monitor"])
    )
    assert isinstance(monitor_data, dict)
    assert set(["total", "available", "usage_percent", "used"]) == set(monitor_data.keys())


def test_yaml_network(load_yaml_config):
    new_config = load_yaml_config["monitoring"]
    monitor_data = get_monitor_data(
        "monitor.monitor_{0}".format(new_config[2]["type"]),
        "Monitor{0}".format(new_config[2]["category"][0].upper() + new_config[2]["category"][1:]),
        "get_{0}".format(new_config[2]["monitor"])
    )
    assert isinstance(monitor_data, dict)
    assert set(["network_interfaces", "network_netstats"]) == set(monitor_data.keys())
