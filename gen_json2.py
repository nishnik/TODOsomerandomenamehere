import json
dict_ = {}
dict_["units"] = {}
dict_["units"]["type"] = "int"
dict_["activation"] = {}
dict_["activation"]["type"] = "str"
dict_["activation"]["values"] = ["softmax", "elu", "softplus", "softsign", "relu", "tanh", "sigmoid", "hard_sigmoid", "linear"]
dict_["use_bias"] = {}
dict_["use_bias"]["type"] = "bool"
dict_["use_bias"]["values"] = ["True", "False"]
with open('arguments.json', 'w') as outfile:
     json.dump(dict_, outfile, indent = 4)