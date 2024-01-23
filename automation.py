'''
Download videos from YouTube using the Python pytube library.

imports and modules 
'''
from python_basics import Ytdownload
ytd = Ytdownload.youtube_downloads.download('./')
# https://youtu.be/kj0jgspgopQ?si=o1e2arWUA3DPKR6y
# https://youtu.be/T37nO9uJNp0?si=Xk5Z_zHcxrqh4_RN
print(ytd)