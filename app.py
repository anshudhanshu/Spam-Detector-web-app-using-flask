from flask import Flask, render_template, request
import pickle as pkl
import warnings

warnings.filterwarnings("ignore")

with open("model.pkl", "rb") as f:
    data = pkl.load(f)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        myDict = request.form
        result = myDict["mail"]
        inputFeature = [result]
        # print(data.predict([inputFeature])[0])
        return render_template("result.html", spam=data.predict([str(inputFeature)])[0])
        # return data.predict([inputFeature])[0]
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
# hello()
