import fedml
from fedml import FedMLRunner
from fedml.model.cv.resnet_gn import resnet18
from data.custom_data_loader import load_data

if __name__ == "__main__":
    # init FedML framework
    args = fedml.init()

    # init device
    device = fedml.device.get_device(args)

    # load data
    dataset, class_num = load_data(args)

    # create model and trainer
    model = resnet18(num_classes=class_num)
    
    # start training
    fedml_runner = FedMLRunner(args, device, dataset, model)
    fedml_runner.run()
