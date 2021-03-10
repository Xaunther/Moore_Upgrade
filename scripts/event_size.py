#Print the composition of a DST's file size.
#Hack for https://gitlab.cern.ch/lhcb-HLT/upgrade-bandwidth-studies/-/blob/master/options/event_size.py
#Which allows to specify which folders must be summed
from __future__ import division, print_function
import argparse
import os

import prettytable
import ROOT

# Each branch has a related branch whose name ends with this suffix
# I don't know what the relationship actually is
WEIRD_SUFFIX = '_R.'
# Ways we can order the table
ORDERING = ['name', 'size', 'ratio']

# SIGH
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Suppress warnings about missing dictionaries for LHCb classes
ROOT.gErrorIgnoreLevel = ROOT.kError


def nbytes(branch):
    """Return a tuple of (uncompressed, compressed) sizes in bytes."""
    ubytes = branch.GetTotBytes("*")
    cbytes = branch.GetZipBytes()
    children = branch.GetListOfBranches()
    for child in children:
        tmp = nbytes(child)
        ubytes += tmp[0]
        cbytes += tmp[1]
    return ubytes, cbytes


def is_any_in(_list, _str):
    for l in _list:
        if l in _str:
            return True
    return False


def event_size(fname, order, pathname, bannednames):
    diskbytes = os.path.getsize(fname)
    f = ROOT.TFile(fname)
    totbytes = 0
    for key in f.GetListOfKeys():
        kname = key.GetName()
        tree = f.Get(kname)
        assert tree.Class().GetName() == 'TTree', tree
        nentries = tree.GetEntries() or 1
        tcbytes = tree.GetZipBytes()
        # Should we show statistics as an average over all events, or in total?
        show_average = kname == 'Event'

        table = prettytable.PrettyTable()
        table.field_names = [
            'Path', 'Uncompressed (B)', 'Compressed (B)', 'Ratio'
        ]
        table.align['Path'] = 'l'
        table.sortby = {
            'name': 'Path',
            'size': 'Uncompressed (B)',
            'ratio': 'Ratio'
        }[order]

        treebytes = 0
        matchbytes = 0
        for branch in tree.GetListOfBranches():
            bname = branch.GetName()
            if bname.endswith(WEIRD_SUFFIX):
                continue
            ubytes, cbytes = nbytes(branch)
            # Include the contribution from the suffixed branch
            # Remove the trailing dot and add the suffix
            branch_r = tree.GetBranch(bname[:-1] + WEIRD_SUFFIX)
            if branch_r:
                ubytes_r, cbytes_r = nbytes(branch_r)
                ubytes += ubytes_r
                cbytes += cbytes_r

            totbytes += cbytes
            treebytes += cbytes
            ratio = ubytes / cbytes

            tespath = bname.replace('_', '/').replace('.', '')
            if pathname in tespath and not is_any_in(bannednames, tespath):
                matchbytes += cbytes
            if show_average:
                ubytes = ubytes / nentries
                cbytes = cbytes / nentries
            if pathname in tespath and not is_any_in(bannednames, tespath):
                table.add_row([
                    tespath,
                    int(ubytes),
                    int(cbytes), '{0:.2f}'.format(ratio)
                ])
        # Check our bookkeeping
        assert tcbytes == treebytes
        units = 'B'
        if show_average:
            matchbytes /= nentries
            units += '/event'
        print('== {0} ({1:.0f} {2}) =='.format(kname, matchbytes, units))
        print(table)

    print('== Total ==')
    print('Disk size: {0:.0f} kB'.format(diskbytes / 1e3))
    print('Trees size: {0:.0f} kB'.format(totbytes / 1e3))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', help='DST file to analyse')
    parser.add_argument(
        '--order',
        choices=ORDERING,
        default='name',
        help='How to order the printed branches')
    parser.add_argument(
        '--path',
        default='',
        help='Specify which branches must be shown and summed')
    parser.add_argument(
        '--banned', default=[], nargs='*', help='Ban branches containing this')
    args = parser.parse_args()
    event_size(args.file, args.order, args.path, args.banned)
