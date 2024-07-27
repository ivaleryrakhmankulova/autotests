# Валерия Рахманкулов, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    assert response.status_code == 201
    assert response.json()["track"] > 0

def test_get_order():
    track = create_order()
    response = sender_stand_request.get_order(track)

    assert response.status_code == 200
    assert response.json()["order"]["track"] == track

def create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    return response.json()["track"]