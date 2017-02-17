##Various tools and scripts for OpenStax Content QA:

* batch-build-pdf (Python): Enqueue a batch of PDF files on the CNX legacy editor (textbook-dev or textbook-QA).
* delete-workgroups (Python + Selenium Webdriver): Automate deleting workgroups using a web browser on the CNX legacy editor.
* GigaTool: Applescript to choose from 8 different URL commands on 8 different textbook servers.
* GitLogin: Applescript to automate logging in to textbook-dev from my local machine, plus a feature to view the real-time transforms. 
* MegaTool : Applescript to speed up common URL commands (enqueue, print info, view latest) on the textbook-dev server.
* PDF Print Status (Python): Check the locked status of a list of PDFs on production, send an email with the results.
* QueueToolChooser: Applescript to quickly load the queue tool on your server of choice.
* URL Commands Dashboard: web-based successor to GigaTool. ([link](http://ks52.web.rice.edu/urlcommands.html))

### Experimental
* CNX Book ID: a Rube Goldberg that uses Selenium Webdriver to automate grabbing a CNX book ID 
* OSWeb broken link checker: checks HTTP response codes on the QA server for every link in the `sitemap.xml` file


##How to get this repo on your local machine (OS X):

1. In Terminal, go to your Documents directory: `cd ~/Documents`
1. Enter the command `git clone https://github.com/kerwinso/ost-tools.git`
This will copy all the files in this repo to your machine and put them in a folder called _ost-tools_ inside your _Documents_ folder.
1. To get the latest version of this repo's files, enter `cd ~/Documents/ost-tools` and enter the command `git pull`.
  * **Note:** If you've been making local edits to files in this directory, doing a `git pull` may overwrite the files on your local machine, or generate an error. This may affect the cron job (launchd job) for _pdf-print-status_, refer to [this wiki page](https://github.com/kerwinso/ost-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29) for more details.
  
## Collaborator instructions:  
*(Adapted from [Git - The Simple Guide](http://rogerdudler.github.io/git-guide/))*

1. Navigate to your local directory for the repo, e.g.: `cd ~/Documents/ost-tools`
1. Create a new local branch and switch to it: `git checkout -b <newbranchname>`
1. Double check which branch you are on: `git branch -a`. You should be on the one you just created. Do **not** make any edits while on the `master` branch!
1. Edit local files. Test them locally to make sure they work before committing.
1. Add the files you want to the index: `git add <filename>` for each file
1. Commit those files with a commit message: `git commit -m "<my commit message>"`
	* Shortcut to add all your tracked and modified files to the index and commit them in one step: `git commit -am "<my commit message>"`
1. Push your commit to the corresponding remote branch (make sure your [push mode](http://stackoverflow.com/questions/21839651/git-what-is-the-difference-between-push-default-matching-and-simple) is set to 'simple')
: `git push origin <newbranchname>` 
1. When all your commits are pushed, create a pull request from github by going to the [New Pull Request] (https://github.com/kerwinso/ost-tools/compare) page and choosing your `<newbranchname>` from the 'compare' pulldown and submitting the PR.
1. I will review your code changes and merge the PR when approved.
1. Branch cleanup after merge:
	* The remote branch will be deleted from github by me after successful merge.
	* To delete your local branch:
		1. Switch back to the master branch: `git checkout master`
		1. Pull down the latest changes from the remote: `git pull`
		1. Delete the finished branch: `git branch -d <newbranchname>`
		1. Prune your cached data about remote branches that no longer exist: `git remote prune origin`
		1. Update your local cache with info on new remote branches: `git fetch`