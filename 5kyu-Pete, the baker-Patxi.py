def cakes(recipe, available):
    return min([int(available[key]/recipe[key]) for key in recipe.keys()]) if all (k in available.keys() for k in recipe.keys()) else 0
