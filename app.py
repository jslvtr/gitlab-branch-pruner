import datetime
import argparse

from gitlab import GitlabAPIConnector

parser = argparse.ArgumentParser(description='Accept Gitlab API private token.')
parser.add_argument('--hostname', default='https://gitlab.com',
                    help='The hostname of your Gitlab installation, e.g. "https://gitlab.com".')
parser.add_argument('--token',
                    help='The private token for your Gitlab API account.')
parser.add_argument('--maxage', type=int, default=90,
                    help='Branches older than this number of days will be pruned.')
args = parser.parse_args()

g = GitlabAPIConnector(args.hostname, args.token)


def main():
    project_name = input('Enter your project name: ')
    projects_by_name = g.get_projects(project_name)

    if len(projects_by_name) == 1:
        project_id = g.get_projects(project_name)[0]['id']
    else:
        project_id = clarify_project(projects_by_name)

    branches = g.get_branches(project_id)

    older_than_maxage = lambda branch: parse_last_commit_date(branch) < datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=args.maxage)
    old_branches = [b for b in branches if older_than_maxage(b)]

    print_branches_sorted(old_branches, last_committed_ago)

    ask_delete_branches(old_branches, project_id)


def clarify_project(projects):
    print(f'There are {len(projects)} projects that match the given name.')
    for i, p in enumerate(projects):
        print(f'--- {i} of {len(projects)} ---')
        print(p)
        if input('\nIs this the right project? (y/N)') == 'y':
            return p['id']
    raise RuntimeError('No project selected, terminating...')


def parse_last_commit_date(branch):
    parseable_date =  branch['commit']['committed_date'][:-3] + branch['commit']['committed_date'][-2:]
    return datetime.datetime.strptime(parseable_date, '%Y-%m-%dT%H:%M:%S.%f%z')


last_committed_ago = lambda branch: datetime.datetime.now(datetime.timezone.utc) - parse_last_commit_date(branch)


def print_branches_sorted(branches, key):
    for b in sorted(branches, key=key):
        name = b['name'].ljust(50)
        committer_name = b['commit']['committer_name'].ljust(30)
        print(f"{name}{committer_name}\tlast committed on {b['commit']['committed_date']}\t\t{last_committed_ago(b)} ago")


def ask_delete_branches(branches, project_id):
    delete_them = input('Do you want to delete these branches? (y/N)')

    if delete_them == 'y':
        for b in branches:
            g.delete_branch(project_id, b['name'])
        print('Old branches deleted.')

    delete_merged_branches = input('Do you want to delete all merged branches? (y/N)')

    if delete_merged_branches == 'y':
        g.delete_merged_branches(project_id)
        print('Merged branches deleted.')


if __name__ == '__main__':
    main()
