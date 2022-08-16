def comparison(adevratio, pdevratio, shaperesult):

    shape_match_limit = 97
    max_adevratio = 2
    max_pdevratio = 2
    min_adevratio = -2
    min_pdevratio = -2

    if shaperesult > shape_match_limit:
        shape = "Matched"
        if adevratio > max_adevratio and pdevratio > max_pdevratio:
            shrinkage = 'Panel Shrunk'
            result = "Failed"
        elif adevratio < min_adevratio and pdevratio < min_pdevratio:
            shrinkage = 'Panel has expanded'
            result = "Failed"
        else:
            result = "Passed"
            shrinkage = "No Shrinkage"
    else:
        result = "Failed"
        shape = "Mis Matched"
        if adevratio > max_adevratio and pdevratio > max_pdevratio:
            shrinkage = 'Panel Shrunk'
        elif adevratio < min_adevratio and pdevratio < min_pdevratio:
            shrinkage = 'Panel expanded'
        else:
            shrinkage = "No Shrinkage"

    return shrinkage, result, shape