from flask import Flask, redirect, render_template, url_for, request
from model.model import BedrockModel

app = Flask(__name__)
bedrock_model = BedrockModel()

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        
        return redirect(url_for("user", usr=user))
    
    else:
        return render_template("data.html")

@app.route("/<usr>")
def user(usr):
    # TODO: Check data type from post request, if not string convert it to string, pass this as parameter to invoke model
    # TODO: usr data already is in string, pass to invoke mdodel
    model_response = bedrock_model.invokeModel(usr)
    # print(model_response)


    return f"<bady>{model_response}</body>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)