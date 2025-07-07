from git import Repo
import datetime

repo_dir = './'
repo = Repo(repo_dir)

repo.git.add('parking.xml')
repo.index.commit(f'Update parking.xml on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
origin = repo.remote(name='origin')
origin.push()
