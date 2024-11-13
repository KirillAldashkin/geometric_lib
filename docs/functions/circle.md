# `circle.py` - geometric functions for circle
## Functions 
### `area`
**Summary:**  
_Calculates the area of a circle with a given radius_

**Parameters:**
1) `r` - radius of a circle

**Return value:**  
Area of a circle with radius `r`

**Raises:**
* `ValueError` - if radius is not positive

**Examples:**
```py
circle.area(1) # 3,141592...
circle.area(3) # 28,274333...
```
### `perimeter`
**Summary:**  
_Calculates the circumference of a circle with a given radius_

**Parameters:**
1) `r` - radius of a circle

**Return value:**  
Circumference of a circle with radius `r`

**Raises:**
* `ValueError` - if radius is not positive

**Examples:**
```py
circle.perimeter(1) # 6,283185...
circle.perimeter(3) # 18,849555...
```
