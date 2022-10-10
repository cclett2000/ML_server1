from flask import Flask
import ml_worker

# name of current module -- Flask sets up PATHs in the background
app = Flask(__name__)

test_list = [0.31500448885053234, 0.8926063109753569, 0.23009089879830358, 0.9356859086385075, 0.8139753193745775, 0.2703561382072832, 0.8022764454104758, 0.29618861591375745, 0.178200029217924, 0.8711950811564656]
predicted_val = ml_worker.prediction(test_list, test_list[-1])

# response for main page requests
@app.route('/')
def main_page():
    return predicted_val

# run it!
if __name__ == "__main__":
    app.run(debug=True)