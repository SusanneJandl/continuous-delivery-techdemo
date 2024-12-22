from flask import Flask, request, render_template_string, redirect, url_for
from calculator import Calculator  # Import your Calculator class

# Initialize the Flask app
app = Flask(__name__)

# Instantiate the Calculator class
calc = Calculator()

# Route for the home page with the form
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error_message = None

    if request.method == 'POST':
        try:
            # Get form data
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']

            # Perform the calculation based on the operator
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                if num2 == 0:
                    error_message = "Division by zero is not allowed."
                else:
                    result = calc.divide(num1, num2)
            else:
                error_message = "Invalid operator."

        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."

    # Render the form and pass the result or error message to display
    return render_template_string("""
    <h1>Welcome to the Python Calculator!</h1>
    <p>This calculator can perform the following operations:</p>
    <ul>
        <li>Addition (+)</li>
        <li>Subtraction (-)</li>
        <li>Multiplication (*)</li>
        <li>Division (/)</li>
    </ul>

    <form method="post">
        <label for="num1">Enter the first number:</label>
        <input type="text" name="num1" id="num1" required><br><br>

        <label for="num2">Enter the second number:</label>
        <input type="text" name="num2" id="num2" required><br><br>

        <label for="operator">Choose an operator:</label>
        <select name="operator" id="operator" required>
            <option value="+">Addition (+)</option>
            <option value="-">Subtraction (-)</option>
            <option value="*">Multiplication (*)</option>
            <option value="/">Division (/)</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>

    {% if result is not none %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
    {% if error_message %}
    <h2 style="color: red;">Error: {{ error_message }}</h2>
    {% endif %}
    """, result=result, error_message=error_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
