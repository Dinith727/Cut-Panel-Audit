def comparison(areadifference, perimeterdiffernce):
    ret = "Panel is good"
    if areadifference > 0:
        if perimeterdiffernce > 0:
            ret = 'Panel has expanded'
        elif perimeterdiffernce < 0:
            ret = 'Shape Mismatch'
    elif areadifference < 0:
        if perimeterdiffernce > 0:
            ret = 'Shape Mismatch'
        elif perimeterdiffernce < 0:
            ret = 'Panel Shrunk'
    return ret