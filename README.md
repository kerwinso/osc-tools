##Various tools and scripts for OpenStax:

* batch-build-pdf (Python): Enqueue a batch of PDF files on the CNX legacy editor (textbook-dev or textbook-QA).

* GitLogin: Applescript to automate logging in to textbook-dev from my local machine, plus a feature to view the real-time transforms. 

* GigaTool: Applescript to choose from 8 different URL commands on 8 different textbook servers.

* MegaTool : Applescript to speed up common URL commands (enqueue, print info, view latest) on the textbook-dev server.

* PDF Print Status (Python): Check the locked status of a list of PDFs on production, send an email with the results.

* QueueToolChooser: Applescript to quickly load the queue tool on your server of choice.

##How to get this repo on your local machine (OS X):

1. In Terminal, go to your Documents directory: `cd ~/Documents`
1. Enter the command `git clone https://github.com/kerwinso/osc-tools.git`
This will copy all the files in this repo to your machine and put them in a folder called _osc-tools_ inside your _Documents_ folder.
1. To get the latest version of this repo's files, enter `cd ~/Documents/osc-tools` and enter the command `git pull`.
  * **Note:** Doing a `git pull` may overwrite the files on your local machine. This will affect the cron job (launchd job) for _pdf-print-status_, refer to [this wiki page](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29) for more details.