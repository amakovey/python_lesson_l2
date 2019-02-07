# testsplitter.py
import splitter
import doctest

nfail, ntests = doctest.testmod(splitter, verbose=True)