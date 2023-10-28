import math


def solver(a_val: float, b_val: float, c_val: float, d_val: float):
    # линейное уравнение
    if a_val == 0 and b_val == 0:
        return 'Линейное уравнение\n x = %s\n' % (round((-d_val * 1.0) / c_val, 4))

    # квадратное уравнение
    elif a_val == 0:

        discriminant = c_val * c_val - 4.0 * b_val * d_val
        if discriminant >= 0:
            discriminant = math.sqrt(discriminant)
            x1 = round((-c_val + discriminant) / (2.0 * b_val), 4)
            x2 = round((-c_val - discriminant) / (2.0 * b_val), 4)
        else:
            discriminant = math.sqrt(-discriminant)
            x1 = str(round(-c_val / (2.0 * b_val), 4) + round(discriminant / (2.0 * b_val), 4) * 1j).replace('(', '')\
                .replace(')', '').replace('j', 'i').replace('-0-', '-').replace('-0+', '+')
            x2 = str(round(-c_val / (2.0 * b_val), 4) - round(discriminant / (2.0 * b_val), 4) * 1j).replace('(', '')\
                .replace(')', '').replace('j', 'i').replace('-0-', '-').replace('-0+', '+')

        return 'Квадратное уравнение\n x1 = %s\n x2 = %s\n' % (x1, x2)

    f = findF(a_val, b_val, c_val)
    g = findG(a_val, b_val, c_val, d_val)
    h = findH(g, f)

    if f == 0 and g == 0 and h == 0:  # 3 равных действительных корня
        if (d_val / a_val) >= 0:
            x = (d_val / (1.0 * a_val)) ** (1 / 3.0) * -1
        else:
            x = (-d_val / (1.0 * a_val)) ** (1 / 3.0)
        return 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (x.__round__(4), x.__round__(4), x.__round__(4))

    elif h <= 0:  # все корни действительные

        i = math.sqrt(((g ** 2.0) / 4.0) - h)
        j = i ** (1 / 3.0)
        k = math.acos(-(g / (2 * i)))
        L = j * -1
        M = math.cos(k / 3.0)
        N = math.sqrt(3) * math.sin(k / 3.0)
        P = (b_val / (3.0 * a_val)) * -1

        x1 = 2 * j * math.cos(k / 3.0) - (b_val / (3.0 * a_val))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        return 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (
        x1.__round__(4), x2.__round__(4), x3.__round__(4))

    elif h > 0:  # Один действительный и два комплексных корня
        R = -(g / 2.0) + math.sqrt(h)
        if R >= 0:
            S = R ** (1 / 3.0)
        else:
            S = (-R) ** (1 / 3.0) * -1
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))
        else:
            U = ((-T) ** (1 / 3.0)) * -1
        x1 = (S + U) - (b_val / (3.0 * a_val))
        x2 = (-(S + U) / 2 - (b_val / (3.0 * a_val))).__round__(4) + ((S - U) * math.sqrt(3) * 0.5).__round__(4) * 1j
        x3 = (-(S + U) / 2 - (b_val / (3.0 * a_val))).__round__(4) - ((S - U) * math.sqrt(3) * 0.5).__round__(4) * 1j

        return 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (round(float(x1), 4),
                                    str(x2).replace('(', '').replace(')', '').replace('j', 'i').replace('-0-', '-')
                                                                         .replace('-0+', '+'),
                                    str(x3).replace('(', '').replace(')', '').replace('j', 'i').replace('-0-', '-')
                                                                         .replace('-0+', '+'))


def findF(coefficient_a, coefficient_b, coefficient_c):
    return ((3.0 * coefficient_c / coefficient_a) - ((coefficient_b ** 2.0) / (coefficient_a ** 2.0))) / 3.0


def findG(coefficient_a, coefficient_b, coefficient_c, coefficient_d):
    return (((2.0 * (coefficient_b ** 3.0)) / (coefficient_a ** 3.0)) - ((9.0 * coefficient_b * coefficient_c) /
                                            (coefficient_a ** 2.0)) + (27.0 * coefficient_d / coefficient_a)) / 27.0


def findH(g, f):
    return (g ** 2.0) / 4.0 + (f ** 3.0) / 27.0
