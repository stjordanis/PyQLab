"""
AWGs
"""

from atom.api import Atom, List, Int, Float, Range, Enum, Bool, Constant, Str

from Instrument import Instrument


import enaml
from enaml.qt.qt_application import QtApplication

from instruments.AWGBase import AWGChannel, AWG, AWGDriver

from plugins import register_plugins

AWGList = register_plugins(AWG, [])

if __name__ == "__main__":
    with enaml.imports():
        from AWGsViews import AWGView

    awg = APS(label='BBNAPS1')
    app = QtApplication()
    view = AWGView(awg=awg)
    view.show()
    app.start()
