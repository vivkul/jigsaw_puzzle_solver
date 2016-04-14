import pickle
import re
import numpy as np

def mse(X,Y):
	val=0.0
	for i in range(0,len(X)):
		val+=(X[i]-Y[i])**2
	return val/len(X)

def cos(X,Y):
	X_np=np.array(X)
	Y_np=np.array(Y)
	val=np.dot(X_np,Y_np)
	val/=(np.linalg.norm(X_np)*np.linalg.norm(Y_np))
	return val
with open ('Results_raw_cropped_created_hog.pickle','rb') as handle:
	Xr=pickle.load(handle)

with open('../Created_dataset/answer_activations_cropped_hog.pickle','rb') as handle:
	Ans=pickle.load(handle)

with open('../Created_dataset/answer_dict_cropped_hog.pickle','rb') as handle:
	Ans_dict=pickle.load(handle)


#print Xr.shape

#print Ans

names=sorted(Ans_dict.keys())
Predicted_Results={}

#print names

for i in range(0,len(names)):
	minpos=-1
	minval=1e9
	for j in range(0,len(Ans[i])):
		if mse(Xr[i][len(Xr[i])-1],Ans[i][j])<minval:
			minval=cos(Xr[i][len(Xr[i])-1],Ans[i][j])
			minpos=j
	Predicted_Results[names[i]]=minpos		


Actual_Results={}

with open('correct_option_numbers.txt','rb') as ins:
	for line in ins:
		match=re.search(r'(\w+):(\w+)',line)
		problem=match.group(1)
		value=match.group(2)
		#print "problem"
		#print problem
		problem_number=int(re.match('.*?([0-9]+)$', problem).group(1))
		for j in range(0,8):
			#print ('admin'+str(problem_number+100*j)+'_big')
			Actual_Results['admin'+str(problem_number+100*j)+'_big']=int(value)


accuracy=0.0
for i in range(0,len(names)):
#	print "problem"
#	print names[i]
#	print "Actual"
#	print Actual_Results[names[i]]  
#	print "Predicted"
#	print Predicted_Results[names[i]]
#	print "-----------------------------\n"
	if Actual_Results[names[i]] == Predicted_Results[names[i]]:
		print names[i]
		accuracy+=1.0

print "Accuracy : "
print accuracy/len(names)



with open('Predicted_Results_raw_cropped_hog.pickle','wb') as handle:
	pickle.dump(Predicted_Results,handle)

with open('Actual_Results_raw_cropped_hog.pickle','wb') as handle:
	pickle.dump(Actual_Results,handle)



