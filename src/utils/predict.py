import sys
from Models.ConvNet import Model
import json

with open("/Users/kisisel/Desktop/Kodlama/Python/Machine Learning/genre_classification_tf/config.json", "r") as fp:
    config = json.load(fp)


def predict(audio_path):
    if len(audio_path) < 1:
        return
    else:
        samples_per_segment = int(
            (config["sample_rate"] * config["sample_duration"]) / config["num_segments"])

        model = Model(data_path=config["data_path"], weights_path=config["weights_path"],
                      test_size=config["test_size"], validation_size=config["validation_size"])
        model.create_model()
        return model.predict(audio_path, sample_rate=config["sample_rate"],
                             samples_per_segment=samples_per_segment, n_mfcc=config["n_mfcc"],
                             n_fft=config["n_fft"], hop_length=config["hop_length"])
