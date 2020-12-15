"""
Коэффициенты для термопар типов R, S, В, J, Т, Е, K, N, А, L, М по ГОСТ 8.585-2001
Метка "не ГОСТ" - расчеты extracting_coefficients_mV.py, extracting_coefficients_T.py
"""

coefficients = {
    'L': {
        'T': {
            (-200, 0): (2.76610203e-04,  6.33712901e-02,  6.37015450e-05,  1.92258094e-08,  1.55574603e-09,  1.23173389e-11,  5.87565838e-14,  1.48328819e-16, 1.49251986e-19), # не ГОСТ
            (0, 800): (-1.40098253e-04, 6.33198398e-02, 5.99633047e-05, -7.82928338e-08, 8.83859264e-11, -1.36314288e-14, -2.79152675e-16, 4.52592512e-19, -2.14300492e-22) # не ГОСТ
        },
        'mV': {
            (-9.488, 0): (-1.12221876e-02, 1.57119487e+01, -3.99136006e-01, -1.26179615e-01, -6.19907084e-02, -1.51642779e-02, -2.14107447e-03, -1.59203047e-04, -4.96908012e-06), # не ГОСТ
            (0, 66.466): (3.63846069e-02,  1.57370869e+01,  -2.13391881e-01,  7.63561103e-03,  -2.22074808e-04,  4.48762988e-06,  -5.36847673e-08,  3.25609022e-10, -7.08470842e-13) # не ГОСТ
        }
    },
    'K': {
        'T': {
            (-270, 0): (0, 3.9450128025e-2, 2.3622373598e-5, -3.2858906784e-7, -4.9904828777e-9, -6.7509059173e-11, -5.7410327428e-13, -3.1088872894e-15 ,-1.0451609365e-17, -1.9889266878e-20, -1.6322697486e-23), # не ГОСТ
            (0, 500): (-0.0024829685, 0.0400866641, -1.27081008e-05, 7.99831713e-07, -1.02599237e-08, 6.08722555e-11, -1.97487299e-13, 3.6312914e-16, -3.56617383e-19, 1.45724739e-22), # не ГОСТ
            (500, 1372): (-1.7600413686e-2, 3.8921204975e-2, 1.8558770032e-5, -9.9457592874e-8, 3.1840945719e-10, -5.6072844889e-13, 5.6075059059e-16, -3.2020720003e-19, 9.7151147152e-23, -1.2104721275e-26) # не ГОСТ
        },
        'mV': {
            (-5.891, 0): (-2.28104654e-02, 2.50139746e+01, -1.47899773e+00, -1.37001813e+00, -1.04066274e+00, -4.14467880e-01, -9.34118723e-02, -1.10487879e-02, -5.41042081e-04), # не ГОСТ
            (0, 20.644): (0, 25.08355, 7.860106e-2, -2.503131e-1, 8.315270e-2, -1.228034e-2, 9.804036e-4, -4.413030e-5, 1.057734e-6, -1.052755e-8),
            (20.644, 54.886): (-1.29255985e+02, 4.77636316e+01, -1.60110357e+00, 5.27353236e-02, -9.21001281e-04, 8.27795856e-06, -2.85838731e-08) # не ГОСТ
        }
    },
    'R': {
        'T': {
            (-50, 1064.18): (0, 5.28961729765e-3, 1.39166589782e-5, -2.38855693017e-8, 3.56916001063e-11, -4.62347666298e-14, 5.00777441034e-17, -3.73105886191e-20, 1.57716482367e-23, -2.81038625251e-27),
            (1064.18, 1664.5): (2.95157925316, -2.52061251332e-3, 1.59564501865e-5, -7.64085947576e-9, 2.05305291024e-12, -2.93359668173e-16),
            (1664.5, 1768.1): (1.52232118209e2, -2.68819888545e-1, 1.71280280471e-4, -3.45895706453e-8, -9.34633971046e-15)
        },
        'mV': {
            (-0.226, 1.923): (0, 1.8891380e2, -93.835290, 1.3068619e2, -2.2703580e2, 3.5145659e2, -3.8953900e2, 2.8239471e2, -1.2607281e2, 31.353611, -3.3187769),
            (1.923, 11.361): (13.34584505, 1.472644573e2, -18.44024844, 4.031129726, -6.249428360e-1, 6.468412046e-2, -4.458750426e-3, 1.994710149e-4, -5.313401790e-6, 6.481976217e-8),
            (11.361, 19.739): (-2.18578125e+01, 1.35001671e+02, -5.59862061e+00, 2.44943729e-01, -5.86318888e-03, 6.98058483e-05),
            (19.739, 21.103): (3.406177836e4, -7.023729171e3, 5.582903813e2, -19.52394635, 2.560740231e-1)
        }
    },
    'S': {
        'T': {
            (-50, 1064.18): (0, 5.40313308631e-3, 1.25934289740e-5, -2.32477968689e-8, 3.22028823036e-11, -3.31465196389e-14, 2.55744251786e-17, -1.25068871393e-20, 2.71443176145e-24),
            (1064.18, 1664.5): (1.32900444085, 3.34509311344e-3, 6.54805192818e-6, -1.64856259209e-9, 1.29989605174e-14),
            (1664.5, 1768.1): (1.46628232636e2, -2.58430516752e-1, 1.63693574641e-4, -3.30439046987e-8, -9.43223690612e-15)
        },
        'mV': {
            (-0.236, 1.874): (0, 1.84949460e2, -80.0504062, 1.02237430e2, -1.52248592e2, 1.88821343e2, -1.59085941e2, 82.3027880, -23.4181944, 2.79786260),
            (1.874, 10.332): (12.91507177, 1.466298863e2, -15.34713402, 3.145945973, -4.163257839e-1, 3.187963771e-2, -1.291637500e-3, 2.183475087e-5, -1.447379511e-7, 8.211272125e-9),
            (10.332, 17.536): (-80.87801117, 1.621573104e2, -8.536869453, 4.719686976e-1, -1.441693666e-2, 2.081618890e-4),
            (17.536, 18.694): (5.333875126e4, -1.235892298e4, 1.092657613e3, -42.65693686, 6.247205420e-1)
        }
    },
    'B': {
        'T': {
            (0, 630.615): (0, -2.4650818346e-4, 5.9040421171e-6, -1.3257931636e-9, 1.5668291901e-12, -1.6944529240e-15, 6.2990347094e-19),
            (630.615, 1820): (-3.8938168621, 2.8571747470e-2, -8.4885104785e-5, 1.5785280164e-7, -1.6835344864e-10, 1.1109794013e-13, -4.4515431033e-17, 9.8975640821e-21, -9.3791330289e-25)
        },
        'mV': {
            (0.000, 0.291): (3.43823983e+01, 6.96707459e+03, -4.87920303e+05, 2.04203404e+07, -4.84966972e+08, 7.04076217e+09, -6.54812595e+10, 3.98079821e+11, -1.57381371e+12, 3.89814772e+12, -5.49289136e+12, 3.35955482e+12), # не ГОСТ
            (0.291, 2.431): (98.423321, 6.9971500e2, -8.4765304e2, 1.0052644e3, -8.3345952e2, 4.5508542e2, -1.5523037e2, 29.886750, -2.4742860),
            (2.431, 13.820): (2.1315071e2, 2.8510504e2, -52.742887, 9.9160804, -1.2965303, 1.1195870e-1, -6.0625199e-3, 1.8661696e-4, -2.4878585e-6)
        }
    },
    'J': {
        'T': {
            (-210, 760): (0, 5.0381187815e-2, 3.0475836930e-5, -8.5681065720e-8, 1.3228195295e-10, -1.7052958337e-13, 2.0948090697e-16, -1.2538395336e-19, 1.5631725697e-23),
            (760, 1200): (2.9645625681e2, -1.4976127786, 3.1787103924e-3, -3.1847686701e-6, 1.5720819004e-9, -3.0691369056e-13)
        },
        'mV': {
            (-8.095, 0): (-3.42872153e-02, 1.94628593e+01, -1.20584249e+00, -9.80256908e-01, -5.25481906e-01, -1.51850395e-01, -2.47050637e-02, -2.10943832e-03, -7.42168294e-05), # не ГОСТ
            (0, 42.919): (0, 19.78425, -2.001204e-1, 1.036969e-2, -2.549687e-4, 3.585153e-6, -5.344285e-8 ,5.099890e-10),
            (42.919, 69.553): (-3.11358187e3, 3.00543684e2, -9.94773230, 1.70276630e-1, -1.43033468e-3, 4.73886084e-6)
        }
    },
    'T': {
        'T': {
            (-270, 0): (-1.88300457e-04, 3.85852283e-02, 1.08334329e-05, -2.76672609e-06, -1.14342843e-07, -2.90512656e-09, -4.78091775e-11, -5.29651294e-13, -4.02466784e-15, -2.10082502e-17, -7.40074840e-20, -1.68016337e-22, -2.21797128e-25, -1.29277716e-28), # не ГОСТ
            # (-270, 0): (0, 3.8748106364e-2, 4.4194434347e-5, 1.1844323105e-7, 2.0032973554e-8, 9.0138019559e-10, 2.2651156593e-11, 3.6071154205e-13, 3.8493939883e-15, 2.8213521925e-17, 1.4251594779e-19, 4.8768662286e-22, 1.0795539270e-24, 1.3945027062e-27, 7.9795153927e-31),
            (0, 400): (0, 3.8748106364e-2, 3.3292227880e-5, 2.0618243404e-7, -2.1882256846e-9, 1.0996880928e-11, -3.0815758772e-14, 4.5479135290e-17, -2.7512901673e-20)
        },
        'mV': {
            (-6.258, 0): (0.241502637730837, 40.91635711678484, 167.2657462084595, 766.0265730597756, 1867.863883892762, 2778.5560387834344, 2719.6779764921016, 1834.9446981967947, 877.7153770803716, 302.06511398676685, 75.02259210146741, 13.322990297063376, 1.649275905644078, 0.13514236896000692, 0.006585974959018617, 0.00014448656353939336), # не ГОСТ
            (0, 20.872): (0, 25.92800, -7.602961e-1, 4.637791e-2, -2.165394e-3, 6.048144e-5, -7.293422e-7)
        }
    },
    'E': {
        'T': {
            (-270, 0): (-4.08402395e-05, 5.87146239e-02, 5.54078532e-05, -1.60901602e-08, 4.60913767e-09, 1.29005481e-10, 1.78546344e-12, 1.20114046e-14, 1.42535606e-17, -3.78406571e-19, -3.01241634e-21, -1.07125427e-23, -1.92304643e-26, -1.41236226e-29), # не ГОСТ
            (0, 1000): (0, 5.8665508710e-2, 4.5032275582e-5, 2.8908407212e-8, -3.3056896652e-10, 6.5024403270e-13, -1.9197495504e-16, -1.2536600497e-18, 2.1489217569e-21,-1.4388041782e-24, 3.5960899481e-28)
        },
        'mV': {
            (-9.835, -8.825): (14341265603.40596, 10821496732.081612, 3498850764.1597767, 628356614.616614, 67694532.9637881, 4374897.174774414, 157045.4786134981, 2415.5851240507145), # не ГОСТ
            (-8.825, 0): (0, 16.977288, -4.3514970e-1, -1.5859697e-1, -9.2502871e-2, -2.6084314e-2, -4.1360199e-3, -3.4034030e-4, -1.1564890e-5),
            (0, 76.373): (0, 17.057035, -2.3301759e-1, 6.5435585e-3, -7.3562749e-5, -1.7896001e-6, 8.4036165e-8, -1.3735879e-9, 1.0629823e-11, -3.2447087e-14)
        }
    },
    'N': {
        'T': {
            (-270, 0): (0, 2.6159105962e-2, 1.0957484228e-5, -9.3841111554e-8, -4.6412039759e-11, -2.6303357716e-12, -2.2653438003e-14, -7.6089300791e-17, -9.3419667835e-20),
            (0, 1300): (0, 2.5929394601e-2, 1.5710141880e-5, 4.3825627237e-8, -2.5261169794e-10, 6.4311819339e-13, -1.0063471519e-15, 9.9745338992e-19, -6.0863245607e-22, 2.0849229339e-25, -3.0682196151e-29)
        },
        'mV': {
            # (-4.345, -3.991): (-1.58459734e+09, -1.92744464e+09, -8.53742507e+08, -1.25943906e+08, 2.19553665e+07, 1.07378397e+07, 1.46988372e+06, 7.14954221e+04), # не ГОСТ
            (-3.990, 0): (0, 38.436847, 1.1010485, 5.2229312, 7.2060525, 5.8488586, 2.7754916, 7.7075166e-1, 1.1582665e-1, 7.3138868e-3),
            (0, 20.613): (0, 38.6896, -1.08267, 4.70205e-2, -2.12169e-6, -1.17272e-4, 5.39280e-6, -7.98156e-8),
            (20.613, 47.513): (19.72485, 33.00943, -3.915159e-1, 9.855391e-3, -1.274371e-4, 7.767022e-7)
        }
    },
    'A1': {
        'T': {
            (0, 2500): (7.1564735e-4, 1.1951905e-2, 1.6672625e-5, -2.8287807e-8, 2.8397839e-11, -1.8505007e-14, 7.3632123e-18, -1.6148878e-21, 1.4901679e-25)
        },
        'mV': {
            # (0, 33.640): (-0.0006400964353982376, 83.14140796250702, -8.483508872422988, 2.1663496586175133, -0.44199301864567386, 0.06956295463004113, -0.008215550166861799, 0.0007237977146743555, -4.743299165979485e-05, 2.2956014326469445e-06, -8.073598800972027e-08, 2.0018120191078407e-09, -3.310590761998342e-11, 3.2722062553722957e-13, -1.4600047772179877e-15) # не ГОСТ
            (0, 33.640): (1.58617164e+00, 7.81177806e+01, -4.28503852e+00, 4.80680603e-01, -3.06201898e-02, 1.15906324e-03, -2.34532214e-05, 1.98815992e-07)
        }
    },
    'A2': {
        'T': {
            (0, 1800): (-1.0850558e-4, 1.1642292e-2, 2.1280289e-5, -4.4258402e-8, 5.5652058e-11, -4.3801310e-14, 2.0228390e-17, -4.9354041e-21, 4.8119846e-25)
        },
        'mV': {
            (0, 27.232): (1.1196428, 80.569397, -6.2279122, 0.9337015, -8.2608051e-2, 4.4110979e-3, -1.3610551e-4, 2.2183851e-6, -1.4527698e-8)
        }
    },
    'A3': {
        'T': {
            (0, 1800): (-1.0649133e-4, 1.1686475e-2, 1.8022157e-5, -3.3436998e-8, 3.7081688e-11, -2.5748444e-14, 1.0301893e-17, -2.0735944e-21, 1.4678450e-25)
        },
        'mV': {
            (0, 26.773): (0.8769216, 81.483231, -5.9344173, 0.8699340, -7.6797687e-2, 4.1814387e-3, -1.3439670e-4, 2.342409e-6, -1.6988727e-8)
        }
    },
    'M': {
        'T': {
            (-200, 100): (2.4455560e-6, 4.2638917e-2, 5.0348392e-5, -4.4974485e-8)
        },
        'mV': {
            (-6.154, 4.722): (-4.96817859e-03, 2.33954781e+01, -6.42939184e-01, 7.01526072e-02, -5.29308586e-03, -1.42219543e-03, -3.09723332e-05, 5.50412433e-05) # не ГОСТ
        }
    }
}
