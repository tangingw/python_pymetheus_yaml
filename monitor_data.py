import importlib


def get_monitor_data(module_name, module_class_name, method_name, *args, **kwargs):

    try:

        my_module = importlib.import_module(module_name)

    except ModuleNotFoundError:

        try:
            my_module = importlib.import_module("monitor.monitor_{0}".format(module_name))

        except ModuleNotFoundError as error_msg:

            return error_msg
 
    my_class = getattr(my_module, module_class_name)()

    if hasattr(my_class, method_name):
        return getattr(my_class, method_name)(*args, **kwargs)
    
    return {
        "status_code": 500,
        "error_msg": "method_not_found"
    }
