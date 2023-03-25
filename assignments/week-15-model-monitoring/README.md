<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">Monitoring Drift</h1>


Today we'll be taking a look at ML monitoring using [Boxkite](https://github.com/boxkite-ml/boxkite) to easily visualize monitoring metrics using [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/). We will be using a modified example from Boxkite where we will deploy a model locally using Flask and Docker, then artifically load the server to view monitoring metrics. Prometheus will hook into the backend to extract information about our deployment and Grafana will be the dashboard we use to visualize the metrics.
