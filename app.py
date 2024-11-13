from flask import Flask, render_template, request

app = Flask(__name__)

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # This is where the actual calculation happens using eval
        return str(eval(expression))
    except Exception as e:
        return "Error"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        # Get the user input
        display = request.form.get("display", "")

        # Handle clear button press
        if "clear" in request.form:
            result = ""
        
        # Handle number button presses
        elif "num" in request.form:
            result = display + request.form["num"]
        
        # Handle operator button presses
        elif "operator" in request.form:
            result = display + request.form["operator"]
        
        # Handle equal button press (calculate the result)
        elif "equal" in request.form:
            result = evaluate_expression(display)
        
        # If nothing happens, just display the current result
        else:
            result = display

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
