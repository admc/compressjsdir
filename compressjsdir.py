#!/usr/bin/python

# This code is original from jsmin by Douglas Crockford, it was translated to
# Python by Baruch Even. The original code had the following copyright and
# license.
#
# /* jsmin.c
#    2007-05-22
#
# Copyright (c) 2002 Douglas Crockford  (www.crockford.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# The Software shall be used for Good, not Evil.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# */

import os, sys, jsmin


if __name__ == '__main__':
   
    files = os.listdir(os.getcwd())
    comp_result = ''

    print 'Reading and compressing...'
    for filename in files:
      if filename.find('.js') != -1:
          comp_result += jsmin.jsmin(open(os.getcwd()+'/'+filename).read())

    print 'Writing file...'
    f = open(os.getcwd()+'/out.js', 'w')
    f.write(comp_result)
          
   

