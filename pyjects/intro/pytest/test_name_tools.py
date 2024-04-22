from name_tools import format_name

def test_format_name():
    "Test multiple inputs"
    tc1 = format_name("The", "Grinch")
    assert tc1 == "The Grinch"