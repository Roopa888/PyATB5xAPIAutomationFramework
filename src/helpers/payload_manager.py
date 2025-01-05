# Payloads-This file contains the diffrent payloads taht w euse for various requests type like the below
# Create Booking
# Update Booking
# Auth

# Create booking payload
def payload_create_booking():
    payload = {
        "firstname": "John",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


# Update booking payload.Data can be changed during runtime if required

def payload_update_booking():
    payload = {
        "firstname": "John",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


# Create token paylaod.username amd password can be repalced  by env variable file(will rewrite later)
def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload