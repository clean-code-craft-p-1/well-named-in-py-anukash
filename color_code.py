MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1

def format_color_reference_manual():
    """Returns a formatted string for the color code reference manual."""
    lines = ["Pair No.| Major Color | Minor Color"]
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major, minor = get_color_from_pair_number(pair_number)
        lines.append(f"{pair_number:2}      | {major:11} | {minor}")
    return "\n".join(lines)
