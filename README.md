# Python-API

Python-API is a small web application that provides an API for 
accessing files stored locally on the server. This project provides two 
versions of application. One using Httpserver and socket server, other using
flask. 

## Installation

If using non-Flask version, no installation is needed.
If using Flask version, use package manager to install Flask first.
```bash
pip install flask
```
## Usage

First, start the server in your terminal using one of the main.py files
```bash
python3 flask.main.py
```
Once the server is running, web browser can be opened and the program can 
be reached using an address (default: localhost:8000). 

Root path (localhost:8000/) gives server status update. 
```json
{"message":"Server is running."}
```
Anything after root will be taken as a directory name and searched for in
project directory. Then the content in directory will be output or an
error raised. (localhost:8000/files)
```json
{"Files": ["grains.sh", "secret_handshake.sh", "leap.sh", 
  "pangram.sh", "errors.sh", "largest_series.sh", "hamming.sh", 
  "raindrops.sh", "armstrong.sh", "dif_of_squares.sh", "reverse.sh", 
  "allergies.sh"]}
```
Anything after directory name will be taken as a file name and searched 
for in before named directory. Then the content in the file will be 
output or an error raised. (localhost:8000/files/grains.sh)
```json
 {
   "filename": "reverse.sh", 
   "content": "['#!/usr/bin/bash\\n', ' \\n', ' read -p \"Enter a word: \" fullname\\n', '\\n', 'echo $fullname | rev']"
 }
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)