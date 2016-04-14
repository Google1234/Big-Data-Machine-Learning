'''
method: 朴素贝叶斯网络 最大似然估计算法
输入：
    file_train/file_test txt文件名，要求文件最后一列为label，其它列为feature
    feature               特征数目
    label_numbers        标签类别数，二分类为题即为2
    feature_numbers      每个特征类别数
label 为0/1，feature 为0/1
'''
def bayes(file_train,file_test,feature_numbers,label_number,feature):
    f=open(file_train)
    combination_numbers=feature_numbers*label_number# 如二分类 每个feature也是2  0:feature[i]=0,label=0 1:0:feature[i]=0,label=1 2:0:feature[i]=1,label=0 3:0:feature[i]=1,label=1
    count=[[0 for i in range(feature)]for j in range(combination_numbers)]
    y_count=[0 for i in range(label_number)]
    while 1:
        line=f.readline()
        if not line:
            break
        list=line.split('\t')
        num=[]
        for word in list:
            if word[-1]=='\n':
                num.append(ord(word[:-1])-ord('0'))
            else:
                num.append(ord(word)-ord('0'))
        for i in range(feature):
            index=num[i]*feature_numbers+num[feature]
            count[index][i]+=1
        ###########################
        #如果不是二分类问题，需要更改
        if num[feature]==0:
            y_count[0]+=1
        else:
            y_count[1]+=1
        ###########################
    f.close()

    sum=0
    for i in range(label_number):
        sum+=y_count[i]
    for i in range(label_number):
        y_count[i]=y_count[i]*1.0/sum
    for i in range(feature):
        #################################
        #如果feature_numbers！=2 label_numbers！=2 需要更改
        sum=(count[0][i]+count[1][i])
        count[0][i]=count[0][i]*1.0/sum
        count[1][i]=count[1][i]*1.0/sum
        sum=(count[2][i]+count[3][i])
        count[2][i]=count[2][i]*1.0/sum
        count[3][i]=count[3][i]*1.0/sum
        #################################################
    print(y_count)
    for i in range(combination_numbers):
        print(count[i])

    f=open(file_test)
    wrong=0
    correct=0
    while 1:
        line=f.readline()
        if not line:
            break
        list=line.split('\t')
        num=[]
        for word in list:
            if word[-1]=='\n':
                num.append(ord(word[:-1])-ord('0'))
            else:
                num.append(ord(word)-ord('0'))
        #######################
        #如果不是二分类问题，需要更改
        pro_0=1.0
        pro_1=1.0
        for i in range(feature):
            pro_0=pro_0*count[num[i]*feature_numbers][i]
            pro_1=pro_1*count[num[i]*feature_numbers+1][i]
        pro_0=pro_0*y_count[0]
        pro_1=pro_1*y_count[1]
        if (pro_0>pro_1 and num[feature]==0) or(pro_0<=pro_1 and num[feature]==1):
            correct+=1
        else:
            wrong+=1
        ##########################
    f.close()
    print('分类正确：',correct)
    print('分类错误：',wrong)


'''
    DEMO
'''
def count():
    file="trainingData.txt"
    f=open(file)
    count=0
    label=[[0 for i in range(2**5)] for j in range(2)]
    while 1:
        line=f.readline()
        if not line:
            break
        count+=1
        list=line.split('\t')
        num=[]
        for word in list:
            if word[-1]=='\n':
                num.append(ord(word[:-1])-ord('0'))
            else:
                num.append(ord(word)-ord('0'))
        index=num[0]+num[1]*2+num[2]*4+num[3]*8+num[4]*16
        if num[len(num)-1]==0:
            label[0][index]+=1
        else :
            label[1][index]+=1
    f.close()

    print(label[0])
    print(label[1])

    f=open("testingData.txt")
    count=0
    wrong=0
    while 1:
        line=f.readline()
        if not line:
            break
        count+=1
        list=line.split('\t')
        num=[]
        for word in list:
            if word[-1]=='\n':
                num.append(ord(word[:-1])-ord('0'))
            else:
                num.append(ord(word)-ord('0'))
        index=num[0]+num[1]*2+num[2]*4+num[3]*8+num[4]*16
        if label[0][index]>label[1][index]:
            pre=0
        else:
            pre=1
        if pre!=num[len(num)-1]:
            wrong+=1
    f.close()
    print('wrong',wrong,'total',count)

count()
bayes('trainingData.txt','testingData.txt',2,2,5)