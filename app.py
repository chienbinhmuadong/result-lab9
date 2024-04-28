from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Feedback of customers')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Feedback(db.Model):
    rating = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(300))
    

    def __repr__(self):
        return f'Feedback: {self.comment}, rate for {self.rating} stars.'



@app.route('/')
def main():
    feedbacks = Feedback.query.all()
    return render_template('index.html', feedback_list=feedbacks)




# @app.route('/in_stock/<product_id>', methods=['PATCH'])
# def modify_product(product_id):
#     product = Feedback.query.get(product_id)
#     product.in_stock = request.json['in_stock']
#     db.session.commit()
   

@app.route('/send', methods=['POST'])
def add_feedback():
    data = request.json
    feedback = Feedback(**data)
    db.session.add(feedback)
    db.session.commit()

    return 'OK'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
