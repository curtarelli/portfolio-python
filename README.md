# Python Script Portfolio
This is a professional Portfolio of data science scripts for engineering and remote sensing applications in order to deal with environmental data fora variety of purposes.
Here one can find simple codes and complex applications write in **Python** (`.py`) and **Jupyter Notebook** (`.ypnb`).

* Data pre processing;
	* Data Frame composing and arranjement;
	* Data smoothing;
	* Data calibration;
* Graphical plots functions;
* Statistical functions and analysis;
* Remote sensing data/images applications;
* Others.

The featured `Python` applications are:

1) [TriOS-RAMSES sensors calibration](./trios-calibration "trios-calibration application"), a application that calibrates radiometric raw data measurements;

2) [Statistical Funcitons](./statistical-functions "statistical-functions application")

## Installation - Requirements

To copy all scripts of this **Portfolio** open a python prompt (e.g. Anaconda or Miniconda prompt). To do that, inside the prompt, go inside the
folder in which you want to download this repository and run the following comands:

```
$	git clone https://github.com/curtarelli/portfolio
$	cd portfolio
$	conda env create --name "your-env-name"
$	conda activate "your-env-name"
$	pip install -r requirements.txt
```