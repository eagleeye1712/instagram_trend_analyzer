import sys
import subprocess

file_path = sys.argv[1]

# Example command to put in HDFS
subprocess.run(["hdfs", "dfs", "-put", file_path, "/user/instagram_data/"])
