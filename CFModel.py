# A simple implementation of matrix factorization for collaborative filtering expressed as a Keras Sequential model

import numpy as np
from keras.layers import Embedding, Reshape, Merge, Dropout, Dense
from keras.models import Sequential

class CFModel(Sequential):

    def __init__(self, n_users, m_items, k_factors, **kwargs):
        P = Sequential()
        P.add(Embedding(n_users, k_factors, input_length=1))
        P.add(Reshape((k_factors,)))
        Q = Sequential()
        Q.add(Embedding(m_items, k_factors, input_length=1))
        Q.add(Reshape((k_factors,)))
        super(CFModel, self).__init__(**kwargs)
        self.add(Merge([P, Q], mode='dot', dot_axes=1))

    def rate(self, user_id, item_id):
        return self.predict([np.array([user_id]), np.array([item_id])])[0][0]
