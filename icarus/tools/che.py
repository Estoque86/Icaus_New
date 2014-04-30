"""Functions for modelling and evaluating the performance of cache
    replacement policies.
    """
from __future__ import division
import math

import numpy as np
from scipy.optimize import fsolve

from icarus.tools import TruncatedZipfDist, DiscreteDist, che_characteristic_time, che_per_content_cache_hit_ratio


def main():
    hit = che_per_content_cache_hit_ratio(TruncatedZipfDist(alpha=1,n=10000).pdf,100)
    f1=open('./cheTeo.txt', 'w+')
    f1.write(hit)

if __name__ == '__main__':
    main()
