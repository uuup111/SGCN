import numpy as np
from sklearn import manifold
import matplotlib.pyplot as plt


def laplacian(W, normalize=True):
    # 检查输入
    N = W.shape[0]
    #assert N == config.graphsize
    d = np.sum(W, axis=0)
    d[d == 0] = 0.1
    if not normalize:
        D = np.diag(d)
        L = D - W
    else:
        d_sqrt = np.sqrt(d)
        d = 1 / d_sqrt
        D = np.diag(d)
        I = np.diag(np.ones(N))
        L = I - np.dot(np.dot(D, W), D)
    return L


def fourier(L):
    def sort(lamb, U):
        idx = lamb.argsort()
        return lamb[idx], U[:, idx]
    # 列 U[:,i] 是特征向量
    lamb, U = np.linalg.eig(L)
    lamb, U = sort(lamb, U)
    return lamb, U


def t_SNE(X, y):
    tsne = manifold.TSNE(n_components=2, init='pca', random_state=501, perplexity=40)
    X_tsne = tsne.fit_transform(X)
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化

    # 画 train data 的分布
    plt.figure(figsize=(6, 6))
    plt.scatter(X_norm[:, 0], X_norm[:, 1], s=150, c=y, alpha=.7)
    plt.xticks([])
    plt.yticks([])
    plt.show()