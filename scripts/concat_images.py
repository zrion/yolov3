# -*- coding: utf-8 -*-
# @Author: Hai N. Nguyen
# @Date:   2021-12-10 13:32:30
# @Last Modified by:   Hai N. Nguyen
# @Last Modified time: 2021-12-10 13:42:53
import cv2
import numpy as np
import argparse, os


def process(fig_dir, label_dir, out_dir, ncomp):
	pictures = sorted([x for x in os.listdir(fig_dir) and x.endswith('.jpg')])

	return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--figdir", type=str,
        help='Path to figure storage')
    parser.add_argument("--labeldir", type=str,
        help='Prefix of the images')
    parser.add_argument("-n", destination='compress', type=int, default=12,
        help='Compression factor')
    parser.add_argument("--outdir", type=int,
        help='Output directory')
    args = parser.parse_args()

    if args.figdir and args.labeldir and args.outdir:
    	process(args.figdir, args.labeldir, args.outdir, args.compress)