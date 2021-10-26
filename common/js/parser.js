module.exports = {
  onWillParseMarkdown: function (markdown) {
    return new Promise((resolve, reject) => {
      markdown = markdown.replace(
        /GNN-HEADER\s+([\w\W]*?)\n/gm,
        (whole, header) =>
          '<div class="header"><img class="hust"><div class="title"><hr class="hr_top"><h5>' +
          header +
          "</h5></div></div>\n"
      );
      markdown = markdown.replace(
        /GNN-FOOTER\s+([\w\W]*?)\s+([\w\W]*?)\s+([\w\W]*?)\n/gm,
        (whole, footer1, footer2, footer3) =>
          '<div class="footer"><hr class="hr_bottom"><div class="multi_column"><h6 class="bottom_left">' +
          footer1 +
          '</h6><h6 class="bottom_center">' +
          footer2 +
          '</h6><h6 class="bottom_right">' +
          footer3 +
          "</h6></div></div>\n"
      );
      markdown = markdown.replace(
        /\$\$([\w\W]+?)\$\$\n/g,
        (whole, content) => '<p>\n$$' + content + '$$\n</p>\n'
      );
      markdown = markdown.replace(
        /我的批注/g,
        (whole, content) => '<span class="yellow">:fa-weixin:</span>'
      );
      return resolve(markdown);
    });
  },
  onDidParseMarkdown: function (html) {
    return new Promise((resolve, reject) => {
      return resolve(html);
    });
  },
};
