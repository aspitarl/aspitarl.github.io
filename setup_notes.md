2024-11-13 setup on debian

Ended up having to delete gemfile.lock, maybe this is all that was needed but did some other steps

save bundle install to local .bundle directory (seems already gitignored...)

`bundle config set --local path '.bundle'`

Install ruby development tools 

`sudo apt-get install ruby-dev`