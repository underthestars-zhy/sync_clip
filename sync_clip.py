#!/usr/bin/env python
#  Copyright (c) 2020.
#  You can freely change the code part, but you must follow the MIT protocol
#  You cannot delete any information about UTS
#  You cannot use this program to disrupt social order.

def clip_command(language):
    if language == 'en':
        from_dir = input('原文件夹: ')
        to_dir = input('新文件夹: ')
    else:
        from_dir = input('Original folder: ')
        to_dir = input('New Folder: ')
    import shutil
    shutil.copytree(from_dir, to_dir)
    return True
