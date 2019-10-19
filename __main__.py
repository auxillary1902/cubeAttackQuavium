from parser import Parser
from cube_attack import RandomCubeAttack
from trivium_cube_attack import TriviumCubeAttack
from quavium_cube_attack import QuaviumCubeAttack
def main():

    args = Parser().args

    if args.mode=="random":

        ca = RandomCubeAttack(degree=args.degree)
        sps = ca.execute_offline_attack()
        equations = ca.execute_online_attack(sps)
        print(ca.possible_maxterms)

    elif args.mode=="trivium":

        f = TriviumCubeAttack(args.n_rounds)
        print(f.possible_maxterms)
        copy_vars = f.possible_maxterms[0:3]
        # print(copy_vars)
        # testing_maxterms = []
        # for i in range(len(copy_vars)):

        #     current_vars = copy_vars[i+1:]
        #     current_var = copy_vars[i]

        #     def gen_maxterms(var, vars):
        #         if len(vars) == 0:
        #             testing_maxterms.append(var)
        #             return

        #         gen_maxterms(var + vars[0],
        #                      vars[1:])

        #         gen_maxterms(var,
        #                      vars[1:])

        #         return

        #     gen_maxterms(current_var, current_vars)
        # print(testing_maxterms)
        # for i in range(len(testing_maxterms)):
        #   print(f.test_maxterm(testing_maxterms[i],675))
        #   print(f.find_superpoly(testing_maxterms[i]))

        print(f.test_maxterm("v1v3v6v7v12v18v22v38v47v58v67v74", 676))
        print(f.find_superpoly("v1v3v6v7v12v18v22v38v47v58v67v74"))
        # f.possible_maxterms = copy_vars
        # f.possible_maxterms.append('')
        # print(f.possible_maxterms)
        # sps1 = f.execute_offline_attack()


    elif args.mode=="quavium":
        g = QuaviumCubeAttack(args.n_rounds)
        print(g.possible_maxterms)
        copy_vars1 = g.possible_maxterms[0:3]
        # print(copy_vars1)
        # testing_maxterms1 = []
        # for i in range(len(copy_vars1)):

        #     current_vars = copy_vars1[i+1:]
        #     current_var = copy_vars1[i]

        #     def gen_maxterms(var, vars):
        #         if len(vars) == 0:
        #             testing_maxterms1.append(var)
        #             return

        #         gen_maxterms(var + vars[0],
        #                      vars[1:])

        #         gen_maxterms(var,
        #                      vars[1:])

        #         return

        #     gen_maxterms(current_var, current_vars)
        # print(testing_maxterms1)
        # for i in range(len(testing_maxterms1)):
        #   print(g.test_maxterm(testing_maxterms1[i],675))
        #   print(g.find_superpoly(testing_maxterms1[i]))
        test_maxterm = ["v4v5v7v19v20v37v53v74v78v79","v5v14v19v20v21v27v29v33v42v43","v6v7v17v27v28v48v60v69v74v75"]
        g.possible_maxterms = test_maxterm
        print(g.possible_maxterms)
        sps2 = g.execute_offline_attack()
        equations2= g.execute_online_attack(sps2)
        # print(g.test_maxterm("v4v5v7v19v20v37v53v74v78v79", 293))
        # print(g.find_superpoly("v4v5v7v19v20v37v53v74v78v79"))  

main()
