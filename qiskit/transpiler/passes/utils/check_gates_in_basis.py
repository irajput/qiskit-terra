# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Check if all the gates are in the basis."""

from qiskit.transpiler.basepasses import AnalysisPass


class CheckGatesInBasis(AnalysisPass):
    """Check if all the gates are in the target basis.

    The result is saved in ``property_set['all_gates_in_basis']`` as an boolean.
    """
    def __init__(self, basis_gates):
        """CheckGatesInBasis initializer.

        Args:
            basis_gates (list[str] or None): Target basis names, e.g. `['u3', 'cx']`.
        """
        super().__init__()
        self._basis_gates = basis_gates

    def run(self, dag):
        """Run the CheckGatesInBasis pass on `dag`."""
        all_basis_gates=True
        if self._basis_gates:
            for gate in dag.gate_nodes():
                if gate.name not in self._basis_gates:
                    all_basis_gates=False
                    break
        print("all basis gates",all_basis_gates)
        print("basis gates: ",self._basis_gates)
        self.property_set["all_gates_in_basis"] = all_basis_gates
