'''
U-calculator

Do the actual calculation for U.

Author: Shuhang Li
Date: Jun 28, 2023
'''

def calculate(materials):
    r_total = 0
    try:
        for material in materials:
            l = float(material["l"])
            k = float(material["k"])
            r_total += l/k
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    except Exception as e:
        print(f"Unknown error: {e}\n materials={materials}")
        return None
    return r_total
