from prectice_5_catalog_tools import (
    published_names,
    count_cheaper,
    verdict,
    seat_label,
)
import pytest

response = {
    "count": 3,
    "movies": [
        {"id": 34, "name": "Дюна", "price": 350, "published": True},
        {"id": 35, "name": "Опенгеймер", "price": 600, "published": True},
        {"id": 36, "name": "Аритмия", "price": 300, "published": False},
    ],
}


def test_published_names():
    assert published_names(response) == ["Дюна", "Опенгеймер"]

def test_count_cheaper():
    assert count_cheaper(response, 400) == 2

def test_verdict_203():
    assert verdict(203) == "ok"

def test_verdict_404():
    assert verdict(404) == "клиент"

def test_verdict_503():
    assert verdict(503) == "сервер"

def test_verdict_120():
    assert verdict(120) == "неизвестно"

def test_verdict_201():
    assert verdict(201) == "ok"


def test_count_cheaper_border():
    assert count_cheaper(response,100) == 0

def test_seat_label():
    assert seat_label(1,1,1) == "1, ряд 1, место 1" 

def test_seat_label_broken():
    assert seat_label(1,1) == "2, ряд 1, место 1"   