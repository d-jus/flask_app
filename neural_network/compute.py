    
from pickle import LIST
from typing import List
from numpy import array,swapaxes, add, matmul, exp

def normalization_input(n1, n2, n3, n4):
    return (n1 - n2) * n3 + n4

def sigmoid(net):
    return 2 / (1 + exp(-2 * net)) - 1

def _pre(INPUT: List) -> int:

    # dla wskaźnika predyspozycja
    b = array(
        variables['PRE']['b']
        )
    b2 = array(
        variables['PRE']['b2']
        )
    input_weight = array(
        variables['PRE']['input_weight']
    )
    layer_weight = array(
        variables['PRE']['input_layer']
    )
    #a1, a2, a3 - coef to normalization
    a1 = array(
        [2, 5.4, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0]
        )
    a2 = array(
        [0.037037037037037, 0.3125, 2, 2, 4, 2, 0.0666666666666667, 0.04, 0.0105263157894737, 3.47826086956522, 2,
         0.434782608695652]
         )
    a3 = array(
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        )
    
    normalization_inpuT = normalization_input(INPUT, a1, a2, a3)
    input_weight = swapaxes(input_weight, 0, 1)
    layer_weight = swapaxes(layer_weight, 0, 1)
    net = add(matmul(normalization_inpuT, input_weight), b)
    a_1 = sigmoid(net)
    a_2_pre = add(matmul(a_1, layer_weight), b2)
    normalization_output_pre = (
        sigmoid(a_2_pre) + 1) / 3.33333333333333 + 0.4
    return round(normalization_output_pre[0], 4)

def _mu(INPUT: List) -> int:
    b = array(
        variables['MU']['b']
        )
    b2 = array(
        variables['MU']['b2']
        )
    input_weight = array(
        variables['MU']['input_weight']
    )
    layer_weight = array(
        variables['MU']['input_layer']
    )
    #a1, a2, a3 - coef to normalization
    a1 = array([2, 5.4, 0, 0, 0, 0, 0, 0, 0, 0.6, 6.4, 1.6, 0, 0.5, 0, 0])
    a2 = array(
        [0.037037037037037, 0.3125, 2, 2, 4, 2, 0.0666666666666667, 0.04, 0.0105263157894737, 3.47826086956522,
         0.18018018018018, 2, 0.0444444444444444, 0.307692307692308, 2, 0.434782608695652])
    a3 = array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

    normalization_Input = normalization_input(INPUT, a1, a2, a3)
    input_weight = swapaxes(input_weight, 0, 1)
    layer_weight = swapaxes(layer_weight, 0, 1)
    net = add(matmul(normalization_Input, input_weight), b)
    a_1 = sigmoid(net)
    a_2 = add(matmul(a_1, layer_weight), b2)
    normalization_output = (sigmoid(a_2) + 1) / 2.85714285714286 + 0.3

    return round(normalization_output[0], 2)

variables = {'PRE':{
    'b': [-0.287687978354995, -0.254145744490595, 0.20553506200414, -2.64574989693001],
    'b2': [0.6846354027686],
    'input_weight':[
        [1.26725653798838, 1.65759921776273, -5.0361717639055, 1.76956731042433, -0.431163288154406, 3.69734722319648,
         1.02857507722956, 0.661808275883479, 0.209339900564082, -1.01218853442114, -1.46969028554141,
         0.541256438501523],
        [-3.09292725249879, -0.103860099051127, 1.72955873331385, -1.87811515801954, -1.33087890523572,
         -1.55636303276972, 1.48442141789297, 1.09271101838906, 3.11750816221168, -0.27260972401501, -2.45435091937436,
         0.674],
        [0.378954618515674, -1.52815854327969, 2.01602090239542, 0.542536531440565, -0.450314982981614,
         -0.700092491637342, -1.08494621589648, 2.07711316155165, 0.507439221130574, 0.632858935601814, 2.6056773976665,
         0.018411737451537],
        [-1.46464314259969, -1.25355425619272, 0.121131988360189, 0.119618446510931, -0.268135668843527,
         -0.74153680952656, 4.26132597267561, -2.77097846630327, 1.16962178643047, 3.20457679748779, 0.419723937623802,
         0.14]
        ],
    'input_layer':[
        [0.346098756218088, 0.250774431519168, 0.508091158190255, -0.729919889465312]
    ]
    },
    'MU':{
    'b': [1.48339316887219, 1.08492883208489, -0.793974006244905, 0.728464525709856, -0.564220413029404,
                  -0.271066479479504, 2.03566940410352, 2.20051665768103],
    'b2': [0.565940872595944],
    'input_weight':[
        [-0.380243288993, -0.300175201712818, -0.281004440161411, -0.332830486360074, 0.156008642457155,
         0.111678603030612, -0.683603556539849, -0.642223750037346, 1.15597327801351, 0.609205864624937,
         -0.702303822551299, 0.0406362614401268, 0.401893364670345, -0.827294642045006, 0.0949570653356762,
         0.524829622005859],
        [-1.08533173309714, -0.21256961759385, 0.0742364961730546, 0.399930564553522, -0.262091017398624,
         -0.603223339698924, -0.169185278065604, 0.127448582732462, 0.0132862240972325, -0.198066501449639,
         0.184217193385349, -0.314833238487254, -0.118995209333859, -0.777992847269311, 0.59367024069462,
         -0.651660258008262],
        [0.225954459695221, -0.904010911207907, 0.435670015063225, -0.0578680209135651, -0.346748531086589,
         1.12107741090145, -0.933281918488416, -0.89862634991907, -0.573580415623607, -0.608260540893736,
         0.256716361311498, 1.04636200791995, -0.559515343333687, -0.0911404609438948, 0.0651366891541776,
         0.263701219294465],
        [0.0194896271876738, 0.433047881018382, -0.420428771632105, 1.00366562908406, 0.355891858986215,
         0.0729908336797084, 0.18868121433102, -0.0107430299531131, 1.12928089337506, 0.233822185502071,
         0.553956900836664, 0.537905688270666, -0.585058638822749, 0.489283687789724, 0.343112638867919,
         -0.266998526994917],
        [0.0752769450394558, 0.12075061401691, -0.186714651102901, -0.391503689471921, -0.122217954984165,
         0.907059939667972, 1.08151651219626, -0.912485238218247, -0.102591181086309, -0.210618125712561,
         0.329981305884741, -0.784274645667204, -0.62533927148021, 0.814162895812021, -1.29585754439226,
         -0.767895670839157],
        [-1.42876798833839, 0.788096832811516, 0.76056473348001, -0.723287125347485, -0.00752786112364666,
         -0.0747843845283547, 0.354566122916609, 0.537957232800058, -0.0233729787134534, -0.572433630067002,
         -0.511804811414359, 0.0730100779106406, 0.0943613910592733, -0.469325473925219, -0.478139056321774,
         -0.0808742129487763],
        [0.552317263450101, -0.532374967991816, 0.731469518361806, -0.94714303798499, -0.149561811304513,
         0.297131656767043, -0.378634753131337, 0.516353506485357, 0.718832704565303, -1.40522662615197,
         -0.1783914723723, -0.13067869858491, -0.998410170798229, -0.346063328263863, -1.62149816939453,
         0.0356453338492707],
        [-0.346664681172561, -0.207508342892562, 0.135215865753101, 0.418742306490479, 0.323270397619853,
         0.702086118402546, 1.04029549224016, 1.03398501629487, -0.967928603233751, 0.0294362921521164,
         0.0174556715112133, 0.0262080756533385, -0.217919115720474, 0.369681669267974, 0.745135266386719,
         -0.345331748196849]
    ],
    'input_layer':[
        [-0.611677244453564, -0.255096748946293, 0.683630206037378, 0.287687247426353, -0.659235559810339,
         0.046307415273694, 0.839652480771805, 0.468721325466003]
    ]
    }}

def compute_p(input,fun = _pre):
    "imput: form type"
    try:
        x = [float(x) for x in list(input.data.values())[:-6]]        # do poprawienia
        return fun(x)
    except:
        raise Exception('wpisano błędne dane')
    
def compute_m(input, fun = _mu):
    "imput: form type"
    try:
        y = [float(x) for x in list(input.data.values())[:-2]]
        return fun(y)
    except:
        raise Exception('wpisano błędne dane')
    
if __name__ == __name__:
    assert _pre([56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	0,	0]) == 0.9247
    assert _mu([56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	6.4,	1.6,	0,	2.5,	0,	0]) == 0.66
    print('działa')