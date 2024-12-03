from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Phil Crawford' work?"""
    formatted_name = get_formatted_name('phil', 'crawford')
    assert formatted_name == 'Phil Crawford'