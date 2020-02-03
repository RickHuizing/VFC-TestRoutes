from datetime import datetime

from src import voorspel

user_id = 114

start = datetime.now()
model = voorspel.make_model(user_id)
print('model created in: ', datetime.now() - start)  # model created in:  0:02:19.446976
print('model:')
print(model)

prediction = voorspel.get_prediction(user_id, hour=23)
print('prediction:')
print(prediction)
