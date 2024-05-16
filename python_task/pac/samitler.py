def Samitlerr(soz):
    return list(filter(lambda x: x.lower() in 'bcçdfgğhxjkqlmnprsştvyz' and x.lower() not in set(), soz))