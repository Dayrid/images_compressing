import os
import time

directory = r"C:\Users\dayri\Downloads\Experimental"
directory_compressed = r"C:\Users\dayri\Downloads\Experimental\compressed"

if not os.path.exists(directory_compressed):
    os.mkdir(directory_compressed)
# os.system("cd mozjpeg")
start = time.time()
with os.scandir(path=directory) as it:
    for entry in it:
        if entry.is_file():
            entry_size = os.path.getsize(entry.path) / 2 ** 20
            if entry_size > 1.1:
                q = 60
            else:
                q = 80
            os.system(f"mozjpeg\cjpeg -quant-table 2 -quality {q} -outfile \
                    {os.path.join(directory_compressed, os.path.splitext(entry.name)[0] + '.jpg')} {entry.path}")
        else:
            pass
print("Executed time: ", time.time() - start)
