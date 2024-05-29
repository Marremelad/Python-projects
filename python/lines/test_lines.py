from lines import line_count

def test_line_count():
    assert line_count("hello.py") == 2
    assert line_count("test_lines.py") == 4


