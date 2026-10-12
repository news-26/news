"""Rzutowania map (wspólne dla mapa_dane.py i build.py).

lambert – Europa: azymutalny równopolowy Lamberta, środek 15°E 52°N.
equal_earth – świat: Equal Earth (Šavrič, Patterson, Jenny 2018), południk środkowy 0°.
Obie zwracają współrzędne w jednostkach rzutu; na piksele przelicza je `piksele` z parametrami
zapisanymi w pliku konturów ({"skala", "cx", "cy", "szer", "wys"}).
"""
import math

LON0, LAT0 = math.radians(15), math.radians(52)
EE = (1.340264, -0.081106, 0.000893, 0.003796)
EE_M = math.sqrt(3) / 2


def lambert(lon, lat):
    l, p = math.radians(lon), math.radians(lat)
    k = math.sqrt(2 / (1 + math.sin(LAT0) * math.sin(p) + math.cos(LAT0) * math.cos(p) * math.cos(l - LON0)))
    x = k * math.cos(p) * math.sin(l - LON0)
    y = k * (math.cos(LAT0) * math.sin(p) - math.sin(LAT0) * math.cos(p) * math.cos(l - LON0))
    return x, y


def lambert_odwr(x, y):
    """Odwrotność `lambert` – (x, y) w jednostkach rzutu -> (lon, lat) w stopniach."""
    r = math.hypot(x, y)
    if r < 1e-12:
        return math.degrees(LON0), math.degrees(LAT0)
    c = 2 * math.asin(min(1, r / 2))
    p = math.asin(math.cos(c) * math.sin(LAT0) + y * math.sin(c) * math.cos(LAT0) / r)
    l = LON0 + math.atan2(x * math.sin(c), r * math.cos(LAT0) * math.cos(c) - y * math.sin(LAT0) * math.sin(c))
    return math.degrees(l), math.degrees(p)


def equal_earth(lon, lat):
    a1, a2, a3, a4 = EE
    t = math.asin(EE_M * math.sin(math.radians(lat)))
    t2 = t * t
    t6 = t2 * t2 * t2
    x = math.radians(lon) * math.cos(t) / (EE_M * (a1 + 3 * a2 * t2 + t6 * (7 * a3 + 9 * a4 * t2)))
    y = t * (a1 + a2 * t2 + t6 * (a3 + a4 * t2))
    return x, y


RZUTY = {"lambert": lambert, "equal_earth": equal_earth}


def piksele(rzut, prm, lon, lat):
    x, y = RZUTY[rzut](lon, lat)
    return (prm["szer"] / 2 + (x - prm["cx"]) * prm["skala"], prm["wys"] / 2 - (y - prm["cy"]) * prm["skala"])
