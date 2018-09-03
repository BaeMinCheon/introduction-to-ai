import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 4x2 matrix
dataIn = [[1.0, 1.0], [1.0, -1.0], [-1.0, 1.0], [-1.0, -1.0]]
# 4x1 matrix
dataOut = [[-1.0], [1.0], [1.0], [-1.0]]

# 2x1 matrix
weight = tf.Variable([[1.0], [1.0]])
# 1x1 matrix
bias = tf.Variable([[1.0]])
# 4x1 matrix
sum = tf.matmul(dataIn, weight) + bias
output = tf.tanh(sum)
error = tf.reduce_mean(tf.square(tf.subtract(output, dataOut)))

# 4x1 matrix
sub = tf.subtract(1.0, tf.square(output))
# 2x4 matrix
derivativeOfWeight = tf.transpose(tf.multiply(dataIn, sub))
# 1x4 matrix
derivativeOfBias = tf.transpose(sub)
learningRate = 0.1

# 2x1 matrix = 2x4 matrix * 4x1 matrix
gradientOfWeight = tf.matmul(derivativeOfWeight, tf.subtract(output, dataOut)) / len(dataOut)
trainOfWeight = tf.assign(weight, tf.subtract(weight, tf.multiply(gradientOfWeight, learningRate)))
# 1x1 matrix = 1x4 matrix * 4x1 matrix
gradientOfBias = tf.matmul(derivativeOfBias, tf.subtract(output, dataOut)) / len(dataOut)
trainOfBias = tf.assign(bias, tf.subtract(bias, tf.multiply(gradientOfBias, learningRate)))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(1001):
        errorV, weightV, biasV, sumV, outputV, weightGD, weightTR, biasGD, biasTR = sess.run([
            error, weight, bias, sum, output, gradientOfWeight, trainOfWeight, gradientOfBias, trainOfBias])
        
        # print("train number #{}".format(i))
        # print(" error : {} \n weight \n{} \n sum \n{} \n output \n{} \n\n".format(errorValue, weightValue, sumValue, outputValue))
        
        if i % 100 == 0:
            print("train number #{}".format(i))
            print(" error : {}".format(errorV))
            print(" weight \n{}".format(weightV))
            print(" bias \n{}\n".format(biasV))

print("\n \t TRAIN DONE")