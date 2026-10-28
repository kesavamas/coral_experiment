# Run from the YOLOv5 repository root after applying the MAFFN patches.
# Example:
# python train_coral_maffn.py --data data/coral.yaml --weights yolov5s.pt --epochs 100 --img 640 --batch-size 16

import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="C:\\Users\\kesavaMas\\program\\python\\yolov5-master\\coral\\data.yaml")
    parser.add_argument("--weights", default="yolov5s.pt")
    parser.add_argument("--cfg", default="models/yolov5s_coral_maffn.yaml")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--img", type=int, default=416)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--device", default="")
    parser.add_argument("--name", default="coral_maffn")
    args = parser.parse_args()

    cmd = [
        sys.executable, "train.py",
        "--data", args.data,
        "--weights", args.weights,
        "--cfg", args.cfg,
        "--epochs", str(args.epochs),
        "--img", str(args.img),
        "--batch-size", str(args.batch_size),
        "--name", args.name,
    ]
    if args.device:
        cmd += ["--device", args.device]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
