from .compute import min_max_ 

def check_val(num, val, min_max=min_max_):
    if min_max[num]['min'] > val:
        return (False, "min")
    elif min_max[num]['max'] < val:
        return (False, "max")
    else:
        return (True, None)
    
def display_error(input_list):
    input_list = [float(x) for x in list(input_list)]  # do usuniecia / przeniesienia
    lista_ = [f'numer {i+1}, z uwagi na {x[1]}' \
              for i,val in enumerate(input_list) \
                if (x := check_val(i,val))[0] == False]
    return lista_

if __name__ == "__main__":
    example = [.2,.3,4,.6,-7,.8,.9,.8,.7,.6,.2,.3,3,-1,3,-1]
    print(display_error(example))
