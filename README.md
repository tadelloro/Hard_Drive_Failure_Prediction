### Hard Drive Failure Prediction in the Data Center

#### Problem
The purpose of this project is to predict hard disk drive (HDD) failure using operational machine sensor data from the Backblaze data center. Most modern enterprise class hard drives include a self-monitoring system ― aptly named Self-Monitoring, Analysis and Reporting Technology (SMART) ― that records real-time sensor data that may be used to detect malfunctions and anticipate system failures. The current study focuses on the Seagate model ST12000NM0007 from the Backblaze dataset, as this model is one of the most common HDDs in the dataset.

#### Jupyter Notebooks and scripts
* funcs_hrddrv.py includes a few functions for plotting and data visualization.
* p0_data_acquisition.py is a script to pull the raw HDD data from the Backblaze data center website. 
* p1_process.py is a script used to process, clean, and format the data prior to modeling. This step also includes the relabeling method used to implement classification of HDD failures.
* Stage 1 includes code for initial exploratory data analysis.
* Stage 2 includes code for failure detection via classification modeling: i.e., model optimization, testing, and performance results.

#### Dataset
The dataset used in this study was acquired from the Backblaze data center and consists of real-world operational data from over 100,000 active hard drives; data include the date of failure, serial number, model type, capacity, and daily SMART attribute readings.

The dataset may be found here:
* https://www.backblaze.com/b2/hard-drive-test-data.html

#### Business Case
Systems failure prediction is of interest in numerous industries including aerospace, agriculture, energy, manufacturing, and technology. Accurate prediction may allow for better inventory management, maintenance scheduling, and reduction of downtime.







