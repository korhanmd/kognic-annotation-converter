# Kognic Annotation Converter
Annotation converter project for Kognic coding test. The package reads a json file in Kognic annotation format and gives response in Open Label annotation format.

## Building

First write below command to the terminal to clone and navigate into the respository.

```
git clone https://github.com/korhanmd/kognic-annotation-converter
cd kognic-annotation-converter
```
Then write:

```
pip install -r requirements.txt
```

Use below command to build the package.

```
python3 setup.py bdist_wheel
```

## Installation

Use below command to install the package.

```
pip install annotation_converter
```

## Usage

To run the applicaton use below command.

```
python3 app.py
```

### Test with example input file
After the server is up and running [click here](http://127.0.0.1:5000/convert?filename=kognic_1.json) to see the result with the example input or write `http://127.0.0.1:5000/convert?filename=kognic_1.json` to the address line of browser.
You can also use the below command in terminal to see the result.

```
curl http://127.0.0.1:5000/convert?filename=kognic_1.json
```

### Test with custom file
To test the application with another file use the below format with browser or curl by changing `<file_name>` with the name of your file

```
http://127.0.0.1:5000/convert?filename=<file_name>
```
