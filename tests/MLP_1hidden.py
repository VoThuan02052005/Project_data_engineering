# khai bai thu vien
import numpy as np

# activatio layer
def relu(z):
    return np.maximum(0, z)
def linear(z):
    return z
# ham sai so
def mse_loss(y, y_hat):
    return np.mean((y-y_hat)**2)
# khoi tao tham so
def init_para(n_input, n_hidden, n_output):
    para = {
        "w1": np.random.randn(n_input, n_hidden),
        "b1" : np.zeros((1, n_hidden)),
        "w2": np.random.randn(n_hidden, n_output),
        "b2" : np.zeros((1, n_output))
    }
    return para
# lan truyen tien
def forward_propagation(X, para):
    w1, b1 , w2, b2 = para["w1"], para["b1"], para["w2"], para["b2"]
    z1 = np.dot(X, w1) + b1
    a1 = relu(z1)
    z2 = np.dot(a1, w2) + b2
    y_hat = linear(z2)
    cache = {
        "z1": z1,
        "a1": a1,
        "z2": z2,
        "y_hat": y_hat
    }
    return cache
# lan truyen nguoc
def backward_propagation(X, y, cache, para):
    a1 , z1 = cache["a1"], cache["z1"]
    w2 = para["w2"]
    n = X.shape[0]
    dz2 = (cache["y_hat"] - y)/n
    dw2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0)
    dz1 = dz2 @ w2.T * (z1 > 0)
    dw1 = np.dot(X.T, dz1)
    db1 = np.sum(dz1, axis=0)
    grads = {
        "dw1": dw1,
        "db1": db1,
        "dw2": dw2,
        "db2": db2
    }
    return grads
# cap nhat trong so
def update_parameters(para, grads, learning_rate):
    para["w1"] -= learning_rate * grads["dw1"]
    para["b1"] -= learning_rate * grads["db1"]
    para["w2"] -= learning_rate * grads["dw2"]
    para["b2"] -= learning_rate * grads["db2"]
    return para
# ham train
def train(X, y, epochs , learning_rate):
    n_input = X.shape[1]
    n_hidden = 50
    n_output = y.shape[1]
    para = init_para(n_input, n_hidden, n_output)
    for i in range (epochs):
        cache =forward_propagation(X, para)
        y_hat = cache["y_hat"]
        loss = mse_loss(y, y_hat)
        grads = backward_propagation(X, y, cache , para)
        para = update_parameters(para, grads, learning_rate)
        print(f"epoch: {i}, loss: {loss}")
    return para
# ham du doan
def predict(X, para):
    cache = forward_propagation(X, para)
    y_hat = cache["y_hat"]
    return y_hat
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = (X[:, 0] * 2 + X[:, 1] * 3 + 1).reshape(-1, 1)
    print(X.shape)

    # Train
    params = train(X, y , epochs=1000, learning_rate=0.1)




