from monitor_data import get_monitor_data


def test_get_monitor_data():

    monitor_data = get_monitor_data(
        "calculator", "Calculator", "return_sum", 5, 6
    )
    assert monitor_data == 11


def test_get_monitor_data():

    monitor_data = get_monitor_data(
        "calculator", "Calculator", "return_multiply", 5, 6
    )
    assert monitor_data == 30
