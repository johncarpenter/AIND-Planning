import os

if __name__=="__main__":

    problems = [1,2,3]
    series = [10]


    os.system("python -m unittest tests.test_my_air_cargo_problems")
    os.system("python -m unittest tests.test_my_planning_graph")


    for p in problems:
        for s in series:
            os.system("python run_search.py -p {} -s {} > results/results_p{}_s{}.log".format(p,s,p,s))
