import network

# wlan access
SSID = "wifi_name"
WPA2_PASS = "wifi_password"

ssid_ = SSID
wpa2_pass = WPA2_PASS


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid_, wpa2_pass)
    print("connecting to network...")
    while not sta_if.isconnected():
        pass
        
    print("network config:", sta_if.ifconfig())


do_connect()
