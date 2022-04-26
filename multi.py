import threading
import os
import time
import shutil

def to_part(lst: list, num: int):
    chunk_size = len(lst) // num
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def compress(lst, directory):
    directory_compressed = os.path.join(directory, "compressed")
    if not os.path.exists(directory_compressed):
        os.mkdir(directory_compressed)
    for entry in lst:
        if os.path.isfile(entry):
            if os.path.splitext(entry)[1] in ['.gif', '.mp4', '.webm', 'm4v']:
                shutil.copy(os.path.join(directory, "bkp", os.path.basename(entry)),
                            os.path.join(directory_compressed, os.path.basename(entry)))
                continue
            entry_size = os.path.getsize(entry) / 2 ** 20
            if entry_size > 1.1:
                q = 60
            elif entry_size > 0.6:
                q = 80
            else:
                continue
            os.system(f"mozjpeg\cjpeg -quant-table 2 -quality {q} -outfile \
                    {os.path.join(directory_compressed, os.path.splitext(os.path.basename(entry))[0] + '.jpg')} {entry}")

        else:
            pass


directory = ""
bkp = os.path.join(directory, "bkp")
if not os.path.exists(bkp):
    shutil.copytree(directory, bkp)
start = time.time()
files = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
lst = to_part(files, 5)
for el in lst:
    kwargs = {"lst": el, "directory": directory}
    th = threading.Thread(target=compress, kwargs=kwargs)
    th.start()
print("Executed time: ", time.time() - start)

