# hello-spark-minikube
Beginner friendly guide on setting up and running your first Spark application on Minikube. 🚀

This repository contains code and commands used in the demonstration shown in this blog - [Hello Spark on Minikube
](https://krohit-de.hashnode.dev/hello-spark-on-minikube)

## Please refer to below commands used in the tutorial

#### Starting Minikube cluster
```
minikube start --vm-driver=docker --cpus=5 --memory=6000
```

#### Building Docker image - (`customspark:3.5.0`). 
Please note to be in your project directory before running this command.
```
docker buildx build --platform=linux/arm64 -t customspark:3.5.0 .
```

#### Switch to Docker daemon from Minikube and import `customspark:3.5.0` in Minikube
```
eval $(minikube docker-env)
minikube image load customspark:3.5.0
```

#### Create Service Account in Minikube for Spark Application
```
kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
```

#### Running Spark Application - `spark-submit`
```
K8S_API_SERVER_URL=$(kubectl cluster-info | grep 'Kubernetes control plane' | awk '{print $7}')

${SPARK_HOME}/bin/spark-submit --master k8s://${K8S_API_SERVER_URL} --deploy-mode cluster \
  --conf spark.kubernetes.container.image=customspark:3.5.0 \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
  --conf spark.kubernetes.executor.deleteOnTermination=false \
  --conf spark.executor.instances=2 local:///opt/spark_etl.py
```
