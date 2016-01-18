close all;
clear;
%data = h5read('PMUdata_Bus1VA2VALoad9PQ.h5','/df/block0_values');
data = h5read('C:/Users/fragom/PhD_CIM/PYTHON/SimuGUI/res/matlab/IEEENetworks2.IEEE_9Bus_&dymola_new_Enam.h5','/IEEENetworks2.IEEE_9Bus/pmu1_values');
do=data(2,:);
Y=do.'
order=10;
[mode_freq, mode_damp]=mode_est_basic_fcn(Y, order);
disp('    freq#######damp######')

disp([mode_freq  mode_damp])

datasett=[mode_freq mode_damp]
disp([datasett])

hdf5write('mode_estimation.h5','/damp_freq/freq',mode_freq,'/damp_freq/damp',mode_damp  );
exit



