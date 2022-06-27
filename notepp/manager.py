import os
from config import config


def _get_root_path():
    return config.ROOT_PATH


def exists(ps_num: int, file_name: str = None) -> bool:
    if file_name is None:
        file_name = config.FILE_NAME
    return os.path.isfile(f'{_get_root_path()}\\{ps_num}\\{file_name}')


# 파일을 ./[문제 번호]/[파일 이름]으로 저장한다.
def save_file(ps_num: int, file_name: str = None) -> None:
    if file_name is None:
        file_name = config.FILE_NAME
    dir_path = f'{_get_root_path()}\\{ps_num}'
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    open(f'{dir_path}\\{file_name}', 'w').close()


# ./[문제 번호]/[파일 이름]에 있는 파일을 노트패드++로 연다.
def open_as_np(ps_num: int, file_name: str = None) -> None:
    if file_name is None:
        file_name = config.FILE_NAME
    result = os.system(f'start notepad++ {_get_root_path()}\\{ps_num}\\{file_name}')
    if result == 1:  # 노트패드++를 못 찾을 시
        print('notepad++를 설치해주시기 바랍니다.')


# 코드를 실행하고, 결과를 반환한다.
def run_code(ps_num: int, file_name: str) -> str:
    _cmd = config.RUN_CMD \
        .replace('{root}', _get_root_path()) \
        .replace('{ps_num}', str(ps_num)) \
        .replace('{file_name}', file_name)
    return os.popen(_cmd).read()


# 문제 코드를 실행하고 입력값을 넣은 후 결과를 반환한다.
def run_code_input(ps_num: int, file_name: str, user_input: str) -> str:
    # returns output
    pass
