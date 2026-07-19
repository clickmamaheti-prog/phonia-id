#!/usr/bin/env python3
"""Output helpers"""

import sys

def info(msg):
    print(f"\033[96m[ℹ]\033[0m {msg}")

def test(msg):
    print(f"\033[93m[⚡]\033[0m {msg}")

def warning(msg):
    print(f"\033[93m[⚠]\033[0m {msg}")

def error(msg):
    print(f"\033[91m[❌]\033[0m {msg}")

def throw(msg):
    print(f"\033[91m[❌]\033[0m {msg}")

def title(msg):
    print(f"\033[96m\033[1m{'='*60}\033[0m")
    print(f"\033[96m\033[1m{msg}\033[0m")
    print(f"\033[96m\033[1m{'='*60}\033[0m")

def plus(msg):
    print(f"  \033[92m[+]\033[0m {msg}")
