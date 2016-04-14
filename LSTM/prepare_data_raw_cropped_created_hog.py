import theano
import theano.tensor as T
import pickle
import numpy as np

with open('../Created_dataset/problem_activations_cropped_hog.pickle','rb') as handle:
	X_L=np.array(pickle.load(handle))

with open('../Created_dataset/problem_dict_cropped_hog.pickle','rb') as handle:
	X_dict=pickle.load(handle)

X_all=np.array(X_L)
#print X_all
num_vectors,timesteps,num_dims=X_all.shape

print "num_vectors"
print num_vectors
#(num_vectors,)=X_all.shape
#timesteps,num_dims=X_all[0].shape

#X=X_all[0:num_vectors][0:timesteps-1]
#Y=X_all[0:num_vectors][1:timesteps]

X=X_all[:,range(0,timesteps-1)]
Y=X_all[:,range(1,timesteps)]


X_T=T.tensor3()
Y_T=T.tensor3()
X_all_T=T.tensor3()

X_T=X
Y_T=Y
X_all_T=X_all

with open('X_T_raw_cropped_created_hog.pickle','wb') as handle:
	pickle.dump(X_T,handle)

with open('Y_T_raw_cropped_created_hog.pickle','wb') as handle:
	pickle.dump(Y_T,handle)

	
with open('X_all_T_raw_cropped_created_hog.pickle','wb') as handle:
	pickle.dump(X_all_T,handle)


