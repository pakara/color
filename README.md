# color.py

## Overview
`color.py` is a script that provides functions to convert between RGB (Red, Green, Blue) and HSV (Hue, Saturation, Value) color formats. It includes functions to convert RGB to HSV and vice versa.

## Functions

### 1. `rgb2hsv(r, g, b)`
- **Description**: Converts an RGB color to HSV.
- **Arguments**:
  - `r`: Red value (a floating-point number between 0 and 1, exclusive)
  - `g`: Green value (a floating-point number between 0 and 1, exclusive)
  - `b`: Blue value (a floating-point number between 0 and 1, exclusive)
- **Returns**: 
  - `hue`: The hue (a value between 0 and 1, exclusive)
  - `saturation`: The saturation (a value between 0 and 1, exclusive)
  - `value`: The brightness (a value between 0 and 1, exclusive)

### 2. `hsv2rgb(h, s, v)`
- **Description**: Converts an HSV color to RGB.
- **Arguments**:
  - `h`: Hue (a floating-point number between 0 and 1, exclusive)
  - `s`: Saturation (a floating-point number between 0 and 1, exclusive)
  - `v`: Value (a floating-point number between 0 and 1, exclusive)
- **Returns**:
  - `r`: Red value (a value between 0 and 1, exclusive)
  - `g`: Green value (a value between 0 and 1, exclusive)
  - `b`: Blue value (a value between 0 and 1, exclusive)

## Usage Examples

### Convert RGB to HSV

```python
from color import rgb2hsv

r, g, b = 0.5, 0.2, 0.7
h, s, v = rgb2hsv(r, g, b)
print(h, s, v)

