### ocl-csv-import
This is a script used to insert the Organization, Source and Concepts to OCL (Open Concept Lab)

#### Dependencies
  - Python 2.7 or Higher (Tested in Python 2.7)
  - `ocldev` library (https://pypi.org/project/ocldev/)


#### How to run
Update the below 3 fields in `csv-import.py` script for your environment.

```
csv_filename = '<csv-filename>'
ocl_env_url = '<ocl-api-endpoint>'
ocl_api_token = '<ocl-api-token>'

```
Run the Python script

```
python csv-import.py
```

#### CSV import Guide
Please follow the below link to understand the meaning of different columns and how to add the values for different objects (Org, Source, Concept, Mappings).
https://docs.google.com/document/d/1bQs1mh0mQhZpGcbl_J06i32e21oT5hy-ruJ34mVasL4/edit

Here is the link from OCL wiki - https://github.com/OpenConceptLab/oclapi/wiki/CSV-Import
