#!/bin/bash
gyp example.gyp --depth=. -f make --generator-output=./out
V=1 make -C out
cp out/out/Default/example.so ./
