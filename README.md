# Pixel Sorter Script
This super simple script sorts an image's pixels

## Why would I want this
To bypass copyright laws ofc

## Installation
You may clone this repository using git
```sh
$ git clone https://github.com/Aceroph/pixel-sorter.git
```
After that, enter the project's directory
```sh
cd pixel-sorter
```

## Setup
After installing the script, you must download its dependencies

### Using virtual environments
First create a virtual environment
```sh
$ python3 -m venv .venv
```
Then install the dependencies ive listed under `requirements.txt`
```sh
$ python3 install -r requirements.txt
```

### Using nix
For those who use nix, simply run
```sh
$ nix-shell
```

## Usage
```sh
python3 main PATH_TO_IMAGE
```
