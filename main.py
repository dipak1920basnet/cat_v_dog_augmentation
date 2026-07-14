from model_training.train_model import train
from visualization.plot_loss import plot_loss_acc
from model_training.deep_model import create_model

model = create_model()
history = train(model)
plot_loss_acc(history=history)