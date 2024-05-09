import pathlib
import re

def findkey(keyword):
    answer=''
    current_path = pathlib.PurePath(__file__).parent
    dbfile = current_path.joinpath("search.db")

    with open(dbfile, encoding='utf-8')as f:
        for line in f.readlines():
            if re.search(keyword,line):
                answer=answer+line.rstrip()
                answer=answer+'\n'

    return answer