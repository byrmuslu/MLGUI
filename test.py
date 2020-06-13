from dbscan import DBSCAN
from fuzzy import FCM
from util import generate_cyclic_data, generate_blobs_data, export_model, import_model
from plot import ModelPlot

X, y = generate_blobs_data()
# export_model(test)


# test2 = import_model('DBSCAN.yuksel')
# print(test2)



def plot_automation(model):
  
  plot = ModelPlot(model)
  plot.plot()


def dbscan_visualization_test(data, eps=0.3, minPoints=10):
  test = DBSCAN(eps, minPoints)
  test.fit(data)
  plot_automation(test)

def fuzzy_means_visualization_test(data, cluster=2):
  test = FCM(cluster)
  test.fit(data)
  plot_automation(test)

def import_test(filename):
  extension = filename.split(".")[-1]
  assert (extension=='yuksel' or extension=='bayram') , "Wrong file extension!"

def dbscan_model_import_test(filename):

  import_test(filename)
  model = import_model(filename)
  assert type(model).__name__=='DBSCAN','Model import error!!!'


def model_export_test(model):
  export_model(model)

# fuzzy_means_visualization_test(X, cluster= 3)
# dbscan_visualization_test(X)

dbscan_model_import_test("DBSCAN.yuksel")
dbscan_model_import_test('test.bayram')
# fuzzy = FCM(2)
# fuzzy.fit(X)
# model_export_test(fuzzy)
def model_import_test(filename):
  model = import_model(filename)
  print(type(model).__name__)
  plot_automation(model)

model_import_test('FCM.yuksel')