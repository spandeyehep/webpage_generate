These scripts populate slac public webpage with images Example: https://www.slac.stanford.edu/~pande230/CUTE/R37/reprocessed/traces/Z3/Event0/


Original php script was written by [Giovanni Petrucciani](https://github.com/musella/php-plots) which works perfectly on CERN webpages.<br/>
Since SLAC does not allow php script execution, therefore python files have been added that generates html files in a similar fashion. 

# How the script works
* `crawler.py` is the main driver script that iterates over each subdirectories, copies `res` folder and `generateHtml.py` file into it. It triggers `generateHtml.py` afterwards. 
* `res` directory contains javascript and css style file that does the cosmetics.
* `generateHtml.py` detects the images in the directory (format supported: png, jpg, jpeg, and gif), and rewrites `res/skeleton.html` as `index.html` accrodingly.   

# Setup generation script
1. If not already done, create `.htaccess` file in `public_html` directory with following lines:<br/>
`DirectoryIndex index.html`<br/>
`Options +Indexes`

2. Clone this repository on centos7:<br/>
`git clone git@github.com:spandeyehep/webpage_generate.git ./webpage_generate`

3. Edit and save [Line-16](https://github.com/spandeyehep/webpage_generate/blob/master/crawler.py#L16) to specify the absolute path of cloned repository.<br/> 
E.g. `/u/dm/<username>/webpage_generate`

4. Add an alias to your ~/.bashrc file which copies and executes `crawler.py` file:<br/>
`alias dothemagic='cp <path_to_repo>/crawler.py .; python crawler.py'`
5. Restart terminal (logout and login to centos7) or run `source ~/.bashrc`.

# Usage
1. Inside public_html, copy (or create) the directories containing images (each subdirectory can also contain images).
2. Run previously created bashrc alias `dothemagic`.
3. Visit your personal web[age to see the effect.
