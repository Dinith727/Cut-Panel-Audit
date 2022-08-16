def comparison(areadifference, perimeterdiffernce, shaperesult):
    shrinkage = "No Shrinkage"
    shape = "Matched"
    shape_match_limit = 97
    max_area_diff = 500
    max_peri_diff = 50
    min_area_diff = -500
    min_peri_diff = -50

    if shaperesult > shape_match_limit:
        result = "Passed"
    else:
        result = "Failed"
        shape = "Mis Matched"
    if areadifference > max_area_diff:
        if perimeterdiffernce > max_peri_diff:
            shrinkage = 'Panel Shrunk'
            result = "Failed"
    elif areadifference < min_area_diff:
        if perimeterdiffernce < min_peri_diff:
            shrinkage = 'Panel has expanded'
            result = "Failed"
    return shrinkage, result, shape