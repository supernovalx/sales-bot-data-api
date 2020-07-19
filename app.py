from flask import Flask
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data.csv')


@app.route('/employee/<employee_id>')
def get_employee(employee_id):
    if employee_id.isnumeric():
        for index, row in df.iterrows():
            if str(row['ID']) == str(employee_id):
                return df.loc[index].to_json()
    return '{}'



if __name__ == '__main__':
    app.run()
