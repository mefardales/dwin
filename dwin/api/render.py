# Documentation for Render API https://api-docs.render.com/reference/introduction
import requests
'''
TODO:
1. Validate request using Pydantic
2. Create a class for each endpoint and methods
'''
class RenderCloud:
    
    CHOICE_REGISTRY = (
        'GITLAB',
        'GITHUB',
        'BITBUCKET',
    )
    
    CHOICE_SERVICE = (
        'WEB_SERVICE',
        'STATIC_SITE',
        'PRIVATE_SERVICE',
        'BACKGROUND_JOB',
        'CRON_JOB',
    )
    endpoint = {
        'services': '/services',
        'owners': '/owners',
        'registrycredentials': '/registrycredentials',
        'deployments': '/deployments',
        'customdomains': '/customdomains',
        'jobs': '/jobs',
    }
    
    CLEAR_CACHE = (
        'DO_NOT_CLEAR',
        'CLEAR'
    )
    
    DOMAIN_TYPE = (
        'APEX',
        'SUBDOMAIN',
    )
    
    VERIFICATION_STATUS = (
        'VERIFIED',
        'UNVERIFIED',
    )
    def __init__(self, **kwargs):
        self.url = kwargs['data'].get('url', None)
        self.data = kwargs['data'].get('data', None)
        self.rate_limit = kwargs['data'].get('rate_limit', 20)
        
    def authentication(self) -> dict:
        endpoint = self.url + f'/services?limit={self.rate_limit}'
        print(endpoint)
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    # Owners
    def list_autorize_users_teams(self, name: str, email: str, cursor: str, limit: int) -> dict:
        endpoint = self.url + f'/owners?name={name}&email={email}&cursor={cursor}&limit={limit}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
        
    def retirve_user_team(self, owner_id: str) -> dict:
        endpoint = self.url + f'/owners/{owner_id}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    
    # Registre Credencials
    def get_list_registries_credentials(self, name: str, username: str, type: str, created_before: str, 
                                        created_after: str, update_before: str, update_after: str, 
                                        owner_id: str,cursor: str, limit: int) -> dict:
        endpoint = self.url + f'/registrycredentials?name={name}&username={username}&type={type}&createdBefore={created_before}&createdAfter={created_after}&updatedBefore={update_before}&updatedAfter={update_after}&ownerId={owner_id}&cursor={cursor}&limit={limit}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def create_registry_credentials(self, registry: str, name: str, username: str, auth_token: str, owner_id: str) -> dict:
        if registry not in self.CHOICE_REGISTRY:
            return {'message': 'Registry not found', 'status_code': 404}
        endpoint = self.url + f'/registrycredentials'
        response = requests.post(endpoint, headers=self.data.get('header', None), json={'registry': registry, 'name': name, 'username': username, 'authToken': auth_token, 'ownerId': owner_id})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
            
    def retrive_registry_credentials(self, register_credentials_id: str) -> dict:
        endpoint = self.url + f'/registrycredentials/{register_credentials_id}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}

    def update_registry_credentials(self, register_credentials_id: str, registry: str, name: str, username: str, auth_token: str, owner_id: str) -> dict:
        if registry not in self.CHOICE_REGISTRY:
            return {'message': 'Registry not found', 'status_code': 404}
        endpoint = self.url + f'/registrycredentials/{register_credentials_id}'
        response = requests.put(endpoint, headers=self.data.get('header', None), json={'registry': registry, 'name': name, 'username': username, 'authToken': auth_token, 'ownerId': owner_id})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def delete_registry_credentials(self, register_credentials_id: str) -> dict:
        endpoint = self.url + f'/registrycredentials/{register_credentials_id}'
        response = requests.delete(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
    
    # Services
    def list_services(self, name: str, type_service: list, env: list, region: list, suspend: list, create_before: str, update_before: str, update_after: str, owner_id: list, cursor: str, limit: int) -> dict:
        endpoint = self.url + f'/services?name={name}&type={type_service}&env={env}&region={region}&suspend={suspend}&createdBefore={create_before}&updatedBefore={update_before}&updatedAfter={update_after}&ownerId={owner_id}&cursor={cursor}&limit={limit}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def create_service(self):
        pass
    
    def retrive_service(self):
        pass
    def update_service(self):
        pass
    def delete_service(self):
        pass
    def retrieve_environment_variables(self):
        pass
    def update_environment_variables(self):
        pass
    def retrieve_headers(self):
        pass
    def retrieve_redirect_rewrite_rules(self):
        pass
    def suspend_service(self):
        pass
    def resume_service(self):
        pass
    def restart_server(self):
        pass
    def scale_service(self):
        pass
    def update_autoscaling_config_for_service(self):
        pass
    def create_preview_for_image_backend_service(self):
        pass
    
    # Deployments
    # NOQA
    def list_deployments(self,service_id: str, created_before: str, created_after: str, update_before: str, update_after: str, finished_before: str, finished_after: str, cursor: str, limit: int) -> dict:
        endpoint = self.url + f'/services/serviceId/deploys?serviceId={service_id}&createdBefore={created_before}&createdAfter={created_after}&updatedBefore={update_before}&updatedAfter={update_after}&finishedBefore={finished_before}&finishedAfter={finished_after}&cursor={cursor}&limit={limit}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def trigger_deployment(self, service_id: str, clear_cache: str, commit_id: str, image_url: str):
        if clear_cache not in self.CLEAR_CACHE:
            return {'message': 'Clear cache not found', 'status_code': 404}
        endpoint = self.url + f'/services/{service_id}/deploys'
        response = requests.post(endpoint, headers=self.data.get('header', None), json={'clearCache': clear_cache, 'commitId': commit_id, 'imageUrl': image_url})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def retrieve_deployment(self, service_id: str, deployment_id: str):
        endpoint = self.url + f'/services/{service_id}/deploys/{deployment_id}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def cancel_deployment(self, service_id: str, deployment_id: str):
        endpoint = self.url + f'/services/{service_id}/deploys/{deployment_id}/cancel'
        response = requests.post(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def rollback_deployment(self, service_id: str, deployment_id: str):
        endpoint = self.url + f'/services/{service_id}/deploys/{deployment_id}/rollback'
        response = requests.post(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
    
    # Custom Domains
    def list_custom_domains(self, service_id: str, cursor: str, limit: int, name: str, domain_type: str, verification_status: str, create_before: str, create_after: str) -> dict:
        if domain_type not in self.DOMAIN_TYPE and verification_status not in self.VERIFICATION_STATUS:
            return {'message': 'Domain type or verification status not found', 'status_code': 404}
        endpoint = self.url + f'/services/{service_id}/customdomains?cursor={cursor}&limit={limit}&name={name}&domainType={domain_type}&verificationStatus={verification_status}&createdBefore={create_before}&createdAfter={create_after}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def add_custom_domain(self, service_id: str, name: str):
        endpoint = self.url + f'/services/{service_id}/customdomains'
        response = requests.post(endpoint, headers=self.data.get('header', None), json={'name': name})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def retrieve_custom_domain(self, service_id: str, custom_domain_id_or_name: str):
        endpoint = self.url + f'/services/{service_id}/customdomains/{custom_domain_id_or_name}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def delete_custom_domain(self, service_id: str, custom_domain_id_or_name: str):
        endpoint = self.url + f'/services/{service_id}/customdomains/{custom_domain_id_or_name}'
        response = requests.delete(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def verify_dns(self, service_id: str, custom_domain_id_or_name: str):
        endpoint = self.url + f'/services/{service_id}/customdomains/{custom_domain_id_or_name}/verify'
        response = requests.post(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
    
    # Jobs
    def list_jobs(self, service_id: str):
        endpoint = self.url + f'/services/{service_id}/jobs'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
    def create_job(self, service_id: str, start_command: str, plan_id: str):
        endpoint = self.url + f'/services/{service_id}/jobs'
        response = requests.post(endpoint, headers=self.data.get('header', None), json={'startCommand': start_command, 'planId': plan_id})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def retrieve_job(self, service_id: str, job_id: str):
        endpoint = self.url + f'/services/{service_id}/jobs/{job_id}'
        response = requests.get(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}
        
    def cancel_job(self,service_id: str, job_id: str):
        endpoint = self.url + f'/services/{service_id}/jobs/{job_id}/cancel'
        response = requests.post(endpoint, headers=self.data.get('header', None))
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'Error to connect', 'status_code': response.status_code}


    