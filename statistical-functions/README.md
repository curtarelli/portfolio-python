# *Statistical Functions*

This is a script with functions to apply statistcal methods to compare a predict data series with the reference data series. The methods are:

* Mean Absolute Percentage Error (MAPE);

	<img src="https://render.githubusercontent.com/render/math?math=MAPE = {1 \over n} \sum_{\substack{i=1}} {\Bigl\lvert {{y_{ref_i} - y_{pred_i}} \over {y_{ref_i}}} \Bigr\rvert}">

* Correlation Coefficient (r);

	<img src="https://render.githubusercontent.com/render/math?math=r = {{n({\sum_{\substack{i=1}} y_{ref_i} . y_{pred_i}})} - ({{\sum_{\substack{i=1}} y_{ref_i}}}) . ({{\sum_{\substack{i=1}} y_{pred_i}}})} \over \sqrt{[n {\sum_{\substack{i=1}} y_{ref_i}^2} - ({{\sum_{\substack{i=1}} y_{ref_i}})^2] . [n {\sum_{\substack{i=1}} y_{pred_i}^2} - ({{\sum_{\substack{i=1}} y_{pred_i}})^2]}">

* Determination Coefficient (R²);



* Bias Error (bias);



* Root-Mean Square Error (RMSE);



## Use of the script

The user can copy the `statistical-function.py` script to your capplication `util` directory and import it into your code.