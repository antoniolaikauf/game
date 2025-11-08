# dal centro si ottiene i suoi punti più estremi
def get_bounds(center_x, center_y, width, height):
    half_w = width / 2
    half_h = height / 2
    
    return (
        center_x - half_w,
        center_x + half_w,
        center_y - half_h,
        center_y + half_h
    )

def get_center(name, size):
    if name == 'square':
        return (size[0] // 2, size[1] // 2)
    if name == 'circle':
        return tuple(size)
    if name == 'polygon':
        # return (size[])
        pass
    

# fare una funzione che se gli dai il tipo d'oggetto e cosa vuoi esempio il punto più a destra o il centro lui ti ritorna quello