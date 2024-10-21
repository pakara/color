# This function caluculates HSV from RGB.
# The arguments are R,G and B, all of which are
# values between 0 (inclusive) and 1 (exclusive).
# The return values are Hue, Satulation, Value.
def rgb2hsv(r, g, b):
    maxv, minv = max(r, g, b), min(r, g, b)
    delta = maxv - minv
    hue = 0.0
    saturation = delta / maxv
    v = maxv

    if delta > 0:

        if maxv == r:
            hue = 60.0 * ((g - b) / delta)
        elif maxv == g:
            hue = 60.0 * (((b - r) / delta) + 2)
        else:
            hue = 60.0 * (((r - g) / delta) + 4)

        if hue < 0:
            hue += 360

        hue /= 360

    return hue, saturation, v


# This function caluculates RGB from HSV.
# The arguments are Hue, Satulation and Value,
# all of which are values between 0 (inclusice)
# and 1 (exclusive). The return values are R, G, B.
def hsv2rgb(h, s, v):
    hue = h * 360.0
    C = v * s
    X = C * (1.0 - abs((hue / 60.0) % 2 - 1.0))
    m = v - C

    r, g, b = 0, 0, 0
    if 0 <= hue < 60:
        r, g, b = C, X, 0
    elif 60 <= hue < 120:
        r, g, b = X, C, 0
    elif 120 <= hue < 180:
        r, g, b = 0, C, X
    elif 180 <= hue < 240:
        r, g, b = 0, X, C
    elif 240 <= hue < 300:
        r, g, b = X, 0, C
    elif 300 <= hue < 360:
        r, g, b = C, 0, X

    r = r + m
    g = g + m
    b = b + m

    return r, g, b