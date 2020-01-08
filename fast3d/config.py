data_dict = {
             "first":{"fw_log": ["first_input.log"],
                      "bw_log":['first_layer_input_grad.log','first_layer_weight_grad_custom.log'],
                      "inshape":[1,1,80,160,160],
                      "kershape":[32,1,3,3,3],
                      "outshape":[1,32,80,80,80],
                      "stride":[1, 2, 2],
                      "padding":[1, 1, 1],
                      "dilation":1,
                      "groups":1,
                      "output_padding": [0, 1, 1],
                      "bias": None
                     },
    
             "second":{"fw_log": ["second_input.log"],
                       "bw_log":['second_layer_input_grad.log','second_layer_weight_grad_custom.log'],
                      "inshape":[1,64,40,40,40],
                      "kershape":[64,64,3,3,3],
                      "outshape":[1,64,40,40,40],
                      "stride":[1, 1, 1],
                      "padding":[1, 1, 1],
                      "dilation":1,
                       "groups":1,
                      "output_padding": [0, 0, 0],
                       "bias": None
                      },
             "third":{"fw_log": ["third_input.log"],
                      "bw_log":['third_layer_input_grad.log','third_layer_weight_grad_custom.log'],
                      "inshape":[1,128,20,20,20],
                      "kershape":[128,128,3,3,3],
                      "outshape":[1,128,20,20,20],
                      "stride":[1, 1, 1],
                      "padding":[1, 1, 1],
                      "dilation":1,
                      "groups":1,
                      "output_padding": [0, 0, 0],  
                      "bias": None
                     },
             "fourth":{"fw_log": ["fourth_input.log"],
                       "bw_log":['fourth_layer_input_grad.log','fourth_layer_weight_grad_custom.log'],
                      "inshape":[1,192,10,10,10],
                      "kershape":[192,192,3,3,3],
                      "outshape":[1,192,10,10,10],
                      "stride":[1, 1, 1],
                      "padding":[1, 1, 1],
                      "dilation":1,
                       "groups":1,
                      "output_padding": [0, 0, 0],
                       "bias": None
                      },
            }
