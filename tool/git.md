# git

* delete remote branch: `git push <remote_name> --delete <branch_name>` # [ref](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely)

## gitpython
* `pip install gitpython`
* https://stackoverflow.com/questions/14989858/get-the-current-git-hash-in-a-python-script
* http://gitpython.readthedocs.io/en/stable/tutorial.html
```
import git
import time

repo = git.Repo(search_parent_directories=True)
csha = repo.head.object.hexsha
ctime = time.asctime(time.localtime(repo.head.object.committed_date))
cmsg = repo.head.object.message.strip()
```
