from .compute import min_max_ 

def check_val(num, val, min_max=min_max_):
    if min_max[num]['min'] > val:
        return (False, "min")
    elif min_max[num]['max'] < val:
        return (False, "max")
    else:
        return (True, None)
    
def display_error(input_list):
    
    input_list = [(num,float(x)) for num, x in enumerate(list(input_list)) if x != ""]  # do usuniecia / przeniesienia
    lista_ = [f'numer {i+1}, z uwagi na {x[1]}' \
              for i,val in input_list \
                if (x := check_val(i,val))[0] == False]
    return lista_

def check_crfp(input_,val):
    input_ =[x for (x,y) in zip(input_,val) if y != '']
    CRFp_table = ['input_1', 'input_2', 'input_3', 'input_4', 'input_5',\
                   'input_6', 'input_7', 'input_8', 'input_9', 'input_10', 'input_15', 'input_16']
    return all(x in input_ for x in CRFp_table)

def check_crfm(input_,val):
    input_ =[x for (x,y) in zip(input_,val) if y != '']
    CRFm_table = ['input_1', 'input_2', 'input_3', 'input_4', 'input_5',\
                  'input_6', 'input_7', 'input_8', 'input_9', 'input_10', \
                    'input_11', 'input_12', 'input_13', 'input_14', 'input_15', 'input_16']
    return all(x in input_ for x in CRFm_table)

if __name__ == "__main__":
    example = [.2,.3,4,.6,-7,.8,.9,.8,.7,.6,.2,.3,3,-1,3,-1]
    print(display_error(example))