#!/usr/bin/env python
import py

args_str = "--browsername=firefox --platform=Linux --browserver=8 tests/test_systems.py"
py.test.cmdline.main(args_str.split(" "))
