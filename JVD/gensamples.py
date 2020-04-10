#!/usr/bin/env python3

## Generate samples of uniform, exponential, and normal distributions.

import scipy.stats as st


with open('data/normal.txt', 'w') as f:
    for n in st.norm.rvs(loc=100., scale=10., size=100):
        f.write('{}\n'.format(n))


with open('data/uniform.txt', 'w') as f:
    for n in st.uniform.rvs(loc=75., scale=50., size=100):
        f.write('{}\n'.format(n))


with open('data/exponential.txt', 'w') as f:
    for n in st.expon.rvs(loc=0., scale=100., size=100):
        f.write('{}\n'.format(n))
