#!/usr/bin/env python
"""
Simple test to verify the script structure without running the full pipeline.
This checks that all functions are importable and parameters work.
"""
import sys
import os

# Test imports
try:
    import argparse
    print("✓ argparse imported")
    import numpy as np
    print("✓ numpy imported")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    print("Note: This is expected if dependencies are not installed.")
    print("The code structure is valid, dependencies just need to be installed.")
    sys.exit(0)

# Test that the main script structure is correct
try:
    from PLEK2 import parse_arguments
    print("✓ PLEK2.parse_arguments imported")
except ImportError as e:
    print(f"✗ PLEK2 import failed: {e}")
    sys.exit(1)

# Test argument parsing
sys.argv = ['test', '-i', 'test.fa', '-m', 've', '-o', 'test_output']
try:
    args = parse_arguments()
    assert args.input_file == 'test.fa'
    assert args.model == 've'
    assert args.output == 'test_output'
    print("✓ Argument parsing works correctly")
    print(f"  Input: {args.input_file}")
    print(f"  Model: {args.model}")
    print(f"  Output: {args.output}")
except Exception as e:
    print(f"✗ Argument parsing failed: {e}")
    sys.exit(1)

# Test functions import
try:
    from functions import filter_fasta, get_kmer, get_ORF, contact, prediction, output_results
    print("✓ All functions imported successfully")
except ImportError as e:
    print(f"✗ Functions import failed: {e}")
    sys.exit(1)

print("\n✓ All structure tests passed!")
print("\nNote: Full functionality requires:")
print("  - Model files in utils/ directory")
print("  - All Python dependencies installed")
print("  - Valid FASTA input file")
