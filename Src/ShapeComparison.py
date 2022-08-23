def comparison(adevratio, pdevratio, shaperesult, area1):

    max_adevratio = 2
    max_pdevratio = 2
    min_adevratio = -2
    min_pdevratio = -2

    if 100000 >= area1:
        shape_match_limit = 60
    elif 100000 < area1 <= 200000:
        shape_match_limit = 70
    elif 200000 < area1 <= 300000:
        shape_match_limit = 80
    elif 300000 < area1 <= 400000:
        shape_match_limit = 90
    elif 400000 < area1 <= 500000:
        shape_match_limit = 95
    else:
        shape_match_limit = 97

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

    return shrinkage, result, shape, shape_match_limit