import requests

PROJECTS_URL = '/projects'
BRANCHES_URL = '/projects/{project_id}/repository/branches'
DELETE_BRANCH_URL = '/projects/{project_id}/repository/branches/{branch_name}'
DELETE_MERGED_BRANCHES = '/projects/{project_id}/repository/merged_branches'

class GitlabAPIConnector:
    def __init__(self, hostname, private_token):
        self.hostname = hostname
        self.headers = {
            'PRIVATE-TOKEN': private_token
        }
    
    def get_projects(self, name=None):
        if not name:
            return requests.get(f'{self.hostname}/api/v4{PROJECTS_URL}', headers=self.headers).json()
        return requests.get(f'{self.hostname}/api/v4{PROJECTS_URL}?search={name}', headers=self.headers).json()

    def get_branches(self, project_id):
        project_branches_url = BRANCHES_URL.format(project_id=project_id)
        return requests.get(f'{self.hostname}/api/v4{project_branches_url}', headers=self.headers).json()

    def get_branches_by_project_name(self, project_name):
        project_id = self.get_projects(project_name)[0]['id']
        return self.get_branches(project_id)
    
    def delete_branch(self, project_id, branch_name):
        print(f'Deleting branch {branch_name}')
        try:
            requests.delete(f'{self.hostname}/api/v4' + DELETE_BRANCH_URL.format(
                project_id=project_id,
                branch_name=branch_name
            ), headers=self.headers)
        except:
            print(f'An error happened when deleting branch {branch_name}')
            raise

    def delete_merged_branches(self, project_id):
        delete_url_for_project = DELETE_MERGED_BRANCHES.format(project_id=project_id)
        return requests.delete(f'{self.hostname}/api/v4{delete_url_for_project}')
