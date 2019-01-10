import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from create_feature import *


columns = ['html', 'javascript', 'urlCount', 'attachCount']
for i in range(100):
    columns.append('vector{}'.format(i))

ham_email_feature = email_feature_ham
spam_email_feature = email_feature_spam

ham_email = DataFrame(ham_email_feature, columns=columns)
spam_email = DataFrame(spam_email_feature, columns= columns)
train_x = pd.concat([spam_email, ham_email], axis= 0)
train_x = train_x.reset_index()
ham_email['label'] = 0
spam_email['label'] = 1
train_y = pd.concat([spam_email['label'], ham_email['label']], axis = 0)
train_y = train_y.reset_index()
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, random_state = 42)
x_train = x_train.drop(['index'], axis= 1)
x_test = x_test.drop(['index'], axis= 1)
y_train = y_train.drop(['index'], axis= 1)
y_test = y_test.drop(['index'], axis= 1)



#gbdt = GradientBoostingClassifier()
mlp = MLPClassifier(solver='lbfgs', activation= 'tanh', random_state= 0, hidden_layer_sizes= [10, 10])
#xgb = XGBClassifier()
mlp.fit(x_train, y_train)
preds =mlp.predict(x_test)
