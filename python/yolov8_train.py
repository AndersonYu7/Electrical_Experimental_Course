from ultralytics import YOLO

# Load a model
model = YOLO("/home/iclab/work/src/models/yolov8n.pt")

# Train the model
train_results = model.train(
    data="/home/iclab/work/src/Hand_Detection_dataset/data.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="0",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
# metrics = model.val(data="/home/iclab-l/work/src/Hand_Detection_dataset/data.yaml")

# Perform object detection on an image
# results = model("/home/iclab-l/work/src/ultralytics/bus.jpg")
# results[0].show()

# predict model
# result = model.predict(
#     source="/home/iclab-l/work/src/ultralytics/bus.jpg",
#     mode="predict",
#     save=True,
#     device="cuda"
# )

# Export the model to ONNX format
# path = model.export(format="onnx")  # return path to exported model