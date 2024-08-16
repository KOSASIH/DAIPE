import tensorflow as tf

class NeuralNetwork:
    def __init__(self, input_shape, output_shape):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(output_shape, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train(self, X, y):
        self.model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

    def predict(self, X):
        return self.model.predict(X)
