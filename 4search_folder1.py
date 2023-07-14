# 4. 폴더에서 다른 폴더나 파일 찾기

# 지정된 경로가 파일인지 폴더인지 알아보기
# import os
# for i in os.listdir('/'):
#     print(i + ' : ' + str(os.path.isdir('/' + i)))
#     print(i + ' : ' + str(os.path.isfile('/' + i)))

# 1) 깊이 우선 탐색
import os

def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(dir + i , '/', name)

search('C:/book', 'book')