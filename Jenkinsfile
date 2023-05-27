node {
         stage("Git Clone"){

         git credentialsId: 'Git-Hub-Credentials', url: "https://github.com/RupaliKhare/bentoml_ccfd.git"
         
         stage("Docker build"){
             sh 'docker version'
             sh 'pip install -r requirements.txt'
             sh 'python3 train.py'
             sh 'bentoml build .'
             sh 'bentoml containerize xgb_classifier:latest -t rupalikhare123/xgb_classifier:latest'
         
         }
         stage("Docker Login"){
                   
             withCredentials([string(credentialsId: 'rupalikhare123', variable: 'PASSWORD')]) {
        	    sh "docker login -u rupalikhare123 -p ${PASSWORD}"
         }
         }
         stage("Push image to docker hub"){
             sh 'docker push rupalikhare123/xgb_classifier:latest'
         }

         stage("Kubernetes deployment"){
             kubernetesDeploy(configs: 'deploymentservice.yaml', kubeconfigId: 'kuberneteskey')
           }

        }
    }
