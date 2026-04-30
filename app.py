from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🛒 Grocery Mart</h1>
    <ul>
        <li>🍎 Apples - ₹100/kg</li>
        <li>🥔 Potatoes - ₹40/kg</li>
        <li>🥛 Milk - ₹50/L</li>
        <li>🍞 Bread - ₹30</li>
    </ul>
    """

app.run(host='0.0.0.0', port=80)
