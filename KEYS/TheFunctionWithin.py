"""
PSIT (10/08/2017)
it60070090 : Wiput Pootong
it60070183 : Teerapat Kraisrisirikul
"""
 
def main():
    """Main Function"""
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
 
    print(fn_f(fn_f(var_a)))
    print(fn_g(fn_f(var_a - var_b)))
    print(fn_h(fn_f(var_a + var_b), fn_f(var_a + var_c), fn_g(fn_f(var_d**2))))
    parameter_a = fn_h(fn_f(var_a + var_b), fn_f(var_a - var_c), fn_g(fn_f(var_d ** 2)))
    parameter_b = fn_g(fn_f(var_a - var_b))
    parameter_c = fn_f(fn_f(fn_f(fn_f(fn_f(var_c)))))
    parameter_d = var_d ** 8
    print(fn_i(parameter_a, parameter_b, parameter_c, parameter_d))
 
 
def fn_f(var_x):
    """ Calculate function f(x) and return result """
    return var_x * 2
 
def fn_g(var_x):
    """ Calculate function g(x) and return result """
    result = 3*var_x**4 - var_x**3 + 2*var_x**2 + 10
    return result
 
def fn_h(var_x, var_y, var_z):
    """ Calculate function h(x, y, z) and return result """
    result = (var_z + var_x)**2 - var_x*var_y + var_y**2
    return result
 
def fn_i(var_a, var_b, var_c, var_d):
    """ Calculate function i(a, b, c, d) and return result """
    result = (var_a ** 2 + var_b ** 2 - var_c ** 2)/(var_d**2 - 2*var_a*var_d + 2*var_a)
    return result
 
main()