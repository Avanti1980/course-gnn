cp ~/.mume/parser.js ./common/js/
cp ~/.mume/mathjax_config.js ./common/js/
git add *
git commit -m $1

case $2 in
"ee")
    git push gitee master
    ;;
"hub")
    git push github master
    ;;
"both")
    git push gitee master
    git push github master
    ;;
*)
    echo "error: 2nd par must be [ee|hub|both]!"
    ;;
esac
