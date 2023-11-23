import configparser
import os
import unittest
import paho.mqtt.client as mqtt


def get_mqtt_ip():
    config = configparser.ConfigParser()
    if os.name == 'nt':  # Windows系统
        config_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    elif os.name == 'posix':  # Linux或者Mac OS系统
        config_path = '/usr/local/SeerRobotics/vda'
    config_path = os.path.join(config_path, 'config.ini')
    # 读取配置文件
    config.read(config_path)
    ip = config.get('mqtt', 'mqtt_host')
    print("ip:", ip)
    return ip


def get_order_topic():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.getcwd()), 'config.ini')
    # 读取配置文件
    config.read(config_path)
    order = config.get('topic', 'order')
    return order

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_creat_order_jackload_1(self):
        import json
        path_to_B = os.path.abspath("../../VDAExample/order/jack")

        json_filename = 'Transport Order 3066 CubicBeizer2_jackLoad.json'

        json_file_path = os.path.join(path_to_B, json_filename)

        with open(json_file_path, 'r') as json_file:
            json_content = json.load(json_file)
            client = mqtt.Client()
            client.connect(get_mqtt_ip(), 1883, 60)
            client.publish("robot/order", json.dumps(json_content))


    def test_creat_order_jackunload_1(self):
        import json
        path_to_B = os.path.abspath("../../VDAExample/order/jack")

        json_filename = 'Transport Order 3066 CubicBeizer2_jackUnload.json'

        json_file_path = os.path.join(path_to_B, json_filename)

        with open(json_file_path, 'r') as json_file:
            json_content = json.load(json_file)
            client = mqtt.Client()
            client.connect(get_mqtt_ip(), 1883, 60)
            client.publish("robot/order", json.dumps(json_content))

    def test_creat_order_jackunload_3(self):
            import json
            path_to_B = os.path.abspath("../../VDAExample/order/jack")

            json_filename = 'Transport Order 3066 CubicBeizer3_jackLoadAndjackUnload.json'

            json_file_path = os.path.join(path_to_B, json_filename)

            with open(json_file_path, 'r') as json_file:
                json_content = json.load(json_file)
                client = mqtt.Client()
                client.connect(get_mqtt_ip(), 1883, 60)
                client.publish("robot/order", json.dumps(json_content))



class instantActionsTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_creat_order_cancel(self):
        import json
        path_to_B = os.path.abspath("../../VDAExample/instantAcions")

        json_filename = 'Cancel Order InstantAction.json'

        json_file_path = os.path.join(path_to_B, json_filename)

        with open(json_file_path, 'r') as json_file:
            json_content = json.load(json_file)
            client = mqtt.Client()
            client.connect(get_mqtt_ip(), 1883, 60)
            client.publish("robot/instantActions", json.dumps(json_content))


    def test_creat_order_jackunload_1(self):
        import json
        path_to_B = os.path.abspath("../../VDAExample/order/jack")

        json_filename = 'Transport Order 3066 CubicBeizer2_jackUnload.json'

        json_file_path = os.path.join(path_to_B, json_filename)

        with open(json_file_path, 'r') as json_file:
            json_content = json.load(json_file)
            client = mqtt.Client()
            client.connect(get_mqtt_ip(), 1883, 60)
            client.publish("robot/order", json.dumps(json_content))



    def test_creat_order_jackunload_3(self):
            import json
            path_to_B = os.path.abspath("../../VDAExample/order/jack")

            json_filename = 'Transport Order 3066 CubicBeizer3_jackLoadAndjackUnload.json'

            json_file_path = os.path.join(path_to_B, json_filename)

            with open(json_file_path, 'r') as json_file:
                json_content = json.load(json_file)
                client = mqtt.Client()
                client.connect(get_mqtt_ip(), 1883, 60)
                client.publish("robot/order", json.dumps(json_content))


if __name__ == '__main__':
    # unittest.main()
    print(182323-67996)
    print((182323-67996)/1000)
