from flask import Flask, jsonify, request
import pandas as pd

# tạo application
app = Flask(__name__)

#app.route để tạo nội dung cũa def
@app.route('/api/churn_count')
@app.route('/api/get_customer_info')

#df.head()      # 5 dòng đầu
#df.tail()      # 5 dòng cuối
#df.info()      # kiểu dữ liệu
#df.describe()  # thống kê
#df.shape       # số dòng, số cột
#df.columns     # tên cột
def get_customer_info():
    customer_id = request.args.get('customerId')

    df = pd.read_csv('Telco-Customer-Churn.csv')

    result = df[df['customerID'] == customer_id]

    return result.to_json(orient='records')

def churn_count():
    df = pd.read_csv('Telco-Customer-Churn.csv')
    # result = list(df['Churn'].value_counts())
    # result = (df['PaymentMethod'].to_json())
    result = df[df['customerID'] == '1452-KIOVK'].to_json()
    return result

if __name__ == "__main__":
    app.run()
    