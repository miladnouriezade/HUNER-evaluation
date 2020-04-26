# HUNER

This repository stands for applying and evaluating [HUNER pre-trained model](https://github.com/hu-ner/huner#models) (`"disease_all"`) on `"BC5CDR-Disease"` data set .

## Installation

1. [Install docker](https://docs.docker.com/install/)
2. Download  pretrained model (`"disease_all"`) from [here](https://drive.google.com/open?id=12vdtSi3hg_htCXXROKkPV4jaDO3ep8OY), place it  into `huner/models` directory and untar it using

```bash
tar xzf disease_all.tar.gz
```

## Prediction

For applying prediction on `BC5CDR-Disease` data set we need to remove labeles from `.tsv` file and convert it to pre-tokenized `.txt` file that tokens are seprated by whitespace.

1. Use `tokenized_txt.py` in `helper` folder for preprocess your `.tsv` data and make it ready for using as model input.

    e.g. `tokenized_test.txt`

    ```
    Selegiline - induced postural hypotension in Parkinson ' s disease : a longitudinal study on the effects of drug withdrawal .
    ```

2. Start HUNER server  using

   ```bash
    ./start_server.sh disease_all
    ```

    > model must reside in `models` directory .

3. While server is running use another terminal tab for tagging input data using

    ```bash
    python client.py --name disease_all --assume_tokenized  /path/to/tokenized_test.txt OUTPUT.CONLL
    ```

    The output will then be written to `OUTPUT.CONLL` .

### Result

`OUTPUT.CONLL` sample result on `tokenized_test.txt` looks like this

```
Torsade	POS	B-NP
de	POS	I-NP
pointes	POS	I-NP
ventricular	POS	I-NP
tachycardia	POS	I-NP
during	POS	O
low	POS	O
dose	POS	O
intermittent	POS	O
dobutamine	POS	O
treatment	POS	O
in	POS	O
a	POS	O
patient	POS	O
with	POS	O
dilated	POS	B-NP
cardiomyopathy	POS	I-NP
and	POS	O
congestive	POS	B-NP
heart	POS	I-NP
failure	POS	I-NP
.	POS	O
The	POS	O
authors	POS	O
describe	POS	O
the	POS	O
case	POS	O
of	POS	O
a	POS	O
56	POS	O
-	POS	O
year	POS	O
-	POS	O
old	POS	O
woman	POS	O
with	POS	O
chronic	POS	O
,	POS	O
severe	POS	O
heart	POS	B-NP
failure	POS	I-NP
secondary	POS	O
to	POS	O
dilated	POS	B-NP
cardiomyopathy	POS	I-NP
and	POS	O
absence	POS	O
of	POS	O
significant	POS	O
ventricular	POS	B-NP
arrhythmias	POS	I-NP
who	POS	O
developed	POS	O
QT	POS	B-NP
prolongation	POS	I-NP
and	POS	O
torsade	POS	B-NP
de	POS	I-NP
pointes	POS	I-NP
ventricular	POS	I-NP
tachycardia	POS	I-NP
during	POS	O
one	POS	O
cycle	POS	O
of	POS	O
intermittent	POS	O
low	POS	O
dose	POS	O
(	POS	O
2	POS	O
.	POS	O
5	POS	O
mcg	POS	O
/	POS	O
kg	POS	O
per	POS	O
min	POS	O
)	POS	O
dobutamine	POS	O
.	POS	O

```

## Evaluation

We use [seqeval](https://github.com/chakki-works/seqeval) `classification_report(y_true, y_pred)` metric to evaluate HUNER model .

### Setting up an environment

1.  [Follow the installation instructions for Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html?highlight=conda#regular-installation).
2. Create a Conda environment called "seqeval" with Python 3.7.6:
    ```bash
    conda create -n seqeval python=3.7.6
    ```
3. Activate the Conda environment:

    ```bash
    conda activate seqeval
    ```

### Installation

To install seqeval, simply run:

```
$ pip install seqeval[cpu]
```

If you want to install seqeval on GPU environment, please run:

```bash
$ pip install seqeval[gpu]
```

### Requirement

* numpy >= 1.14.0

### Preprocess and Evaluate

Since `OUTPUT.CONLL` format is a little bit different from `BC5CDR-Disease` IOB schemed, we need to modify our `BC5CDR-Disease` data.

* `BC5CDR-Disease`

    ```
    Torsade	B
    de	I
    pointes	I
    ventricular	B
    tachycardia	I
    during	O
    low	O
    dose	O
    intermittent	O
    dobutamine	O
    treatment	O
    in	O
    a	O
    patient	O
    with	O
    dilated	B
    cardiomyopathy	I
    and	O
    congestive	B
    heart	I
    failure	I
    .	O

    ```

* `OUTPUT.CONLL`
    ```
    Torsade	POS	B-NP
    de	POS	I-NP
    pointes	POS	I-NP
    ventricular	POS	I-NP
    tachycardia	POS	I-NP
    during	POS	O
    low	POS	O
    dose	POS	O
    intermittent	POS	O
    dobutamine	POS	O
    treatment	POS	O
    in	POS	O
    a	POS	O
    patient	POS	O
    with	POS	O
    dilated	POS	B-NP
    cardiomyopathy	POS	I-NP
    and	POS	O
    congestive	POS	B-NP
    heart	POS	I-NP
    failure	POS	I-NP
    .	POS	O
    ```

Use `test.tsv` or any file that you used it for prediction in `BC5CDR-Disease` data set and replace all `B` tags with `B-NP` and all `I` tags with `I-NP` using Exel .

E.g.`test.tsv` shuold look like this after modification .

```
Torsade	B-NP
de	I-NP
pointes	I-NP
ventricular	B-NP
tachycardia	I-NP
during	O
low	O
dose	O
intermittent	O
dobutamine	O
treatment	O
in	O
a	O
patient	O
with	O
dilated	B-NP
cardiomyopathy	I-NP
and	O
congestive	B-NP
heart	I-NP
failure	I-NP
.	O
```

Now use `evaluation.py` in `helper/evaluation` folder to evaluate model .
