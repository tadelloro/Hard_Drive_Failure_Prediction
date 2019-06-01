## Hard Drive Failure Prediction in the Data Center

#### Problem
The purpose of this project is to predict hard disk drive (HDD) failure using operational machine sensor data. Most modern enterprise class hard drives include a self-monitoring system ― aptly named Self-Monitoring, Analysis and Reporting Technology (SMART) ― that records real-time sensor data that may be used to detect malfunctions and anticipate system failures. The current study focuses on the Seagate model ST4000DM000, since this model is consistently among the most likely to fail, the oldest, and the most common HDDs in the dataset.

#### Jupyter Notebooks
* Stage 0 includes code for data acquisition.
* Stage 1 includes code for exploratory data analysis.
* Stage 2 includes code for Remaining Useful Life (RUL) estimation, i.e., target generation, model optimization, testing, and regression results.
* Stage 3 includes code for Anomaly Detection, i.e., relabeling methods, model optimization, testing, and classification results.

#### Datasets
The dataset used in this study was acquired from the Backblaze data center and consists of real-world operational data from over 100,000 active HDDs; data include the date of HDD failure, serial number, model type, capacity, and daily SMART attribute readings.

The dataset may be found here:
* https://www.backblaze.com/b2/hard-drive-test-data.html

#### Business Case
Systems failure prediction is a topic of interest in various industries including aerospace, agriculture, energy, manufacturing, and technology. Accurately predicting failure may allow for better inventory management, maintenance scheduling, and reduction of downtime.


