node {
         stage("Git Clone"){

         git credentialsId: 'Git-Hub-Credentials', url: "https://github.com/sachin-pharande/-bentoml_ccfd.git"
         
         stage("Docker build"){
             sh 'docker version'
             sh 'pip install -r requirements.txt'
             sh 'python3 train.py'
             sh 'bentoml build .'
             sh 'bentoml containerize xgb_classifier:latest -t sachinpharande/xgb_classifier:latest'
         
         }
         stage("Docker Login"){
                   
             withCredentials([string(credentialsId: 'sachinpharande', variable: 'PASSWORD')]) {
        	    sh "docker login -u sachinpharande -p ${PASSWORD}"
         }
         }
         stage("Push image to docker hub"){
             sh 'docker push sachinpharande/xgb_classifier:latest'
         }

         stage("Kubernetes deployment"){
             kubernetesDeploy(configs: 'deploymentservice.yaml', kubeconfigId: 'kuberneteskey')
           }

        }
    }
