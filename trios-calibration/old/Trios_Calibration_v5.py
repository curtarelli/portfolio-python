'''
This is a Ramsés TriOS sensor calibration script based on its manual Rel. 1.1 (Principle of Operation)
http://www.controlcomponents.com.au/Open-File/961/RAMSES%20-%20manual%20(v.1_1_01).pdf

@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   May, 2020.
'''
###############################################################################
##  Packages importation:
import os
import glob
import pandas as pd
import statistics as st
import unicodedata as ud
###############################################################################
##  Calibration function definition:
def trios_calibration(campaign, above_water, under_water): 
    '''
    ----------
    Parameters
    ----------
    campaign : String
        Campaign folder name inside input directory.
        
    above_water : List of Strings
        List with tags for measurements gathered above water surface.
        Ex.: ['Sup', 'sup', 'surface']
        
    under_water : List of Strings
        List with tags for measurements gathered above water surface.
        Ex.: ['Sub', 'sub', 'Prof', 'prof', 'Perf', 'perf']

    -------
    Returns
    -------
    calibrated_data: DataFrame
        ".txt" and ".csv" calibrated data saved on campaign folder inside
        output directory.
    '''     
    ##  ['input'] directory call:
    dir_i = os.path.join(os.getcwd(), r'input\\' + campaign)
    ##  ['output'] directory call:
    dir_o = os.path.join(os.getcwd(), r'output\\' + campaign)
    ##  ['util'] directory call:
    dir_u = os.path.join(os.getcwd(), r'util')
    
    ##  Getting inside input ['campaign'] folder:
    os.chdir(dir_i)
    
    sensor_list = glob.glob('*_RAW.txt')
    
    for i in sensor_list:
        sensor = i.replace('_RAW.txt', '')
        
        ##  Input for which environments were measured by the sensor, one may have in
        ##  mind how the sensor was used in the campaign, usually the sensors "SAM_8404",
        ##  "SAM_xxxx" and "SAM_xxxx" are used just for above-water measurements, while
        ##  "SAM_xxxx", "SAM_xxxx" and "SAM_xxxx" are used for measurements taken above
        ##  and underwater, but other configurations can be used:
        amb = str(input('Underwater measurements were taken with the sensor: ' + sensor + '? [Yes/No]'))
        ##  Nomalization of the answer (string):
        amb = ud.normalize('NFD', amb)
        amb = amb.encode('ascii', 'ignore')
        amb = amb.decode('utf-8')
        amb = amb.lower()
        
        ##  In case of wrong answer the script ask it again:
        while amb not in ['yes', 'no', 'y', 'n']:
            print('[PLEASE ANSWER IT AGAIN!!]')
            amb = str(input('Underwater measurements were taken with the sensor: ' + sensor + '? [Yes/No]'))
            ##  Nomalization of the answer (string):
            amb = ud.normalize('NFD', amb)
            amb = amb.encode('ascii', 'ignore')
            amb = amb.decode('utf-8')
            amb = amb.lower()
        
        ##  From sensors name the script mounts the variables to call each ".txt" archive;
        ##  Input data has to be name in uppercase inside the directory:
        back = sensor + '_BACK.txt'
        cal = sensor + '_CAL.txt'
        raw = sensor + '_RAW.txt'
        ##  Output ".csv" data name:
        data_csv = sensor + '.csv'
        ##  Output ".txt" data name:
        data_txt = sensor + '.txt'
        ##  Ancillary data frame with index column to normalize output data. It must
        ##  be inside ['util'] directory found on the root of the application:
        mcol = 'mcol.txt'                                          
        
        ##  Using Pandas to open Data Frames used in the final arrange of the product:
        df_calibrated = pd.read_csv(raw,
                                    delimiter = '\t',
                                    na_values = '',
                                    engine = 'python')
        
        os.chdir(dir_u)
        
        df_mcol = pd.read_csv(mcol,
                              delimiter = '\t',
                              na_values = '',
                              engine = 'python')
        
        os.chdir(dir_i)
        
        ##  Indexes used to operate over Data Frames during the routine;
        ##  Index for wavelength column data:
        i_mcol = df_mcol.loc[df_mcol['[Spectrum]'] == '[Data]'].index[0] + 1
        ##  Index for the integration time of the measurements:
        i_time = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'IntegrationTime'].index[0]
        ##  Index to call the data inside Data Frame:
        i_data = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 1
        ##  Index for +NAN data in the claibrated product:
        i_data2 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 5
        ##  Index to call end of Data Frame to compose data:
        i_data3 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[Data]'].index[0] + 196
        ##  Index for +NAN data at the end of calibrated Data Frame product:
        i_data4 = df_calibrated.loc[df_calibrated['[Spectrum]'] == '[END] of [Data]'].index[0]
        ##  Index for CommentSub2 line ['under_water', 'above_water'] for each measurement:
        i_cal = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'CommentSub2'].index[0]
        ##  Index with location of the data status ['Raw', 'Calibrated']:
        i_type = df_calibrated.loc[df_calibrated['[Spectrum]'] == 'IDDataTypeSub1'].index[0]
        ##  Series based on indexes inside data range in the Data Frame:
        i_range = pd.Series(range(i_data2, i_data3))
        
        ##  Column with wavelength in nanometers and insertion in the final data:
        df_mcol = df_mcol.iloc[i_mcol:, 0]
        ##  Output Data Frame ready to receive calibrated data after process:
        df_calibrated.iloc[i_data:, 0] = df_mcol
        
        ##  Opening Data Frames only with the data to be operated using indexes:
        data_back = pd.read_csv(back,               ##  Name of the Data Frame;
                                delimiter = '\t',   ##  Delimitation with TAB;
                                na_values = '',     ##  NaN values using '';
                                engine = 'python',  ##  Pandas engine;
                                skiprows = i_data,  ##  Rows to skip using index;
                                skipfooter = 2)     ##  Rows to skip from bottom to head;
        
        data_cal = pd.read_csv(cal,
                               delimiter = '\t',
                               na_values = '',
                               engine = 'python',
                               skiprows = i_data2,
                               skipfooter = 62)
        
        data_raw = pd.read_csv(raw,
                               delimiter = '\t',
                               na_values = '',
                               engine = 'python',
                               skiprows = i_data,
                               skipfooter = 2)
        
        ##  Preset of calculation parametes used in the calibration. The calibration
        ##  consists in a offset and background removal, followed by a normalization
        ##  by integration time and calibration coefficient of the sensor:
        t0 = 8192                       ##  Maximum integration time in [ms];
        b16 = (2 ** 16) - 1             ##  16 bits counting for normalization;
        S_air = data_cal.iloc[:, 1]     ##  "AIR" constant of calibration;
        S_aqua =  data_cal.iloc[:, 2]   ##  "AQUA" constant of calibration;
        
        ###########################################################################
        ####################       Calibration Steps       ########################
        ###########################################################################
        ##  Nomalization of digital numbers (DN) with 16 bits:
        M = data_raw.iloc[:, 1:] / b16
        ##  Measurements counting variable (number of columns in Data Frame):
        M_count = M.iloc[0, :].count() - 1
        ##  Empty Data Frame to start the process with Background removal:
        C = pd.DataFrame()
        
        ##  Background removal and insartion of new data into "C" Data Frame:
        x = 0
        while x <= M_count:
            i = 'Unnamed: ' + str(x + 1)
            t = int(df_calibrated.iloc[i_time, x + 1])                    ##  Measurements integration time;
            coef_t = t / t0                                               ##  "B" coefficient;
            B = data_back.iloc[0:, 1] + (data_back.iloc[0:, 2] * coef_t)  ##  Background to remove;
            C[i] = M.iloc[:, x] - B
            x += 1
        ##  Offset calculation indexes, related to sensor dark current effect:
        n1 = 237 - 1
        n2 = 254
        
        D = pd.DataFrame()      ##  Empty Data Frame to offset;
        
        ##  Offset and insertion of new data into "D" Data Frame:
        y = 0
        while y <= M_count:
            j = 'Unnamed: ' + str(y + 1)
            D[j] = C.iloc[:, y] - st.mean(C.iloc[n1:n2, y])
            y += 1
        
        E = pd.DataFrame()      ##  Empty Data Frame for K normalization;
        
        ##  K normalziation and insertion of new data tion "E" Data Frame:
        z = 0
        while z <= M_count:
            q = 'Unnamed: ' + str(z + 1)
            t = int(df_calibrated.iloc[i_time, z + 1])      ##  Measurements integration time;
            k = t0 / t                                      ##  K coefficient;
            E[q] = D.iloc[:, z] * k
            z += 1
        
        F = E.iloc[4:195].copy()    ##  Copy of "E" for division by "S_air" or "S_aqua";
        F = F.reset_index()         ##  Index reset;
        del F['index']              ##  Deleting column create by the code;
        
        ##  Calibrating data due to choosed environment "Air" or "Aqua":
        if amb in ['n']:
            S_aqua = S_air
        u = 0
        while u <= M_count:
            if df_calibrated.iloc[i_cal, u + 1] in above_water:
                F.iloc[:, u] = F.iloc[:, u] / S_air
            elif df_calibrated.iloc[i_cal, u + 1] in under_water:
                F.iloc[:, u] = F.iloc[:, u] / S_aqua
            u += 1
        
        ##  Index seting to "F" Data Frame:
        F = F.set_index(i_range)
        
        ##  Copying calibrated data into final Data Frame:
        df_calibrated.iloc[i_data2:i_data3, 1:] = F
        ##  Invalid data wavelengths:
        df_calibrated.iloc[i_data:i_data2, 1:] = '+NAN'
        df_calibrated.iloc[i_data3:i_data4, 1:] = '+NAN'
        ##  Changing the data status:
        df_calibrated.iloc[i_type, 1:] = 'CALIBRATED'
    
        ##  Getting inside output ['campaign'] folder:
        os.chdir(dir_o)
        
        ##  Saving final Data Frame into ".csv" and ".txt" archives on output directory:
        df_calibrated.to_csv(data_txt, sep = '\t', encoding = 'utf-8', index = False)
        df_calibrated.to_csv(data_csv, encoding = 'utf-8', index = False)
        ##  The results are identical to the default calibrated data released by TriOS
        ##  using MSDA_xe software;
        