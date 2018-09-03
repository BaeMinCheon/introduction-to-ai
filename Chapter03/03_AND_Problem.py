import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

learningRate = 0.1

dataIn = [[1.0, 1.0], [1.0, -1.0], [-1.0, 1.0], [-1.0, -1.0]] # 4x2
dataOut = [[1.0], [-1.0], [-1.0], [-1.0]] # 4x1

weight = tf.Variable([[1.0], [1.0]]) # 2x1
bias = tf.Variable([1.0]) # 1x0
output = tf.tanh(tf.add(tf.matmul(dataIn, weight), bias)) # 4x1
error = tf.divide(tf.reduce_mean(tf.square(tf.subtract(output, dataOut))), 2.0)

# input -> mul -> add -> tanh -> error
#        weight   bias

devError = tf.subtract(output, dataOut) #4x1
devTanh = tf.multiply(devError, tf.subtract(1.0, tf.square(output))) # 4x1
devAdd = devTanh # 4x1

devOfWeight = tf.divide(tf.matmul(tf.transpose(dataIn), devAdd), 2.0) # 2x1 = 2x4 * 4x1
devOfBias = tf.reduce_mean(devAdd, axis=[0])

trainOfWeight = tf.assign(weight, tf.subtract(weight, tf.multiply(devOfWeight, learningRate)))
trainOfBias = tf.assign(bias, tf.subtract(bias, tf.multiply(devOfBias, learningRate)))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(1001):
        errorV, weightV, biasV, outputV, weightTR, biasTR = sess.run([
            error, weight, bias, output, trainOfWeight, trainOfBias])
        
        # print("train number #{}".format(i))
        # print(" error : {} \n weight \n{} \n sum \n{} \n output \n{} \n\n".format(errorValue, weightValue, sumValue, outputValue))
        
        if i % 100 == 0:
            print("train number #{}".format(i))
            print(" error : {}".format(errorV))
            print(" weight \n{}".format(weightV))
            print(" bias \n{}".format(biasV))
            print()

print("\n \t TRAIN DONE")