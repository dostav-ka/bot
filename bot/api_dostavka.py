import requests

from config import DOSTAVKA_HOST, DOSTAVKA_PORT


def send_confirmation_request(courier_id, tg_id):
    url = f"http://{DOSTAVKA_HOST}:{DOSTAVKA_PORT}/courier/{courier_id}/confirm"
    data = {
        "tg_id": tg_id
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def update_order_status(order_id, tg_id, status):
    url = f"http://{DOSTAVKA_HOST}:{DOSTAVKA_PORT}/delivery/order/{order_id}/status"
    data = {
        "tg_id": tg_id,
        "status": status
    }
    try:
        response = requests.post(url, json=data)
        return response.status_code
    except Exception:
        return False


def get_last_orders(tg_id):
    url = f"http://{DOSTAVKA_HOST}:{DOSTAVKA_PORT}/courier/orders"
    params = {'tg_id': tg_id}
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception:
        return None
