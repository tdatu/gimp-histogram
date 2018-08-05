#!/bin/bash

gimp -i --batch-interpreter=python-fu-eval -b 'execfile("gimp_hist.py"); pdb.gimp_quit(1)'
