from collections import deque
from itertools import repeat
from sys import version_info
import logging
import numpy as np

"""
degree

self.publicvariables = []
self.secretvariables = []
self.maxterms = []
self.coefficients = {}
def evaluate(self, assignment_dict):
"""


class Quavium:
    def __init__(self, n_rounds, key=None):

        self.degree = 80
        self.publicvariables = ['v' + str(i) for i in range(1, 81)]
        self.secretvariables = ['x' + str(i) for i in range(1, 81)]
        
        copy_vars = self.publicvariables + self.secretvariables
       

        self.maxterms = copy_vars
        self.n_rounds = n_rounds

        if not key:
            self.private_key = np.random.randint(0, 2, self.degree)

        else:
            self.private_key = key

        sk_list = [str(x) for x in self.private_key.tolist()]

        self.sk_list = sk_list

        logging.info("private key is %s", "".join(sk_list))

        sk_hex = "{:020X}".format(int("".join(sk_list), 2))

        logging.info("private key (hex) is %s", sk_hex)

    def _init_quavium(self, iv, sk_list):

        init_list = list(map(int, list(sk_list)))
        # len 80
        init_list += list(map(int, list(iv)))
        #len 160
        init_list += list(repeat(0, 35))

        # len 195
        init_list += list(repeat(0, 90))
        init_list += list([1, 1, 1])
        self.state = init_list
        for i in range(self.n_rounds):
            self._gen_keystream()

    def evaluate(self, assignment_dict, out_bit):

        public_assignment = {}
        private_assignment = {}
        for i in range(self.degree):
            public_assignment[self.publicvariables[i]] = 0
            private_assignment[self.secretvariables[i]] = self.private_key[i]

        for as_var in assignment_dict.keys():

            if 'v' in as_var:
                public_assignment[as_var] = assignment_dict[as_var]

            elif 'x' in as_var:
                private_assignment[as_var] = assignment_dict[as_var]

        pub_binary = "".join([str(public_assignment['v'+str(z)]) for z in range(1, 81)])
        pri_binary = "".join([str(private_assignment['x'+str(z)]) for z in range(1, 81)])

        self._init_quavium(pub_binary, pri_binary)

        for i in range(out_bit - self.n_rounds):
            self._gen_keystream()

        if out_bit < self.n_rounds:
            raise Exception("output bit index {} must be >= number of rounds {}".format(out_bit,
                                                                                        self.n_rounds))

        return self._gen_keystream()

    def _gen_keystream(self):

        t_1 = self.state[2] ^ self.state[50]
        t_2 = self.state[56] ^ self.state[107]
        t_3 = self.state[125] ^ self.state[194]
        t_4 = self.state[203] ^ self.state[287]

        out = t_1 ^ t_2 ^ t_3 ^ t_4

        t_1 = t_1 ^ self.state[48] & self.state[49] ^ self.state[95]
        t_2 = t_2 ^ self.state[105] & self.state[106] ^ self.state[134]
        t_3 = t_3 ^ self.state[192] & self.state[193] ^ self.state[227]
        t_4 = t_4 ^ self.state[285] & self.state[286] ^ self.state[32]

        self.state[0:51] = [t_4] + self.state[0:50]
        self.state[51:108] = [t_1] + self.state[51:107]
        self.state[108:195] = [t_2] + self.state[108:194]
        self.state[195:288] = [t_3] + self.state[195:287]

        return out

def hex_to_bits(n):
    return list("{:080b}".format(int(n, 16)))

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)

    f = {'v' + str(k): 0 if v < 20 else 1 for (v, k) in enumerate(range(1, 81), 0)}

    pu = "".join([str(f['v'+str(z)]) for z in range(1, 81)])

    print("{:020X}".format(int(pu, 2)))

    tv = Quavium(4*288)

    for i in range(20):
        print(tv.evaluate(f, i+4*288))

#
# if __name__ == "__main__":
#     main()
