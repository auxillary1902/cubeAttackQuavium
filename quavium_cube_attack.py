import logging
logging.basicConfig(level=logging.INFO)
import cube_attack
from quavium import Quavium
from blackboxpoly import BlackBoxPoly
from blackboxpoly import sum_mod2


class QuaviumCubeAttack(cube_attack.CubeAttack):
    def __init__(self, n_rounds, action="verify"):
        super().__init__(degree=80)

        self.bbpoly = Quavium(n_rounds)
        self.action = action
        possible_maxterms = self.bbpoly.maxterms[:-1]

        self.possible_maxterms = []

        for term in possible_maxterms:
            if 'x' not in term:
                self.possible_maxterms.append(term)

