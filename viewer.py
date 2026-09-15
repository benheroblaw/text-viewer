#!/usr/bin/env python3
import extra
try: extra.createfile('options.txt', '0.05')
except: print('options.txt exists, continuing...')
import fih, fish

def main():
  fish.Barracuda()