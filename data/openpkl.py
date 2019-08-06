import pickle

f=open('people_relation_test.pkl','rb')
test=pickle.load(f)
print(test)