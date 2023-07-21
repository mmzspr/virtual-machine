import subprocess

directory = "ffi/"
c_files = ["print","key_windows","unix_time"]


cmd_o_files = ""

for c_file in c_files:
    subprocess.run(f"gcc -O2 -c {directory}{c_file}.c -o {directory}{c_file}.o")
    cmd_o_files += f"{directory}{c_file}.o "

subprocess.run(f"gcc -shared {cmd_o_files} -o {directory}library.so")