import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s \t %(message)s")


def record_net_data_stats(y_train, net_dataidx_map):
    net_cls_counts = {}

    for net_i, dataidx in net_dataidx_map.items():
        unq, unq_cnt = np.unique(y_train[dataidx], return_counts=True)
        tmp = {unq[i]: unq_cnt[i] for i in range(len(unq))}
        net_cls_counts[net_i] = tmp
        logging.info("Data statistics %d: %s" % (net_i, str(tmp)))
    return net_cls_counts


min_size = 0
K = 10
#N = y_train.shape[0]
N = 50000
device_count = 3
logging.info("N = " + str(N))

device_data_proportions = [0.1, 0.8, 0.1]

net_dataidx_map = {}
y_train = np.random.randint(10, size=N)

while min_size < 10:
    idx_batch = [[] for _ in range(device_count)]
    # for each class in the dataset
    for k in range(K):
        idx_k = np.where(y_train == k)[0]
        np.random.shuffle(idx_k)
        proportions = np.random.dirichlet([100, 10, 1])
        ## Balance
        proportions = np.array([p * (len(idx_j) < N * sample_size) 
                                for p, idx_j, sample_size 
                                in zip(proportions, idx_batch, device_data_proportions)])
        proportions = proportions / proportions.sum()
        proportions = (np.cumsum(proportions) * len(idx_k)).astype(int)[:-1]
        idx_batch = [idx_j + idx.tolist() for idx_j, idx in zip(idx_batch, np.split(idx_k, proportions))]
        min_size = min([len(idx_j) for idx_j in idx_batch])

    for j in range(device_count):
        np.random.shuffle(idx_batch[j])
        net_dataidx_map[j] = idx_batch[j]
        logging.info("Data statistics %d: %d" % (j, len(idx_batch[j])))
traindata_cls_counts = record_net_data_stats(y_train, net_dataidx_map)