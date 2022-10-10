from flask import Flask
import ml_worker

# name of current module -- Flask sets up PATHs in the background
app = Flask(__name__)

test_list = [10.74,10.70,10.52,10.38,10.54,10.99]

# response for main page requests
@app.route('/')
def main_page():
    predicted_val = ml_worker.prediction(test_list, test_list[-1])
    return predicted_val

# run it!
if __name__ == "__main__":
    app.run(debug=True)