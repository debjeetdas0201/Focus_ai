import os
import subprocess
import sys

if getattr(sys, 'frozen', False):
    path_to_main = os.path.join(sys._MEIPASS, 'vsapp.py')
    # executable = os.path.join(sys._MEIPASS, 'python.exe')
    executable = os.path.join(os.getcwd(),r'.venv\Scripts\python.exe')
    # executable = r'\venv\Scripts\python.exe'

    print('In IF')
    print(path_to_main)
else:
    print('ELSE')
    path_to_main = './vsapp.py'
    executable = r'.venv\Scripts\python.exe'

print(executable)
print(path_to_main)

result = subprocess.run(f"{executable} -m streamlit run {path_to_main} --server.port=8502", shell=True, capture_output=True,
                        text=True, check=True)

print(result.stdout)
print(result.stderr)



# if getattr(sys, 'frozen', False):
#     path_to_main = os.path.join(sys._MEIPASS, 'app.py')
#     # executable = os.path.join(sys._MEIPASS, 'python.exe')
#     # executable = os.path.join(sys._MEIPASS, 'venv\Scripts\python.exe')
#     executable = os.path.join(os.getcwd(),r'venv\Scripts\python.exe')
#     print('In IF')
#     print(path_to_main)
# else:
#     print('ELSE')
#     path_to_main = './app.py'
#     # executable = os.path.join(os.getcwd(),r'venv\Scripts\python.exe')
#     executable = os.path.join(os.getcwd(),r'venv\Scripts\python.exe')
#
# print(executable)
# print(path_to_main)
# try:
#     result = subprocess.call(f"{executable} -m streamlit run {path_to_main} --server.port=8504", shell=True,
#                         text=True)
# except Exception as e:
#     print(e)