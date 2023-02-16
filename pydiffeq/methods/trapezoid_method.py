from copy import copy

import numpy as np

from pydiffeq.ode_solver import ODE_Solver


class TrapezoidMethod(ODE_Solver):
    def solve(self, t_eval, y0):
        dt = t_eval[1] - t_eval[0]
        y = copy(y0)
        solution = [y0]
        for t in t_eval[1:]:
            k1 = self.system.func(y, t)
            k2 = self.system.func(y + dt * k1, t + dt)
            y += dt / 2 * (k1 + k2)
            y0 = copy(y)
            solution.append(y0)
        return np.array(solution), t_eval
