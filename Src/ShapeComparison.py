def comparison(areadifference, perimeterdiffernce, shaperesult):
    shrinkage = "No Shrinkage"
    shape = "Matched"
    if shaperesult > 97:
        result = "Passed"
    else:
        result = "Failed"
        shape = "Mis Matched"
    if areadifference > 500:
        if perimeterdiffernce > 50:
            shrinkage = 'Panel Shrunk'
            result = "Failed"
    elif areadifference < -500:
        if perimeterdiffernce < -50:
            shrinkage = 'Panel has expanded'
            result = "Failed"
    return shrinkage, result, shape