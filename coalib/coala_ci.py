# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import functools

from pyprint.ConsolePrinter import ConsolePrinter

from coalib.coala_main import run_coala
from coalib.output.ConsoleInteraction import (
    print_results_no_input, print_section_beginning)
from coalib.parsing.DefaultArgParser import default_arg_parser


def main():
    args = default_arg_parser().parse_args()
    console_printer = ConsolePrinter(print_colored=not args.no_color)
    partial_print_sec_beg = functools.partial(
        print_section_beginning,
        console_printer)
    results, exitcode, _ = run_coala(
        print_results=print_results_no_input,
        print_section_beginning=partial_print_sec_beg,
        force_show_patch=True,
        console_printer=console_printer)

    return exitcode


if __name__ == '__main__':  # pragma: no cover
    main()
