# hadoop-transaction-count

Simple transaction count using Hadoop MapReduce.

## Requirements

1. [Python 3](https://www.python.org/)
2. [Apache Hadoop](https://hadoop.apache.org/releases.html)
3. [Apache Hadoop Streaming Library](https://jar-download.com/artifacts/org.apache.hadoop/hadoop-streaming/3.3.6)

## How to Use

1. Copy the sample data. Make sure to replace `/home/hadoop` with the actual location in your local machine. `hdfs dfs -copyFromLocal <Path_Local> <Path_hdfs>`

```sh
hdfs dfs -mkdir /data
hdfs dfs -copyFromLocal /home/hadoop/transaksi.csv /data/transaksi.csv
```

2. Run this command to run Hadoop MapReduce.

```sh
hadoop jar $HADOOP_HOME/lib/hadoop-*streaming*.jar \
-file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py \
-input /data/transaksi.csv -output /data/result_output
```

3. Check the result.

```sh
hdfs dfs -cat /data/result_output/part-00000
```
