import base64
from seleniumbase import SB

# Ask the user for base64 input
b_input = 'aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM='
jor = base64.b64decode(b_input)
jrdn = jor.decode('utf-8')
with SB(uc=True, test=True) as jordan:
    url = jrdn
    jordan.uc_open_with_reconnect(url, 5)
    jordan.uc_gui_click_captcha()
    jordan.sleep(2)
    jordan.uc_gui_handle_captcha()
    while(jordan.is_element_present('video#video-player')):
        jordan.sleep(10)
