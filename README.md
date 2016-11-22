 ---------------------
|Batch Assignment Tool|
 ---------------------
 ~**by_Brian_Evans**~


============
1. Objective
============
This tool allows the input of a CSV list of carrierIDs that all share the same starting periodID to be assigned out. They can be assigned to any member of the time, and they can be assigned for any of the following: 1st, 2nd, QA, or GoLive. In general the tool will be most useful for large sets of carrierIDs, such as multistate carriers. However, it is functional if you wanted to use it to assign single carrierIDs as well.

======
2. Use
======
Enter the data asked for and all will function fine. The username is generally an e-mail address (use your work front login info).

========
3. Notes
========
A. Requires python 2.7.X
B. Requires the workfront file 'api.py' included in this folder.
C. Send feature requests or questions to brian.evans(AT)quotit.com
D. An executable version is available, it functions the same as the PY version. To use this version, just download the zip file BROADSWORDwf.zip from this repository. Extract the contents to a folder and run the file BROADSWORDwf.exe. This version does not provide direct access to console logging, and as such should be used carefully and with purpose (don't screw the pooch with careless updates).
