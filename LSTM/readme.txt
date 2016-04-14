This is multilayer perceptron.

First data is prepared from pickle of question and option images using prepare_data_raw_cropped_created_hog.py
Then the lstm is run using lstm_raw_cropped_created_hog.py
Finally, the output of lstm is used to choose the correct option which is evaluated using evaluate_results_raw_cropped_created_hog.py
