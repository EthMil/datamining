import numpy as np

data_headers=['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','salary']

data=np.array(np.genfromtxt('adult.data', dtype=(int, 'S32',int, 'S32',int,'S32','S32','S32','S32','S32',int,int,int,'S32','S32'),delimiter=',',autostrip=True,names=data_headers))

data.shape

row_idx_to_delete=[]
for i in range(0,len(data)):
    if "?" in data[i]:
        row_idx_to_delete.append(i)

print len(row_idx_to_delete)," records have incomplete data and will be deleted"
data=np.delete(data,row_idx_to_delete)

np.histogram(data['age'],3);

idx_age_0=data['age']<30
idx_age_1=(data['age']>=30) & (data['age']<=55)
idx_age_2=data['age']>55



data['age'][idx_age_0]=0
data['age'][idx_age_1]=1
data['age'][idx_age_2]=2

workclass_attributes=["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",\
 "Local-gov", "State-gov", "Without-pay", "Never-worked"]
idx_workclass={}
for workclass in workclass_attributes:
    idx_workclass[workclass]=data["workclass"]==workclass

#Converting the datatype to integer now
for i in range(0,len(workclass_attributes)):
    data["workclass"][idx_workclass[workclass_attributes[i]]]=int(i)

a=np.histogram(data['fnlwgt'],8)
means=[(a[1][i]+a[1][i+1])/2.0 for i in range(0,len(a[1])-1)]
means,a[0]
print(means, a[0])


idx_wgt_0=data['fnlwgt']<=105702
idx_wgt_1=(data['fnlwgt']>=105702) & (data['fnlwgt']<=289569) 
idx_wgt_2=data['fnlwgt']>=289569


data['fnlwgt'][idx_wgt_0]=0
data['fnlwgt'][idx_wgt_1]=1
data['fnlwgt'][idx_wgt_2]=2

education_attributes=["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"]

idx_education={}
for education in education_attributes:
    idx_education[education]=data["education"]==education

#Converting the datatype to integer now

for i in range(0,len(education_attributes)):
    data["education"][idx_education[education_attributes[i]]]=int(i)

a=np.histogram(data['education_num'],4)
means=[(a[1][i]+a[1][i+1])/2.0 for i in range(0,len(a[1])-1)]
means,a[0]
print(means,a[0])

idx_enum_0=data['education_num']<=means[0]
idx_enum_1=(data['education_num']>means[0]) & (data['education_num']<=means[1]) 
idx_enum_2=(data['education_num']>=means[1]) & (data['education_num']<=means[2])
idx_enum_3=data['education_num']>means[2]


data['education_num'][idx_enum_0]=0
data['education_num'][idx_enum_1]=1
data['education_num'][idx_enum_2]=2
data['education_num'][idx_enum_3]=3

marital_status_attributes=['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent','Married-AF-spouse']

idx_marital_status={}
for marital_status in marital_status_attributes:
    idx_marital_status[marital_status]=data["marital_status"]==marital_status

#Converting the datatype to integer now

for i in range(0,len(marital_status_attributes)):
    data["marital_status"][idx_marital_status[marital_status_attributes[i]]]=int(i)

occupation_attributes=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

idx_occupation={}
for occupation in occupation_attributes:
    idx_occupation[occupation]=data["occupation"]==occupation

#Converting the datatype to integer now

for i in range(0,len(occupation_attributes)):
    data["occupation"][idx_occupation[occupation_attributes[i]]]=int(i)

relationship_attributes=['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

idx_relationship={}
for relationship in relationship_attributes:
    idx_relationship[relationship]=data["relationship"]==relationship

#Converting the datatype to integer now

for i in range(0,len(relationship_attributes)):
    data["relationship"][idx_relationship[relationship_attributes[i]]]=int(i)

race_attributes=['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

idx_race={}
for race in race_attributes:
    idx_race[race]=data["race"]==race

#Converting the datatype to integer now

for i in range(0,len(race_attributes)):
    data["race"][idx_race[race_attributes[i]]]=int(i)

sex_attributes=['Female', 'Male']

idx_sex={}
for sex in sex_attributes:
    idx_sex[sex]=data["sex"]==sex

#Converting the datatype to integer now

for i in range(0,len(sex_attributes)):
    data["sex"][idx_sex[sex_attributes[i]]]=int(i)

a=np.histogram(data['capital_gain'],2)
means=[(a[1][i]+a[1][i+1])/2.0 for i in range(0,len(a[1])-1)]
means,a[0]


idx_cap_gain_0=data['capital_gain']<=means[0]
idx_cap_gain_1=(data['capital_gain']>means[0]) & (data['capital_gain']<=means[1]) 


data['capital_gain'][idx_cap_gain_0]=0
data['capital_gain'][idx_cap_gain_1]=1

a=np.histogram(data['capital_loss'],2)
means=[(a[1][i]+a[1][i+1])/2.0 for i in range(0,len(a[1])-1)]
means,a[0]
print(means,a[0])

idx_cap_loss_0=data['capital_loss']<=means[0]
idx_cap_loss_1=(data['capital_loss']>means[0]) & (data['capital_loss']<=means[1]) 


data['capital_loss'][idx_cap_loss_0]=0
data['capital_loss'][idx_cap_loss_1]=1

a=np.histogram(data['hours_per_week'],4)
means=[(a[1][i]+a[1][i+1])/2.0 for i in range(0,len(a[1])-1)]
means,a[0]
print(means, a[0])

idx_hours_0=data['hours_per_week']<=means[0]
idx_hours_1=(data['hours_per_week']>means[0]) & (data['hours_per_week']<=means[1]) 
idx_hours_2=(data['hours_per_week']>=means[1]) & (data['hours_per_week']<=means[2])
idx_hours_3=data['hours_per_week']>means[2]


data['hours_per_week'][idx_hours_0]=0
data['hours_per_week'][idx_hours_1]=1
data['hours_per_week'][idx_hours_2]=2
data['hours_per_week'][idx_hours_3]=3

native_country_attributes=['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)','India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala','Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

idx_native_country={}
for native_country in native_country_attributes:
    idx_native_country[native_country]=data["native_country"]==native_country

#Converting the datatype to integer now

for i in range(0,len(native_country_attributes)):
    data["native_country"][idx_native_country[native_country_attributes[i]]]=int(i)

salary_attributes=['<=50K','>50K']

idx_salary={}
for salary in salary_attributes:
    idx_salary[salary]=data["salary"]==salary

#Converting the datatype to integer now

for i in range(0,len(salary_attributes)):
    data["salary"][idx_salary[salary_attributes[i]]]=int(i)

np.savetxt('filtered.txt',data,fmt="%s",delimiter=',')

from sklearn import preprocessing

filtered_data=np.array(np.genfromtxt('filtered.txt', delimiter=',',autostrip=True))

scaled_filtered_data=preprocessing.scale(filtered_data)

salary=scaled_filtered_data[:,14]
scaled_filtered_data=scaled_filtered_data[:,:-1]

print salary

print scaled_filtered_data.shape

from sklearn import svm
salary2=np.array([-1]*len(salary))
for i in range(0,len(salary2)):
    if salary[i]>0:
        salary2[i]=1

import random,math
training_size_fraction=.09
test_idx=np.array(random.sample(xrange(len(salary2)), int((1-training_size_fraction)*len(salary2))))
train_idx=np.array([x for x in xrange(len(salary2)) if x not in test_idx])
test_samples=scaled_filtered_data[test_idx]
train_samples=scaled_filtered_data[train_idx]
test_out=salary2[test_idx]
train_out=salary2[train_idx]

import time

clf = svm.SVC(kernel='linear')
libsvm_start=time.time()

clf.fit(train_samples, train_out)
libsvm_train_end=time.time()

a=np.array(clf.predict(test_samples).astype(int))
libsvm_test_end=time.time()
c=a==np.array(test_out)
c=np.array(a)==np.array(test_out)

print "Accuracy                                    : ",str(sum(c)*100.0/len(a))+" %"
print "Number of support vectors for positive class: ",clf.n_support_[0]
print "Number of support vectors for negative class: ",clf.n_support_[1]
print "Time Required for training                  : ",str(libsvm_train_end-libsvm_start)+" s"
print "Time Required for testing                   : ",str(libsvm_test_end-libsvm_train_end)+" s"

test_data_string=""
for i in range(0,len(test_out)):
    if test_out[i]==1:
        c='+1'
    else:
        c='-1'
    test_data_string=test_data_string+c
    for j in range(0,14):
        test_data_string=test_data_string+" "+str(j+1)+":"+str(test_samples[i][j])
    test_data_string=test_data_string+"\n"
f=open('adult.test','w')
f.write(test_data_string)

train_data_string=""
for i in range(0,len(train_out)):
    if train_out[i]==1:
        c='+1'
    else:
        c='-1'
    train_data_string=train_data_string+c
    for j in range(0,14):
        train_data_string=train_data_string+" "+str(j+1)+":"+str(train_samples[i][j])
    train_data_string=train_data_string+"\n"
f=open('train.dat','w')
f.write(train_data_string)

import subprocess

svmlight_start=time.time()
p = subprocess.Popen('./svm_learn train.dat model', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
svmlight_train_end=time.time()
train_output= p.stdout.readlines()

p = subprocess.Popen('./svm_classify test.dat model', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
svmlight_test_end=time.time()
test_output= p.stdout.readlines()

test_output
train_output

print "Accuracy                                    : ",str(81.62)+" %"
print "Number of support vectors                   :  1262" 
print "Time Required for training                  : ",str(svmlight_train_end-svmlight_start)+" s"
print "Time Required for testing                   : ",str(svmlight_test_end-svmlight_train_end)+" s"

import pegasos
pegasos_start_time=time.time()
weight_vector,bias,sv_array=pegasos.train(train_samples,train_out,1,1000)
pegasos_train_end=time.time()
classification=pegasos.test(test_samples,test_out,a,b)
pegasos_test_end=time.time()

f=-1*ones(len(classification))
idxz=classification>0
f[idxz]=1
f=f.astype(int)

print "Accuracy                                    : ",str(100.0*sum(f==test_out)/len(test_out))+"%"
print "Number of support vectors                   : ",len(sv_array[(sv_array<.1) & (sv_array>-0.1)]) 
print "Time Required for training                  : ",str(pegasos_train_end-pegasos_start_time)+" s"
print "Time Required for testing                   : ",str(pegasos_test_end-pegasos_train_end)+" s"

figsize(7,5)
bar(0,0.947898864746,label='LibSVM',color='r')
bar(1,0.0196049213409,label='SVMLight',color='g')
bar(2,0.437710046768,label='Pegasos');
legend()
ylabel("Time in seconds")
xlabel("Algorithms");
title("Training Time for different SVM implementations");

bar(0,1.50630402565,label='LibSVM',color='r')
bar(1,0.980164051056,label='SVMLight',color='g')
bar(2,0.0149388313293,label='Pegasos');
legend()
ylabel("Time in seconds")
xlabel("Algorithms");
title("Testing Time for different SVM implementations");

bar(0,81.2839290269,label='LibSVM',color='r')
bar(1,81.62,label='SVMLight',color='g')
bar(2,77.5239552592,label='Pegasos');
legend()
ylabel("Accuracy")
xlabel("Algorithms");

title("% Accuracy for different SVM implementations");

bar(0,1201,label='LibSVM',color='r')
bar(1,1262,label='SVMLight',color='g')
bar(2,266,label='Pegasos');
legend()
ylabel("Number of Support Vectors")
xlabel("Algorithms");

title("Number of Support Vectors for different SVM implementations");

from IPython.display import Image
Image(filename='svm.png');

