import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import torch_geometric
import PySpice.Logging.Logging as Logging

logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Unit import *
from PySpice.Physics.SemiConductor import ShockleyDiode
from PySpice.Spice import Simulation

import PySpice

# 设置ngspice是以subprocess的形式来使用
PySpice.Spice.Simulation.CircuitSimulator.DEFAULT_SIMULATOR = 'ngspice-subprocess'

# 元器件库所在的目录
libraries_path = "C:/Users/tczrr/ngspice/PySpice/examples/libraries"
spice_library = SpiceLibrary(libraries_path)

circuit = Circuit('Diode Characteristic Curve')

circuit.include(spice_library['1N4148'])  # 导入二极管元件：1N4148

circuit.V('input', 'in', circuit.gnd, 10 @ u_V)
circuit.R(1, 'in', 'out', 1 @ u_Ω)  # not required for simulation
circuit.X('D1', '1N4148', 'out', circuit.gnd)

# Fixme: Xyce ???
temperatures = [0, 25, 100] @ u_Degree
analyses = {}

# 分析不同温度下的二极管的特性
for temperature in temperatures:
    # 创建仿真器
    simulator = circuit.simulator(temperature=temperature,
                                  nominal_temperature=temperature)
    # 进行直流分析：DC, 电压从-2V -- 5V, 步进: 0.01V
    analysis = simulator.dc(Vinput=slice(-2, 5, .01))
    analyses[float(temperature)] = analysis

silicon_forward_voltage_threshold = .7

shockley_diode = ShockleyDiode(Is=4e-9, degree=25)


def two_scales_tick_formatter(value, position):
    if value >= 0:
        return '{} mA'.format(value)
    else:
        return '{} nA'.format(value / 100)


formatter = ticker.FuncFormatter(two_scales_tick_formatter)

figure = plt.figure(1, (20, 10))

axe = plt.subplot(121)
axe.set_title('1N4148 Characteristic Curve ')
axe.set_xlabel('Voltage [V]')
axe.set_ylabel('Current')
axe.grid()
axe.set_xlim(-2, 2)
axe.axvspan(-2, 0, facecolor='green', alpha=.2)
axe.axvspan(0, silicon_forward_voltage_threshold, facecolor='blue', alpha=.1)
axe.axvspan(silicon_forward_voltage_threshold, 2, facecolor='blue', alpha=.2)
axe.set_ylim(-500, 750)  # Fixme: round
axe.yaxis.set_major_formatter(formatter)
Vd = analyses[25].out
# compute scale for reverse and forward region
forward_region = Vd >= 0 @ u_V
reverse_region = np.invert(forward_region)
scale = reverse_region * 1e11 + forward_region * 1e3
for temperature in temperatures:
    analysis = analyses[float(temperature)]
    axe.plot(Vd, - analysis.Vinput * scale)
axe.plot(Vd, shockley_diode.I(Vd) * scale, 'black')
axe.legend(['@ {} °C'.format(temperature)
            for temperature in temperatures] + ['Shockley Diode Model Is = 4 nA'],
           loc=(.02, .8))
axe.axvline(x=0, color='black')
axe.axhline(y=0, color='black')
axe.axvline(x=silicon_forward_voltage_threshold, color='red')
axe.text(-1, -100, 'Reverse Biased Region', ha='center', va='center')
axe.text(1, -100, 'Forward Biased Region', ha='center', va='center')

axe = plt.subplot(122)
axe.set_title('Resistance @ 25 °C')
axe.grid()
axe.set_xlim(-2, 3)
axe.axvspan(-2, 0, facecolor='green', alpha=.2)
axe.axvspan(0, silicon_forward_voltage_threshold, facecolor='blue', alpha=.1)
axe.axvspan(silicon_forward_voltage_threshold, 3, facecolor='blue', alpha=.2)
analysis = analyses[25]
static_resistance = -analysis.out / analysis.Vinput
dynamic_resistance = np.diff(-analysis.out) / np.diff(analysis.Vinput)
axe.semilogy(analysis.out, static_resistance, basey=10)
axe.semilogy(analysis.out[10:-1], dynamic_resistance[10:], basey=10)
axe.axvline(x=0, color='black')
axe.axvline(x=silicon_forward_voltage_threshold, color='red')
axe.axhline(y=1, color='red')
axe.text(-1.5, 1.1, 'R limitation = 1 Ω', color='red')
axe.legend(['{} Resistance'.format(x) for x in ('Static', 'Dynamic')], loc=(.05, .2))
axe.set_xlabel('Voltage [V]')
axe.set_ylabel('Resistance [Ω]')

plt.tight_layout()
plt.show()
