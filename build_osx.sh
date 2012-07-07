#!/bin/sh
cc -c example.c
cc -bundle -undefined dynamic_lookup -o example.so example.o
