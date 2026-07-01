#!/bin/bash


helm install prometheus prometheus-community/kube-prometheus-stack -f monitoring/prometheus-values.yaml

helm install loki grafana/loki -f monitoring/loki-values.yaml

helm install alloy grafana/alloy -f monitoring/alloy-values.yaml

helm install web-helm ./webchart
