import pathlib
from pathlib import Path
import configparser

def read_dirs(ini_filename,section,arg):
    current_path =pathlib.PurePath(__file__).parent
    inifile = current_path.joinpath(ini_filename)

    cf = configparser.ConfigParser()

    cf.read(inifile)
    return cf.get(section,arg).split(",")

def locate_file(base_dir, keywords='**/*'):
    p = Path(base_dir)
    p = p.resolve()
    return p.glob(keywords)

def write_to_db(dirs,result):
    current_path = pathlib.PurePath(__file__).parent
    dbfile = current_path.joinpath("search.db")

    with open(dbfile,'w',encoding='utf-8') as f:
         for r in result:
             f.write(f"{str(r)}\n")

def rewrite(keyword):
    path = 'search.ini'
    config = configparser.ConfigParser()
    config.read(path,encoding='UTF-8')
    config.set('chioce','searchpath',keyword)
    with open('search.ini','w') as f:
        config.write(f)

