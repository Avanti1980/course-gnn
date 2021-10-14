# coding:utf-8
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
data = digits.images.reshape((len(digits.images), -1))
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)

clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)  # 训练
predicted = clf.predict(X_test)  # 预测

figure = plt.figure(figsize=(12, 7))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

with plt.style.context('Solarize_Light2'):

    for i in range(30):
        ax = plt.subplot(5, 10, i+1)
        ax.set_axis_off()
        ax.imshow(digits.images[i], interpolation='nearest')
        ax.set_title('训练: %i' % digits.target[i], fontdict={'fontsize': 12})

    for i in range(20):
        ax = plt.subplot(5, 10, i+31)
        ax.set_axis_off()
        ax.imshow(X_test[i].reshape(8, 8), interpolation='nearest')
        ax.set_title('预测: %i' % predicted[i], fontdict={'fontsize': 12})

print(f"{clf}的分类结果\n"
      f"{metrics.classification_report(y_test, predicted)}\n")

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("混淆矩阵")
print(f"混淆矩阵\n{disp.confusion_matrix}")

plt.tight_layout()
plt.show()
