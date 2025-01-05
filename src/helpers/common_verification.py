# Common Verification

# HTTP status code
# Headers
# Data Verification
# JSON schema
# Verify HTTP status code
def verify_HTTP_status_code(response_data, expected_status_code):
    assert response_data.status_code == expected_status_code, "Failed  to get the status code match "


# Verify the key is as expected
def verify_response_key(key, expected_key):
    assert key == expected_key, "Falied to match the key"


# Verify if the key value  is not null
def verify_json_key_not_null(key):
    assert key != 0,"Failed.Key is null"


# Verify if key value is greater than zero
def verify_json_key_gr_zero(key):
    assert key > 0,"Failed .Key is not gretaer than zero"
