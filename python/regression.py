import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, np.newaxis, 2]  # 只是用一个特征
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)

print('Coefficients: \n', regr.coef_)
print('Mean squared error: %.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('Coefficient of determination: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

with plt.style.context('Solarize_Light2'):
    plt.scatter(diabetes_X_test, diabetes_y_test)
    plt.plot(diabetes_X_test, diabetes_y_pred, color="#859900", linewidth=3)

    plt.xticks(())
    plt.yticks(())

plt.savefig('regression.svg', transparent=True)
plt.show()
