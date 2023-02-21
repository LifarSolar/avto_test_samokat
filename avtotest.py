import requests


def test_create_order_and_check_track():
    # Шаг 1: Создаем заказ
    url_create_order = "https://69882277-7404-4b4a-bea9-df1393b6570a.serverhub.praktikum-services.ru"
    payload = {"product": "Test product", "quantity": 1}
    response_create_order = requests.post(url_create_order, json=payload)
    assert response_create_order.status_code == 200, f"Ошибка создания заказа: {response_create_order.content}"
    order_track = response_create_order.json()["track"]

    # Шаг 2: Проверяем, что можно получить данные о заказе по треку
    url_get_order = "https://69882277-7404-4b4a-bea9-df1393b6570a.serverhub.praktikum-services.ru"
    response_get_order = requests.get(url_get_order)
    assert response_get_order.status_code == 200, f"Ошибка получения заказа: {response_get_order.content}"

