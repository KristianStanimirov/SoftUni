def rect_area_funct(width: int, high: int):
    result = width * high
    return result


rect_width = int(input())
rect_height = int(input())

print(rect_area_funct(rect_width, rect_height))
