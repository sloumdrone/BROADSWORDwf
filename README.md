# BROADSWORDwf: Batch Assignment Tool


## Objective
This tool allows the input of a CSV list of carrierIDs that all share the same starting periodID to be assigned out. They can be assigned to any member of the team, and they can be assigned for any of the following: 1st, 2nd, QA, or GoLive. In general the tool will be most useful for large sets of carrierIDs, such as multistate health carriers. However, it is functional if you wanted to use it to assign single carrierIDs as well.

## Use
#### General
Enter the data asked for and all will function fine. The username is generally an e-mail address (use your work front login info).

#### Dependencies
 - Requires python 2.7.X

##### Notes
1. Requires the workfront file 'api.py' included in this repo.
1. An executable version is available, it functions the same as the PY version. To use this version, just download the zip file BROADSWORDwf.zip from this repository. Extract the contents to a folder and run the file BROADSWORDwf.exe. This version does not provide direct access to console logging, and as such should be used carefully and with purpose.
1. Designed for a particular company. Could likely be modified to work with other Workfront setups for any batch assignment needs (which WF doesn't appear to easily support out of the box).
