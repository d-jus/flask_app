def compute(input):
    "imput: form type"
    try:
        return sum([float(x) for x in list(input.data.values())[:-2]])
    except:
        raise Exception('wpisano błędne dane')
    