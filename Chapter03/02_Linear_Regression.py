import tensorflow as tf
import matplotlib.pyplot as plt

trainX = [1, 2, 3]
trainY = [1, 2, 3]

inputX = tf.placeholder(tf.float32)
inputY = tf.placeholder(tf.float32)
weight = tf.Variable([1.0], name='weight')
bias = tf.Variable([1.0], name='bias')

hypothesis = weight * inputX + bias
cost = tf.reduce_mean(tf.square(hypothesis - inputY)) / 2.0

learning_rate = 0.1
gradient = tf.reduce_mean((weight * inputX + bias - inputY) * inputX)
descent = weight - learning_rate * gradient
update = weight.assign(descent)

weightHistory = []
costHistory = []

sess01 = tf.Session()
sess01.run(tf.global_variables_initializer())
for step in range(21):
    sess01.run(update, feed_dict={inputX: trainX, inputY: trainY})
    currentWeight = sess01.run(weight)
    currentCost = sess01.run(cost, feed_dict={inputX: trainX, inputY: trainY})
    weightHistory.append(currentWeight)
    costHistory.append(currentCost)
    print(step, currentCost, currentWeight)
    
plt.plot(weightHistory, costHistory)
plt.show()