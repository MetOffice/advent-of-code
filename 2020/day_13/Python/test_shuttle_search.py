from shuttle_search import id_by_minutes, first_timestamp


def test_id_by_minutes():
    test_estimate = 939
    test_buses = ['7','13','x','x','59','x','31','19']
    expected = 295
    actual = id_by_minutes(test_estimate, test_buses)
    assert expected == actual

def test_first_timestsamp():
    test_estimate = 939
    test_buses = ['7','13','x','x','59','x','31','19']
    expected = 1068781
    actual = first_timestamp(test_buses)
    assert expected == actual