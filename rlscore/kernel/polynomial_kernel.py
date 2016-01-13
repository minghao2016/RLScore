from scipy import sparse as sp
from rlscore.utilities import array_tools


class PolynomialKernel(object):
    """Polynomial kernel.
    
    k(xi,xj) = (gamma * <xi, xj> + coef0)**degree

    Parameters
    ----------
    X: {array-like, sparse matrix}, shape = [n_samples, n_features]
        Data matrix
    gamma : float, optional (default 1.0)
        Kernel parameter
    coef0 : float, optional (default 0.)
        Kernel parameter
    degree : float, optional (default 2)
        Kernel parameter
    """

    def __init__(self, X, degree=2, gamma=1.0, coef0=0):
        self.train_X = X
        self.degree = degree
        self.gamma = gamma
        self.coef0 = coef0
        

    def getKM(self, X):
        """Returns the kernel matrix between the basis vectors and X.
        
        Parameters
        ----------
        X: {array-like, sparse matrix}, shape = [n_samples, n_features]
        
        Returns
        -------
        K : array, shape = [n_samples, n_bvectors]
            kernel matrix
        """
        test_X = X
        degree, coef0, gamma = self.degree, self.coef0, self.gamma
        if sp.issparse(test_X):
            test_X = array_tools.spmat_resize(test_X, self.train_X.shape[1])
        else:
            test_X = array_tools.as_dense_matrix(test_X)
        train_X = self.train_X
        K = array_tools.as_array(train_X * test_X.T)
        K *= gamma
        K += coef0
        K = K ** degree
        return K.T

