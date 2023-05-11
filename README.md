# Image Resizer and Compressor Script

This is a Python script that resizes and compresses .jpeg images in a specified directory. It uses the [Pillow](https://python-pillow.org/) library for resizing and the [TinyPNG](https://tinypng.com/) API for compression.

## Prerequisites

- Python 3
- [Pillow](https://python-pillow.org/) library
- [tinify](https://tinypng.com/developers) Python package

## Installation

1. Install Python 3 if you haven't already. You can download it from the [official website](https://www.python.org/downloads/).

2. Clone this repository:

    ```bash
    git clone https://github.com/Bistaaaa/resize-and-compress.git
    ```

3. Install the required Python packages:

    ```bash
    pip install pillow tinify
    ```

## Usage

1. Set your TinyPNG API key in the script:

    ```python
    tinify.key = "YOUR_API_KEY"
    ```

2. Specify the input and output directories in the script:

    ```python
    input_directory = r'C:\path\to\input\directory'
    output_directory = r'C:\path\to\output\directory'
    ```

3. Run the script:

    ```bash
    python "Resize and Compress Script.py"
    ```

This will resize and compress all .jpeg images in the input directory and save the processed images in the output directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Note

All of the above was written by ChatGPT-4. These are the only two sentences written by Bista XD
