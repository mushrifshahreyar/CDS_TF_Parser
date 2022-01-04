## Python Script for CDS and Table Functions

### Installation
1. Install python3 using the link provided below

    [Python Installation Demo] (https://phoenixnap.com/kb/how-to-install-python-3-windows)

    [Python Installer Download Link] (https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe)

2. Install the `xlsxwriter` python module using the following command.

    ```pip install xlsxwriter```

    [For installation help, click on the link below] (https://xlsxwriter.readthedocs.io/getting_started.html)


### For executing the script

For CDS Parser: `cds_parser.py` 

For Table function Parser: `tablefunc_parser.py`

#### Steps to execute: *CDS_PARSER.py*

1. Open cmd and navigate to the current folder.
2. Copy paste the contents of the required cds file into the ```cdsview.txt``` file.
3. For executing the python script for cds parser.

    - ```python cds_parser.py *outputfilename*.xlsx```
    - Replace the `outputfilename` with the required filename. For example: 
    ```
    python cds_parser.py CDS_view.xlsx
    ```
4. You will be the able to see the generated excel sheet with the required components and associations.


#### Steps to execute: *TABLEFUNC_PARSER.py*

1. Open cmd and navigate to the current folder.
2. Copy paste the contents of the required table function file into the ```tf.txt``` file.
3. For executing the python script for table function parser.

    - ```python tablefunc_parser.py *outputfilename*.xlsx```
    - Replace the `outputfilename` with the required filename. For example: 
    ```
    python tablefunc_parser.py TF_VIEW.xlsx
    ```
4. You will be the able to see the generated excel sheet with the required components and Date Type.


