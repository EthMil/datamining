#from pylab import plot,show
import numpy
from scipy.cluster.vq import kmeans,vq

# data import
data = numpy.fromfile("/home/ethan/datamining/assignment_2/dataset.csv", dtype = float, count=-1, sep=" ")
print(data)
data = numpy.array_split(data, 403)

#print data


k = 4
# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(data,k)
print centroids
# assign each sample to a cluster
#idx,_ = vq(dataset,centroids)

# some plotting using numpy's logical indexing
#plot(fullDataSet[idx==0,0],fullDataSet[idx==0,1],'ob',
 #    fullDataSet[idx==1,0],fullDataSet[idx==1,1],'or',
  #   fullDataSet[idx==2,0],fullDataSet[idx==2,1],'og') # third cluster point
#plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
#show()
