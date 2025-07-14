
from color_code import get_color_from_pair_number, get_pair_number_from_color, format_color_reference_manual

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
    print('\nReference Manual:')
    print(format_color_reference_manual())



"""
output will be:
Done :)
----------------------------------------------
Reference Manual:
Pair No.| Major Color | Minor Color
 1      | White       | Blue
 2      | White       | Orange
 3      | White       | Green
 4      | White       | Brown
 5      | White       | Slate
 6      | Red         | Blue
 7      | Red         | Orange
 8      | Red         | Green
 9      | Red         | Brown
10      | Red         | Slate
11      | Black       | Blue
12      | Black       | Orange
13      | Black       | Green
14      | Black       | Brown
15      | Black       | Slate
16      | Yellow      | Blue
17      | Yellow      | Orange
18      | Yellow      | Green
19      | Yellow      | Brown
20      | Yellow      | Slate
21      | Violet      | Blue
22      | Violet      | Orange
23      | Violet      | Green
24      | Violet      | Brown
25      | Violet      | Slate
"""