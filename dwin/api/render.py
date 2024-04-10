# Documentation for Render API https://api-docs.render.com/reference/introduction
class RenderCLoud:
    def __init__(self):
        pass

    def authentication(self):
        pass
    
    def rate_limit(self):
        # https://api-docs.render.com/reference/rate-limiting
        pass
    
    # Owners
    def list_autorize_users_teams(self):
        pass
    def retirve_user_team(self):
        pass
    
    # Registre Credencials
    def get_list_registries_credentials(self):
        pass
    def create_registry_credentials(self):
        pass
    def retrive_registry_credentials(self):
        pass
    def update_registry_credentials(self):
        pass
    def delete_registry_credentials(self):
        pass
    
    # Services
    def list_services(self):
        pass
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
    def list_deployments(self):
        pass
    def trigger_deployment(self):
        pass
    def retrieve_deployment(self):
        pass
    def cancel_deployment(self):
        pass
    def rollback_deployment(self):
        pass
    
    # Custom Domains
    def list_custom_domains(self):
        pass
    def add_custom_domain(self):
        pass
    def retrieve_custom_domain(self):
        pass
    def delete_custom_domain(self):
        pass
    def verify_dns(self):
        pass
    
    # Jobs
    def list_jobs(self):
        pass
    def create_job(self):
        pass
    def retrieve_job(self):
        pass
    def cancel_job(self):
        pass