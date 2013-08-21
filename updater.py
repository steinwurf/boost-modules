#!/usr/bin/python -O

import os
from subprocess import call

submodules = ['algorithm',
    'any',
    'asio',
    'bind',
    'chrono',
    'concept_check',
    'config',
    'container',
    'core',
    'date_time',
    'exception',
    'function',
    'functional',
    'integer',
    'interprocess',
    'intrusive',
    'io',
    'iterator',
    'math',
    'move',
    'mpl',
    'multi_index',
    'optional',
    'parameter',
    'preprocessor',
    'range',
    'ratio',
    'signals2',
    'smart_ptr',
    'static_assert',
    'system',
    'test',
    'thread',
    'timer',
    'tuple',
    'type_traits',
    'units',
    'utility',
    'variant']

def main():
    current_dir = os.getcwd()

    for submodule in submodules:
        os.chdir(submodule)
        try:
            retcode = call("git pull origin release/Boost_1_54_0", shell=True)
        except OSError as e:
            print("Execution failed:{}", e)
        os.chdir(current_dir)

if __name__ == "__main__":
    main()