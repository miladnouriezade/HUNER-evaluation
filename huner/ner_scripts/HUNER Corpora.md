# HUNER Corpora

## Setting up an environment

1.  [Follow the installation instructions for Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html?highlight=conda#regular-installation).
2. Create a Conda environment called "huner-corpora" with Python 3.6:
    ```bash
    conda create -n huner-corpora python=3.6
    ```
3. Activate the Conda environment:

    ```bash
    conda activate huner-corpora
    ```

## Installation

Use `requirments.txt` in `huner/ner_scripts` and install requirment packages using

```bash
pip install -r requirments.txt
```

Download and install [Apache OpenNLP](https://opennlp.apache.org/download.html)

1. Download `apache-opennlp-1.9.2-bin.tar.gz` and untar it using

    ```bash
    tar xzf apache-opennlp-1.9.2-bin.tar.gz
    ```

2. Save `asc` file for `apache-opennlp-1.9.2-bin.tar.gz` as `apache-opennlp-1.9.2-bin.tar.gz.asc` .

3. Save [KEYS file](https://www.apache.org/dist/opennlp/KEYS)
as `KEYS.txt` and import it using

    ```bash
    gpg --import KEYS.txt

    ```

4. Use below commands to verify the integrity:

    ```bash
    gpg --print-md sha512 apache-opennlp-1.9.2-bin.tar.gz
    ```

    ```bash
    gpg --verify apache-opennlp-1.9.2-bin.tar.gz.asc

    ```

5. Download following models from [here](http://opennlp.sourceforge.net/models-1.5/), create a `models/` subdirectory in `apache-opennlp-1.9.2` and move downloaded models there .

    ```
    en-pos-maxent.bin
    en-sent.bin
    en-token.bin
    ```

## Usage

To obtain the corpora run:

```bash
python download_files.py
```

If you get the error

```bash
rarfile.RarUnknownError: Unknown exit code [1]: bsdtar: Error opening archive:
```

look at this question in [Stackoverflow](https://stackoverflow.com/questions/37737850/python-rarfile-package-fail-to-open-files)
.
> You'll be instructed to download the CDR and bc2gm data .

> For bc2gm data you must download `Task 1 - GM Subtask, test set, v1.0` and `Task 1 - GM Subtask, training set, v1.1` untar them and move `train` and `test` folders to `bc2gm`.

To convert and split the corpora please run:
```
OPENNLP=/apache-opennlp-1.9.2/bin/opennlp 
 ./convert_corpora.sh
```
Please be aware that this will take a couple of days, as the syntactic analysis of hugh corpora are computationally expensive.

If you are an experienced unix user and have a multi-core machine with at least 32GB of memory available, you can also use:
```
OPENNLP=/apache-opennlp-1.9.2/bin/opennlp 
 ./convert_corpora_parallel.sh
```
This will run all conversions in parallel, reducing the runtime to less than a day. Please be aware that due to concurrency issues, some conversion tasks may fail. Those have to be restarted manually, together with the downstream processing.