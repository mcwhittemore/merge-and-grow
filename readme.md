# merge-and-grow

This is a simple cli that takes in as arguments the path to 640x640 images. It then merges them and grows them to 3200x3200 pixels.

## Usage

`python run.py OUTFILE.jpg in_file_one.jpg in_file_two.jpg ... in_file_n.jpg`


## Example

`python run.py test.jpg $(ls ./test-imgs/*.jpg)`

![](./test.jpg)
