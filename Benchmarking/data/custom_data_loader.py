import fedml
from .efficient_loader import efficient_load_partition_data_cifar10
import json

def load_data(args):
    fedml.logging.info("load_data. dataset_name = %s" % args.dataset)
    (
        train_data_num,
        test_data_num,
        train_data_global,
        test_data_global,
        train_data_local_num_dict,
        train_data_local_dict,
        test_data_local_dict,
        class_num,
    ) = efficient_load_partition_data_cifar10(
        args.dataset,
        args.data_cache_dir,
        args.partition_method,
        args.partition_alpha,
        args.client_num_in_total,
        args.batch_size,
        client_proportions= json.loads(args.client_proportions),
    )
    
    dataset = [
        train_data_num,
        test_data_num,
        train_data_global,
        test_data_global,
        train_data_local_num_dict,
        train_data_local_dict,
        test_data_local_dict,
        class_num,
    ]
    return dataset, class_num
