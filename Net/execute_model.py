from . import Net



def execute_model() -> float:

    net = Net(
        train_path="Net/image_set/train", 
        test_path="Net/image_set/test", 
        valid_path="Net/image_set/validator"
        )
    
    train_generator, test_generator, valid_generator = net.load_image_set()
    model = net.neural_model(train_generator, valid_generator)

    return model.evaluate(test_generator)[1]