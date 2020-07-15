import numpy as np
import matplotlib.pyplot as plt

def import_txt_data(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(line.replace("\n","").split(","))
    data = np.array(data, dtype = np.float)
    return data
def load_dataset(raw_data):
    m = len(raw_data)
    X = raw_data[:, :-1].reshape(1,m)
    Y = raw_data[:, -1].reshape(1,m)
    return X, Y

def normalize_data(X):
    X_norm = np.linalg.norm(X, axist=1)
    return X / X_norm 

def scatter_plot (X, Y, X_label, Y_label, marker, hold= True):
    X_raw = X.flatten()
    Y_raw = Y.flatten()
    plt.plot(X_raw, Y_raw, marker)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    if not hold:
        plt.show()

def initialize_parameters(num_features):
    w = np.zeros((num_features,1))
    b = 0
    return w, b

def compute_cost_and_gradients(X, Y, w, b):
    m = X.shape[1]
    Y_hat = w.T.dot(X) + b 
    
    ## Compute cost
    error = (Y_hat - Y)**2
    cost = (1/2*m)*np.sum(error)
    
    ## Compute gradients
    dw = (1/m)*X.dot((Y_hat - Y).T)
    db = (1/m)* np.sum((Y_hat -Y))
    grads = {'dw' : dw, 'db' : db}
    return cost, grads

def optimize(X, Y, w, b, learning_rate, num_iterations, plot=True):
    costs = []
    for i in range(num_iterations):
        cost, grads = compute_cost_and_gradients(X, Y, w, b)
        dw = grads['dw']
        db = grads['db']
        ## START CODING HERE
        w = w - learning_rate*grads['dw']
        b = b - learning_rate*grads['db']
        ## END
        costs.append(cost)
     
    if plot:
        plt.xlim([0, num_iterations])
        plt.plot(np.arange(num_iterations), costs, 'b,')
        plt.xlabel('iterations')
        plt.ylabel('J(w, b)')
        plt.show()
    
    params = {'w' : w, 'b' : b}
    return params, grads, costs

def model(X, Y, learning_rate, num_iterations, plot=True):
    num_features = len(X)
    w, b = initialize_parameters(num_features)
    
    params, grads, cost = optimize(X, Y, w, b, learning_rate, num_iterations, plot=True)
    return params, grads, cost    

file_name = 'exdata1.txt'
raw_data = import_txt_data(file_name)
X, Y = load_dataset(raw_data)
scatter_plot(X, Y, 'area (feet$^2$)', 'prices (1000$)', 'rx', hold=False)
params, grads, cost = model(X, Y, 0.01, 200, False)

scatter_plot(X, Y, 'area (feet$^2$)', 'prices (1000$)', 'rx', hold=True)
# Plot linear fit
plt.plot(X.flatten(), (params['w'].T.dot(X) + params['b']).flatten())
plt.show()
    
    