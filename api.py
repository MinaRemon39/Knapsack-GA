from flask import Flask,jsonify,request
from knapsack_genetic import genetic_algorithm

app = Flask(__name__)

# number of items , total benfit , items
@app.route("/genetic",methods=["post"])
def get_res():
    json = request.json
    knapsack_size = json["size"]
    weights = json["weights"]
    benfits = json["benfits"]
    items = json["items"]
    res_items=[]
    best_solution, benfit = genetic_algorithm(benfits,weights,knapsack_size)
    for i in range(len(best_solution)):
        if best_solution[i]==1:
            res_items.append(items[i])
    count = best_solution.count(1)
    return jsonify({"Count of items":count,"Items":res_items,"Total benfit":benfit})



if (__name__=="__main__"):
    app.run(debug=True)