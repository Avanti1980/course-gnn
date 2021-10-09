cp ~/.mume/parser.js ./common/js/
cp ~/.mume/mathjax_config.js ./common/js/
git add *
git commit -m $1
git push github master
# git push gitee master
